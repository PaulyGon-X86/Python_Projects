#!/usr/bin/env python2
#2017-06-04
#Reading a text file into an array, processing it, then writing to a file
def read(f, age):
    age = f.readlines()
    print(age, '#2')
    return(age)

def process(age):
    age.sort()
    print(age, '#4')
    return(age)

#def write(age):
#    for element in age:
#    print(element) 
#    return

def main():
    age_list = []
    print(age_list, '#1')
    file_handler = open('agelist.txt', 'r')
    age_list = read(file_handler, age_list)
    print(age_list, '#3')
    age_list = process(age_list)
    print(age_list, '#5')
#    write(age_list)
    return

if __name__ == "__main__":
    main()