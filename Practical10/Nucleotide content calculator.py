def percent(x):
    percent_base=[0,0,0,0]
    number_base=[0,0,0,0]
    for i in range(len(x)):
        if x[i]=="A":
            number_base[0]=number_base[0]+1
        elif x[i]=="T":
            number_base[1] = number_base[1] + 1
        elif x[i]=="C":
            number_base[2] = number_base[2] + 1
        else:
            number_base[3] = number_base[3] + 1
    for i in range(4):
        percent_base[i]=number_base[i]/len(x)
    return percent_base
strand=input()
strand =strand.upper()
result=percent(strand)
print("the percent of A is", str(result[0]))
print("the percent of T is", str(result[1]))
print("the percent of C is", str(result[2]))
print("the percent of G is", str(result[3]))
