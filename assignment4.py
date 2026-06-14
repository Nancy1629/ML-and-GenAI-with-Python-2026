import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression

current_folder = os.path.dirname(__file__)
csv_path = os.path.join(current_folder, "Dataset 2.csv")

df = pd.read_csv(csv_path)

#Q1
print(df.head())

#Q2
print("\nRows and Columns:")
print(df.shape)

#Q3
print("\nColumn Names:")
print(df.columns)

#Q4
print("\nDataset Information:")
print(df.info())

# Q5
print("\nMissing Values:")
print(df.isnull().sum())

# Q6
average_age = df["Age"].mean()

print("Average Age:", average_age)

# Q7
average_watch_hours = df["WatchHoursPerWeek"].mean()

print("Average Watch Hours Per Week:", average_watch_hours)

# Q8
average_spend = df["MonthlySpend"].mean()

print("Average Monthly Spending:", average_spend)

# Q9
subscription_count = df["SubscriptionType"].value_counts()

print(subscription_count)

# Q10
renewal_percentage = (df["SubscriptionRenewed"] == "Yes").mean() * 100

print("Renewal Percentage:", renewal_percentage, "%")


# Q11
df_encoded = pd.get_dummies(df, drop_first=True)

print(df_encoded.head())

# Q12
X = df_encoded.drop("SubscriptionRenewed_Yes", axis=1)

y = df_encoded["SubscriptionRenewed_Yes"]

print("Features (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())


# Q13
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)


# Q14
dt_model = DecisionTreeClassifier(random_state=42)

dt_model.fit(X_train, y_train)

print("Decision Tree Model Trained Successfully")


# Q15
y_pred_dt = dt_model.predict(X_test)

accuracy_dt = accuracy_score(y_test, y_pred_dt)

print("Decision Tree Accuracy:", accuracy_dt)


# Q16
cm = confusion_matrix(y_test, y_pred_dt)

print("Confusion Matrix:")
print(cm)


# Q17
knn_model = KNeighborsClassifier(n_neighbors=5)

knn_model.fit(X_train, y_train)

print("KNN Model Trained Successfully")


# Q18
y_pred_knn = knn_model.predict(X_test)

accuracy_knn = accuracy_score(y_test, y_pred_knn)

print("KNN Accuracy:", accuracy_knn)

print("Decision Tree Accuracy:", accuracy_dt)



# Q19
X_reg = df_encoded.drop("MonthlySpend", axis=1)
y_reg = df_encoded["MonthlySpend"]

model = LinearRegression()
model.fit(X_reg, y_reg)

print("Linear Regression Model Trained")


# Q20
prediction = model.predict(X_reg.iloc[[0]])

print("Predicted Monthly Spending:", prediction[0])