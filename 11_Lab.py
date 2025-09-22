# import heapq

# # Goal state
# goal_state = [[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 0]]   # 0 = empty tile

# # Helper: find position of tile in state
# def find_pos(state, value):
#     for i in range(3):
#         for j in range(3):
#             if state[i][j] == value:
#                 return i, j

# # Heuristic: number of misplaced tiles
# def h(state):
#     misplaced = 0
#     for i in range(3):
#         for j in range(3):
#             if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
#                 misplaced += 1
#     return misplaced

# # Generate next states (neighbors)
# def get_neighbors(state):
#     neighbors = []
#     x, y = find_pos(state, 0)  # empty tile position
#     moves = [(0,1),(1,0),(0,-1),(-1,0)]  # right, down, left, up
#     for dx, dy in moves:
#         nx, ny = x+dx, y+dy
#         if 0 <= nx < 3 and 0 <= ny < 3:
#             new_state = [row[:] for row in state]
#             new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
#             neighbors.append(new_state)
#     return neighbors

# # Convert state to tuple (for hashing in sets/dict)
# def state_to_tuple(state):
#     return tuple(num for row in state for num in row)

# # A* algorithm
# def a_star(start):
#     open_list = [(h(start), 0, start, [])]  # (f, g, state, path)
#     visited = set()

#     while open_list:
#         f, g, state, path = heapq.heappop(open_list)

#         if state == goal_state:
#             return path + [state]

#         visited.add(state_to_tuple(state))

#         for neighbor in get_neighbors(state):
#             if state_to_tuple(neighbor) not in visited:
#                 g_new = g + 1
#                 f_new = g_new + h(neighbor)
#                 heapq.heappush(open_list, (f_new, g_new, neighbor, path + [state]))
#     return None

# # Example: Initial state
# start_state = [[1, 2, 3],
#                [4, 0, 6],
#                [7, 5, 8]]

# # Run
# solution = a_star(start_state)

# print("Solution steps:")
# for step in solution:
#     for row in step:
#         print(row)
#     print()



import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# Step 1: Create the dataset
# This sample dataset is created to make the code runnable.
# In a real-world scenario, you would load this from a CSV file.
data = {
    "Alternate": ["Yes", "No", "Yes", "Yes", "Yes", "No", "No", "Yes", "No", "No", "No", "Yes"],
    "Bar": ["No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes", "Yes", "No", "No", "Yes"],
    "Fri/Sat": ["No", "No", "No", "No", "No", "Yes", "No", "Yes", "No", "No", "No", "Yes"],
    "Hungry": ["Yes", "No", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "No", "Yes"],
    "Patrons": ["Some", "Full", "Some", "Full", "Full", "Some", "Some", "Full", "Some", "Full", "Some", "Full"],
    "Price": ["$$$", "$", "$$", "$", "$$$", "$$", "$", "$$$", "$", "$$", "$", "$"],
    "Raining": ["No", "No", "No", "No", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "No"],
    "Reservation": ["Yes", "No", "No", "No", "No", "Yes", "No", "No", "No", "No", "No", "Yes"],
    "Type": ["French", "Thai", "Burger", "Thai", "French", "Burger", "Thai", "French", "Burger", "Thai", "Thai", "Burger"],
    "WaitEstimate": ["0-10", "30-60", "10-30", "30-60", "30-60", "0-10", "0-10", "0-10", "0-10", "30-60", "10-30", "30-60"],
    "Wait": ["Yes", "No", "Yes", "No", "Yes", "Yes", "No", "Yes", "No", "No", "No", "Yes"]
}

df = pd.DataFrame(data)

# Step 2: Prepare the data
# Separate features (X) from the target variable (y).
X = df.drop("Wait", axis=1)
y = df["Wait"]

# Convert categorical variables to numeric format using one-hot encoding.
# This creates new columns for each unique categorical value.
X = pd.get_dummies(X)

# Step 3: Train and visualize the decision tree
print("Training and Visualizing Decision Tree with Entropy (max_depth=4)")
# Initialize and train the decision tree classifier using entropy as the criterion.
tree_clf_entropy = DecisionTreeClassifier(criterion="entropy", max_depth=4, random_state=42)
tree_clf_entropy.fit(X, y)

# Visualize the tree and save it as an image.
plt.figure(figsize=(20, 10))
plot_tree(tree_clf_entropy, feature_names=X.columns, class_names=["No", "Yes"], filled=True)
plt.title("Decision Tree with Entropy")
plt.show()

# Step 4: Exercises and Evaluation

# Exercise 1: Train with Gini criterion and visualize
print("\nExercise 1: Training and Visualizing Decision Tree with Gini (max_depth=4)")
tree_clf_gini = DecisionTreeClassifier(criterion="gini", max_depth=4, random_state=42)
tree_clf_gini.fit(X, y)

plt.figure(figsize=(20, 10))
plot_tree(tree_clf_gini, feature_names=X.columns, class_names=["No", "Yes"], filled=True)
plt.title("Decision Tree with Gini")
plt.show()

# Exercise 2: Compare accuracy with different depths
print("\nExercise 2: Comparing Accuracy at different depths")

# Train a new tree with max_depth=2.
tree_clf_depth2 = DecisionTreeClassifier(criterion="entropy", max_depth=2, random_state=42)
tree_clf_depth2.fit(X, y)

# Evaluate the model with max_depth=4.
y_pred_depth4 = tree_clf_entropy.predict(X)
accuracy_depth4 = accuracy_score(y, y_pred_depth4)
print(f"Training Accuracy (max_depth=4): {accuracy_depth4:.2f}")

# Evaluate the model with max_depth=2.
y_pred_depth2 = tree_clf_depth2.predict(X)
accuracy_depth2 = accuracy_score(y, y_pred_depth2)
print(f"Training Accuracy (max_depth=2): {accuracy_depth2:.2f}")

# Step 5: Experiment
# Experiment: Remove the 'Reservation' attribute and retrain the tree.
print("\nExperiment: Retraining the tree after removing the 'Reservation' attribute")

X_exp = df.drop(["Wait", "Reservation"], axis=1)
X_exp = pd.get_dummies(X_exp)

tree_clf_exp = DecisionTreeClassifier(criterion="entropy", max_depth=4, random_state=42)
tree_clf_exp.fit(X_exp, y)

plt.figure(figsize=(20, 10))
plot_tree(tree_clf_exp, feature_names=X_exp.columns, class_names=["No", "Yes"], filled=True)
plt.title("Decision Tree without 'Reservation' attribute")
plt.show()