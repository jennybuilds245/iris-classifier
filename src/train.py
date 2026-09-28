#loading Iris dataset into the model 
from sklearn.datasets import load_iris

#spliting the model between testing and training data 
from sklearn.model_selection import train_test_split

#importing the classifier and making an instance of the classifier
from sklearn.tree import DecisionTreeClassifier

#determing the porpotion of accurate predictions from the total number of predictions
from sklearn.metrics import accuracy_score

iris = load_iris()
x = iris.data
y = iris.target
print(iris.feature_names, iris.target_names)

#size of the test data is 20% of the total data and the random state is set to 42 to reproducibility
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)  



model = DecisionTreeClassifier(random_state=42)
#fitting the model with the training data and the decision tree algortithm finds patterns in X_train that corresponds with y_train
model.fit(x_train, y_train)
#predicting the species of the iris flower based on the test data, it wwill return an array of predicted labels for the test sample
y_pred = model.predict(x_test)

#printing the predicted lables and the actual labels of the test data
print("Predicted labels:", y_pred[:5])
print("Actual labels:", y_test[:5])

accuracy = accuracy_score(y_test, y_pred)  
print("Accuracy:", accuracy)