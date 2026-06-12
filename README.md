## Key Kalman Filter Matrices and Equations

State vector:

```math
\mathbf{x}_k =
\begin{bmatrix}
x_k \\
v_{x,k} \\
y_k \\
v_{y,k}
\end{bmatrix}
```

Measurement vector:

```math
\mathbf{z}_k =
\begin{bmatrix}
x_{measured,k} \\
y_{measured,k}
\end{bmatrix}
```

State transition model:

```math
\mathbf{F} =
\begin{bmatrix}
1 & \Delta t & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & \Delta t \\
0 & 0 & 0 & 1
\end{bmatrix}
```

Control model:

```math
\mathbf{G} =
\begin{bmatrix}
\frac{1}{2}\Delta t^2 & 0 \\
\Delta t & 0 \\
0 & \frac{1}{2}\Delta t^2 \\
0 & \Delta t
\end{bmatrix}
```

Measurement model:

```math
\mathbf{H} =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}
```

Noise covariance matrices:

```math
\mathbf{Q} =
\sigma_a^2
\begin{bmatrix}
\frac{\Delta t^4}{4} & \frac{\Delta t^3}{2} & 0 & 0 \\
\frac{\Delta t^3}{2} & \Delta t^2 & 0 & 0 \\
0 & 0 & \frac{\Delta t^4}{4} & \frac{\Delta t^3}{2} \\
0 & 0 & \frac{\Delta t^3}{2} & \Delta t^2
\end{bmatrix}
```

```math
\mathbf{R} =
\begin{bmatrix}
\sigma_x^2 & 0 \\
0 & \sigma_y^2
\end{bmatrix}
```

Prediction:

```math
\hat{\mathbf{x}}_k^- = \mathbf{F}\hat{\mathbf{x}}_{k-1} + \mathbf{G}\mathbf{u}
```

```math
\mathbf{P}_k^- = \mathbf{F}\mathbf{P}_{k-1}\mathbf{F}^T + \mathbf{Q}
```

Update:

```math
\mathbf{K}_k = \mathbf{P}_k^-\mathbf{H}^T(\mathbf{H}\mathbf{P}_k^-\mathbf{H}^T + \mathbf{R})^{-1}
```

```math
\hat{\mathbf{x}}_k = \hat{\mathbf{x}}_k^- + \mathbf{K}_k(\mathbf{z}_k - \mathbf{H}\hat{\mathbf{x}}_k^-)
```

```math
\mathbf{P}_k = (\mathbf{I} - \mathbf{K}_k\mathbf{H})\mathbf{P}_k^-
```

Here, `Q` is process noise, `R` is measurement noise, and `K` is the Kalman gain.

## References

https://github.com/hannanmustajab/2D-Billiard-Ball-Tracking-Using-Kalman-Filter.