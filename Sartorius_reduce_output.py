import pandas as pd;

filename=input('filename? \n')


df = pd.read_csv(filename, sep=';', header=[0,1,2,3], decimal=',')

pO2=df.filter(like='pO2_1').filter(like='Value')
time=df.filter(like='ProcessTime')
pH=df.filter(like='pH_1').filter(like='Value')

outputfile=filename+'_res.txt'

with open (outputfile, 'w') as output:
    pd.concat([time, pO2, pH], axis=1).to_csv(output, sep=';', decimal='.')

