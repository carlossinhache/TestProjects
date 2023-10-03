def add_dots(string):
    dotted_string = ""
    for char in string:
        dotted_string += char + "."
    dotted_string = dotted_string[:-1]
    return dotted_string


def remove_dots(string):
    no_dotted_string = ""
    for char in string:
        if char is not ".":
            no_dotted_string += char
    return no_dotted_string


string = "hello"
print(add_dots(string))
print(remove_dots(string))


# the short way
# def add_dots(s):
#     return ".".join(s)
#
# def remove_dots(s):
#     return s.replace(".", "")