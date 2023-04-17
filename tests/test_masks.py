import json
import os

from utils import masks, operations


def test_get_masked_num():
    assert (masks.get_masked_num("Счет 35383033474447895560")) == "Счет **5560"
    assert (masks.get_masked_num("MasterCard 7158300734726758")) == 'MasterCard 7158 30** **** 6758'
    assert (masks.get_masked_num("Счет 895560")) is None


def test_get_valid_operations():
        file_dir = os.path.dirname(os.path.abspath(__file__))
        test_data_path = os.path.join(file_dir, "../test_data/test_data.json")
        file_dir_result = os.path.dirname(os.path.abspath(__file__))
        test_data_path_result = os.path.join(file_dir_result, "../test_data/test_data_expected.json")
        with open(test_data_path_result, encoding="UTF-8") as f:
            result = json.load(f)
        assert operations.get_valid_operations(test_data_path) == result

        file_dir = os.path.dirname(os.path.abspath(__file__))
        test_data_path = os.path.join(file_dir, "../test_data/empty.json")
        assert operations.get_valid_operations(test_data_path) == 'Файл пустой'


def test_get_5_last_operations_info():
    file_dir = os.path.dirname(os.path.abspath(__file__))
    test_data_path = os.path.join(file_dir, "../test_data/test_data.json")
    data = operations.get_valid_operations(test_data_path)
    check = operations.get_5_last_operations_info(data)
    file_dir_result = os.path.dirname(os.path.abspath(__file__))
    test_data_path_result = os.path.join(file_dir_result, "../test_data/test_data_expected.json")
    with open(test_data_path_result, encoding="UTF-8") as f:
        result = json.load(f)
    assert check == result


def test_print_info_to_client():
    file_dir_result = os.path.dirname(os.path.abspath(__file__))
    test_data_path_result = os.path.join(file_dir_result, "../test_data/test_data_expected.json")
    with open(test_data_path_result, encoding="UTF-8") as f:
        result = json.load(f)
    correct = f"26.08.2019 Перевод организации\n" \
              f"Maestro 1596 83** **** 5199 -> Счет **9589\n" \
              f"31957.58 руб.\n\n"
    # operations.print_info_to_client(result))
    assert operations.print_info_to_client(result) == correct
