from passlib.context import CryptContext

from config.settings import admin_settings

password_context = CryptContext(schemes="bcrypt", deprecated="auto")


def bcrypt_password(password):
    return password_context.hash(password)


def verify_password(password, hashed_password):
    return password_context.verify(password, hashed_password)


def verify_admin_data(email, password):
    if email == admin_settings.admin_email \
            and password == admin_settings.admin_password:
        return True
    return False