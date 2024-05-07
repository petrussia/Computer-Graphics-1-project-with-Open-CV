import cv2
import os
import sys


def check_for_input(folder_path):
    # Делаем проверки, чтобы питончик сильно не ругался
    if any(ord(char) > 127 for char in folder_path):
        print("Yours path includes russian symbols.")
        sys.exit(1)
    if not os.path.exists(folder_path):
        print("Entered path does not exist.")
        sys.exit(1)


def picture_saturation(path_to_image):
    # Грузим нашу картинку в RGB
    image = cv2.imread(path_to_image, cv2.IMREAD_COLOR)
    # Преобразуем RGB в HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Разделяем HSV на каналы
    hue, satiation, value = cv2.split(hsv_image)
    # Считаем среднюю насыщенность у каждого изображения
    mean_saturation_of_image = satiation.mean()

    return mean_saturation_of_image


def sort_list_of_pictures():
    list_of_files = os.listdir(path)

    # Создание списка для хранения результата нашей сортировки
    result_list = []

    # Обработка каждой фотографии в папке
    for file in list_of_files:
        # Полный путь к файлу
        file_path = os.path.join(path, file)

        # Вычисление насыщенности изображения
        saturation = picture_saturation(file_path)

        # Добавление результатов в список
        result_list.append((file, saturation))

    # Сортировка списка результатов по возрастанию насыщенности
    sorted_list = sorted(result_list, key=lambda x: x[1])
    return sorted_list


def output_pictures(sorted_list):
    for i, f in enumerate(sorted_list):
        # Генерируем новое имя файла в формате "цифра.расширение"
        new_name = str(-i - 1) + ".jpg"

        # Полный путь к старому файлу
        old_path = os.path.join(path, f[0])

        # Полный путь к новому файлу
        new_path = os.path.join(path, new_name)

        # Переименовываем файл
        os.rename(old_path, new_path)

    for i, f in enumerate(sorted_list):
        # Генерируем новое имя файла в формате "цифра.расширение"
        new_name = str(i + 1) + ".jpg"

        # Полный путь к старому файлу
        old_path = os.path.join(path, str(-i - 1) + ".jpg")

        # Полный путь к новому файлу
        new_path = os.path.join(path, new_name)

        # Переименовываем файл
        os.rename(old_path, new_path)

    print("Sorting of pictures finished successfully!")


# Вызываем все наши функции
path = input("Please, enter an absolute or relative path to the directory without Russian characters: ")

check_for_input(path)

output_pictures(sort_list_of_pictures())
