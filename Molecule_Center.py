# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 08:55:16 2021

@author: 216366
"""
import os
import numpy as np
name='in_2021_32_(279885new).xyz'

def center(name,out_name,R):
    
    #name='5CH3_mol_graph.vasp'
    file=open(name,'r')
    Lines = file.readlines() #Reads the lines of file "file". but it has to be a small file
    
    
    # Writing to a file
    file2 = open(name[:-4]+out_name, 'w')
    
    #R=[100,100,100]
    
    for i,line in enumerate(Lines):
        # if line is empty
        # end of file is reached
        line2=line.split()
        if i<2: #line of the headder
            file2.writelines(line)
        # elif float(line2[2]) == 8:
        #     file2.writelines(line)
        else:
            line3=''
            for j,l in enumerate(line2):
                if (0<j)and(j<4):
                    #line3= line3+ str(float(l)+R[j]) + '  '
                    line3= line3+ '\t'+ '{:.6f}'.format(float(l)+R[j-1])
                else:
                    line3= line3+'\t' + l
            file2.writelines(line3 + '\n')
            # print(line)
    
    file.close()
    file2.close()


R=[-1.264722,-3.692248,-11.313059]
center(name, '_centered.xyz',R)

