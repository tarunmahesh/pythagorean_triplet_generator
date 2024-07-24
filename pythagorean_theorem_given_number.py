# -*- coding: utf-8 -*-
"""Pythagorean Theorem

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hI0I6iy8SgdNrTZND6yAGRvazMO513iM
"""

import math

def processingEvenNumbers(x):
  #Precondition: x is even
  count = 0
  while x/2 == math.floor(x/2):
    x /= 2
    count += 1
  return int(x), count

def oddATriplet(z):
  x = (pow(z,2) - 1)/2
  y = (pow(z,2) + 1)/2

  return x,y

def findingTriplet(a):
  if a % 2 == 1:
    b,c = oddATriplet(a)


  if a % 2 == 0 and math.log2(a) != math.floor(math.log2(a)):
    m,n = processingEvenNumbers(a)
    temp_b,temp_c = oddATriplet(m)
    b = temp_b * (pow(2,n))
    c = temp_c * (pow(2,n))

  if math.log2(a) == math.floor(math.log2(a)):
    l = math.log2(a)
    b = 3 * (pow(2, l-2))
    c = 5 * (pow(2, l-2))

  b = int(b)
  c = int(c)

  #Final check
  if pow(a,2) + pow(b,2) == pow(c,2):
    return a, b, c

a = input("Pick a whole number greater than 2: ")
a = float(a)

while a<2 or a != math.floor(a):
  print("You didn't meet the criteria given.")
  a = input("Pick another whole number that is greater than 2: ")
  a = float(a)

a=int(a)

l, m, n = findingTriplet(a)

if l < m:
  print("A Pythagorean Triplet containing your number is "+str(l)+", "+str(m)+", and "+str(n)+".")
else:
  print("A Pythagorean Triplet containing your number is "+str(m)+", "+str(l)+", and "+str(n)+".")
