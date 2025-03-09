def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_character_count(text):
    character_dict = {}
    for word in text.split():
        for char in word.lower():
            if character_dict.get(char):
                curr_count = character_dict[char]
                curr_count += 1
                character_dict[char] = curr_count
            else:
                character_dict[char] = 1
    return character_dict

def character_report(report_dict):
    sorted_dict_list = []
    keys_list = []
    for key, _ in report_dict.items():
        if key.isalpha():
            keys_list.append(key)

    keys_list.sort()

    for key in keys_list:
        sorted_dict_list.append({key: report_dict[key]})
    return sorted_dict_list