def add(numbers):
    if numbers == "":
        return 0
    elif numbers.count(',') == 0:
        return int(numbers)
    else:
        return sum(list(eval(numbers)))