import pandas as pd

def main():
        
    DatasetPath = "Advertising.csv"

    df = pd.read_csv(DatasetPath)

    print("Dataset det loaded successfully...")

if __name__ == "__main__":
    main()
