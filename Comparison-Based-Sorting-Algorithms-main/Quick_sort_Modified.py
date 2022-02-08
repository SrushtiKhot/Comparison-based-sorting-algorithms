# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:45:16 2021

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

def median(arr, minimum, maximum):
    s = int((maximum + minimum))
    middle=int(s/2)
    if arr[minimum] > arr[middle]:
        arr[minimum]= arr[middle]
        arr[middle] = arr[minimum]
    if arr[minimum] > arr[maximum]:
        arr[maximum]= arr[minimum]
        arr[minimum] =arr[maximum]
    if arr[middle] > arr[maximum]:
        arr[maximum] = arr[middle]
        arr[middle] = arr[maximum]

    return middle

def quick_sort_median(arr, low, high):
        if low +10 < high:
            p = median(arr, low, high)
            quick_sort_median(arr, low, p - 1)
            quick_sort_median(arr, p + 1, high)
        else:
            insertionSort(arr, low, high)
        
        
setrecursionlimit(1000*10000)

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
    
    
#Perform Quick Sort sort and take average time by running it thrice
print("\n*********************PROCESSING RANDOM LIST*********************")
randTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(reverse_list)
    start_time=time.time();
    result = quick_sort_median(checkerArr,0,len(checkerArr)-1)
    end_time=time.time()
    rand_time=end_time-start_time
    randTime_array.append(rand_time)
temp_time=0.0
for x in range(3):
    temp_time+=randTime_array[x]
randTime_array=temp_time/3
print("Execution time for Random list Modified Quick Sort is:",rand_time*1000)

print("\n*********************PROCESSING SORTED LIST*********************")
sortTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(sort_list)
    start_time=time.time();
    result = quick_sort_median(checkerArr,0,len(checkerArr)-1)
    end_time=time.time()
    sort_time=end_time-start_time
    sortTime_array.append(sort_time)
temp_time=0.0
for x in range(3):
    temp_time+=sortTime_array[x]
sort_time=temp_time/3
print("Execution time for Sorted list Modified Quick Sort is:",sort_time*1000)


print("\n*********************PROCESSING REVERSE LIST*********************")
reverseTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(reverse_list)
    start_time=time.time();
    result = quick_sort_median(checkerArr,0,len(checkerArr)-1)
    end_time=time.time()
    reverse_time=end_time-start_time
    reverseTime_array.append(reverse_time)
temp_time=0.0
for x in range(3):
    temp_time+=reverseTime_array[x]
reverse_time=temp_time/3
print("Execution time for Reverse list Modified Quick Sort is:",reverse_time*1000)