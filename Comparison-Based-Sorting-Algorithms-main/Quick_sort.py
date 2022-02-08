# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:32:04 2021

@author: Sanket Revadigar
"""
import copy
import random
from sys import setrecursionlimit
import time

#Function to partion the array
def partition(arr, low, high):
    i =low - 1
    n=random.randint(low,high)
    pivot = arr[n]
    for j in range(low, high):
        if arr[j] <= pivot:
            i+= 1
            arr[i] = arr[j]
            arr[j] = arr[i]

    arr[i + 1] = arr[high]
    arr[high] =  arr[i + 1]
    return (i + 1)

def Quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        Quick_sort(arr, low, p - 1)
        Quick_sort(arr, p + 1, high)


setrecursionlimit(10*100)

n = int(input("Enter the number of elements to be sorted: "))


#Generate sorted list of numbers for the given number of elements 
sort_list=[]
for x in range(n):
    sort_list.append(x)
    
    
#Generate reverse list of for the given number of elements    
reverse_list=sort_list[::-1]

#Generate random_list numbers for the given number of elements 
rand_list =[]
for x in range(n):
    rand_list.append(random.randint(1,int(0.95*n)))
    
    
#Perform Quick Sort for random numbers sort and take average time by running it thrice
print("\n*********************PROCESSING RANDOM LIST*********************")
randTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(reverse_list)
    start_time=time.time();
    result = Quick_sort(checkerArr,0,len(checkerArr)-1)
    end_time=time.time()
    rand_time=end_time-start_time
    randTime_array.append(rand_time)
temp_time=0.0
for x in range(3):
    temp_time+=randTime_array[x]
randTime_array=temp_time/3
print("Execution time for Random list Quick Sort in ms:",rand_time*1000)


#Perform Quick Sort for sorted numbers sort and take average time by running it thrice
print("\n*********************PROCESSING SORTED LIST*********************")
sortTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(sort_list)
    start_time=time.time();
    result = Quick_sort(checkerArr,0,len(checkerArr)-1)
    end_time=time.time()
    sort_time=end_time-start_time
    sortTime_array.append(sort_time)
temp_time=0.0
for x in range(3):
    temp_time+=sortTime_array[x]
sort_time=temp_time/3
print("Execution time for Sorted list Quick Sort in ms:",sort_time*1000)


#Perform Quick Sort for reverse numbers sort and take average time by running it thrice
print("\n*********************PROCESSING REVERSE LIST*********************")
reverseTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(reverse_list)
    start_time=time.time();
    result = Quick_sort(checkerArr,0,len(checkerArr)-1)
    end_time=time.time()
    reverse_time=end_time-start_time
    reverseTime_array.append(reverse_time)
temp_time=0.0
for x in range(3):
    temp_time+=reverseTime_array[x]
reverse_time=temp_time/3
print("Execution time for Reverse list Quick Sort in ms:",reverse_time*1000)