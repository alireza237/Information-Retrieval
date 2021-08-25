import matplotlib.pyplot as plt
from math import log



mydict={}
n= 0
m = 0
dict={}
with open('Untitled.txt', 'r') as file:

    for line in file:

        for word in line.split():
            n =n +1
            if word in mydict:
                mydict[word] = mydict[word]+1
            else:
                mydict[word]=1
                m = m+1

            if n%100==0:
                dict[log(n)]=log(m)









s =sorted(mydict.items(), key=lambda x: x[1],reverse=True)
x=[]
y=[]
r=0
print(s)
for i in s:

    r=r+1
    y.append(log(i[1]))
    x.append(log(r))

print(x)
print(dict)


plt.plot(x, y)

plt.xlabel('x - log')

plt.ylabel('y - log')


plt.title('Zipf law')




plt.show()

x =list( dict.keys())

y = list(dict.values())



plt.plot(x, y)

plt.xlabel('x - log')
# naming the y axis
plt.ylabel('y - log')


plt.title('Heaps law')




plt.show()

