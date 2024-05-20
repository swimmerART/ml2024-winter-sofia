import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import sys

N = int(input("Enter the number of points: "))
print(f"Number of Points is {N}")

k = int(input("Enter the number of nearest neighbors: "))
print(f"Number of Nearest Neighbors is {k}")

if k > N:
    print("Error: k should be less than or equal to N")
    quit()


points = np.zeros((N, 2))

# Read the (x, y) points
for i in range(N):
    x = float(input(f"Enter x value for point {i+1}: "))
    y = float(input(f"Enter y value for point {i+1}: "))
    points[i] = [x, y]

# Separation of labels and points
X_train = points[:, 0].reshape(-1, 1)
y_train = points[:, 1]

#Variance
variance_y = np.var(y_train)
print(f"Variance of data: {variance_y}")

# Read the input X for prediction
X_predict = float(input("Enter the X value: "))
print(f"X value for prediction is {X_predict}")
# Perform k-NN regression using scikit-learn
knn_regressor = KNeighborsRegressor(n_neighbors=k)
knn_regressor.fit(X_train, y_train)
Y_predict = knn_regressor.predict(np.array([[X_predict]]))

# Output the result
print(f"The predicted Y = {Y_predict[0]}")
