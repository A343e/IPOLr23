from PIL import Image

# Задание
image2 = Image.open('image2_NN.jpg')
# Обрезка изображения (замените координаты на нужные вам)
left = 100
top = 100
right = 300
bottom = 300
image3 = image2.crop((left, top, right, bottom))
image3.save('image3_NN.jpg')
image3.show()