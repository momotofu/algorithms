def ransom_note(magazine, ransom):
    ransom_hash = create_word_hash_table(ransom)
    magazine_hash = create_word_hash_table(magazine)

    for key in ransom_hash:
        if not key in magazine_hash or not ransom_hash[key] - magazine_hash[key] <= 0:
            return False
    return True


def create_word_hash_table(string_array):
    dictionary = {}

    for el in string_array:
        if el in dictionary:
            dictionary[el] += 1
        else:
            dictionary[el] = 1
    return dictionary
