import matplotlib.pyplot as plt
import numpy as np
##Import an entire module and specify an alias
paternal_age=[30,35,40,45,50,55,60,65,70,75]#input the parental age
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]#input the relative	risk for congenital	heart disease
offs = dict(zip(paternal_age, chd))#make a dicyionary of parental age and chd
print(offs)#output the dictionary
n = 10
x = paternal_age
y = chd
plt.scatter(x,y,marker='o')#draw a scatter plot according to the dictionary
plt.title("the effect of paternal age on offspring health")
plt.xlabel("paternal age")
plt.ylabel("chd")
plt.show()#output the scatter plot

ag=input()#input a parental age
age_order=paternal_age.index(int(ag))#Find the corresponding chd value
print(chd[age_order])#output the corresponding chd
