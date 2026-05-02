"""Day 11 — Error Handling"""

# Define an AppError base exception and two subclasses: ValidationError and NotFoundError

class AppError(Exception):
    pass


class ValidationError(AppError):
    pass


class NotFoundError(AppError):
    def __init__(self, name):
        super().__init__(f"User '{name}' not found.")


# Write a function safe_divide(a, b) that:
# Returns the float result of a / b
# Returns None if b is zero
# Returns None if either input is not a number (catch TypeError)
# Uses else to return the result (not inside try)
def safe_divide(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        return None
    else:
        return result


# Write a function create_user(name, age) that:
# Raises ValidationError if name is an empty string
# Raises ValidationError if age is not between 0 and 150 (inclusive)
# Raises TypeError if age is not an int
# Returns a dict {"name": name, "age": age} if all valid
def create_user(name, age):
    if (not name) or (not name.strip()): raise ValidationError("Name is empty")

    if not isinstance(age, int): raise TypeError("Age is not an integer")

    if not (0 <= age <= 150): raise ValidationError("Age should be between 1 and 150")

    return {"name": name, "age": age}

# Write a find_user(users, name) function that takes a list of user dicts and
# raises NotFoundError if no match is found, otherwise returns the matching dict
# Update your tests to use pytest.raises(ValidationError) etc.
def find_users(users, name):
    result = list(filter(lambda p: p["name"] == name, users))
    if not result: raise NotFoundError(name)
    return result[0]
