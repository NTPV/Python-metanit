#Генерация 8 значного пароля

import secrets
import string

alphabet = string.ascii_letters + string.digits
password = ''
for x in range(8):
    password = password + secrets.choice(alphabet)

print(password)
