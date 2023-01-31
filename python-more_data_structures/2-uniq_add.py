#!/usr/bin/python3
def uniq_add(my_list=[]):
   result = 0
   unique_numbers = set(my_list)
   for element in unique_numbers:
       result = result + element
   return(result)
