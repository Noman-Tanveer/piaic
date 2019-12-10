# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a Data Types script file.
"""
import this
import math
print(2+3)

print(type(2+(334-54)*43/7*math.exp(3)))
print(2+334-54*43/7*math.exp(3))
print(2+(334-54)*43/7*math.exp(3))

a = (2+(334-54)*43/7*math.exp(3))
print (id(a))
print (a)
b = 232-234+323*2
print(type(b))

c = ['Apple', 'Orange', 'Banana', 'Apricot']
print(c[2])
print(c[-1])

c[1] = 'Dates'
print( c )
print(c[1:4:2])


d = (23, 43, 42, 56, 78, 83, 32)
print (d[3:7:3])
print (d)

e = {43,43,54,65,67,97,8,3423,424,34,65,7567,5,8867,54,5,3423,4,1,3,5,3,6}
print(e)
#e= e[4:17:2]
#print (e)
f = {3:'Dog', 4:'Cat', 5:'Donkey', 6:'Goat'}
print(f[3])
print(f.values)

g = "I am a bad boy not just the bad boy but sometimes: \nI can prove to be h\
orrible and sometimes even terrible"
print(g)

h =g.find('bad')
print (h)

i = g.strip(g)
print(i)

print(c.count(c))
g = g.split
print (g)

print (c[2])
del c[2]
print (c)

#next you have to do different methods of assigning the
#values in strings which can be used for things like making cades