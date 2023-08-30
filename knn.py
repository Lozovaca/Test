import pandas as pd
import numpy as np
import math

def knn_algorithm(data,k,input_value,distance_metric_type):
    # 1 korak - izracunati distancu od za svaki podatak
    # uzeti najmanjih k vrednosti distance
    # od tih k gledati najzastupljeniji broj klase
    distances = []
    intervals = ["<35","35-50","50-100","100-150","150-200","200-500","500+"]
    classes = dict.fromkeys(intervals, 0)
    minimum_distances_index = []
    for index,row in data.iterrows():
        # print(row)
        x = row['povrsina'] - input_value['povrsina']
        y = row['rastojanje'] - input_value['rastojanje']
        z = row['sobnost'] - input_value['sobnost']
        distance = 0
        if(distance_metric_type == 'eucledian'):
            distance = math.sqrt(x**2 + y**2 + z**2)
        elif(distance_metric_type == 'menhetn'):
            distance =  abs(x) + abs(y) + abs(z)
        distances.append(distance)
    
        # uzeti indekse k najmanjih vrednosti
    arr = np.array(distances)
    ind = np.argpartition(arr, k)[:k]

    for i in ind:
        cena = data.iloc[i]["cena"]
        if(cena < 35000):
            classes["<35"]+=1
        elif(cena >=35000 and cena<50000):
            classes["35-50"]+=1
        elif(cena >=50000 and cena < 100000):
            classes["50-100"]+=1
        elif(cena >=100000 and cena < 150000 ):
            classes["100-150"]+=1
        elif(cena >=150000 and cena < 200000):
            classes["150-200"]+=1
        elif(cena >=200000 and cena < 500000 ):
            classes["200-500"]+=1
        elif(cena>=500000):
            classes["500+"]+=1

    klasa = max(classes, key=classes.get) #naci maksimalan broj pojavljivanja u klasi
    #print(klasa)
    return klasa

    
data = pd.read_csv('Beogradski-stanovi.csv')

df = data.sort_values(by=['opstina'])
df = df[df['sobnost'].notna()]
df = df[df['spratnost'].notna()]
df = df.reset_index(drop = True)
train_data = df.iloc[lambda x: x.index % 4 != 0]
test_data = df.iloc[lambda x: x.index % 4 == 0] # I will get every 4th row of sorted df

# k = int(math.sqrt(len(train_data)))
k = 8
input_value = {"povrsina":150,"rastojanje":1.0,"sobnost":4}
#klasa = knn_algorithm(data,k,input_value,distance_metric_type="eucledian")
klasa = knn_algorithm(data,k,input_value,distance_metric_type="menhten")
print(klasa)
        


