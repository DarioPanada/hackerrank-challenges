"""
Word Order Problem

https://www.hackerrank.com/challenges/word-order/problem
"""
num_words = int(input())

words = []
word_count = {}

for _ in range(num_words):
    word = input()

    try:
        word_count[word] += 1
    except KeyError:
        words.append(word)
        word_count[word] = 1

print(len(words))
print(" ".join(map(str, [word_count[w] for w in words])))
