# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 08:55:16 2021

@author: 216366
"""
import os
import numpy as np
name='299885_config4.vasp'

def shifter(name,out_name,R):
    
    #name='5CH3_mol_graph.vasp'
    file=open(name,'r')
    Lines = file.readlines() #Reads the lines of file "file". but it has to be a small file
    
    
    # Writing to a file
    file2 = open(name[:-5]+out_name, 'w')
    
    #R=[100,100,100]
    
    for i,line in enumerate(Lines):
        # if line is empty
        # end of file is reached
        line2=line.split()
        if i<8: #line of the headder
            file2.writelines(line)
        elif float(line2[2]) == 15.0:
            file2.writelines(line)
        elif float(line2[2]) != 15.0:
            line3=''
            for j,l in enumerate(line2):
                if j<3:
                    #line3= line3+ str(float(l)+R[j]) + '  '
                    line3= line3+  '\t'+'{:.6f}'.format(float(l)+R[j]) 
                else:
                    line3= line3+  '\t' + l
            file2.writelines(line3 + '\n')
            # print(line)
    
    file.close()
    file2.close()


#Z=np.arange(-0.8,5,1)
# Z=[-0.8,1.0,2,3,4]
#Z=np.arange(-0.5,0.6,0.1)
Z=[0.1056]
for z in Z:
    shifter(name, '_'+'{:.2f}'.format(z)+'.vasp', [0,0,z])

