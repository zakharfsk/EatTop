from django.db import models


class Printer(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100, unique=True)
    check_type = models.CharField(max_length=100)
    point_id = models.IntegerField()

    def __str__(self):
        return f'Printer #{self.id} | {self.name}'

    class Meta:
        db_table = 'printer'
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтери'


class Check(models.Model):
    printer_id = models.ForeignKey(Printer, on_delete=models.PROTECT)
    order_id = models.IntegerField()
    type = models.CharField(max_length=100)
    order = models.JSONField()
    status = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='pdf/', null=True, blank=True)

    def __str__(self):
        return f'Check #{self.id} | {self.status}'

    class Meta:
        db_table = 'check'
        verbose_name = 'Чек'
        verbose_name_plural = 'Чеки'
