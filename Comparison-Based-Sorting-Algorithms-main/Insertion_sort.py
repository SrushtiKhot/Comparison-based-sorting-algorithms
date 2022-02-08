# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:11:57 2021

@author: Sanket Revadigar
"""
import copy
import random
from sys import setrecursionlimit
import time


def insertionSort(arr, min, max):
    for i in range(min, max + 1):
        key_ele = arr[i]
        j = i - 1
        while j >= min and key_ele < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_ele
    return arr


setrecursionlimit(10*10)

n = int(input("Enter the total number of elements to be sorted: "))


#Generate sorted list of numbers for the given number of elements 
sort_list=[]
for x in range(n):
    sort_list.append(x)
    
    
#Generate reverse list for the given number of elements    
reverse_list=sort_list[::-1]

#Generate random numbers for the given number of elements 
rand_list =[]
for x in range(n):
    rand_list.append(random.randint(1,int(0.95*n)))
    
    
#Perform insertion sort for random numbers and take average time by running it 3 times
print("\n*********************PROCESSING RANDOM LIST*********************")
randTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(reverse_list)
    start_time=time.time();
    result = insertionSort(checkerArr, 0, len(reverse_list)-1)
    end_time=time.time()
    rand_time=end_time-start_time
    randTime_array.append(rand_time)
temp_time=0.0
for x in range(3):
    temp_time+=randTime_array[x]
randTime_array=temp_time/3
print("Execution time for Random list Insertion Sort in ms:",rand_time*1000)


#Perform insertion sort for sorted numbers and take average time by running it 3 times
print("\n*********************PROCESSING SORTED LIST*********************")
sortTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(sort_list)
    start_time=time.time();
    result = insertionSort(checkerArr, 0, len(sort_list)-1)
    end_time=time.time()
    sort_time=end_time-start_time
    sortTime_array.append(sort_time)
temp_time=0.0
for x in range(3):
    temp_time+=sortTime_array[x]
sort_time=temp_time/3
print("Execution time for Sorted list Insertion Sort in ms:",sort_time*1000)


#Perform insertion sort for reverse numbers and take average time by running it 3 times
print("\n*********************PROCESSING REVERSE LIST*********************")
reverseTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(reverse_list)
    start_time=time.time();
    result = insertionSort(checkerArr, 0, len(reverse_list)-1)
    end_time=time.time()
    reverse_time=end_time-start_time
    reverseTime_array.append(reverse_time)
temp_time=0.0
for x in range(3):
    temp_time+=reverseTime_array[x]
reverse_time=temp_time/3
print("Execution time for Reverse list Insertion Sort in ms:",reverse_time*1000)