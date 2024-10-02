def log(filename=None):
    """Декоратор, автоматически логирует выполнение функции."""

    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                result = None

            if filename:
                with open(filename, "a") as f:
                    f.write(log_message + "\n")
            else:
                print(log_message)

            return result

        return inner

    return wrapper


# if __name__ == "__main__":
#
#     @log(filename="mylog.txt")
#     def my_function(x, y):
#         """Функция сложения для использования с декоратором log"""
#         return x + y
#
#     my_function(1, 2)
