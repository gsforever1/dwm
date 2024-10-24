from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
Weather = ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy',
 'Overcast', 'Sunny', 'Sunny', 'Rainy', 'Sunny',
 'Overcast', 'Overcast', 'Rainy']
Temp = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool',
 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild']
Play = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No',
 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
le = preprocessing.LabelEncoder()
weather_encoded = le.fit_transform(Weather)
print("Weather Encoded:", weather_encoded)
temp_encoded = le.fit_transform(Temp)
print("Temp Encoded:", temp_encoded)
label = le.fit_transform(Play)
print("Play Encoded:", label)
features = [tup for tup in zip(weather_encoded, temp_encoded)]
print("Features:", features)
model = GaussianNB()
model.fit(features, label)
predicted = model.predict([[0, 2]]) # 0: Overcast, 2: Mild
print("Predicted Value:", predicted)