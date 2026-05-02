import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

import matplotlib.pyplot as plt

import seaborn as sb

from sklearn.metrics import(
    accuracy_score,
    confusion_matrix
)

def main():
        
    Border = "-" * 50

    ###################################################################################################
    # Step 1 : Data Loading
    ###################################################################################################

    print(Border)
    print("Step 1 : Data Loading")
    print(Border)

    DataSetPath = "student_performance_ml.csv"

    df = pd.read_csv(DataSetPath)

    print("DataSet get loaded successfully...")

    ###################################################################################################
    # Step 2 : Data Analysis(EDA)
    ###################################################################################################

    print(Border)
    print("Step 2 : Data Analysis(EDA)")
    print(Border)

    print("Shape of Dataset : ",df.shape)
    print("Columns name : ",list(df.columns))

    print("Missing Values(per column)")
    print(df.isnull().sum())

    print("Class Distribution")
    print(df["FinalResult"].value_counts())

    print("Statistical Report of Dataset")
    print(df.describe())

    ###################################################################################################
    # Step 3 : Data Visualization
    ###################################################################################################

    print(Border)
    print("Step 3 : Data Visualization")
    print(Border)

    plt.figure(figsize=(7,5))

    plt.scatter(df["StudyHours"], df["PreviousScore"])

    plt.title("Study Hours vs Previous Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.grid(True)
    plt.legend()

    plt.show()

    ###################################################################################################
    # Step 4 : Split the Dataset for Training and Testing
    ###################################################################################################

    print(Border)
    print("Step 4 : Split the Dataset for Training and Testing")
    print(Border)

    Feature_col = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours"
    ]

    X = df[Feature_col]
    Y = df["FinalResult"]


    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2, 
        random_state=42   
    )

    ###################################################################################################
    # Step 5 : Model Building and Training
    ###################################################################################################

    print(Border)
    print("Step 5 : Model Building and Training")
    print(Border)

    # Model Building

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=None,
        random_state=42
    )

    print("Model is Build Successfully...")

    # Train the Model

    model.fit(X_train, Y_train)
    print("Model Trainig is Completed...")

    ###################################################################################################
    # Step 6 : Model Testing or Prediction
    ###################################################################################################

    print(Border)
    print("Step 6 : Model Testing or Prediction")
    print(Border)

    Y_Pred = model.predict(X_test)
    print("Model Testing is Completed...")

    print("The actual answer : ")
    print(Y_test)

    print("The Predicted answer : ")
    print(Y_Pred)

    ###################################################################################################
    # Step 7 : Accuracy Calculation
    ###################################################################################################

    print(Border)
    print("Step 7 : Accuracy Calculation")
    print(Border)

    accuracy = accuracy_score(Y_test, Y_Pred)
    print("Accuracy of the model is : ",accuracy * 100)

    ###################################################################################################
    # Step 8 : Confusion Matrix
    ###################################################################################################

    print(Border)
    print("Step 8 : Confusion Matrix")
    print(Border)

    cm = confusion_matrix(Y_test, Y_Pred)
    print("Confusion matrix is : ")
    print(cm)

if __name__ == "__main__":
    main()