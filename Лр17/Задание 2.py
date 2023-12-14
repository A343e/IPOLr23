from PIL import Image

# Задание
image1 = Image.open('image1_NN.png')
# Поворот изображения на 20 градусов по часовой стрелке
image2 = image1.rotate(-20)
image2.save('image2_NN.jpg')

image2.show()