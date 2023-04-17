import json

from utils import masks, operations

def test_get_masked_num():
    assert (masks.get_masked_num("Счет 35383033474447895560")) == "Счет **5560"
    assert (masks.get_masked_num("MasterCard 7158300734726758")) == 'MasterCard 7158 30** **** 6758'
    assert (masks.get_masked_num("Счет 895560")) is None


def test_get_valid_operations():
    with open('/test_data/test_data.json', encoding="UTF-8") as f:
        oper_list = json.load(f)
    assert (operations.get_valid_operations(oper_list['test_data'])) == oper_list['expected_result']

def test_get_5_last_operations_info():
    pass


def test_print_info_to_client():
    pass