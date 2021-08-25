from sklearn import preprocessing, metrics
from sklearn.ensemble import RandomForestClassifier

import csv
import random


my_words = []
data = []


with open("StrictOMD.csv", 'r') as file:
    data =list( csv.reader(file))



inputs = []

unique=[]


#my compiler cant use tokinize from nltk library so i tokinize with string.spilit()
#if i use nltk library then i give better result

for i in data:
    my_words = my_words + i[1].split()




for i in my_words:
    if i in unique:
        continue
    else:
        unique.append(i)


for i in data:
    tokenized_tweets = i[1].split()
    my_list = []
    for j in unique:
        c = 0
        for k in tokenized_tweets:
            if j == k:
                c += 1
        my_list.append(c)
    inputs.append([my_list,i[0]])


sum=0


for i in range(20):

    ti = []
    tl = []
    tei = []
    tel = []
    random.shuffle(inputs)

    for i in range(len(inputs)-100):
        ti.append(inputs[i][0])
        tl.append(inputs[i][1])


    for i in range(len(inputs)-100,len(inputs)):
        tei.append(inputs[i][0])
        tel.append(inputs[i][1])






    ti = preprocessing.StandardScaler().fit_transform(ti)
    classifier = RandomForestClassifier(max_depth=300)

    classifier.fit(ti, tl)
    y_prediction = classifier.predict(tei)

    sum = sum +metrics.accuracy_score(tel, y_prediction)

print(sum/20)

