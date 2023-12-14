from PIL import Image, ImageDraw, ImageFont
# Открытие изображения
image = Image.open("image1_NN.png")
# Создание объекта, позволяющего рисовать на изображении
draw = ImageDraw.Draw(image)
# Загрузка шрифта
font = ImageFont.truetype("arial.ttf", 18)
# Добавление текста в левом нижнем углу, заключенного в прямоугольник
text = "Побединский Архип"
text_color = "black"
background_color = "white"
text_position = (10, 10)
rectangle_size = draw.textbbox(text_position, text, font=font)
draw.rectangle(rectangle_size, fill=background_color)
draw.text(text_position, text, font=font, fill=text_color)
# Новое имя для сохранения подписанного изображения
new_name = 'image5_NN.jpg'
# Сохранение изображения под новым именем
image.save("image5_NN.jpg")
image.show()