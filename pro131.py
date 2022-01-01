import csv
import pandas as pd

df= pd.read_csv('final_data.csv')

df['Radius']= df['Radius'].apply(lambda x: x.replace('$','').replace(',','')).astype(float)

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()

def convert_to_si_units(radius,mass):
    for i in range(0,len(radius)-1):
        radius[i] = radius[i]*6.957e+8
        mass[i] = mass[i]*1.989e+30
        
convert_to_si_units(radius,mass)

gravity =[]

def gravity_calc(radius,mass):
    G = 6.674e-11
    for j in range(0,len(mass)):
        g= (mass[j]*G)/((radius[j])**2)
        gravity.append(g)
        
gravity_calc(radius,mass)

df["Gravity"] = gravity
print(df)

df.to_csv('stars_gravity.csv')