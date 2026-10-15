# 2. House Price Data Preprocessing System

# Intermediate:

# Goal: Prepare a housing dataset for machine learning without using Pandas or Scikit-learn.
# What you'll build:
# - Generate 100 house records with features such as area, bedrooms, age and distance from the city.
# - Identify missing values using np.isnan().
# - Replace missing values with column means.
# - Detect outliers using statistical methods.
# - Normalize features using Min-Max scaling.
# - Standardize features using Z-score normalization.
# - Shuffle the dataset randomly.
# - Split features and prices into training and testing sets (80:20).
# NumPy functions:
# random.default_rng(), isnan(), nanmean(), where(), percentile(), mean(), std(), min(), max(), concatenate()
# ML skills: Data cleaning, feature engineering, normalization, dataset preparation.


import numpy as np

# STEP 1: Generate housing dataset
rng = np.random.default_rng(42)     # Generates random numbers - 42 is random seed

area = rng.integers(500, 4000, 100)     
bedrooms = rng.integers(1, 6, 100)
age = rng.integers(0, 40, 100)
distance = rng.uniform(1, 30, 100)

X = np.column_stack((area, bedrooms, age, distance))
X = X.astype(float)

# House prices in lakhs (synthetic target)
price = (
    area * 0.012
    + bedrooms * 5
    - age * 0.3
    - distance * 0.5
    + rng.normal(0, 5, 100)
)

print("Original dataset shape:", X.shape)
print("First 5 houses:\n", X[:5])


# STEP 2: Introduce missing values
X[5, 0] = np.nan
X[15, 2] = np.nan
X[25, 3] = np.nan

print("\nMissing values:", np.isnan(X).sum())


# STEP 3: Shuffle and split data first
indices = rng.permutation(len(X))

X = X[indices]
price = price[indices]

X_train = X[:80].copy()
X_test = X[80:].copy()

y_train = price[:80]
y_test = price[80:]


# STEP 4: Replace missing values using training means
column_means = np.nanmean(X_train, axis=0)

for data in (X_train, X_test):
    rows, cols = np.where(np.isnan(data))
    data[rows, cols] = column_means[cols]

print("\nMissing values after cleaning:",
      np.isnan(X_train).sum() + np.isnan(X_test).sum())


# STEP 5: Detect and handle outliers using IQR
Q1 = np.percentile(X_train, 25, axis=0)
Q3 = np.percentile(X_train, 75, axis=0)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = (X_train < lower) | (X_train > upper)

print("\nOutliers detected:", np.sum(outliers))

# Clip outliers using training boundaries
X_train = np.clip(X_train, lower, upper)
X_test = np.clip(X_test, lower, upper)


# STEP 6: Min-Max normalization
min_values = np.min(X_train, axis=0)
max_values = np.max(X_train, axis=0)

ranges = max_values - min_values
ranges = np.where(ranges == 0, 1, ranges)

X_train_minmax = (X_train - min_values) / ranges
X_test_minmax = (X_test - min_values) / ranges

print("\nMin-Max normalized data:\n",
      X_train_minmax[:5])


# STEP 7: Z-score standardization
mean_values = np.mean(X_train, axis=0)
std_values = np.std(X_train, axis=0)

std_values = np.where(std_values == 0, 1, std_values)

X_train_zscore = (X_train - mean_values) / std_values
X_test_zscore = (X_test - mean_values) / std_values

print("\nStandardized data:\n",
      X_train_zscore[:5])


# STEP 8: Final dataset
# Choose ONE scaling method for model training
X_train_final = X_train_zscore
X_test_final = X_test_zscore

print("\nTraining features:", X_train_final.shape)
print("Testing features:", X_test_final.shape)
print("Training prices:", y_train.shape)
print("Testing prices:", y_test.shape)

# Optional: combine features and prices for inspection
train_dataset = np.concatenate(
    (X_train_final, y_train.reshape(-1, 1)),
    axis=1
)

print("\nFinal training dataset:\n",
      train_dataset[:5])
