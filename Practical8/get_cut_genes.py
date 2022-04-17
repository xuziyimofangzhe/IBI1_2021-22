f=open("C:/Users/xzy/IBI1_2021-22/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
fout = open('C:/Users/xzy/IBI1_2021-22/Practical8/cut_genes.fa','w')
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
        judge=True
        while (i<=len(sum_1)-5) and judge:
            i=i+1
            if sum_1[i:i+6]==EcoRI:
                judge=False
                name_now=list_name[gene_order-2]
                j=0
                genename=""
                while name_now[j]!="_":
                    genename=genename+name_now[j]
                    j=j+1
                gene_info1=str(genename)+str("        ")+str(len(sum_1))+"\n"
                fout.write(gene_info1)
                gene_info2=str(sum_1+"\n")
                fout.write(gene_info2)
    if not line.startswith('>'):
        seqs.append(line.replace('\n',''))
f.close()
fout.close()



