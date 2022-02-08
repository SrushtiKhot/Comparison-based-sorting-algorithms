# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 19:41:20 2021

@author: Sanket Revadigar
"""

import copy
import random
from sys import setrecursionlimit
import time



#Heapify function with root as the largest element
def heapify(arr, n, i):
    maximum = i  
    left = 2 * i + 1     
    right = 2 * i + 2     

    if left < n and arr[maximum] < arr[left]:
        maximum = left
    if right < n and arr[maximum] < arr[right]:
        maximum = right
    if maximum != i:
        arr[i], arr[maximum] = arr[maximum], arr[i]
        
        heapify(arr, n, maximum)


def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


setrecursionlimit(10*10)

n = int(input("Enter the total number of elements to be sorted: "))


#Generate sorted list of numbers for the given number of elements 
sort_list=[]
for x in range(n):
    sort_list.append(x)
    
    
#Generate reverse list for the given number of elements    
reverse_list=sort_list[::-1]

#Generate random_list numbers for the given number of elements 
rand_list =[]
for x in range(n):
    rand_list.append(random.randint(1,int(0.95*n)))
    
    
#Perform heap sort for random numbers and take average time by running it 3 times
print("\n*********************PROCESSING RANDOM LIST*********************")
randTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(reverse_list)
    start_time=time.time();
    result = heapSort(checkerArr)
    end_time=time.time()
    rand_time=end_time-start_time
    randTime_array.append(rand_time)
temp_time=0.0
for x in range(3):
    temp_time+=randTime_array[x]
randTime_array=temp_time/3
print("Execution time for Random list Heap Sort in ms:",rand_time*1000)


#Perform heap sort for sorted numbers and take average time by running it 3 times
print("\n*********************PROCESSING SORTED LIST*********************")
sortTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(sort_list)
    start_time=time.time();
    result = heapSort(checkerArr)
    end_time=time.time()
    sort_time=end_time-start_time
    sortTime_array.append(sort_time)
temp_time=0.0
for x in range(3):
    temp_time+=sortTime_array[x]
sort_time=temp_time/3
print("Execution time for Sorted list Heap Sort in ms:",sort_time*1000)


#Perform heap sort for reverse numbers and take average time by running it 3 times
print("\n*********************PROCESSING REVERSE LIST*********************")
reverseTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(reverse_list)
    start_time=time.time();
    result = heapSort(checkerArr)
    end_time=time.time()
    reverse_time=end_time-start_time
    reverseTime_array.append(reverse_time)
temp_time=0.0
for x in range(3):
    temp_time+=reverseTime_array[x]
reverse_time=temp_time/3
print("Execution time for Reverse list Heap Sort in ms:",reverse_time*1000)