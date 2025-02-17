#1
def compute_power(x, y):
    i = 1
    z = x
    while i < y:
            z = x * z
            i += 1
    return(z)

print(compute_power(2, 4))


#2
def temperatureRange(list):
    high = max(list)
    low = min(list)
    return(low, high)


tempList = (9, 14, 29, 12, 6, 22, 19)
print(temperatureRange(tempList))


#3
def weekendCheck(day):
    if day == 6 or day == 7:
        return(True)
    else:
        return(False)
    
print(weekendCheck(7))
print(weekendCheck(2))


#4
def fuel_efficiency(distance, fuel):
    efficiency = distance / fuel
    return(efficiency)

print(fuel_efficiency(90.77, 24.28))


#5
def last_to_first(int):
    last = int % 10
    int_no_last = int // 10
    int_no_last_length = 1
    while int_no_last // 10 != 0:
        int_no_last //= 10
        int_no_last_length += 1
    int_no_last = int // 10
    new_int = last * (10 ** int_no_last_length) + int_no_last
    return(new_int)
    
print(last_to_first(847619))


#6.1
def minFor(input):
    min = input[0]
    for num in input:
        if num < min:
            min = num
    return(min)

def maxFor(input):
    max = input[0]
    for num in input:
        if num > max:
            max = num
    return(max)

number_list = [20, 305481, 93712, 4719, 12, 985]
print(minFor(number_list))
print(maxFor(number_list))


#6.2
def minWhile(input):
    min = sum(input)
    i = 0
    current_num = input[i]
    while current_num != input[-1]:
        current_num = input[i]
        if current_num < min:
            min = current_num
        i = i+1
    return(min)

def maxWhile(input):
    max = 0
    i = 0
    current_num = input[i]
    while current_num != input[-1]:
        current_num = input[i]
        if current_num > max:
            max = current_num
        i = i+1
    return(max)

print(minWhile(number_list))
print(maxWhile(number_list))


#7
def vowels_consonants(string):
     vowel_count = 0
     consonant_count = 0
     other_count = 0
     for letter in string:
        if letter.isalpha():
            if letter == "A" or letter == "a" or letter == "E" or letter == "e" or letter == "I" or letter == "i" or letter == "O" or letter == "o" or letter == "U" or letter == "u":
                vowel_count += 1
            else:
                consonant_count += 1
        else:
            other_count += 1
     return(vowel_count, consonant_count)

print(vowels_consonants("Physics 5A is going to make me need antidepressants!"))


#8
def sum_of_digits(input):
    sum = 0
    new_int = str(input)
    for num in new_int:
        new_num = int(num)
        sum += new_num
    return(sum)

print(sum_of_digits(12345))
