---
layout: post
published: True
hidden: True
---

Suppose we observe a network with time-dependent edges. At random times $t$ a pair of nodes $(i,j)$ becomes connected, and the edge disappears immediately, i.e. the arrival of edges is a point process. Let $t_n$ denote the time of the $n^\mathrm{th}$ edge which connects the two nodes $i_n$, and $j_n$. We can define a time-dependent adjacency matrix

$$
A_{uv}(t,\lambda)=\sum_{n:t_n \leq t}\exp\left(-\lambda(t-t_n)\right)\left(\delta_{ui_t}\delta_{vj_t} + \delta_{uj_t}\delta_{vi_t}\right),
$$

where the sum is over all edges that arrived before the current time, and the symmetrisation of indices in the parentheses ensures that the matrix is symmetric. The parameter $\lambda$ determines the time resolution of interest: small values of $\lambda$ give the adjacency matrix long memory and large values lead to short memory.

The time-dependent adjacency matrix has an interesting property: At a time $t'=t_m+\Delta<t_{m+1}$, the adjacency matrix can be obtained by rescaling the adjacency matrix at time $t_m$. In particular,

$$\begin{align*}
A_{uv}(t_m+\Delta,\lambda)&=\sum_{n:t_n \leq t}\exp\left(-\lambda(t_m+\Delta-t_n)\right)\left(\delta_{ui_t}\delta_{vj_t} + \delta_{uj_t}\delta_{vi_t}\right)\\
&=\exp\left(-\lambda \Delta\right)\sum_{n:t_n \leq t}\exp\left(-\lambda(t_m-t_n)\right)\left(\delta_{ui_t}\delta_{vj_t} + \delta_{uj_t}\delta_{vi_t}\right)\\
&=\exp\left(-\lambda\Delta\right)A_{uv}(t_m,\lambda).
\end{align*}$$

Suppose we want to perform community detection on the time-dependent adjacency by maximising the modularity. If the null model scales in the same manner as the adjacency matrix, the community assignments are fixed unless a new edge arrives. Consider the modularity given a vector of community assignments $c$

$$\begin{align*}
Q(t,\lambda)&=\frac{1}{2m(t,\lambda)}\sum_{uv}\left[A_{uv}(t,\lambda)-\frac{k_u(t,\lambda)k_v(t,\lambda)}{2m(t,\lambda)}\right]\delta_{c_uc_v}\\
\text{where }m(t,\lambda)&=\sum_{uv}A_{uv}(t,\lambda)\\
\text{and }k_u(t,\lambda)&=\sum_{v} A_{uv}(t,\lambda).
\end{align*}$$

Multiplying the adjacency matrix by a constant leaves the modularity unchanged because $m$ and $k$ are scaled by the same constant. Consequently, it is sufficient to optimize the modularity after every arrival of a new edge to know the community assignments at all times.

{% include mathjax.html %}