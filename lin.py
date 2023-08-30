import pandas as pd
import numpy



data = pd.read_csv('Beogradski-stanovi.csv')

df = data.sort_values(by=['opstina'])
df = df[df['sobnost'].notna()]
df = df.reset_index(drop = True)
print(df)

train_data = df.iloc[lambda x: x.index % 4 != 0]
test_data = df.iloc[lambda x: x.index % 4 == 0] # I will get every 4th row of sorted df


#Tesiram - rastojanje, kvadraturu
def gradient_descent(data,L,max_iterations, weights, features):

    m = len(data)
    # print(L)
    # print(m)
    # print(weights)
    # print(features)
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
                print(sumi)
                # if(numpy.isnan(sumi)):
                #     print(i)
                sume[feature]+=sumi
            
            #print(sume)
        # u ovom trenutku imamo sume svih odlika

        # azuriranje vrednosi odlika
        weights['w0'] = weights['w0'] - (L/m)*sume['w0']
        for feature in features:
            gradient = (L/m)*sume[feature]
            weights[feature] = weights[feature] - gradient
            gradients[feature] = gradient
        
        #print(weights)
            # azuriranje gradijenata
            # if(gradient < 0.01): gradient_to_low = True

        # if(gradient_to_low): 
        #     print("Gradient is to low, time to break")
        #     print("List of gradients:", gradients)
        #     return weights, gradients
        
    return weights


def gradient_descen_test(data,L,max_iterations, weights, features):

    m = len(data)
    # print(L)
    # print(m)
    # print(weights)
    # print(features)
    sume = {'rastojanje':0,'povrsina':0,'w0':0}
    gradients = {}
    gradient_to_low = False

    for i in range(max_iterations):
        for index,row in data.iterrows():
            y = row['cena']
            h = weights['w0'] + weights['povrsina'] * row['povrsina'] + weights['rastojanje'] * row['rastojanje']
            sume['w0']+= h-y
            for feature in features:
                x = row[feature] #xn(i)
                sumi = (h-y) * x
                #print(sumi)
                # if(numpy.isnan(sumi)):
                #     print(i)
                sume[feature]+=sumi
            
            #print(sume)
        # u ovom trenutku imamo sume svih odlika

        # azuriranje vrednosi odlika
        weights['w0'] = weights['w0'] - (L/m)*sume['w0']
        for feature in features:
            gradient = (L/m)*sume[feature]
            weights[feature] = weights[feature] - gradient
            gradients[feature] = gradient
        
        #print(weights)
            # azuriranje gradijenata
            # if(gradient < 0.01): gradient_to_low = True

        # if(gradient_to_low): 
        #     print("Gradient is to low, time to break")
        #     print("List of gradients:", gradients)
        #     return weights, gradients
        
    return weights

# weights = { 'w0':3000, 'rastojanje': 100, 'povrsina': 60, 'sobnost':20}

weights = { 'w0':0, 'rastojanje': 0, 'povrsina': 0, 'sobnost':0}
features = ['povrsina', 'rastojanje','sobnost']

# print(len(train_data))
# print(len(test_data))
cena_nan_count = df['cena'].isna().sum()
# print("Nan count",cena_nan_count)
cena_nan_count = df['rastojanje'].isna().sum()
# print("Nan count",cena_nan_count)
cena_nan_count = df['sobnost'].isna().sum()
# print("Nan count spratbist",cena_nan_count)

avg_price_train = train_data["cena"].mean()
avg_distance_train = train_data["rastojanje"].mean()
avg_rooms_train = train_data["sobnost"].mean()
avg_distance_test = test_data["rastojanje"].mean()
avg_price_test = test_data["cena"].mean()
avg_room_test = test_data["sobnost"].mean()
# print(avg_price_train)
# print(avg_distance_train)
# print(avg_rooms_train)
# print(avg_price_test)
# print(avg_distance_test)
# print(avg_room_test)
weights = gradient_descent(train_data,L=0.1,max_iterations=5, weights = weights, features=features)


# print(weights)

razlike = []
for index,row in test_data.iterrows():

    predicted_val =  weights['w0'] + weights['povrsina'] * row['povrsina'] + weights['rastojanje'] * row['rastojanje'] + weights['sobnost'] * row['sobnost']
    print("Predicted val",predicted_val)
    y = row['cena']
    razlike.append(abs(y-predicted_val))

#print(razlike)
    
# print("Tezine:",test)



#rastojanje': 1.456837214510932e+277, 'povrsina': 7.03132733424158e+280, 'sobnost': 6.561546708895282e+276, 'w0': 2.3572870790941087e+276}



# treniranje modela

# dijagrami + ubaciti model u aplikaciju..