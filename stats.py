def get_num_words(file_contents):
    split_contents = file_contents.split()
    return len(split_contents)


def get_char_count(file_contents):
    split_contents = file_contents.split()
    full_dict = {}
    for word in split_contents:
        for value in word:
            if value.lower() not in full_dict:
                full_dict[value.lower()] = 1
            else:
                full_dict[value.lower()] += 1
    return full_dict


def sort_on(items):
    return items["num"]

def get_sorted_list(file_contents):
    full_dict = get_char_count(file_contents)
    sorted_list = []
    for value in full_dict:
        if value.isalpha():
            temp_dict = {}
            temp_dict["char"] = value
            temp_dict["num"] = full_dict[value]
            sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list