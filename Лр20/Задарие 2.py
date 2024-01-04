import urllib.parse

# Задание 1
url = "https://inbusiness.kz/ru"  # Замените на URL новостной статьи
parsed_url = urllib.parse.urlparse(url)
print(f"Разобранный URL: {parsed_url}")

# Элементы кортежа:
# scheme: протокол URL (например, 'http' или 'https')
# netloc: сетевое местоположение (обычно доменное имя)
# path: путь к ресурсу на сервере
# params: параметры для ресурса (редко используется)
# query: строка запроса, часто используется для передачи данных методом GET
# fragment: фрагмент URL, указывающий на часть ресурса

# Задание 2
# Протокол уже включен в разобранный URL (это 'scheme')

# Задание 3
reconstructed_url = urllib.parse.urlunparse(parsed_url)
print(f"Восстановленный URL: {reconstructed_url}")