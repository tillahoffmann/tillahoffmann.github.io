---
layout: post
published: true
---

Let the vector of random variables $\mathbf{x}$ be Dirichlet-distributed with parameters $\boldsymbol{\alpha}$ such that 
\begin{equation\*}
P_ {\boldsymbol{\alpha}}\left(\mathbf{x}\right)=\frac{\delta\left(1-\sum_ {i=1}^{n}x_ {i}\right)}{B\left(\boldsymbol{\alpha}\right)}\prod_ {i=1}^{n}x_ {i}^{\alpha_ {i}-1}, 
\end{equation\*}
where $B\left(\boldsymbol{\alpha}\right)=\frac{\prod_ {i=1}^{n}\Gamma\left(\alpha_ {i}\right)}{\Gamma\left(\sum_ {i=1}^{n}\alpha_{i}\right)}$ ensures the correct normalisation of the distribution. Consider the expectation value of powers of the random variables under the Dirichlet distribution 
\begin{align\*} 
\left\langle \prod_ {i=1}^{n}x_ {i}^{\beta_ {i}}\right\rangle & =\int d\mathbf{x}\,\frac{\delta\left(1-\sum_ {i=1}^{n}x_ {i}\right)}{B\left(\boldsymbol{\alpha}\right)}\prod_ {i=1}^{n}x_ {i}^{\alpha_ {i}+\beta_ {i}-1}\\\\ & =\frac{B\left(\boldsymbol{\alpha}+\boldsymbol{\beta}\right)}{B\left(\boldsymbol{\alpha}\right)}\int d\mathbf{x}\, P_ {\boldsymbol{\alpha}+\boldsymbol{\beta}}\left(\mathbf{x}\right)\\\\ & =\frac{B\left(\boldsymbol{\alpha}+\boldsymbol{\beta}\right)}{B\left(\boldsymbol{\alpha}\right)},
\end{align\*} 
where the last equality holds because the integral over a probability distribution is unity. Plugging in the explicit form yields 
\begin{equation\*} 
\left\langle \prod_ {i=1}^{n}x_ {i}^{\beta_ {i}}\right\rangle =\frac{\Gamma\left(\sum_ {i=1}^{n}\alpha_ {i}\right)}{\Gamma\left(\sum_ {i=1}^{n}\alpha_ {i}+\beta_ {i}\right)}\times\prod_ {i=1}^{n}\frac{\Gamma\left(\alpha_ {i}+\beta_ {i}\right)}{\Gamma\left(\alpha_{i}\right)}.
\end{equation\*}
