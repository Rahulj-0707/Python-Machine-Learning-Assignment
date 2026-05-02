import math

def EucDistance(P1, P2):
    return math.sqrt((P1['Hours'] - P2['Hours'])**2 + (P1['Attendance'] - P2['Attendance'])**2)


def KNeighborsClassifier():

    Border = "-" * 50

    data = [
        {'Hours':2, 'Attendance':60, 'label':'Fail'},
        {'Hours':5, 'Attendance':80, 'label':'Pass'},
        {'Hours':6, 'Attendance':85, 'label':'Pass'},
        {'Hours':1, 'Attendance':50, 'label':'Fail'}
    ]

    print(Border)
    print("Training Dataset")
    print(Border)

    for d in data:
        print(d)

    print(Border)

    # Accept input from user
    study_hours = int(input("Enter Study Hours : "))
    attendance = int(input("Enter Attendance : "))

    new_point = {'Hours':study_hours, 'Attendance':attendance}

    # Calculate distances
    for d in data:
        d['distance'] = EucDistance(d, new_point)

    print(Border)
    print("Calculated Distances")
    print(Border)

    for d in data:
        print(d)

    # Sort dataset
    sorted_data = sorted(data, key=lambda item: item['distance'])

    print(Border)
    print("Sorted Data")
    print(Border)

    for d in sorted_data:
        print(d)

    k = 3

    nearest = sorted_data[:k]

    print(Border)
    print("Nearest",k,"Neighbors")
    print(Border)

    for d in nearest:
        print(d)

    # Voting
    Votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        Votes[label] = Votes.get(label,0) + 1

    print(Border)
    print("Voting Result")
    print(Border)

    for v in Votes:
        print(v,"=",Votes[v])

    predicted_class = max(Votes, key=Votes.get)

    print(Border)
    print("Prediction :", predicted_class)


def main():
    KNeighborsClassifier()


if __name__ == "__main__":
    main()
    