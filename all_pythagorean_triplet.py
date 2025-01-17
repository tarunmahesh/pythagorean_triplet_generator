# -*- coding: utf-8 -*-
"""all_pythagorean_triplet.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qR4X_5wfCsD8Vibf_vQ2YRBh9w-lWH5H
"""

from fractions import Fraction
import numpy as np
import math

def finding_factors(n):
  factors_list_first_half = []
  for i in range(1, math.ceil(math.sqrt(n+1))):
    if n % i == 0:
      factors_list_first_half.append(int(i))
  factor_list = []
  for number in factors_list_first_half:
    factor_list.append(number)
  for j in reversed(factors_list_first_half):
    factor_list.append(int(n/j))
  return factor_list
print(finding_factors(91))

def all_pythagorean_triplets(x):
  t_list = np.linspace(0.01, x, 100*x).tolist()
  triplet_list = []
  for t in t_list:
    if t != 1:
      print(t)
      x = (math.sqrt(t**2 - t**2 + 1) - t*t)/(t**2 + 1)
      y = t*x + t
      x_fraction = list(str((Fraction(x).limit_denominator())))
      y_fraction = list(str((Fraction(y).limit_denominator())))
      x_numerator_list = x_fraction[0:x_fraction.index('/')]
      x_denominator_list = x_fraction[x_fraction.index('/')+1:len(x_fraction)]
      y_numerator_list = y_fraction[0:y_fraction.index('/')]
      y_denominator_list = y_fraction[y_fraction.index('/')+1:len(y_fraction)]
      x_num = int(''.join([str(item) for item in x_numerator_list]))
      x_denom = int(''.join([str(item) for item in x_denominator_list]))
      y_num = int(''.join([str(item) for item in y_numerator_list]))
      y_denom = int(''.join([str(item) for item in y_denominator_list]))
      if x_denom == y_denom and x_num**2 + y_num**2 == x_denom**2:
        triplet_list.append(sorted([abs(x_num), abs(y_num), x_denom]))
  return_list = []
  [return_list.append(x) for x in triplet_list if x not in return_list]
  return return_list
all_triplets = all_pythagorean_triplets(2000)

list1 = all_pythagorean_triplets(1000)
list2 = all_pythagorean_triplets(1500)

difference = [x for x in list2 if x not in list1]

print(difference)
print(len(difference))

def triplets_containing_number(x):
  factors = finding_factors(x)
  return_triplets = []
  for factor in factors:
    for triplet in all_triplets:
      if factor in triplet:
        new_triplet = [int(n*(x/factor)) for n in triplet]
        return_triplets.append(new_triplet)
  return return_triplets

def max_number_of_triplets(x):
  max_len = 0
  current_maxes = []
  for i in range(1, x+1):
    if len(triplets_containing_number(i)) > max_len:
      max_len = len(triplets_containing_number(i))
      current_maxes = [i]
    elif len(triplets_containing_number(i)) == max_len:
      current_maxes.append(i)
  string = "Out of the first " + str(x) + " numbers, the numbers with the most Pythagorean Triplets are " + str(current_maxes) + ", with a total of " + str(max_len) + " triplets."
  return string

def total_number_of_triples(x):
  primitive_triples = []
  for triplet in all_triplets:
    if triplet[2] < x:
      primitive_triples.append(triplet)
  actual_triples = []
  for triple in primitive_triples:
    constant = 1
    while (triple[2] * constant < x):
      actual_triples.append([int(n*(constant)) for n in triple])
      constant += 1
  print(primitive_triples)
  print(actual_triples)
  return len(primitive_triples), len(actual_triples)


def max_number():
  l = []
  for triplet in all_triplets:
    l.append(max(triplet))
  return max(l)

print(len(triplets_containing_number(840)))
print(triplets_containing_number(18))

print(35**2 + 84**2 == 91**2)
print(max_number_of_triplets(1500))
print(max_number())
print(total_number_of_triples(100))

print(1/3 * 3)