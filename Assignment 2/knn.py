# -------------------------------------------------------------------------
# AUTHOR: Gavin Hughes
# FILENAME: knn.py
# SPECIFICATION: use LOOCV for 1NN to calculate the error rate
# FOR: CS 4210- Assignment #2
# TIME SPENT: 20 minutes
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
wrong = 0

# reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)


# loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    # add the training features to the 2D array X and remove the instance that will be used for testing in this iteration.
    # For instance, X = [[1, 3], [2, 1,], ...]]. Convert values to float to avoid warning messages

    # transform the original training classes to numbers and add them to the vector Y. Do not forget to remove the instance that will be used for testing in this iteration.
    # For instance, Y = [1, 2, ,...]. Convert values to float to avoid warning messages

    classification = {
        "+": 1,
        "-": 2
    }

    # --> add your Python code here
    # X =
    # Y =
    # testSample =

    X = []
    Y = []

    for j, data in enumerate(db):
        if j != i:
            X.append([float(data[0]), float(data[1])])
            Y.append(classification[data[2]])

    # fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    # use your test sample in this iteration to make the class prediction. For instance:
    # class_predicted = clf.predict([[1, 2]])[0]
    # --> add your Python code here
    class_predicted = clf.predict([[float(instance[0]), float(instance[1])]])[0]

    # compare the prediction with the true label of the test instance to start calculating the error rate.
    # --> add your Python code here
    if class_predicted != classification[instance[2]]:
        wrong += 1

# print the error rate
# --> add your Python code here
print("Error rate: " + str(wrong/len(db)))
