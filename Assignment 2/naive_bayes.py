# -------------------------------------------------------------------------
# AUTHOR: Gavin Hughes
# FILENAME: naive_bayes.py
# SPECIFICATION: output classification for test data only if naive bayes confidence >= 0.75
# FOR: CS 4210- Assignment #2
# TIME SPENT: 30 minutes
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

# reading the training data in a csv file
# --> add your Python code here
db = []
X = []
Y = []

# reading the data in a csv file
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)

# transform the original training features to numbers and add them to the 4D array X.
# For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
# --> add your Python code here
# X =

# transform the original training classes to numbers and add them to the vector Y.
# For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
# Y =

outlook = {
    "Sunny": 1,
    "Overcast": 2,
    "Rain": 3,
}

temperature = {
    "Cool": 1,
    "Mild": 2,
    "Hot": 3,
}

humidity = {
    "Normal": 1,
    "High": 2,
}

wind = {
    "Weak": 1,
    "Strong": 2,
}

play = {
    "Yes": 1,
    "No": 2,
}

for data in db:
    X.append([outlook[data[1]], temperature[data[2]], humidity[data[3]], wind[data[4]]])
    Y.append(play[data[5]])

# fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

# reading the test data in a csv file
# --> add your Python code here
dbTest = []

# reading the data in a csv file
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTest.append(row)

# printing the header os the solution
print("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

# use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
# --> add your Python code here
for data in dbTest:
    class_predicted = clf.predict_proba([[outlook[data[1]], temperature[data[2]], humidity[data[3]], wind[data[4]]]])[0]

    # check if confidence level for either class is >= 0.75, if yes print prediction
    if class_predicted[0] >= 0.75:
        print(data[0].ljust(15) + data[1].ljust(15) + data[2].ljust(15) + data[3].ljust(15) + data[4].ljust(15) +
              "Yes".ljust(15) + str(round(class_predicted[0], 2)).ljust(15))
    elif class_predicted[1] >= 0.75:
        print(data[0].ljust(15) + data[1].ljust(15) + data[2].ljust(15) + data[3].ljust(15) + data[4].ljust(15) +
              "No".ljust(15) + str(round(class_predicted[1], 2)).ljust(15))
