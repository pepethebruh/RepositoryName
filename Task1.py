numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers_without_none_list = numbers[0:4] + numbers[5:] #Создание списка без слова none
average = sum(numbers_without_none_list) / len(numbers) #Нахождение среднего арифметического
numbers[4] = average #Замена изначального списка на новый с правильным значением

print("Измененный список:", numbers )
