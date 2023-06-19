import codecs
import json
import requests
from typing import NamedTuple
from collections import OrderedDict

from django.template.loader import render_to_string

from EatTop import settings


class ReturnedData(NamedTuple):
    """ Class for storing data from the convert to pdf file service

    :param response: response from the convert to pdf file service
    :param order_id: order id
    :param type_check: type check
    """
    response: requests.Response
    order_id: int
    type_check: str


def convert_to_pdf(data: list) -> list[ReturnedData]:
    """ Function for sending checks to the printer

    :param data: list of checks
    :return: ReturnedData
    """

    returned_data = []

    for check in data:
        template = _render_template(check['type'], check['order'], check['order_id'])
        response = _make_request(template, check['type'], check['order_id'])

        returned_data.append(ReturnedData(
            response[0],
            response[1],
            response[2]
        ))

    return returned_data


def _render_template(type_receipt: str, data: OrderedDict, order_id: int) -> str:
    """ Function for rendering html receipt

    :param type_receipt: type receipt
    :param data: data for rendering
    :return: html receipt
    """
    return render_to_string(
        f'order_receipt_{type_receipt}.html',
        {
            'title': 'Client Receipt',
            'order': dict(data),
            'order_id': order_id,
        }
    )


def _make_request(html: str, type_check: str, order_id: int) -> tuple[requests.Response, int, str]:
    """ Function for sending html receipt to the convert to pdf file service

    :param html: html receipt
    :return: pdf file
    """
    data = {
        'contents': codecs.encode(html.encode(), 'base64').decode()
    }
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(settings.CONVERTER_PDF_SERVICE, data=json.dumps(data), headers=headers)

    return response, order_id, type_check
