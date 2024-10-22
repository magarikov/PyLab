numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers = [(sum(numbers[:i]) + sum(numbers[(i+1):])) / len(numbers) if type(numbers[i]) != int else numbers[i] for i in range(len(numbers))]

print("Измененный список:", numbers)
