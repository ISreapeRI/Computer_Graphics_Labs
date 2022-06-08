import os
from PIL import Image, ImageEnhance

'''

Для работы программы без изменений, требуется поместить файл программы в каталог, в котором могут находиться другие
директории и файлы формата .jpg.

'''

thresh = 150
photos = []
files_count = 0

for root, dirs, files in os.walk("."):
    files_count += len(files)
    for file in files:
        if file.endswith(".jpg"):
            create_file = True
            if file.endswith(f"_byn_thresh_{thresh}.jpg"):
                create_file = False
                os.remove(os.path.join(root, file))
            elif file.endswith("_constrast.jpg"):
                create_file = False
                os.remove(os.path.join(root, file))

            if create_file:
                photos.append(os.path.join(root, file))
                print(os.path.join(root, file))

print(f"Колличество файлов в директории и поддиректориях: {len(photos)}") # Выводит количество файлов с форматом .jpg

for i in range(len(photos)):
    photo = Image.open(photos[i])
    photo.show()

    # Преобразование в бинарный формат

    fn = lambda x: 255 if x > thresh else 0
    photo_byn = photo.convert('L').point(fn, mode='1')

    photo_byn.save(photos[i][:-4] + f"_byn_thresh_{thresh}.jpg")
    photo_byn.show()

    # Контрастирование изображения

    Enchancer_object = ImageEnhance.Contrast(photo)
    photos_contrast = Enchancer_object.enhance(2.2)

    photos_contrast.save(photos[i][:-4] + "_constrast.jpg")
    photos_contrast.show()
