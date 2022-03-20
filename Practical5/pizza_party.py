# pseudocode:
# begin with no cut
# if the number of the pieces of the pizza is less than what we need
#  have one more cut and output the total piece now
#  if still cannot meet our requirement
#  repeat the above command
#  if the number of the pieces of the pizza is enough, the program ends
i=0
while (i*i+i+2)/2<64: #If the total is still less than 64
    i=i+1 #one more cut
    print("The pizza was cut",i,"times and divided into",(i*i+i+2)/2,"pieces")#Print the number of pizza slices at this point