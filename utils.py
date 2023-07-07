def delete_exp(number):
    string_number = str(number)
    index = None

    if 'e-' in string_number:
        index = string_number.index('-') - 1
        return string_number[:index]
    return number