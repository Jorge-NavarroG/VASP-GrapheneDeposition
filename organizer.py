# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 08:55:16 2021

@author: 216366
"""

name='in_2021_32_(279885new).xyz'
file=open(name,'r')
Lines = file.readlines() #Reads the lines of file "file". but it has to be a small file


# Writing to a file
file2 = open(name[:-4]+'_modif.vasp', 'w')


for elem in [' C',' H',' N',' O','Co']:    
    for line in Lines:
        # if line is empty
        # end of file is reached
        if line[:2] == elem:
            file2.writelines(line)
            print(line)

file.close()
file2.close()

