from PIL import Image

# Открываем изображение
img = Image.open('чына.jpg')

# Отображаем изображение
img.show()

# Сохраняем изображение в другом формате
img.save('image1_NN.png')

# Выводим характеристики изображения
print(f'Формат: {img.format}')
print(f'Размер: {img.size}')
print(f'Цветовой режим: {img.mode}')