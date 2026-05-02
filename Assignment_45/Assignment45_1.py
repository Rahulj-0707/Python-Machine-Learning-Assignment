import pandas as pd

def main():

    DatasetPath = "WinePredictor.csv"

    df = pd.read_csv(DatasetPath)

    print("Dataset loaded Successfully...")

if __name__ == "__main__":
    main()
