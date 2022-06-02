eng_word = input('Введите число буквами: ')
trans_dic = {'zero': 'ноль',
             'one': 'один',
             'two': 'два',
             'three': 'три',
             'four': 'четыре',
             'five': 'пять',
             'six': 'шесть',
             'seven': 'семь',
             'eight': 'восемь',
             'nine': 'девять',
             'ten': 'десять'}


def num_translate(eng_word):
    return trans_dic.get(eng_word.lower())


def num_translate_adv(eng_word):
    capitell = trans_dic.get(eng_word.lower())
    if capitell:
        return capitell.capitalize() if eng_word[0].isupper() else capitell


print(num_translate(eng_word))
print(num_translate_adv(eng_word))
