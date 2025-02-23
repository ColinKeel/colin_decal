#1
# Number_list.append(i), error: name 'Number_list' is not defined, fixed by changing "Number_list.append(i)" to "Number_list_0_to_20.append(i)"
# for i in range(1:26):, error: invalid syntax, fixed by changing "for i in range(1:26):" to "for i in range(26):"


#2.1
Number_list_0_to_20 = list()

for i in range(21):
    Number_list_0_to_20.append(i)

print(Number_list_0_to_20)


#2.2
Number_list_squared = list()

for i in Number_list_0_to_20:
    Number_list_squared.append(i**2)

print(Number_list_squared)


#2.3
Num_list_squared_first_15 = Number_list_squared[0:16]

print(Num_list_squared_first_15)


#2.4
Num_list_squared_every_5 = Number_list_squared[0:21:5]

print(Num_list_squared_every_5)


#2.5
Num_list_idk_what_to_name_this_its_the_one_with_a_lot_going_on = list()
Num_list_squared_every_3 = Number_list_squared[21:0:-3]

for i in Num_list_squared_every_3:
    Num_list_idk_what_to_name_this_its_the_one_with_a_lot_going_on.append(i)

print(Num_list_idk_what_to_name_this_its_the_one_with_a_lot_going_on)


#3.1
matrix = list()
num_0_to_25 = list()
x = 1
y = 1
z = 6

for i in range(26):
    num_0_to_25.append(i)

while x <= 5:
    matrix.append(list(num_0_to_25[y:z]))
    y += 5
    z += 5
    x += 1

print(matrix)


#3.2
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 3 == 0:
            matrix[i][j] = "?"

print(matrix)


#3.3
new_list = list()
sum_new_list = 0
new_list = matrix

for i in range(len(new_list)):
    for j in range(len(new_list[i])):
        if new_list[i][j] != "?":
            sum_new_list += new_list[i][j]

print(sum_new_list)