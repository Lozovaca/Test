import pandas as pd
import numpy as np
import math

def k_mean(data,K,x,max_iterations):

    #izaberemo nasumicnih k tezista
    random_centers = data.sample(n = K)
    data.drop(random_centers.index) # remove init centers from df
    centers = {}
    for i in range(0,K): # init first centers
        centers[i] = {}
    j = 0
    for i, center in random_centers.iterrows():
        w = 10 if center['parking'] == 'da' else 0
        centers[j] = {'x': center['spratnost'], 'y': center['sobnost'], 'z': center['kupatila'],'w':w}
        j+=1
    clusters = {}
    for i in range(0,K):
        clusters[i] = []


    for m in range(0,max_iterations):
        for index,row in data.iterrows():
            min_j = 0
            min_distance = 0
            j = 0
            parking = 10 if row['parking'] == 'da' else 0
            dot = {'spratnost': row['spratnost'], 'kupatila': row['kupatila'],'sobnost': row['sobnost'], 'parking': parking}
            for s in range(0,len(centers)):
                x = dot['spratnost'] - centers[j]["x"]
                y = dot['sobnost'] - centers[j]["y"]
                z = dot['kupatila'] - centers[j]["z"]
                w = dot['parking'] - centers[j]["w"]
                dist = math.sqrt(x**2 + y**2 + z**2 + w**2)
                if(j ==0 ):
                    min_j = 0
                    min_distance = dist
                elif(dist < min_distance):
                    min_j = j
                    min_distance = dist
                j+=1
            clusters[min_j].append(dot)

        # # ovde imamo nova tezista
        j = 0
        for key,value in clusters.items():
            sum_spratnost = 0
            sum_kupatila = 0
            sum_sobnost = 0
            sum_parking = 0
            n = len(value)
            for item in value:
              sum_spratnost+= item['spratnost']  #ovde bih mogao da nacrtam klaster
              sum_kupatila+= item['sobnost']
              sum_sobnost+= item['kupatila']
              parking = 10 if item['parking'] == 'da' else 0
              sum_parking+= parking
            centers[j]['x'] = sum_spratnost/n
            centers[j]['y'] = sum_kupatila/n
            centers[j]['z'] = sum_sobnost/n
            centers[j]['w'] = sum_parking/n

            j+=1
        print(centers)
    return centers, clusters
    # svaku instancu dodeljujemo najblizem tezistu
    # za svaki klaster izracuna se novo teziste
    # ponavlja se sve dok se ne dostigne max ili neko teziste ne konvergira..


data = pd.read_csv('Beogradski-stanovi.csv')

df = data.sort_values(by=['opstina'])
df = df[df['sobnost'].notna()]
df = df[df['spratnost'].notna()]
df = df[df['kupatila'].notna()]
df = df.reset_index(drop = True)
df = df[['cena','spratnost','sobnost','kupatila','parking']].copy()
centers, clusters = k_mean(df,5,x=["sobnost","spratnost","kupatila","parking"],max_iterations=10)
# trebalo bi iscrtati centre i ostale tacke?

