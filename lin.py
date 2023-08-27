import pandas as pd



data = pd.read_csv('Beogradski-stanovi.csv')

df = data.sort_values(by=['opstina'])
df = df.reset_index(drop = True)
print(df)

train_data = df.iloc[lambda x: x.index % 4 == 1]
test_data = df.iloc[lambda x: x.index % 4 == 0] # I will get every 4th row of sorted df


#Tesiram - rastojanje, kvadraturu
def gradient_descent(data,L,max_iterations, weights, features):

    m = len(data)
    print(L)
    print(m)
    print(weights)
    print(features)
    sume = {'rastojanje':0,'povrsina':0,'sobnost':0, 'w0':0}
    gradients = {}
    gradient_to_low = False

    for i in range(max_iterations):
        for index,row in data.iterrows():
            y = row['cena']
            h = weights['w0'] + weights['povrsina'] * row['povrsina'] + weights['rastojanje'] * row['rastojanje'] + weights['sobnost'] * row['sobnost']
            sume['w0']+= h-y
            for feature in features:
                x = row[feature] #xn(i)
                sumi = (h-y) * x
                sume[feature]+=sumi
        # u ovom trenutku imamo sume svih odlika

        # azuriranje vrednosi odlika
        weights['w0'] = weights['w0'] - (L/m)*sume['w0']
        for feature in features:
            gradient = (L/m)*sume[feature]
            weights[feature] = weights[feature] - gradient
            gradients[feature] = gradient
            # azuriranje gradijenata
            # if(gradient < 0.01): gradient_to_low = True

        # if(gradient_to_low): 
        #     print("Gradient is to low, time to break")
        #     print("List of gradients:", gradients)
        #     return weights, gradients
        
    return weights


weights = { 'w0':0, 'rastojanje': 0, 'povrsina': 0, 'sobnost':0}
features = ['povrsina', 'rastojanje', 'sobnost']
weights = gradient_descent(train_data,L=0.0001,max_iterations=1000, weights = weights, features=features)




for index,row in test_data.iterrows():
    predicted_val =  weights['w0'] + weights['povrsina'] * row['povrsina'] + weights['rastojanje'] * row['rastojanje'] + weights['sobnost'] * row['sobnost']
    y = row['cena']
    print("Razlika:", abs(y-predicted_val),"\n")
    
# print("Tezine:",test)







# treniranje modela