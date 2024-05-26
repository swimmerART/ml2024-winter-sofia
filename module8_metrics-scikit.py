import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter the number of points: "))
    X = np.zeros(N)
    Y = np.zeros(N)

    # Read N (x, y) points
    print("Enter the points x and y")
    for i in range(N):
        x = int(input("Enter x value for point {}: ".format(i+1)))
        y = int(input("Enter y value for point {}: ".format(i+1)))
        X[i] = x
        Y[i] = y

    # Calculate Precision and Recall
    precision = precision_score(X, Y)
    recall = recall_score(X, Y)

    # Output Precision and Recall
    print("Precision: {:.2f}".format(precision))
    print("Recall: {:.2f}".format(recall))

if __name__ == "__main__":
    main()
