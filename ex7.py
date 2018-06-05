def print_max(numbers):
    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number
    print("Max number is ", max_number)
print_max([1, 25, 56, 14])