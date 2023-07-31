#HW «Decorators»

from ex1 import test_1
from ex2 import test_2
from ex3 import test_3


def print_task_header(title, n=25):
    print('\n', '-' * n, 'Задание - ' + title, '-' * n)


if __name__ == '__main__':
    print_task_header('1')
    test_1()
    print_task_header('2')
    test_2()
    print_task_header('3')
    test_3()
