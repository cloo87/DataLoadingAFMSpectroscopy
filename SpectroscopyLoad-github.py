import os
import glob
import pandas as pd

#%% Functions used

# to turn a nested list into a list (use in creating header)
def flatten(ls):
    new_ls = []
    for element in ls:
        if isinstance(element, list):
            new_ls = new_ls + flatten(element)
        else:
            new_ls.append(element)
    return(new_ls)

#%% LOADING RAW DATA

# ! Insert file path of data folder
path = r" " 
os.chdir(path)

"""
When retrieving file from nanoscope analysis, use the following convention; 
the amplitude and phase curves (also known as butterfly and hysteresis loops) 
measured at the first point are named as point00_a2.txt and point00_p2.txt, respectively.

Here,00 indicates the point number while a/p represents amplitude/phase curves,
and 2 represents retrace (1 can be used to represent trace). 

"""
# ! Insert name of the file
file = " "

txt_file = []

#Follows the convention used, only file ends with 2.txt will be imported
#If both trace and retrace are desired, then change it to ".txt"
for infile in glob.glob(os.path.join(os.getcwd(), file, "*2.txt")): # insert name of folder
    txt_file.append(infile)

header_list = []
L = len(txt_file)/2 

# Headers are assigned to the amplitude and phase curves obtained at each point
# For instance, at point 1, the amplitude curve is composed of V1 and pm1
# while the phase curve consists of V*1 and Deg1
for i in range(int(L)):
    inlist = ['V%s' %i, 'pm%s' %i, 'V*%s' %i, 'Deg%s' %i] # compile amplitude and phase data into a single dataframe
    header_list.append(inlist)


# Create a dataframe that contains the amplitude and phase curves obtained at differnt points on a sampling area.
header = flatten(header_list) 
df = pd.concat([pd.read_csv(txt_file[i], sep='\t', skiprows=1, header=None) for i in range(len(txt_file))], axis=1)
df.columns = header


# check the if there is any measurement where the amplitude is given in nm instead of pm

data_in_nm = []
for w in range(int(len(df.columns)/4)):
    if df['pm%s' %w].max() < 5.0 :
        data_in_nm.append(w)
        print(w)

print(data_in_nm)

# convert the unit from nm to pm (to standardize the unit before exporting the data)
for c in range(len(data_in_nm)):
    df['pm%s' %data_in_nm[c]] = 1000*df['pm%s' %data_in_nm[c]]



#%% Exporting dataframe as csv

filename = f"{file}.csv"
df.to_csv(os.path.join(path, filename), index=False)

