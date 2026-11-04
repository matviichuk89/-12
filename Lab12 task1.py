import random
s = input("Введіть рядок слів: ").split()
marks = [".", "!", "?", ","]
def find_repeated_words(words):
    repeated = []
    for word in words:
        if words.count(word) > 1 and word not in repeated:
            repeated.append(word)
    return repeated
repeated_words = find_repeated_words(s)
if repeated_words:
    print("Повторювані слова:", ", ".join(repeated_words))
else:
    print("Повторюваних слів не знайдено.")
def add_marks(words):
    for i in range(len(words)):
        words[i] += random.choice(marks)
    return words
s = add_marks(s)
print(" ".join(s))