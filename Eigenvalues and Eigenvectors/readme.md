# Eigenvalues and Eigenvectors

<code>InverseIterationShifted</code> gets us the lowest eigenvalue in absolute value. Shifted method theoretically gives us all eigenvalues and their respectives eigenvectors. Some matrices gives us an error of singularity (adjust u for non-diagonal values, and try changing the increase on u), in the linalg.solve we cannot solve for a singular matrix, so it gives us this error. AllEigen is the function which returns all eigenvalues and their respective eigenvectors.
<br>

<code>Jacobi_Method</code> we use Jacobi's matrices and Jacobi sweep to return the accumulated matrix P (eigenvector's matrix) and our A diagonal matrix (eigenvalues are located in its diagonal).
<br>

<code>HouseholderTransformation</code> we use Householder to return our tri-diagonal matrix as well as our accumulated matrix. We return 1 of our eigenvalues and its respective eigenvector.
<br>

<code>PowerIteration</code> in a similar way with the inverseIteration, in PowerIteration we are able to return the highest absolute value eigenvalue of a specific matrix.
<br>

<code>QR_Algorithm</code> we use the QR decomposition, aswell as the Jacobi's matrices for this. We return a diagonal matrix A (eigenvalues located on the diagonal), an accumulated matrix P (with the original matrix's eigenvectors). Later on, we return the eigenvalues and its respective eigenvectors.
<br>


