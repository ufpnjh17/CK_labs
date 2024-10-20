numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index = numbers.index(None)
mean_value = sum([num for num in numbers if num is not None]) / (len(numbers))
numbers[missing_index] = mean_value

print("Измененный список:", numbers)
