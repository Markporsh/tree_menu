import functools
import time
from django.db import reset_queries, connection


def queries_counter(func):
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()
        start_queries = len(connection.queries)
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        end_queries = len(connection.queries)
        print(f"Количество запросов : {end_queries - start_queries}")
        print(f"Скорость выполнения запросов : {(end_time - start_time):.2f}s")
        return result
    return inner_func

