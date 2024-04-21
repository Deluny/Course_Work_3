import json

from src.dto import Operation


def get_operations(filename) -> list[Operation]:
    """
    Функция, получающая список операций из json файла
    :rtype: object
    """
    operations: list[Operation] = []
    with open(filename, encoding='utf-8') as f:
        for data in json.load(f):
            if data:
                op = Operation.init_from_dict(data)
                operations.append(op)
    return operations


def filter_operations_by_state(*operations: Operation, state: str) -> list[Operation]:
    filtered_operations: list[Operation] = []
    for operation in operations:
        if operation.state == state:
            filtered_operations.append(operation)
    return filtered_operations


def sort_operations_by_date(*operations):
    return sorted(operations, key=lambda op: op.operation_date, reverse=True)
