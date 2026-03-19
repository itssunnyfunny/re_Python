from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role == "admin":
            return func(user_role) #return None
        else:
            return print("Access denied")
    return wrapper


@require_admin
def access_tea_inverntory(role):
    print("Access granted to tea inventory")


access_tea_inverntory("admin")
access_tea_inverntory("user")