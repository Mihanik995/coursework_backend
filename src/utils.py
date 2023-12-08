import json
import os.path
from datetime import datetime


def unpack_json():
    result = None
    with open(os.path.join('..', 'operations.json'), 'r', encoding='utf-8') as file:
        result = json.load(file)
    return result


def form_transaction(transaction):
    date_string = transaction['date']
    date_string_format = datetime.strptime(date_string[:10], '%Y-%m-%d').date().strftime('%d.%m.%Y')

    final_string = f"{date_string_format} {transaction['description']}\n"

    if 'from' in transaction.keys():
        final_string += form_address(transaction['from'])

    final_string += f" -> {form_address(transaction['to'])}\n"

    final_string += f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}"

    return final_string


def form_address(address):
    if address.count('Счет'):
        return f"Счет **{address[-4:]}"
    else:
        return f"{address[:-12]} {address[-12:-10]}** **** {address[-4:]}"
