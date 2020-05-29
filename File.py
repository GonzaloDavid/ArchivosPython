#!/usr/bin/python
class File:
    order = 0
    value = ''
    sizeList =0
    rowNumber = 0
    key =''

    def __init__(self, n, s,size,rowNumber,key):
        self.order = n
        self.value = s
        self.sizeList=size
        self.rowNumber=rowNumber
        self.key=key

     
    def print_order(self):
        print self.order
         
    def print_value(self):
        print self.value