from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀You calling {func.__name__}({args}, {kwargs})")
        result =  func(*args, **kwargs)
        print(f"✅{func.__name__} returned {result}")
        return result
    return wrapper


@log_activity
def brew_chai(type):
    print(f"Brewing {type} chai")


brew_chai("black")