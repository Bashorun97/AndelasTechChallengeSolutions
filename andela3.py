#This code was written by victor

import random


def generate_sum(no):
    result = []
    curr_result = 0
    while True:
        rand = random.randint(1, no)
        curr_result += rand
        if curr_result < 100:
            result.append(rand)
            continue # move on to the next loop
        elif curr_result > 100:
            remainder = 100 - sum(result)
            result.append(remainder)
        break
    return sorted(result)


if __name__ == '__main__':
    no = int(input('Enter a number between 0 & 30: '))
    if no >= 0 and no <= 30:
        answer = generate_sum(no)
        print('Answer = {}'.format(answer))        
    else:
        print("Your input must be between 0 & 30")
