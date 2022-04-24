def num(total_money,price):
    number=total_money//price
    left=total_money%price
    return number,left
tot_money=input()
pri=input()
result=num(int(tot_money),int(pri))
print(result[0],result[1])
