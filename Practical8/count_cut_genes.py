f=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
fout1 = open('countgene.fa','w')
EcoRI='GAATTC'
gene_order=0
seqs=[]
list_name=[]
for line in f:
    if line.startswith('>'):
        list_name.append(line)
        gene_order=gene_order+1
    if (line.startswith('>'))and (gene_order!=1):
        sum_1 = ''
        for seq in seqs:
            sum_1 = sum_1 + str(seq)
        sum_1 = sum_1.upper()
        seqs=[]
        i=0
        count=0
        while (i<=len(sum_1)-5) :
            i=i+1
            if sum_1[i:i+6]==EcoRI:
                count=count+1
                name_now=list_name[gene_order-2]
        if count!=0:
            j = 0
            genename = ""
            while name_now[j] != "_":
                genename = genename + name_now[j]
                j=j+1
            info1=str(genename)+str("        ")+str(count+1)+"\n"
            info2=str(sum_1)+"\n"
            fout1.write(info1)
            fout1.write(info2)
    if not line.startswith('>'):
        seqs.append(line.replace('\n',''))
f.close()
fout1.close()

