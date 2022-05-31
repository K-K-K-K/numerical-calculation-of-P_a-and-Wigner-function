# numerical-calculation-of-P_a-and-Wigner-function
This program numerically calculates $P_a$ and Wigner function $W(x, p)$ to search $\eta$(transmissivity of a beamsplitter) with which approximate photon-subtracted squeezed vacuum state $\rho$ become non-convex gaussian state having positive wigner function.

Calculated formulas are as follows:
$$ P_a = \frac{1}{67}((64\eta + 9\eta(1-\eta)^2) - a\times(9\eta^2(1-\eta)+3\eta^3)) $$

$$
\begin{align}
  W(x,p) &= \frac{2}{67\pi} \mathrm{exp}(-2(x^2 + p^2)) ( (67-146\eta+36\eta^2 -24\eta^3)\\
  &\quad + ((292 + 96\sqrt{2})\eta - (144 + 192\sqrt{2})\eta^2 + 144\eta^3) x^2 \\
  &\quad + ((292 - 96\sqrt{2})\eta - (144 - 192\sqrt{2})\eta^2 + 144\eta^3) p^2 \\
  &\quad + ((72 + 128\sqrt{2})\eta^2 - 144\eta^3) x^4 + ((72 - 128\sqrt{2})\eta^2 - 144\eta^3) p^4 \\
  &\quad + 32\eta^3 x^6 + 32 \eta^3 p^6 + 96\eta^3 x^4 p^2 + 96\eta^3 x^2 p^4)
\end{align}
$$

## environment
- Python 3.6.9
- numpy 1.19.5
