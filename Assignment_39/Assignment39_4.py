import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import(
    accuracy_score,
    confusion_matrix
)


def main():
        
    DataSetPath = "student_performance_ml.csv"

    df = pd.read_csv(DataSetPath)

    print("DataSet get loaded successfully...")

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

    # Model Building

    model = DecisionTreeClassifier(
        criterion="gini",
        max_depth=3,
        random_state=42
    )

    print("Model is Build Successfully...")

    # Train the Model

    model.fit(X_train, Y_train)
    print("Model Trainig is Completed...")

    #  Test the MOdel

    Y_Pred = model.predict(X_test)
    print("Model Testing is Completed...")

    print("The actual answer : ")
    print(Y_test)

    print("The Predicted answer : ")
    print(Y_Pred)

    # Calculate the model performance

    accuracy = accuracy_score(Y_test, Y_Pred)
    print("Accuracy of the model is : ",accuracy * 100)

    # Confusion matrix

    cm = confusion_matrix(Y_test, Y_Pred)
    print("Confusion matrix is : ")
    print(cm)

if __name__ == "__main__":
    main