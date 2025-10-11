
import random, string

def gen_email(first="egor", last="testov", cohort="1999", domain="yandex.ru"):
    # имя_фамилия_номер_случайные3цифры@домен
    return f"{first}_{last}_{cohort}_{random.randint(100,999)}@{domain}"

def gen_password(n=8):
    n = max(6, n)
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(n))
