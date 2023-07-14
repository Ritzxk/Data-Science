# swap two number given in a string seperated by comma
inp_str = input()
inp_list = inp_str.split(',')

# assaigning number to x and y
x = int(inp_list[0])
y = int(inp_list[1])

# printing values before swapping
print(f'value of x before swpping : {x}')
print(f'value of y before swpping : {y}')

# swapping values of x and y
temp = x
x = y
y = temp

# printing values after swapping
print(f'x after swapping: {x}')
print(f'y after swapping : {y}')