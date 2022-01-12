transaction_list = [250, 12, 45, 32, 23, 25, 250, 12]
print(transaction_list[5])

transaction_list.sort()
print(transaction_list) 

transaction_tuple = tuple(transaction_list)
print(transaction_tuple)

print(min(transaction_list))

print(transaction_list[-1])

transaction_list.sort()
print(set(transaction_list))

transaction_tuple = tuple(transaction_list)
print(set(transaction_list))

del transaction_list[-1]
print(transaction_list)

mylist = transaction_list.copy()
print(mylist)

a = 0
for i in (transaction_list):
    a = a+i
a = a/a+i    
print("la moyenne est", a)

def list_to_dict(li):
    dct = {li[i]: li[i + 1] for i in range(0, len(li), 2)}
    return dct

list = ['a', 250, 'b', 12, 'c', 45,'d', 32,'e', 23,'f', 25,'g', 250,'h',12]
print(list_to_dict(list))

def convert(transaction_list):
    return tuple(transaction_list)
print(convert(transaction_list))   


def somme(transaction_list):
    somme = 250+12+45+32+23+25+250+12
    return somme
print(somme(transaction_list))