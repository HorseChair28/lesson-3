import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    jokes = []
    for i in range(num):
        rand_nouns = random.shuffle(nouns)
        rand_adverbs = random.choice(adverbs)
        rand_adjectives = random.choice(adjectives)
        jokes.append(f'{rand_nouns}, {rand_adverbs}, {rand_adjectives}')
    return jokes

print(get_jokes(3))



