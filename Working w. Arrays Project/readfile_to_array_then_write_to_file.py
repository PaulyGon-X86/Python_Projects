#!/usr/bin/env python2
#2017-06-04
#Reading a text file into an array, processing it, then writing to a file
import math

def read(f, age):
    age = f.readlines()
    return(age)

def process(age):
    age.sort()
    return(age)

def write(age, maxx, mini):
    for element in age:
        print(element)
    print("The largest element is: ", maxx)
    print("The smallest element is: ", mini) 
    return

def main():
    age_list = []
    file_handler = open('agelist.txt', 'r')
    maximum = 0
    minimum = 0
    age_list = read(file_handler, age_list)
    age_list = map(int, age_list)
    age_list = process(age_list)
    maximum = max(age_list)
    minimum = min(age_list)
    write(age_list, maximum, minimum)
    return

if __name__ == "__main__":
    main()