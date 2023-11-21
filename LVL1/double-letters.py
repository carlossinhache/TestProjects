def double_letters(str):
    str_lower = str.lower()
    lettr = ""
    for letter in str_lower:
        if letter == lettr:
            return True
        lettr = letter
    return False


string = "nonunionn"
print(double_letters(string))