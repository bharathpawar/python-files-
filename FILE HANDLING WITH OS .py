#print('helo')
'''n1 = 50
n2 = 10
def addnums(n1,n2):
    res=n1+n2
    return res
def subnums(n1,n2):
    res=n1-n2
    return res
def mulnums(n1,n2):
    res=n1*n2
    return res
def divnums(n1,n2):
    res=n1//n2
    return res
addres = addnums(n1,n2)
subres = subnums(addres,n2)
mulres = mulnums(subres,n2)
divres = divnums(mulres,n2)
print((addres,subres,mulres,divres))'''


'''def reversestring(string):
    opt=''
    for z in range(len(string)-1,-1,-1):
        opt+=string[z]
    print(opt)
string=input("reverse of string")
reversestring(string)'''

'''fo=open("demo.txt","a")
n=input("enter a name")
n1=input("enter a password")
lines=file.readline(fo)
output=[]

if n not in output:
    
    fo.write(n+"   -   "+n1)

fo.close()'''

'''def checkname(name):
    fo=open("demo.txt","r")
    data=fo.readlines()
    users=[]
    for i in data:
        users.append((i.split("-")[0]).rstrip())
    fo.close()
    if name in users:
        return 1
    else:
        return 0


n=input("enter a name")
n1=input("enter a password")
n2=checkname(n)
if n2 ==1 :
    print("name already exists")
else:
    fo=open("demo.txt","a")
    
    fo.write(n+" - " +n1 +"\n")
    fo.close()
    '''
    
'''list=[2,4,6,7,8,4,6,8,3,4]
output=[]
newlist=[]
for i in range(len(list)-1):
    output=[list[i],list[i+1]]
    newlist.append(output)
    output=[]
print(newlist)'''




'''def name(string):
    lower=0
    upper=0

    for i in string:
        if i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
    print("there are " + str(lower)+ 'lower case letters')
    print('there are' + str(upper) + 'upper case letters')
            
string=input("enter a name")
print()
name(string)
name("pYthon is easy")'''

'''def palindrome(name):
    reversestring=''
    for i in range(len(name)-1,-1,-1):
        reversestring+=name[i]
    if name == reversestring:
        print('It is a palindrome')
    else:
        print("name is not palindrome")
name=input("enter a name")
print()
palindrome(name)'''

'''def number(operation):
    add=0
    mul=1
    for i in operation:
        i=int(i)
        add += i
        mul *= i

    print(add)
    print(mul)
    
    
    
        
    
operation=input("enter a  number")
operation=operation.split()
number(operation)'''


        
'''class organisation:
     org_name="lync"
     org_adress ="hyd"
     org_strength="10"
o1=organisation()
o2=organisation()
o3=organisation()


print(o2)
print(o1.org_name)'''


'''class organisation:
    org_name ="lync"
    org_adress="hyd"
    org_strength=10
    def inpu(self,name,role,sal):
        print("name of the employe is "+ name)
        print("employe role is "+ role)
        print("employe sal "+ sal)
    def __init__(self,emp_name,emp_role,emp_sal):
        self.emp_name=emp_name
        self.emp_role=emp_role
        self.emp_sal=emp_sal
        organisation.org_strength=organisation.org_strength+1
    def printer(self):
        print("name of the employe is "+ self.emp_name)
        print("employe role is "+self.emp_role)
        print("employe sal is "+self.emp_sal)
    @classmethod
    def changecname(cls,newname):
        cls.org_name =newname
        print("company nam has been changed to "+cls.org_name)
    @staticmethod
    def calc(num,perc):
        res=num+(num*perc)
        print(res)
o1=organisation("john","pd","1")
o2=organisation("jane","hh","2")

o1.printer()

o1.changecname("love")

o2.printer()
o2.inpu("khan","yy","5")
    
o1.calc(1000,5)'''

'''class num:
    def __init__(self,n):
        self.n=n
    def __add__(first,second):
        res=first.n -second.n
        return res
a=num(10)
b=num(20)
print(a+b)'''

import os
import random

'''def usernameexist(username):
    
        file=open ('demo123.txt','r')
        for i in file.readlines():
                if username == i.split('-')[0].rstrip():
                        return True
        file.close()
        return False
    


def addusername(username,password):
    file=open('demo123.txt','a')
    file.write(username + '  -  ' + password+ '\n')
    file.close()



def generatepassword():
    password=''
    password+=noofrandomstrings(numberofsets)
    password+=noofrandomintegers(numberofsets)
    return password



def noofrandomstrings(n):
    global chrlist
    tempstring=''
    for i in range(n):
        tempstring+=random.choice(chrlist)
    return tempstring



def noofrandomintegers(n):
    tempinteger=''
    for i in range(n):
        tempinteger+=str(random.randint(0,9))
    return tempinteger


def fileexist():
        if not (os.path.isfile('/Users/pawarbharath/Desktop/demo123.txt')):
                fo=open('demo123.txt','w')
                fo.close()

        
def createchrlist():
    chrlist=[chr(i) for i in range(65,91)]
    for i in range(97,123):
        chrlist.append(chr(i))
        random.shuffle(chrlist)
        return chrlist


username=input('enter a user name : ')
fileexist()

if not(usernameexist(username)):
    numberofsets=int(input('how many strings and integers are needed ? : '))
    
    chrlist = createchrlist()
    password = generatepassword()
    addusername(username,password)
    print('your new password is' + password)
    
else:
    print('user namae already exist')
    print()'''

import os
import shutil

path=input("enter path :")
os.chdir(path)
def move_file(path):
        files=os.listdir(path)
        print(files)
        for i in files:
                file_path=path+'//'+i
                print(file_path)
                if os.path.isfile(file_path):
                        ext=os.path.splitext(file_path)[1]
                        dirc_name=ext[1:]+"s"
                        
                        if os.path.isdir(dirc_name):
                                shutil.move(i,dirc_name)
                        else:
                                os.mkdir(f'{dirc_name}')
                                shutil.move(i,dirc_name)
        
move_file(path)                               
                      
        
        
        
        
    

    

    
