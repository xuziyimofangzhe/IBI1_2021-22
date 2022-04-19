def num(total_money,price):
    number=total_money//price
    left=total_money-number*price
    print(number,left)
    return
tot_money=input()
pri=input()
num(int(tot_money),int(pri))

