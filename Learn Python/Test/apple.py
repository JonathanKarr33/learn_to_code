num_list = [1,2,3,4]
new_list = []
for i in range (len(num_list)):
    j=0
    product = 1
    while (j<i):
        product *= num_list[j]
        j+=1
    j+=1
    while (j < len(num_list)):
        product *= num_list[j]
        j+=1
    new_list.append(product)
    print(new_list)
print(new_list)
