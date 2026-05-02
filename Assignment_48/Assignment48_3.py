from sklearn.preprocessing import StandardScaler
import numpy as np

def main():

    Data = np.array([[25,20000],
                     [30,40000],
                     [35,80000]]) 
    
    print("Original Data", Data)

    Scaler = StandardScaler()

    ScaledData = Scaler.fit_transform(Data)

    print("Scaled Data : ")
    print(ScaledData)

if __name__ == "__main__":
    main()