import numpy as np

class k_NN_regression:
  def __init__(self):
    self.data = None

  def fit(self, X, y):
    self.data = np.column_stack((X, y))

  def predict(self, X, k):
    if k > self.data.shape[0]:
      raise ValueError("k cannot be greater than the number of training samples")

    predictions = []
    for x in X:
      distances = np.abs(self.data[:, 0] - x)  # Absolute difference in x values
      nearest_neighbors = self.data[distances.argsort()[:k]]
      # Predict the target value by averaging the y values of neighbors
      prediction = np.mean(nearest_neighbors[:, 1])
      predictions.append(prediction)
    return np.array(predictions)

def main():
  while True:
    try:
      N = int(input("Enter a positive integer N: "))
      k = int(input("Enter a positive integer k: "))
      if N <= 0 or k <= 0:
        raise ValueError
      break
    except ValueError:
      print("Invalid input. Please enter positive integers for N and k.")

  data = np.empty((N, 2))

  for i in range(N):
    print(f"Enter point coordinates {i+1} (x, y): ")
    try:
      data[i, 0] = float(input("x: "))
      data[i, 1] = float(input("y: "))
      print(f"Point: {data[i, 0], data[i, 1]}")
    except ValueError:
      print("Invalid input. Please enter real numbers for x and y.")
      break

  model = k_NN_regression()
  model.fit(data[:, 0], data[:, 1])

  while True:
    try:
      X_pred = float(input("Enter a number X to predict: "))
      break
    except ValueError:
      print("Invalid input. Please enter a real number for input X.")

  # Predict Y using k-NN regression
  if k <= N:
      predicted_y = model.predict(np.array([X_pred]).reshape(-1, 1), k)[0]
      print(f"Prediction: {predicted_y}")
  else:
    print("Error: k cannot be greater than the number of training samples.")

if __name__ == "__main__":
  main()
