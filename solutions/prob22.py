# Problem 22
# Names score

n_file = open('extras/prob22_names.txt')

names = [string.replace('"', '') for string in str(n_file.read()).split(',')]

print(sum(map(lambda x, y: x * sum(((ord(ch) - 64) for ch in y)),
              [i for i in range(1, len(names) + 1)],
              sorted(names))))
