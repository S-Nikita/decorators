import datetime
import os
import sys

# Настройка кодировки для работы с кириллицей
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

file_name = 'log.txt'
path = f'{os.getcwd()}/logs/{file_name}'

# Фабрика декораторов
def logger(path):


    def _logger(some_function):


        def log_func_calculation(*args, **kwargs):
            # Получение значений параметров для записи в лог файл
            calculation_start_dt = datetime.datetime.now()
            name = some_function.__name__
            arguments = args
            result = some_function(*args, **kwargs)
            
            # Запись информации в файл путем добавления новых строк
            with open(path, mode='a', encoding='utf-8') as f:
                f.write(f'Дата начала расчета: {calculation_start_dt} \n')
                f.write(f'Название рассчитываемой функции: {name} \n')
                f.write(f'Аргументы, передаваемые функции как входные значения: {arguments} \n\n')
                f.close()


            return result


        return log_func_calculation


    return _logger

# Вызов декоратара для функции flat_generator
@logger(path)
def flat_generator(some_nested_list):
    start = 0
    end = len(some_nested_list)
    while start < end:
        for item in some_nested_list[start]:
            yield item
        start += 1
# Вывод результата работы функции в консоль
for item in flat_generator(nested_list):
    print(item)
