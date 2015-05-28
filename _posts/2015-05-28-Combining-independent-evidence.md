---
layout: post
published: true
---

Suppose we know the conditional distributions $P\left(x|y\right)$ and $P\left(x|z\right)$ which we would like to combine to obtain the distribution $P\left(x|yz\right)$. Using Bayes' theorem, we find 
$$P\left(x|yz\right)=\frac{P\left(yz|x\right)P\left(x\right)}{P\left(yz\right)}.$$ 
We assume conditional independence of $y$ and $z$ given $x$ to obtain 
\begin{align} P\left(x|yz\right)&=\frac{P\left(y|x\right)P\left(x\right)P\left(z|x\right)P\left(x\right)}{P\left(x\right)P\left(yz\right)}\\\\
&=\frac{P\left(y\right)P\left(z\right)}{P\left(yz\right)}\frac{P\left(x|y\right)P\left(x|z\right)}{P\left(x\right)}\\\\
&\propto\frac{P\left(x|y\right)P\left(x|z\right)}{P\left(x\right)}, 
\end{align}
where we have dropped the first term because it is only an overall normalisation.

Note: The above relation only holds if $y$ and $z$ are conditionally independent given $x$. Intuitively, this is the case if $y$ and $z$ are independent sources of information (see below for an example).

##Example

Let $x=1$ if a sportsman took a performance enhancing drug, let $y=1$ if a drug test was positive, and let $z=1$ if the sportsman won a competition. The conditional independence assumption holds because the outcome of the drug test will not affect the outcome of the competition given $x$. Note that $y$ and $z$ are not unconditionally independent because the events are coupled by cheating.

Our prior suspicion of doping is $P\left(x\right)=\left(\begin{array}{cc}0.99 & 0.1\end{array}\right)$, where the first element corresponds to $x=0$ and the second corresponds to $x=1$. We assume that the test is 95% reliable such that 
$$P\left(y|x\right)=\left(\begin{array}{cc} 0.95 & 0.05\\ 0.05 & 0.95 \end{array}\right), $$ 
where $y$ is the row index and $x$ is the column index. Furthermore, assume that a competitor gains a 5% advantage to win a competition by taking a performance enhancing drug such that 
$$ P\left(z|x\right)=\left(\begin{array}{cc} 1-p & 1-1.05\times p\\ p & 1.05\times p \end{array}\right), $$ 
where $p=0.1$ is the probability to win a competition if the sportsman has not taken a drug.

Using Bayes' theorem and the relation derived above, the conditional probabilities that the sportsman cheated are 
\begin{align} 
P\left(x=1|y\right) &=\left(\begin{array}{cc} 0.161017 & 0.000531\end{array}\right),\\\\ 
P\left(x=1|z\right) &=\left(\begin{array}{cc} 0.009995 & 0.010498\end{array}\right),\\\\ 
P\left(x=1|yz\right) &=\left(\begin{array}{cc} 0.000531 & 0.000558\\\\ 0.160949 & 0.167718 \end{array}\right), 
\end{align}
where $y$ is the row index and $z$ is the column index in the last equation. As expected, the drug test provides stronger evidence for cheating than winning a competition $P\left(x=1|y=1\right)>P\left(x=1|z=1\right)$ but both pieces of evidence provide an even stronger case for the sportsman cheating $P\left(x=1|y=1\cap z=1\right)>P\left(x=1|y=1\right)$.
