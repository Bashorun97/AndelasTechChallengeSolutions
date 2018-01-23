def fib(n, d):
    '''assumes n an int>= 0
    d is a dictionary of fibonacci as values
    returns Fibonacci of n'''

    if n in d:
        return d[n]
    else:
        ans = fib(n-1, d) + fib(n-2, d)
        d[n] = ans
        return ans

def fib_even_sum(fib_list):
    '''
    fib4
    '''

    even_list = []
    even_sum = 0
    for num in fib_list:
        if num % 2 == 0:
            even_list += [num]
            even_sum += num
    print("The evens are:", even_list)
    print()
    return even_sum

def fib_all(num):
    x = 1
    fib_list = []
    while True:
        if fib(x, d) <= num:
            fib_list.append(d[x])
            x += 1
        else:
            break
    print("list of fib numbers up to", num, "are:", fib_list)
    print()
    return "Sum of evens: " + str(fib_even_sum(fib_list))

d = {1:1, 2:2}
print(fib_all(4000000))
