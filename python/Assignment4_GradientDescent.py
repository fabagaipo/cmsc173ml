# -*- coding: utf-8 -*-
"""Bagaipo - Assignment 4 - Gradient Descent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1apgAPy_EKX2ivFrFo-lmdEjZGTvyX1PU

Perform one step of gradient descent on the following unregularized objective using exponential loss:

With the following inputs:

$$X = \begin{bmatrix}1 & 1 & 1\\
2 & 2 & 1\\
1 & 2 & 3
\end{bmatrix}$$

$$Y = \begin{bmatrix}-1\\
1\\
1
\end{bmatrix}$$

$$w = \begin{bmatrix}0.64\\
0.5\\
0.85
\end{bmatrix}$$

$$ b = 1 $$

$$ n = 0.3 $$

---


1. Compute the different values of the dot product of $w \cdot x_n$ for $1 \leq n \leq 3$ (since $x$ has 3 rows).
"""

#Write your solution here

"""Solution:

$$X = \begin{bmatrix}1 & 1 & 1\\
2 & 2 & 1\\
1 & 2 & 3
\end{bmatrix}$$

$$w = \begin{bmatrix}0.64\\
0.5\\
0.85
\end{bmatrix}$$

$$ \text{dot product} =  ((0.64 + 0.5 + 0.85)
     (1.28 + 1 + 0.85)
     (0.64 + 1 + 2.55))$$

$$ \text{dot product} = (1.99, 3.13, 4.19)$$

---

2. Solve for the derivative with respect to the bias, $\frac{∂𝓛}{∂b}$:

$
\begin{align*}
\frac{∂𝓛}{∂b} &= -∑_{n}{y_n \exp [-y_n (w \cdot x_n + b)]} \\
\end{align*}
$
"""

#Write your solution here

"""Solution:

$$\text{Derivative with respect to the bias} = -[-1(exp[1 (0.64 * 1 + 1)]) +  -1(exp[1 (0.5 * 1 + 1)]) + -1(exp[1 (0.85 * 1 + 1)])
  1(exp[-1 (0.64 * 2 + 1)]) +  1(exp[-1 (0.5 * 2 + 1)]) + 1(exp[-1 (0.85 * 1 + 1)])
  1(exp[-1 (0.64 * 1 + 1)]) +  1(exp[-1 (0.5 * 2 + 1)]) + 1(exp[-1 (0.85 * 3 + 1)])]$$
\
  $$\text{Derivative with respect to the bias} = 19.86 $$

---

3. Solve for the gradient with respect to the weights, ∇_w𝓛:

$
\begin{align*}
∇_w𝓛 &= -∑_{n}{y_n x_n \exp [-y_n (w \cdot x_n + b)]} \\
\end{align*}
$
"""

#Write your solution here

"""Solution:

$$\text{Derivative with respect to the weights} = -[(-1*1)exp(-(-1)(0.64*1+1) + (-1*1)exp(-(-1)(0.5*1+1)) + (-1*1)exp(-(-1)(0.85*1+1)
  (1*2)exp(-(1)(0.64*2+1) + (1*2)exp(-(1)(0.5*2+1)) + (1*1)exp(-(1)(0.85*2+1)
  (1*1)exp(-(1)(0.64*1+1) + (1*2)exp(-(1)(0.5*2+1)) + (1*3)exp(-(1)(0.85*3+1)]  $$
\
$$\text{Derivative with respect to the weights} = (19.848, 19.842, 19.853) $$

---

4. Update the bias

$
\begin{align*}
b_1 &= b - η\frac{∂𝓛}{∂b} \\
\end{align*}
$
"""

#Write your solution here

"""Solution:

$$b_1 = 1 -0.3 \times 19.85$$
$$b_1 = -4.96$$

---

5. Update the weights:
## $
\begin{align*}
w_1 &= w_1 - η∇_w𝓛 \\
\end{align*}
$
"""

#Write your solution here

"""Solution:

$$w_1 = 0.64 - 0.3 \times 19.848$$
$$w_1 = -5.3144$$
\
$$w_2 = 0.5 - 0.3 \times 19.842$$
$$w_2= -5.4526$$
\
$$w_3 = 0.85 - 0.3 \times 19.853$$
$$w_3 = -5.1059$$

#Write your conclusion and explanation of the process.

---

To do one step of gradient descent, we had to do the following:
- Compute the dot product
- Solve for the derivative with respect to the biad
- Solve for the derivative with respect to the weights
- Update the bias
- Update the weights

By taking the function's derivative with respect to the given weight and bias, we calculated the gradient. Take the partial derivatives with respect to each weight and bias since there are multiple parameters. Multiplying the value of derivatives with our learning rate (0.3) and -1 will yield the descent value for our parameters. By combining the parameter's current value and the descending value, we updated the value of our weight and bias.
"""