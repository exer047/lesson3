def find_max(number_list):
    maximum_number = number_list[0]
    for i in range(len(number_list)):
        if number_list[i] > maximum_number:
            maximum_number = number_list[i]
    print("Maximum number is: ", maximum_number)
    return maximum_number

find_max([4, 5, 2, 23, 5])

