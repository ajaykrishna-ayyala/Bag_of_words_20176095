import os.path
path=input("Enter the path of dir")
Listy=os.listdir(path)
print(Listy)
os.chdir(path)


def plagiarism(f1,f2):
    def convert(s):
        s=s.lower()
        c="abcdefghijklmnopqrstuvxxyz_0123456789"
        for i in s:
            if i not in c:
                s=s.replace(i," ")
        s=s.replace("\n"," ").replace("\xa0"," ")
        s=s.split(" ")
        return s
    s1=convert(f1.read())
    s2=convert(f2.read())
    
    def dictionary(s,d):
        for i in s:
            if i==' ' or i=='':
                pass
            elif i not in d:
                d[i]=1
            else:
                d[i]+=1
        return d
    d1=dictionary(s1,{})
    d2=dictionary(s2,{})
    
    def dotproduct_numerator(d1,d2):
        L=[]
        for i in d1:
            for j in d2:
                if i==j:
                    L.append(d1[i]*d2[j])
        return L

    numerator=sum(dotproduct_numerator(d1,d2))

    def dotproduct_denominator(d):
        dum=0
        for i in d:
            dum+=(d[i])**2
        dum=(dum)**(1/2)
        return dum
    denominator=(dotproduct_denominator(d1))*(dotproduct_denominator(d2))
    return (numerator/denominator)*100


plist=[]
for i in range (len(Listy)):
    for j in range (len(Listy)):
        if i==j:
            plist.append("Nil")
        else:
            f1=open(Listy[i],"r")
            f2=open(Listy[j],"r")
            plist.append(plagiarism(f1,f2))
            f1.close()
            f2.close()
    print(Listy[i],plist,"\n")
    plist=[]


