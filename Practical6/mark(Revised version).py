marks=[45,36,86,57,53,92,65,45]#input the mark

print(sorted(marks))#output the sorted mark
from numpy import*
import numpy as np
import matplotlib.pyplot as plt
#Import an entire module and specify an alias
n=8
plt.boxplot(marks,
            vert=True,#Whether the boxplot needs to be placed vertically. By default, the boxplot should be placed vertically.
            whis = 1.5,#Specify the distance between the upper and lower quartiles. Default is 1.5 times the quartile difference
            patch_artist =True,#Whether to fill the box color
            meanline = False,#Is the mean represented by a line? By default, it is represented by a dot
            showbox=True,#Whether to display the box of the box diagram by default
            showcaps=True,#Whether to display the top and end lines of the boxplot, default display
            showfliers =True,#Whether to display outliers by default
            notch=False#Whether the boxplot is displayed in the form of notch, default non-notch
              )
plt.title("Rob marks")
plt.xlabel("Rob")
plt.ylabel("mark")
plt.show()#output the boxplot
if mean(marks)<60:
    print("Rob failed this ICA")
else:
    print("Rob passed this ICA")
#Rob failed this ICA