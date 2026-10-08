Problem 26: Solving a Linear System

Create a small system of linear equations represented as Ax = b.

Requirements:
- Create a square coefficient matrix A.
- Create a target vector b.
- Solve the system using np.linalg.solve().
- Verify the solution by calculating A @ x.
- Calculate the residual between A @ x and b.
- Use allclose() to verify that the solution is numerically correct.
