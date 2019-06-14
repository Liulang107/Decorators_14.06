from datetime import datetime
import random

def path_log(path):
    def logger(old_function):
        def new_function(*args, **kwargs):
            start_time = datetime.now()
            result = old_function(*args, **kwargs)
            with open(path, 'a') as file:
                file.write(f'Функция {old_function.__name__} \n'
                       f'Время запуска функции: {start_time}; \n'
                       f'Аргументы: {str(args) [1:-1].rstrip(",")}; \n'
                       f'Возвращаемое значение: {result}.\n')
            return result
        return new_function
    return logger

@path_log('logs.txt')
def summ(*args, **kwargs):
    return sum(args)

if __name__ == '__main__':
    summ(*[random.randrange(1, 100) for _ in range(100)])