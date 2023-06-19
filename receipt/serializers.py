from django.template.loader import render_to_string
from rest_framework import serializers

from .models import Printer, Check
from .services.converter.service import convert_to_pdf
from .tasks import create_pdf


class DishSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    quantity = serializers.IntegerField()

    class Meta:
        fields = '__all__'


class OrderSerializer(serializers.Serializer):
    client_full_name = serializers.CharField(max_length=100)
    client_phone = serializers.CharField(max_length=100)
    client_email = serializers.CharField(max_length=100)
    client_address = serializers.CharField(max_length=100)
    client_comment = serializers.CharField(max_length=100)
    dishes = DishSerializer(many=True)
    total_price = serializers.IntegerField()
    payment_method = serializers.CharField(max_length=100)
    delivery_method = serializers.CharField(max_length=100)

    class Meta:
        fields = '__all__'


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = '__all__'


class CheckSerializer(serializers.ModelSerializer):
    order = OrderSerializer(write_only=True)
    point_id = serializers.IntegerField(write_only=True)
    order_id = serializers.IntegerField(write_only=True)
    response = serializers.JSONField(read_only=True)

    def validate_point_id(self, value):
        if not Printer.objects.filter(point_id=value):
            raise serializers.ValidationError('Printer with this point_id does not exist.')
        return value

    def validate_order_id(self, value):
        if Check.objects.filter(order_id=value):
            raise serializers.ValidationError('Check with this order_id already exists.')
        return value

    def create(self, validated_data):
        printers = Printer.objects.filter(point_id=validated_data.pop('point_id'))
        checks = []

        for printer in printers:
            check = Check.objects.create(**validated_data, printer_id=printer, type=printer.check_type, status='new')
            checks.append(check)

        create_pdf.delay([{'order': check.order, 'order_id': check.order_id, 'type': check.type} for check in checks])

        for check in checks:
            check.status = 'rendered'
            check.save()

        return {'response': [{'id': check.id, 'status': check.status, 'type': check.type} for check in checks]}

    class Meta:
        model = Check
        exclude = ['pdf_file', 'printer_id', 'type', 'status']


