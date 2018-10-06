
# coding: utf-8

# In[1]:


from collections import Counter
coins = [2000, 500, 100, 50, 10, 1]
stock={2000:6,500:2,100:20,50:15,10:100,1:200}

def fun():
    bill=int(input("your bill in rupees"))
    givenamount=0   
    while givenamount<bill:
        givenamount+=int(input("given amount in rupees"))
        if givenamount>=bill:
            change=givenamount-bill
            coinsReturned = []
            for i in coins:
                if stock[i]>0:
                       while (change>=i and stock[i]>0):
                                change=change-i
                                coinsReturned.append(i)
                                stock[i]-=1 
                                       
    a=stock
    print(a)
    print(coinsReturned)    
    stock.update(a)
    print((stock))
    
    
def update():
    total=[]
    full_amount=[]
    d=int(input("enter two thousand notes:"))
    f=int(input("enter five hundred notes:"))
    l=int(input("enter hundred notes:"))
    k=int(input("enter fifty rupee notes:"))
    j=int(input("enter ten rupee:"))
    p=int(input("enter one rupee:"))    
    new_collec={2000:d,500:f,100:l,50:k,10:j,1:p}
    for i,j in new_collec.items():
        mul=i*j
        total.append(mul)    
    print("Total deposit amount:",sum(total)) 
    updated=dict(Counter(stock)+Counter(new_collec))
    stock.update(updated)
    for u,l in stock.items():
        apx=u*l
        full_amount.append(apx)
    print("Total updated amount:",sum(full_amount))            
fun()


# In[27]:


update()


# fun()

# In[25]:


fun()


# In[19]:


update()


# In[20]:


fun()


# In[17]:


posting={'Rs500': ['23'],'Rs10': ['4'], 'Rs200': ['3'], 'Rs1': ['6'], 'Rs2000': ['23'], 'Rs50': ['5'], 'Rs100': ['4'], 'Rs5': ['3'], 'Rs2': ['2']}
for x,y in posting.items():
    for i in range(0,len(y)):
        y[i]=int(y[i])  
    #print(x,y) 
    for s in y:
        s=int(s)
        b={x:s}
        posting.update(b)
print(posting)
    
      
    
    
   
        


# In[14]:


posting={'Rs500': ['23'],'Rs10': ['4'], 'Rs200': ['3'], 'Rs1': ['6'], 'Rs2000': ['23'], 'Rs50': ['5'], 'Rs100': ['4'], 'Rs5': ['3'], 'Rs2': ['2']}
for key,values in posting.items():
   val=values
   for x in val:
       y=int(x)
       d={key:y}
       posting.update(d)
print(posting)


# In[68]:


d={'given_amount': ['50'], 'bill_amount': ['8']}
li=[]
x={}
for key,values in d.items():
   val=values
   for x in val:
           y=int(x)
           d={key:y}
           li.append(y)
           x.update
l=li[0]-li[1]
d['change']=l
print(l)
print(d)
                
   

  


# In[3]:


c={'Rs5': 14, 'Rs10': 16, 'Rs200': 32, 'Rs1': 71, 'Rs50': 12, 'Rs100': 18, 'Rs500': 28, 'Rs2': 18, 'Rs2000': 8, 'id': 1}

l=[]
a=c.keys()
print((a))
b=c.values()
print(b)
import re
d=[re.findall(r'(\w+?)(\d+)', key)[0] for key,values in c.items() if key!='id']
print(d)
for w,q in d:
    
    l.append(int(q))
print("fu:",sorted(l,reverse=True))
       
print(d)

        




# In[ ]:


h=dict(d)
print(h)
for x,y in h.items():
    j=y
    for u in j:
        v=int(u)
        l.append(v)
print(v)


# In[57]:


c={'Rs5': 14, 'Rs10': 16, 'Rs200': 32, 'Rs1': 71, 'Rs50': 12, 'Rs100': 18, 'Rs500': 28, 'Rs2': 18, 'Rs2000': 8, 'id': 1}
d=[re.findall(r'(\w+?)(\d+)', key)[0] for key,values in c.items() if key!='id']
print(d)
l=[]
p=[]
z=c.values()
print(z)
for w,q in d:   
    l.append(int(q))
    p.append(w)
print("rupees:",p)
print("fu:",(l))
dic=dict(zip(l,z))
print("full:",dic)
print("dic:",dic.items())
i={'Rs' + str(key):values for key,values in dic.items()}
print("sdfhd:",i)



f={ key:values for key,values in c.items() if key!='id' }
print("list :",c.items())
print(f)


# In[ ]:




