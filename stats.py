def count_words(text):
#    word_count = 0
    splitted_text = text.split()
    # for i in splitted_text:
    #     if i.isalpha():
    #         word_count += 1
    #return word_count
    num_words = len(splitted_text)
    return num_words



def count_chars(text):
    text_lowercase = text.lower()
    char_list = set(text_lowercase)
    char_dict = {char:0 for char in char_list}

    for char in text_lowercase:
        if char in char_dict:
            char_dict[char] += 1
    
    return char_dict



def sorted_list(dict):
    sorted_list = []

    for k, i in dict.items():
        sorted_list.append({"char": k, "num":i})
        sorted_list = sorted(sorted_list, key=lambda x: x["num"], reverse= True)
        
    return sorted_list

