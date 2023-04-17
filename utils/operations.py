from datetime import datetime
import json
from utils import masks


def get_valid_operations(file):
    '''Возвращает список операций из файла JSON, которые непустые
    и у которых статус Проведен'''
    with open(file, encoding="UTF-8") as f:
        operations_list = json.load(f)
        if len(operations_list) > 0:
            valid_oper_list = []
            for operation in operations_list:
                if operation:
                    if operation['state'] == 'EXECUTED':
                        valid_oper_list.append(operation)
            return valid_oper_list
        return f"Файл пустой"

def get_5_last_operations_info(data):
    '''возвращает список 5 последних операций
    если операций меньше, возвращает все операции'''
    time_list = [operation['date'] for operation in data]
    time_list.sort(reverse=True)
    if len(time_list) < 5:
        last_operation_time = time_list[:len(time_list)]
    else:
        last_operation_time = time_list[:5]
    last_operations = []
    for operation in data:
        if operation["date"] in last_operation_time:
            last_operations.append(operation)
    return last_operations


def print_info_to_client(data):
    """Выводит операции в требуемом формате"""
    for operation in data:
        oper_date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f')
        print(f"{oper_date.strftime('%d.%m.%Y')} {operation['description']}")
        try:
            print(f"{masks.get_masked_num(operation['from'])} -> {masks.get_masked_num(operation['to'])}")
        except:
            print(f"{masks.get_masked_num(operation['to'])}")
        print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")



