Problem 20: Random Dataset Shuffling and Selection

Create a dataset of 50 samples with 4 features and a matching target array.

Requirements:
- Generate a reproducible random permutation of sample indices.
- Shuffle the dataset using those indices.
- Select the first 40 samples as a training portion and the remaining 10 as a testing portion.
- Keep features and targets aligned.
- Verify the shapes.
- Verify that every original sample appears exactly once after shuffling.
- Use NumPy only for the split operation.
