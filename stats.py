def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    char_count = {}
    for c in text:
        lower_c = c.lower()
        if (lower_c in char_count):
            char_count[lower_c] += 1
        else:
            char_count[lower_c] = 1
    return char_count

def analyse_char_count(char_count):
    sorted_list = []
    for k,v in char_count.items():
        if (not k.isalpha()):
            continue
        dict = {"char": k, "count": v}
        sorted_list.append(dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(dict):
    return dict["count"]
    