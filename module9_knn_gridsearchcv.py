import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import accuracy_score

def get_pairs(n):
    pairs = []
    for _ in range(n):
        x = float(input("Enter x value: "))
        y = int(input("Enter y value: "))
        pairs.append((x, y))
    return pairs

def main():
    N = int(input("Enter the number of training pairs (N): "))

    print("Enter the training pairs (x, y):")
    train_pairs = get_pairs(N)

    X_train = np.array([x for x, y in train_pairs]).reshape(-1, 1)
    y_train = np.array([y for x, y in train_pairs])

    M = int(input("Enter the number of test pairs (M): "))

    print("Enter the test pairs (x, y):")
    test_pairs = get_pairs(M)

    X_test = np.array([x for x, y in test_pairs]).reshape(-1, 1)
    y_test = np.array([y for x, y in test_pairs])

    param_grid = {'n_neighbors': np.arange(1, 11)}

    # Initialize the kNN classifier
    knn = KNeighborsClassifier()
    unique, counts = np.unique(y_train, return_counts=True)
    min_samples = min(counts)

    n_splits = min(5, min_samples)

    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)

    # Perform GridSearchCV to find the best k
    grid_search = GridSearchCV(knn, param_grid, cv=skf)
    grid_search.fit(X_train, y_train)

    # Best k
    best_k = grid_search.best_params_['n_neighbors']

    y_pred = grid_search.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)

    # Output the results
    print(f"The best k for the kNN Classification method is: {best_k}")
    print(f"The corresponding test accuracy is: {test_accuracy:.4f}")

if __name__ == "__main__":
    main()
