Problem 30: Complete NumPy ML Preprocessing Challenge

Build a complete numerical preprocessing pipeline using only NumPy.

Create a synthetic dataset with:
- At least 100 samples.
- At least 5 numerical features.
- A target array containing at least 2 classes.

Requirements:
1. Generate reproducible synthetic data.
2. Inspect shape, dtype, ndim, and size.
3. Detect and report NaN values.
4. Intentionally introduce some missing values.
5. Replace missing values with feature-wise means.
6. Detect and handle infinite values.
7. Calculate feature-wise mean, median, minimum, maximum, variance, and standard deviation.
8. Detect obvious extreme values and clip them to chosen bounds.
9. Shuffle the samples reproducibly.
10. Split the data into training and testing portions.
11. Standardize the training features.
12. Apply the training-set scaling parameters to the testing features.
13. Perform min-max scaling as a second scaling approach.
14. Use Boolean masking to inspect samples meeting a condition.
15. Calculate class counts using unique().
16. Use matrix multiplication to calculate a simple linear-model output from the processed training data.
17. Verify important shapes throughout the pipeline.
18. Confirm the final training and testing arrays contain no NaN or infinite values.

Restriction:
- Use only NumPy for numerical processing.
- Do not use Pandas, Scikit-learn, SciPy, TensorFlow, or PyTorch.
- This problem is intended as the final revision challenge before moving to Pandas.
