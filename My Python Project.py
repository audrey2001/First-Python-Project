# start project
num= input('enter any number:')
first= '*' * int(len(num)/2)
second= num[:int(len(num)/2)]
third=  num[int(len(num)/2):]
fourth= ' ' *len(second)
print((second+first), '\n' + fourth + first + third)

# end project