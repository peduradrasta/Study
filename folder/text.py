import re

mail = 'vasya@yandex.ru'

pattern = re.compile('@(\w.+)')

print(pattern.findall(mail))
['yandex.ru']
