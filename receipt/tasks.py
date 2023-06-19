from time import sleep

from celery import shared_task
from django.core.files.base import ContentFile

from receipt.models import Check
from receipt.services.converter.service import convert_to_pdf


@shared_task()
def create_pdf(checks):
    """ Function for creating pdf files

    :type checks: list[Check]
    :return:
    """
    sleep(5)  # emulate sending to the printer
    data = convert_to_pdf(checks)
    for item in data:
        send_to_printer.delay(item.order_id, item.type_check, item.response.content)


@shared_task()
def send_to_printer(order_id, type_check, response):
    """ Function for sending checks to the printer

    :param order_id: Order id
    :param response: Response from the convert to pdf file service
    :param type_check: Type check
    :return:
    """

    sleep(5)
    check = Check.objects.get(order_id=order_id, type=type_check)
    check.pdf_file.save(f'{order_id}_{type_check}.pdf', ContentFile(response), save=True)
    check.status = 'printed'
    check.save()

