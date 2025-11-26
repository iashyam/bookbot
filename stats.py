def count_words(book: str)->int:
    """ counts the number of words in the given string
        param: book(str) the string
        returns: num_words: int numgber of worlds"""

    num_words = len(book.split())
    return num_words

def count_letters(string: str)->dict:

    string = string.lower()
    count_dict = {}
    sorted(count_dict, key=lambda f: count_dict.values)
    for l in string:
        if l not in count_dict.keys():
            count_dict[l] = 0
        count_dict[l] += 1

    return count_dict

def sort_dictionary(count_dict: dict):
    sorted_dict = dict(sorted(count_dict.items(), reverse=True, key=lambda item: item[1]))
    return sorted_dict
