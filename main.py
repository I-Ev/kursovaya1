from utils import operations as op

file = "data/operations.json"

operations = op.get_valid_operations(file)
last_operations = op.get_5_last_operations_info(operations)

op.print_info_to_client(last_operations)