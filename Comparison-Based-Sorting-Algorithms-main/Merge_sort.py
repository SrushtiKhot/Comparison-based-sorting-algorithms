# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:17:02 2021

@author: Sanket Revadigar
"""
import copy
import random
from sys import setrecursionlimit
import time


def merge_sort(arr):
    length= len(arr)
    if length==1:
        return arr
    middle =length//2
    l= merge_sort(arr[:middle])
    r = merge_sort(arr[middle:])
    return merge(l,r)

def merge(l, r):
    i=0
    j=0
    k=0

    merge_array =[]
    while(i<len(l) and j<len(r)):
        if l[i] <= r[j]:
            merge_array.append(l[i])
            i=i+1
        elif l[i] > r[j]:
            merge_array.append(r[j])
            j=j+1
        k=k+1
    
    while(i<len(l)):
        merge_array.append(l[i])
        i+=1
        k+=1
    while(j<len(r)):
        merge_array.append(r[j])
        j=j+1
        k=k+1            
    return merge_array


setrecursionlimit(10*100)

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
    
    
#Perform Merge sort for random numbers and take average time by running it 3 times
print("\n*********************PROCESSING RANDOM LIST*********************")
randTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(reverse_list)
    start_time=time.time();
    result = merge_sort(checkerArr)
    end_time=time.time()
    rand_time=end_time-start_time
    randTime_array.append(rand_time)
temp_time=0.0
for x in range(3):
    temp_time+=randTime_array[x]
randTime_array=temp_time/3
print("Execution time for Random list Merge Sort in ms:",rand_time*1000)


#Perform Merge sort for sorted numbers and take average time by running it 3 times
print("\n*********************PROCESSING SORTED LIST*********************")
sortTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(sort_list)
    start_time=time.time();
    result = merge_sort(checkerArr)
    end_time=time.time()
    sort_time=end_time-start_time
    sortTime_array.append(sort_time)
temp_time=0.0
for x in range(3):
    temp_time+=sortTime_array[x]
sort_time=temp_time/3
print("Execution time for Sorted list Merge Sort in ms:",sort_time*1000)

#Perform Merge sort for reverse numbers and take average time by running it 3 times
print("\n*********************PROCESSING REVERSE LIST*********************")
reverseTime_array=[]
for x in range(3):
    checkerArr=copy.deepcopy(reverse_list)
    start_time=time.time();
    result = merge_sort(checkerArr)
    end_time=time.time()
    reverse_time=end_time-start_time
    reverseTime_array.append(reverse_time)
temp_time=0.0
for x in range(3):
    temp_time+=reverseTime_array[x]
reverse_time=temp_time/3
print("Execution time for Reverse list Merge Sort in ms:",reverse_time*1000)