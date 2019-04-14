import random
from code_jam.crypto_pangrams.solution3 import solve


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
        return True


def get_primes(N):
    primes = []
    for i in range(2, N + 1):
        if is_prime(i):
            primes.append(i)
    return primes


alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']

for testround in range(500):
    if testround % 100 == 0:
        print("test round:", testround)

    N = random.randint(103, 10000)
    primes = get_primes(N)
    picked_primes = random.sample(primes, 26)
    picked_primes.sort()
    cipher_map = dict(zip(alphabets, picked_primes))

    plain_text_list = []
    for letter in alphabets:
        count = random.randint(1, 3)
        for i in range(count):
            plain_text_list.append(letter)
    random.shuffle(plain_text_list)
    plain_text = "".join(plain_text_list)  # 정답

    cipher_text_list = []
    for i in range(1, len(plain_text_list)):
        cipher_text_list.append(str(cipher_map[plain_text_list[i - 1]] * cipher_map[plain_text_list[i]]))
    cipher_text = " ".join(cipher_text_list)  # 문제
    L = len(cipher_text_list)

    print_texts = []
    print_texts.append("<Question>")
    print_texts.append("\n{} {}".format(N, L))
    print_texts.append("\n" + cipher_text)

    print_texts.append("\n<Answer>")
    print_texts.append("\n" + plain_text)
    print_texts.append("\n%s" % cipher_map)

    solved_text = solve(N, L, cipher_text_list)

    print_texts.append("\n====================================")

    if solved_text == plain_text:
        print_texts.append("\nCorrect !!!\nAnswer : %s" % solved_text)
        # print("".join(print_texts))
        print("Correct")
    else:
        print_texts.append("\nWrong Answer")
        print_texts.append("\nSubmit Answer  : %s" % solved_text)
        print_texts.append("\nCorrect Answer : %s" % plain_text)
        print("".join(print_texts))
        # print(cipher_map)
        break
