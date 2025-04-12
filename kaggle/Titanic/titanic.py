import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text


def process_data(df, is_train=True):
	df = df.drop(labels=["Cabin", "Ticket", "Name"], axis=1)
	df = pd.get_dummies(df, columns=['Sex', 'Embarked'])

	# Fill missing values instead of dropping rows
	if 'Age' in df.columns:
		df['Age'] = df['Age'].fillna(df['Age'].median())
	if 'Fare' in df.columns:
		df['Fare'] = df['Fare'].fillna(df['Fare'].median())
	if 'Embarked_C' in df.columns:
		df[['Embarked_C', 'Embarked_Q', 'Embarked_S']] = df[['Embarked_C', 'Embarked_Q', 'Embarked_S']].fillna(0)

	ids = df["PassengerId"]
	df = df.drop(labels=["PassengerId"], axis=1)

	# If training set, drop label separately
	if is_train and 'Survived' in df.columns:
		df = df.dropna(subset=['Survived'])

	df = df.astype({col: 'int' for col in df.select_dtypes(include='float').columns})
	return df, ids


def train_model():
	# Read in the data
	df = pd.read_csv('train.csv')
	survivors = pd.read_csv('gender_submission.csv')
	# Attach label to each row
	df,_= process_data(df)
	# end of preprocessing
	# Get labeled data
	y_train = df["Survived"]
	x_train = df.drop(["Survived"], axis=1)
	X_train, X_test, Y_train, Y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=42)
	model = DecisionTreeClassifier()
	model.fit(X_train, Y_train)
	y_pred = model.predict(X_test)
	print(f"Accuracy {accuracy_score(Y_test, y_pred)}")
	return model, X_train
model, X_train = train_model()
tree_rules = export_text(model, feature_names=list(X_train.columns))
print(tree_rules)
X_test,ids = process_data(pd.read_csv('test.csv'))
y_pred = model.predict(X_test)
submission = pd.DataFrame(
	{
		'PassengerId': ids,
		'Survived': y_pred
	}
)

submission.to_csv("submission.csv", index=False)
