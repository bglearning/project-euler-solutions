# Coded Triangle Numbers


def calculate_word_value(word):
    value = 0
    for char in word:
        value += ord(char) - ord('A') + 1
    return value

words = []
with open('../resources/p042_words.txt') as f:
    words = [word[1:-1:] for line in f for word in line.split(',')]

triangular_nums = [False] * 1000

tri_num = 1
n = 1

while tri_num <= 1000:
    triangular_nums[tri_num - 1] = True
    n += 1
    tri_num += n

print(sum(1 for w in words if triangular_nums[calculate_word_value(w) - 1]))
