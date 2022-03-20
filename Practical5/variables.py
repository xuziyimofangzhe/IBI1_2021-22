a=19245301#the number of cases of COVID-19 in the UK since the pandemic began
b=4218520#the number of cases of COVID-19 in 2021
c=271#the number of cases of COVID-19 in 2020
d=b-c#the difference between the numbers of	cases in 2020 and 2021
e=a-b#the difference between the numbers of	cases in 2021 and 2022
#the	rate	of	new	cases	greater	in 2021
if d>e :
    print("the rate of new case in 2020 is greater")
else:
    print("the rate of new case in 2021 is greater")#Compare d to e and output the year has the greater new case number
#comment: we can find that 2022 has the greatest number of COVID-19 cases
X=input()#input a boolean variable X
Y=input()#input a boolean variable Y
W=X and Y#W encodes	the	Boolean	variable that encodes	“X	and	Y”
print(W)#output W

