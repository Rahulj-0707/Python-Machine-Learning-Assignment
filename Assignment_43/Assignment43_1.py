import pandas as pd

def main():
        
    DatasetPath = "PlayPredictor.csv"

    df = pd.read_csv(DatasetPath)

    print("DataSet Loaded Successfully...")

if __name__ == "__main__":
    main()
