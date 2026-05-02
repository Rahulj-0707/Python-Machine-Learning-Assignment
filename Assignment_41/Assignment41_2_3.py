import numpy as np
import math

def EucDistance(P1, P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2) 
    return Ans


def KNeighborsClassifier():
    Border = "-" * 50
    data = [
            {'point' : 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red'},
            {'point' : 'A', 'X' : 2, 'Y' : 3, 'label' : 'Red'},
            {'point' : 'A', 'X' : 3, 'Y' : 1, 'label' : 'Blue'},
            {'point' : 'A', 'X' : 5, 'Y' : 6, 'label' : 'Blue'}
            ]
    
    print(Border)
    print("Marvellous Userdifine KNN")
    print(Border)

    print(Border)
    print("Training Dataset")
    print(Border)

    for i in data:
        print(i)
    
    print(Border)

    new_point = {'X' : 2, 'Y' : 2}

    # Calculate all Distances

    for d in data:
        d['distance'] = EucDistance(d,new_point)

    print(Border)
    print("Calculated distances are : ")
    print(Border)

    for d in data:
        print(d)

    sorted_data = sorted(data, key= lambda item : item['distance'])

    print(Border)
    print("Sorted data is : ")
    print(Border)

    for d in sorted_data:
        print(d)
    
    k = 5   

    nearest = sorted_data[:k]

    print(Border)
    print("Nearest 3 elements are : ")
    print(Border)

    for d in nearest:
        print(d)

    # voting

    Votes = {}
    for neighbour in nearest:
        label = neighbour['label']
        Votes[label] = Votes.get(label,0) + 1

    print(Border)
    print("Voting result is : ")
    print(Border)

    for d in Votes:
        print("Name : ",d, "Number of Votes : ",Votes[d])

    print(Border)

    predicted_class = max(Votes, key=Votes.get)

    print("Predicted class of (2,2) is : ", predicted_class)


def main():
    KNeighborsClassifier()

if __name__ == "__main__":
    main()