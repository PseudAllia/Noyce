import random
from timeit import timeit


def factorial(n:int) -> int:
    number = 1
    for i in range(n):
        number *= (i+1)
    return number

def shuffle(name:str) -> int:
    count = len(name)
    characters = set(name)

    repetitions = []
    sum = 1

    for i in characters:
        repetitions.append(name.count(i))

    for i in repetitions:
        sum *= factorial(i)

    return int(factorial(count) / sum)


def generate_permutations(name: str):
    check = shuffle(name)
    chars = []
    print(check)

    for i in name:
        chars.append(i)

    words = []
    master_count = 0
    while True:
        master_count += 1
        word = ''
        chars_copy = chars.copy()
        for i in range(len(chars_copy)):
            curr = random.randint(0, len(chars_copy) - 1)
            word += chars_copy[curr]
            chars_copy.pop(curr)

        if word not in words:
            words.append(word)

        if len(words) == check:
            break

    return words, master_count


if __name__ == '__main__':
    # name = input('Enter a name: ')
    # a, b = generate_permutations(name)
    # print(b)
    # print(a)

    print(
        timeit(
            lambda:
            generate_permutations('sonyaaa'), number=100
        )
        )
