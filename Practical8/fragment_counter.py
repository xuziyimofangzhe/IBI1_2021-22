seq ='ATGCAATCGACTACGATCAATCGAGGGCC'
count=0
for i in range(len(seq)-5):
    if seq[i:i+6]=="GAATTC":
        count=count+1
print('the total number of fragments is', count)
