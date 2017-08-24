import os.path
import re
path=input("Enter")                             
Listu=os.listdir(path)                                  #forming a list all the available documents in the directory
os.chdir(path)                                          #Changing the path of dir
print("       ",Listu,"\n")                             #printing the list of documents
import re

class Lcs(object):                                      #creating a class Lcs
    def __init__(self,f1,f2,ku=""):                     #Constructor for the  
        self.f1=f1                                       #
        self.f2=f2
        self.ku=ku
    def set_ku(self,new_ku):
        self.ku=new_ku
    def get_ku(self):
        return self.ku
#method
    def stringu(self):
        be=0
        for i in range(len(self.f1)):
            itemp=i
            for j in range(len(self.f2)):
                if (itemp<len(self.f1)):
                    if self.f1[itemp]==self.f2[j]:
                        itemp+=1
                        if (itemp-i)>be:
                            be=itemp-i
                            ku=self.f1[i:itemp]
                    else:
                        itemp=i
        self.set_ku(ku)
        return self.get_ku()
        
    def calcu(self):
        valu=len(self.stringu())
        valu=((valu*2)/(len(self.f1)+len(self.f2)))*100
        return round(valu)


for i in range(len(Listu)):
    M,Ma=[],[]
    for j in range(len(Listu)):
        if i==j:
            Ma.append("Nil")
            M.append("Nil")
        if i!=j:
            a=open(Listu[i],"r")
            b=open(Listu[j],"r")
            kg=a.read()
            kg=re.sub("[^a-zA-Z0-9\_\n ,' ]+","",kg)
            kg=kg.replace(",","")
            pg=b.read()
            pg=re.sub("[^a-zA-Z0-9\_\n ,' ]+","",pg)
            pg=pg.replace(",","")
            ajay=Lcs(kg,pg)
            Ma.append(ajay.stringu())
            M.append(str(ajay.calcu())+"%")
            a.close()
            b.close()
    print(Listu[i],M)
    print("       ",Ma)
    print("")

