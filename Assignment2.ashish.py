#!/usr/bin/env python
# coding: utf-8

# In[1]:


def myreduce(function, iterable):
    a = iter(iterable)
    initial = None
    if initial is None:
        value = next(a)
    else:
        value = initial
        
    for i in a:
        value = function(value,i)
    return value

m = [1,2,3,4,5,6]
myreduce(lambda x,y:x+y,m)


# In[2]:


def myfilter(n, lst):
    a = []
    b = []
    
    for i in lst:
        a.append(n(i))
    
    for i in range(0, len(a)):
        
        if a[i] == False:
            continue
        
        else:
            b.append(a[i])
    
    return b
        

def even_number(i):
    if i%2 == 0:
        return i
    else:
        return False

print(myfilter(even_number,[3, 7, 5, 8,9,10,11,12]))


# In[3]:


m = 'ACADGILD'
l = []
for i in m:
    l.append(i)
print(l)


# In[4]:


m = [i * j for j ibn ['x', 'y', 'z'] for i in range(1, 5)]
print(m)


# In[5]:


n = [i * j for j in range(1, 5) for i in ['x', 'y', 'z']]
print(n)


# In[7]:


a = [2,3,4]
b = []
for i in a:
    for j in range(0,3):
        c = i+j
        b.append([c])
print(b)


# In[8]:


q = [[i + j for j in [0, 1, 2, 3]] for i in range(2, 6)]
print(q)


# In[9]:


r = [(i,j) for j in [1, 2, 3] for i in [1, 2, 3]]
print(r)


# In[11]:


def longestWord(m):
    new_wor = m.split(' ')
    st = max(new_wor)
    long = (len(max(new_wor, key=len)))
    for i in m.split():
        if len(i)== long:
            print(i)
    
longestWord("my favourite destination is Simla")


# In[15]:


class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
class Area(Triangle):
    def __init__(self,a,b,c):
        super(Area,self).__init__(a,b,c) 
        
    def Area(self):
        
        s = (self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
    
b = Area(4,6,8)
b.Area()


# In[18]:


def filter_longer_words(words, n):
    return filter(lambda x: len(x) > n, words)

list(filter_longer_words(['my ', 'name','is','Ashish','Nayak'], 3))


# In[22]:


l = ["my","name","is","ashish","nayak"]
m = []
for i in l:
    n = len(i)
    m.append(n)
print(m)


# In[26]:


def vowel_Check():
    char = input("Enter a char :")
    if char in ('a','e','i','o','u'):
        return True
    else:
        return False

vowelCheck()


# In[ ]:




