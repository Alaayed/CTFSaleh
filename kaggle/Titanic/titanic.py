import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
df = pd.read_csv('test.csv')
survivors = pd.read_csv('gender_submission.csv')
features = ["Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"]
map_id_survival = dict(zip(survivors["PassengerId"],survivors["Survived"]))
x_train = df[features]
y_train =df["PassengerId"].map(map_id_survival).values

X_train, Y_train , x_test , y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)
y_pred = model.predict(x_test)
print(f"Accuracy {accuracy_score(y_test, y_pred)}")

