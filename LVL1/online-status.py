statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def online_count(my_dict):
    online_num = 0
    for key in my_dict:
        if my_dict[key] == "online":
            online_num +=1
    return online_num


print(online_count(statuses))

