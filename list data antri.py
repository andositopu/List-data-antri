# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:30:15 2020

@author: andositopu
"""


names = []
cmd = " "
while cmd!= '4':
    print("1. List names")
    print("2. Add name")
    print("3. Call next patient")
    print("\n4.Quit")
    
    cmd = input("\rCommand: ")
    
    if cmd == '1':
        for name in names:
            print(name)
        print("\n")
        
    elif cmd  == '2':
        newName=input("Name : ")
        names.append(newName)
    elif cmd == '3':
        if len(names) == 0:
            print("There are no more patients!")
        else:
            nextPatient = names[0]
            names.remove(nextPatient)
            print("Calling %s" % nextPatient)
    elif cmd !='4':
        print("Invalid command!")
    