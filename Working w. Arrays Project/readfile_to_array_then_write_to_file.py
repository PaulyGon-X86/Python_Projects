#!/usr/bin/env python2
#2017-06-04
#Reading a text file into an array, processing it, then writing to a file
def read(f, age):
    age = f.readline()
    return(age)

def process():
    pass
    return

def write():
    pass
    return

def main():
    age_list = []
    file_handler = open('#path to file', 'r')
    age_list = read(file_handler, age_list)
    process()
    write()
    return

if __name__ == "__main__":
    main()