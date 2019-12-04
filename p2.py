import csv
a=list(csv.reader(open('2.csv','r')))
print(a)
s=['$','$','$','$','$','$']
g=[['?','?','?','?','?','?']]
for i in range(len(a)):
    if(a[i][6]=="Y"):
        for j in range(len(s)):
            if(s[j]=='$'):
                s[j]=a[i][j]
               
            elif(s[j]!=a[i][j] and s[j]!="?"):
                for k in range(len(g)):
                    if g[k][j]==s[k]:
                        g.pop(k)
                        break
                s[j]="?"
        print("The specific array at {} is".format(i), s)
        print("The general array at {} is".format(i), g)
    elif(a[i][6]=="N"):
        for j in range(len(s)):
            b=['?','?','?','?','?','?']
            if g[0]==b:
                g.pop(0)
            if( s[j]!=a[i][j]and s[j]!='?'):
                b[j]=s[j]
                g.append(b)
        print("The specific array at {} is".format(i), s)
        print("The general array at {} is".format(i), g)
