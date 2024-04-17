from src.utils import get_operations, filter_operations_by_state, sort_operations_by_date


def main(filename):
    operations = get_operations('operations.json')
    operations = filter_operations_by_state(*operations, state='EXECUTED')
    operations = sort_operations_by_date(*operations)

    for op in operations[:5]:
        print(op.safe())
        print()


if __name__ == '__main__':
    main('operations.json')
