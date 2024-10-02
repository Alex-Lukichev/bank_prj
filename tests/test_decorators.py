from src.decorators import log


# Образцы функций для тестирования декоратора log
@log()
def my_function(x, y):
    return x + y


@log()
def another_function(a, b):
    return a / b


# Тесты
def test_log_successful_function(capsys):
    """Тест декоратора на возврат сообщения my_function ok"""
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out.strip() == "my_function ok"


def test_log_function_exception(capsys):
    """Тест декоратора на обработку исключения"""
    another_function(3, 0)
    captured = capsys.readouterr()
    assert "another_function error: ZeroDivisionError. Inputs: (3, 0), {}" in captured.out.strip()
