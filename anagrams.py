def is_anagram(str1, str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if sorted_str1 == sorted_str2:
        return True
    return False


print(is_anagram("lol", "oll"))