def isPrime(num):

    inc = 2
    while inc < num:
        if num % inc == 0:
            return False
        inc += 1
    return True


def nthPrime(n):
    prime_dict = {1: 2, 2: 3}

    max_key_inc = max(dict.keys(prime_dict)) + 1
    max_value_inc = max(dict.values(prime_dict)) + 1
    done = False
    while max_key_inc <= n:
        while not done:
            if isPrime(max_value_inc):
                prime_dict[max_key_inc] = max_value_inc
                break
            max_value_inc += 1
        max_key_inc += 1
        max_value_inc = max(dict.values(prime_dict)) + 1
    return prime_dict[n]


if __name__ == '__main__':
        n = int(input("Enter a value: "))
        print(nthPrime(n))
