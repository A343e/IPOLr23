from PIL import Image
from PIL import ImageFilter

image3 = Image.open('image3_NN.jpg')
# Применение фильтра к изображению
image4 = image3.filter(ImageFilter.FIND_EDGES)
image4.save('image4_NN.jpg')

# Применение нескольких фильтров к изображению
image44 = image3.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.SMOOTH)
image44.save('image44_NN.jpg')
image44.show()