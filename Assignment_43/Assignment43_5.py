import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import(
    accuracy_score
)
def CheckAccuracy(Y_test, Y_Pred):
    Accurracy = accuracy_score(Y_test, Y_Pred)
    print("The Accuracy of the model is : ", Accurracy * 100)

def PlayPredictor(DatasetPath):

    Border = "-" * 50

    ###############################################################################################
    # Step 1 : Dataset Loading
    ###############################################################################################

    print(Border)
    print("Step 1 : Dataset Loading")
    print(Border) 

    df = pd.read_csv(DatasetPath)

    print("Original Dataset\n")
    print(df)

    ###############################################################################################
    # Step 2 : Feature Encoding
    ###############################################################################################

    print(Border)
    print("Step 2 : Feature Encoding")
    print(Border) 

    encoder = LabelEncoder()

    df["Whether"] = encoder.fit_transform(df["Whether"])
    df["Temperature"] = encoder.fit_transform(df["Temperature"])

    print("Encoded Dataset")

    print(df)

    ###############################################################################################
    # Step 3 : Data Spliting And Training
    ###############################################################################################

    print(Border)
    print("Step 3 : Data Spliting And Training")
    print(Border)

    Feature_col = [
        "Whether",
        "Temperature"
    ]

    X = df[Feature_col]
    Y = df["Play"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    ###############################################################################################
    # Step 4 : Model Selection
    ###############################################################################################

    print(Border)
    print("Step 4 : Model Selection")
    print(Border)

    model = KNeighborsClassifier(
        n_neighbors=5,
    )

    print("Model Successfully created...")
 
    ###############################################################################################
    # Step 5 : Train the Model
    ###############################################################################################

    print(Border)
    print("Step 5 : Train the Model")
    print(Border) 

    model.fit(X_train, Y_train)
    print("Model Training is Complted...")

    ###############################################################################################
    # Step 6 : Model Testing
    ###############################################################################################

    print(Border)
    print("Step 6 : Model Testing")
    print(Border) 

    Y_Pred = model.predict(X_test)

    print("Model Testing is Done...")

    print("Prediction is : ",Y_Pred)

    ###############################################################################################
    # Step 7 : Calculate Accuracy
    ###############################################################################################

    print(Border)
    print("Step 7 : Calculate Accuracy")
    print(Border) 

    CheckAccuracy(Y_test, Y_Pred)


def main():
    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()