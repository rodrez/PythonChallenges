import re

def password_check(password):
    """
    :param password: pass in the password to be tested
    :return: none if the password does not match the criteria
    """
    password_pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")
    a = password_pattern.search(password)
    return a

def email_check(email):
    """
    :param email: pass in the email to be tested
    :return: none if the password does not match the criteria
    """
    email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    b = email_pattern.search(email)
    return b

print(password_check(''))
print(email_check(''))
