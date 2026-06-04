import time

def log_execution(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[LOG] {func.__name__} wykonane w {end-start:.4f}s")
        return result
    return wrapper

def sample_generator(samples):
    for sample in samples:
        yield sample
