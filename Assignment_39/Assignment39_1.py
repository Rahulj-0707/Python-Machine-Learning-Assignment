import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree


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

if __name__ == "__main__":
    main()

