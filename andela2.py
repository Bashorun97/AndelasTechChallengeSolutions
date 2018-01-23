def multiples(nat_int):
    
    range_of_numbers = list(range(1, nat_int))
    lst = [i for i in range_of_numbers if i % 5 == 0 or i % 3 == 0]
    return lst

if __name__ == '__main__':
    nat_int = int(input("Enter a value: "))
    total = 0
    for i in multiples(nat_int):
        total += i
	print(total)
