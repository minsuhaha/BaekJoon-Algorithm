words = input()

def prime(words):
    total = 0
    for word in words:
        # word 글자가 소문자이면
        if word.islower():
            total += ord(word) - 96
        else:
            total += ord(word) - 38

    for i in range(2, total):
        if total % i == 0:
            return print('It is not a prime word.')
    return print('It is a prime word.')

prime(words)