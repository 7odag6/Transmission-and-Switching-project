# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 21:06:51 2023

@author: Dell
"""

import pandas as pd

import matplotlib.pyplot as plt

import math
import numpy as np

def trns (x):
    #0.00%	0.10%	0.20%	0.50%	1%	1.20%	1.30%	1.50%	2%	3%	5%	7%	10%	15%	20%	30%	40%	50%
    z=""
    if(x==0):
        z="0.00%"
    elif(x==0.001):
        z="0.10%"

    elif(x==0.002):
        z="0.20%"

    elif(x==0.005):
        z="0.50%"

    elif(x==0.01):
        z="1%"

    elif(x==0.012):
        z="1.20%"

    elif(x==0.013):
        z="1.30%"

    elif(x==0.015):
        z="1.50%"

    elif(x==0.02):
        z="2%"

    elif(x==0.03):
        z="3%"

    elif(x==0.05):
        z="5%"

    elif(x==0.07):
        z="7%"

    elif(x==0.1):
        z="10%"

    elif(x==0.15):
        z="15%"

    elif(x==0.2):
        z="20%"

    elif(x==0.3):
        z="30%"

    elif(x==0.4):
        z="40%"

    elif(x==0.5):
        z="50%"
    return z
   
        



def reuse(a,b,v):
    [N,i,j]=[0,1,0]
    x=[]
    while (i<v):
        while(j<=i):
            N=(i**2)+(j**2)+(i*j)
            
            if(i==j):
                x.append(N+a)
            else:
                x.append(N+b)
            j=j+1
        i=i+1
        j=0
    x=np.sort(x) 
    return x




def calculate_cells360(tdmuser,tdmchannel,blpr,CI,city_size, population_density, avg_calls_per_user, avg_call_duration, available_channels, max_channels_per_base_station,erlang):
    # Calculate the total number of users in the city
    
    total_users = city_size * population_density
    #calculate reuse factor 
    N=(CI*6)/3
    #channels per cell
    channels_per_cell=math.floor((available_channels/N)*(tdmchannel/tdmuser))
    if(channels_per_cell>max_channels_per_base_station):
        channels_per_cell=max_channels_per_base_station
    
    a_user =(avg_calls_per_user*avg_call_duration)/(24*60)
    a_cell=float(erlang[blpr][channels_per_cell])
    subs_per_cell=a_cell/a_user
    cells_required=math.ceil(total_users/subs_per_cell)
    
    return cells_required
def calculate_cells120(tdmuser,tdmchannel,blpr,CI,city_size, population_density, avg_calls_per_user, avg_call_duration, available_channels, max_channels_per_base_station,erlang):
    # Calculate the total number of users in the city
    total_users = city_size * population_density
    #calculate reuse factor 
    possiblevalues=reuse(0.3,0.2,10) #3.2 N.n
    [N,n]=[0,0]
    z=0
    while z < len(possiblevalues):
        x=int(possiblevalues[z])
        y=(possiblevalues[z]-x)*10
        if((3*x/y)>=CI):
            [N,n]=[x,y]
            break
        z=z+1
    
    #N =0
    
    
    while(N==0):
        m=12
        possiblevalues=reuse(0.3,0.2,12)
        [N,n]=[0,0]
        z=0
        while z < len(possiblevalues):
            x=int(possiblevalues[z])
            y=(possiblevalues[z]-x)*10
            if((3*x/y)>=CI):
                [N,n]=[x,y]
                break
            z=z+1
        m=m+2
     # N,n   
    #channels per cell
    channels_per_cell=math.floor((available_channels/N)*(tdmchannel/tdmuser))
    
    if(channels_per_cell>max_channels_per_base_station):
        channels_per_cell=max_channels_per_base_station
    
    channels_per_sector=math.floor(channels_per_cell/3)
    
    
    a_user =(avg_calls_per_user*avg_call_duration)/(24*60)
    a_sector=float(erlang[blpr][channels_per_sector])
    subs_per_cell=(a_sector*3)/a_user
    cells_required=math.ceil(total_users/subs_per_cell)
    
    return cells_required
def calculate_cells10(tdmuser,tdmchannel,blpr,CI,city_size, population_density, avg_calls_per_user, avg_call_duration, available_channels, max_channels_per_base_station,erlang):
    # Calculate the total number of users in the city
    total_users = city_size * population_density
    #calculate reuse factor 

    N=1
    n=1
    while True :
        
        if((3*N/n)>=CI):
            break
        N=N+1
    #channels per cell
    channels_per_cell=math.floor((available_channels/N)*(tdmchannel/tdmuser))
    
    if(channels_per_cell>max_channels_per_base_station):
        channels_per_cell=max_channels_per_base_station
    
    channels_per_sector=math.floor(channels_per_cell/36)
    
    
    a_user =(avg_calls_per_user*avg_call_duration)/(24*60)
    a_sector=float(erlang[blpr][channels_per_sector])
    subs_per_cell=(a_sector*36)/a_user
    cells_required=math.ceil(total_users/subs_per_cell)
    
    return cells_required
def calculate_cells180(tdmuser,tdmchannel,blpr,CI,city_size, population_density, avg_calls_per_user, avg_call_duration, available_channels, max_channels_per_base_station,erlang):
    # Calculate the total number of users in the city
    total_users = city_size * population_density
    #calculate reuse factor 
    #i==j n=4 else n=3 
    possiblevalues=reuse(0.4,0.3,10)
    [N,n]=[0,0]
    z=0
    while z < len(possiblevalues):
        x=int(possiblevalues[z])
        y=(possiblevalues[z]-x)*10
        if((3*x/y)>=CI):
            [N,n]=[x,y]
            break
        z=z+1
    while(N==0):
        m=12
        possiblevalues=reuse(0.3,0.2,12)
        [N,n]=[0,0]
        z=0
        while z < len(possiblevalues):
            x=int(possiblevalues[z])
            y=(possiblevalues[z]-x)*10
            if((3*x/y)>=CI):
                [N,n]=[x,y]
                break
            z=z+1
        m=m+2
    
    #channels per cell
    channels_per_cell=math.floor((available_channels/N)*(tdmchannel/tdmuser))
    
    if(channels_per_cell>max_channels_per_base_station):
        channels_per_cell=max_channels_per_base_station
    
    channels_per_sector=math.floor(channels_per_cell/2)
    
    
    a_user =(avg_calls_per_user*avg_call_duration)/(24*60)
    a_sector=float(erlang[blpr][channels_per_sector])
    subs_per_cell=(a_sector*2)/a_user
    cells_required=math.ceil(total_users/subs_per_cell)
    
    return cells_required

# Example usage
erlang = pd.read_csv(r'D:\guc\Semester 6\transmission/alo.csv') #change to your directory 
############################################Input data heree###############################################################

city_size = 450  # in Km2
population_density = 500400/450  # users per Km2
avg_calls_per_user = 10
avg_call_duration = 1  # in minutes
available_channels = 2300
max_channels_per_base_station = 90  #very big values will result in very big channel per cell value which is not available in csv file
CI= 6.25
tdmchannel=8
tdmuser=2
blpr=0.001  #avialable values :     #0.00%	0.10%	0.20%	0.50%	1%	1.20%	1.30%	1.50%	2%	3%	5%	7%	10%	15%	20%	30%	40%	50%
###########################################################################################################
blpr=trns(blpr)
no=[]
cells_required360 = calculate_cells360(tdmuser,tdmchannel,blpr,CI,city_size, population_density, avg_calls_per_user, avg_call_duration, available_channels, max_channels_per_base_station,erlang)
print("number of cells 360 sectoring : "+ str(cells_required360))
#print(cells_required360)
cells_required180 = calculate_cells180(tdmuser,tdmchannel,blpr,CI,city_size, population_density, avg_calls_per_user, avg_call_duration, available_channels, max_channels_per_base_station,erlang)

print("number of cells 180 sectoring : "+ str(cells_required180))
#print(cells_required180)
cells_required120 = calculate_cells120(tdmuser,tdmchannel,blpr,CI,city_size, population_density, avg_calls_per_user, avg_call_duration, available_channels, max_channels_per_base_station,erlang)
print("number of cells 120 sectoring : "+str(cells_required120))

#print(cells_required120)
cells_required10 = calculate_cells10(tdmuser,tdmchannel,blpr,CI,city_size, population_density, avg_calls_per_user, avg_call_duration, available_channels, max_channels_per_base_station,erlang)
print("number of cells 10 sectoring : "+str(cells_required10))

#print(cells_required10)
no.append(cells_required10)
no.append(cells_required120)
no.append(cells_required180)
no.append(cells_required360)
print("chosen sectoring level is:")
if(max(no)==cells_required360):
    print("360 (no sectoring)")
if(max(no)==cells_required180):
    print("180")
if(max(no)==cells_required120):
    print("120")    
if(max(no)==cells_required10):
    print("10")
print("corresponding to number of cells= "+ str(max(no)))
#print(max(no))


#  
