import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.vtb.by/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

exchange_rates = soup.find_all('div', class_='exchange-rate')

# Создаем и открываем файл CSV для записи данных.
with open('exchange_rates.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for rate in exchange_rates:
        currency = rate.find('div', class_='currency').text
        value = rate.find('div', class_='value').text
        writer.writerow([currency, value])