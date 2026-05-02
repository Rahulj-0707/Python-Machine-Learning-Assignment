def main():

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    n = len(X)

    SumX = 0
    for i in X:
        SumX = SumX + i

    MeanX = SumX / n


    SumY = 0
    for i in Y:
        SumY = SumY + i

    MeanY = SumY / n


    Numerator = 0
    Denometer = 0

    for i in range(n):
        Numerator = Numerator + (X[i] - MeanX) * (Y[i] - MeanY)
        Denometer = Denometer + (X[i] - MeanX) ** 2

    m = Numerator / Denometer

    c = MeanY - (m * MeanX)

    print("Mean of X :", MeanX)
    print("Mean of Y :", MeanY)
    print("Slope (m) :", m)
    print("Intercept (c) :", c)

    print("Regression Equation:")
    print("Y =", m, "X +", c)

if __name__ == "__main__":
    main()
