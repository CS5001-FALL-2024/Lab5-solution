def print_tri(num: int):
    if num == 0:
        print ("0\n")
    else:
        print_tri(num-1)
        for i in range(num):
            print (i,end=" ")
        print()
        print_tri(num-1)

print_tri(5)
    