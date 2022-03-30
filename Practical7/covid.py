import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/xzy/IBI1_2021-22/Practical7")# importing the .csv file
covid_data = pd.read_csv("full_data(2).csv")
print(covid_data.iloc[9:20,[0,2]])#showing the first and third columns from rows 10-20 (inclusive)

#used a Boolean to show “total cases” for all rows corresponding to Afghanistan
my_row=[]
for i in range(7996):
    if covid_data.iloc[i,1]=="Afghanistan":#Determine if it's the country you're looking for
        my_row.append(True)
    else:
        my_row.append(False)
print(covid_data.loc[my_row,"total_cases"])

china_new_data=covid_data.iloc[1454:1546,[0,2,3]]
mean_new_case=np.mean(china_new_data.iloc[0: ,1])
mean_new_death=np.mean(china_new_data.iloc[0: ,2])#computed the mean number of new cases and new deaths in China
print(mean_new_case)
print(mean_new_death)

china_new_cases=china_new_data.iloc[0: ,1]
china_new_death=china_new_data.iloc[0: ,2]

#created a boxplot of new cases and new deaths in China worldwide
dt = pd.DataFrame({"china_new_cases": china_new_cases, "china_new_death": china_new_death})
plt.xlabel('object')
plt.ylabel('number')
plt.boxplot(x=dt.values,labels=dt.columns,
            vert=True,#Whether the boxplot needs to be placed vertically. By default, the boxplot should be placed vertically.
            whis = 1.5,#Specify the distance between the upper and lower quartiles. Default is 1.5 times the quartile difference
            patch_artist =True,#Whether to fill the box color
            meanline = False,#Is the mean represented by a line? By default, it is represented by a dot
            showbox=True,#Whether to display the box of the box diagram by default
            showcaps=True,#Whether to display the top and end lines of the boxplot, default display
            showfliers =False,#Whether to display outliers by default
            notch=True#Whether the boxplot is displayed in the form of notch, default non-notch
            )
plt.show()

# draw the plot of the data over time,and set different color and dot shape of each plot
china_dates=china_new_data.iloc[0: ,0]
plt.ylabel('number')
plt.xlabel('date')
plt.title('comparing new cases and new deaths in China')
plt.plot(china_dates,china_new_cases,'b+',label='China new cases') #"r" and "b" are the color of the points, "o" is the shape of plot pionts
plt.plot(china_dates,china_new_death,'ro',label='China new deaths')
plt.xticks(china_dates.iloc[0:len(china_dates):8],rotation=-30) #Interval of dates and rotate the dates
plt.legend()#show legend
plt.show()

#How have new cases and total cases developed over time in Germany?Plot the new numbers and total numbers of COVID cases over time in Germany.
germany_new_data=covid_data.iloc[2725:2817,[0,2,3]]
germany_dates=germany_new_data.iloc[0: ,0]
total_germany=0
everyday_total=[]
for i in range(92):
    total_germany=total_germany+int(germany_new_data.iloc[i,1])
    everyday_total.append(total_germany)#calculate the total data by myself
germany_new_cases=germany_new_data.iloc[0: ,1]
plt.ylabel('number')
plt.xlabel('date')
plt.title('comparing new cases and total cases in Germany')
plt.plot(germany_dates,germany_new_cases,'mD',label='Germany new cases')#"m" means magenta, "D"means rhombus
plt.plot(germany_dates,everyday_total,'yv',label='Germany total cases')#"y" means yellow, "v" means nabla
plt.xticks(germany_dates.iloc[0:len(germany_dates):8],rotation=-30)
plt.legend()
plt.show()





