

#print("shell")
#l1=[10,30,40,50]
#l2=[100,40,500,70]
#dict={}
#for i in range(len(l1)):
 #   dict[l1[i]]=l2[i]
#print(dict)
'''stmt=input("enter a statement")
words=stmt.split()
dict={}
tempphrase=''
for z in words:
    for i in z:
        if i!='z':
            tempphrase+=chr(ord(i)+1)
        else:
            temphase +='a'
    dict[z] =tempphrase
    tempphrase=''
print(dict)'''
        
'''l1={1:2,8:8,3:7}
print(l1)
keys=int(input('enter a key'))
l1.pop(keys)
print(l1)'''


'''list2=[]
list3=[]
ds=int(input("enter number of numbers to be entered"))
for i in range(ds):
	x=int(input("enter a number"))
	list2.append(x)
for i in list2:
	list3.append([list2.count(i),i])
print(list3)	
list3.sort(reverse=True)
print(list3)
if list3[0]==1:
	print("there is no mode")
else:
	print("mode is : ",list3[0][1])
	i=0
	j=1
	while list3[i][0]==list3[j][0]:
		if list3[i][1]!=list3[j][1]:
			print("mode is : ",list3[j][1]) 
		i=i+1
		j=j+1'''



'''list5=[2,3,2,4,2,3,4,5,6,74,5]
list6=[]
for i in list5:
	if i not in list6: 
		list6.append(i)
print(list6)
x=0
for k in range(2):
	for i in list5:
		x=list5.count(i)
		if x>1:
			for j in range(x-1):
				list5.remove(i)

		x=0		
print(list5)'''

'''dicto1={1:'a',2:'b',3:'c',4:'d',5:'f'}
key=input('enter any key')
value=input('enter any value')
print("before : ",dicto1)
for i in dicto1.keys():
	if type(i) is int:
		key=int(key)
		if i==key:
			dicto1[key]=tuple(value)
		else:
			dicto1[key]=value
		break	
	else:
		if i is key:
			dicto1[key]=tuple(value)
		else:
			dicto1[key]=value	
		break			
print("after : ",dicto1)'''
'''def avg(*args):
    res=sum(args)//len(args)
    print(res)
avg(10,20,30,40,50)


def makecake(flav='cho',shape='round',weight=3):
    print("flav is "+flav)
    print(f"shape is {shape}")
    print(f'weight is  {weight}')
    print()
makecake('van','round','4')
makecake(flav='cho',weight='4')
makecake(flav='buttrr',shape='round')
makecake()
'''
'''def avg (a,b,*args):
    total=0
    for i in args:
        total+=i
    ans=total /len(args)
    print(ans)
avg(1,3)
avg(4,6,8)'''






    
