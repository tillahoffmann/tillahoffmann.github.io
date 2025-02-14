---
layout: post
published: false
---

## 1\. Bipartite graphical models

Consider a hierarchical model $M$ with parameters $\Theta=\left\\{ \theta_ {1},\theta_ {2},\ldots\right\\}$ that we want to fit to data $d$. Without loss of generality, we can consider the data as part of the parameter set if we demand that "data parameters" are leaf nodes of the graphical model. In the following, we will not distinguish between parameters and data.

We represent the hierarchical model as a directed, acyclic, bipartite graph [1]: Each node is classified as either a **parameter** or a **distribution**; links are directed and are only allowed between groups but not within groups; the graph must not have any directed cycles. As an example, we consider the simple linear model shown in Fig. 1.


Focusing on a single parameter $\theta_ {i}\in\Theta$, we partition the parameters into disjoint sets
$$\Theta =\left\{ \theta_ {i}\right\} \cup N_ {i}\cup\bar{N}_ {i}. $$
The **neighbours** $N_ {i}$ are parameters separated from $\theta_ {i}$ by exactly two links. The remaining parameters $\bar{N}_ {i}$ are separated from $\theta_ {i}$ by more than two links. We further partition the neighbours into parents $N_ {i}^{\mathrm{p}}$ that are two levels above $\theta_ {i}$ in the hierarchy, children $N_ {i}^{\mathrm{c}}$ that are two levels below $\theta_ {i}$, and siblings $N_ {i}^{\mathrm{s}}$ that share a child distribution with $\theta_ {i}$ and are at the same level as $\theta_ {i}$.

Recall that two events $A$ and $B$ are conditionally independent given a third event $C$ if $P\left(AB|C\right)=P\left(A|C\right)P\left(B|C\right)$ [2]. Consequently,
\begin{align\*}
P\left(A|BC\right) & =\frac{P\left(AB|C\right)}{P\left(B|C\right)}\\\\
& =\frac{P\left(A|C\right)P\left(B|C\right)}{P\left(B|C\right)}\\ & =P\left(A|C\right).
\end{align\*}
To utilise the structure of the graphical model, we demand the following conditional independence relations
\begin{align}
P\left(\theta_ {i}\bar{N}_ {i}|MN_ {i}\right) & =P\left(\theta_ {i}|MN_ {i}\right)P\left(\theta_ {i}|MN_ {i}\right)\label{eq:independence-nbar}\\\\\\
P\left(\theta_ {i}N_ {i}^{\mathrm{s}}|MN_ {i}^{\mathrm{p}}\right) & =P\left(\theta_ {i}|MN_ {i}^{\mathrm{p}}\right)P\left(N_ {i}^{\mathrm{s}}|MN_ {i}^{\mathrm{p}}\right).\label{eq:independence-sibling}
\end{align}

The first relation states that $\theta_ {i}$ is independent of other parameters $\bar{N}_ {i}$ given its neighbours $N_ {i}$. The second relation states that $\theta_ {i}$ is independent of its siblings $N_ {i}^{\mathrm{s}}$ given its parents $N_ {i}^{\mathrm{p}}$.

In Sec. 2, we derive an expression for the conditional distribution of a parameter given its neighbours. We apply this expression to the simple linear model in Sec. 4.

## 2\. Conditional distributions

For the purpose of Gibbs sampling, we are interested in the conditional distribution of a parameter $\theta_ {i}$ given all the other parameters
\begin{equation\*}
C_ {i}\equiv P\left(\theta_ {i}|MN_ {i}\bar{N}_ {i}\right).
\end{equation\*}
By Eq. (\ref{eq:independence-nbar}), $\theta_ {i}$ and $\bar{N}_ {i}$ are conditionally independent given $N_ {i}$ such that
\begin{equation} P\left(\theta_ {i}|MN_ {i}\bar{N}_ {i}\right) =P\left(\theta_ {i}|MN_ {i}\right),\label{eq:reduced-conditional} \end{equation}
i.e. the distribution of $\theta_ {i}$ depends only on the parameter values of its neighbours $N_ {i}$ as expected. Expanding the parameter set $N_ {i}$ and applying Bayes' theorem to Eq. (\ref{eq:reduced-conditional}), we find
\begin{align\*}
P\left(\theta_ {i}|MN_ {i}^{\mathrm{c}}N_ {i}^{\mathrm{s}}N_ {i}^{\mathrm{p}}\right) & =\frac{P\left(N_ {i}^{\mathrm{c}}|MN_ {i}^{\mathrm{s}}N_ {i}^{\mathrm{p}}\theta_ {i}\right)}{P\left(N_ {i}^{\mathrm{c}}|MN_ {i}^{\mathrm{s}}N_ {i}^{\mathrm{p}}\right)}\\\\
& \quad\times P\left(\theta_ {i}|MN_ {i}^{\mathrm{s}}N_ {i}^{\mathrm{p}}\right).
\end{align\*}
We are only interested in the form of the conditional distribution $C_ {i}$ as a function of $\theta_ {i}$ and drop the normalisation to find
\begin{equation} C_ {i}\propto P\left(N_ {i}^{\mathrm{c}}|MN_ {i}^{\mathrm{s}}N_ {i}^{\mathrm{p}}\theta_ {i}\right)P\left(\theta_ {i}|MN_ {i}^{\mathrm{p}}\right),\label{eq:final}
\end{equation}
where we have used the conditional independence relation Eq. (\ref{eq:independence-sibling}) to simplify the second term. We can easily obtain both terms from the bipartite graph. The general structure is shown in Fig. 2.


## 3\. Marginalisation

Whenever possible, we want to marginalise over latent parameters analytically. Consider the model shown in Fig. 3 with latent parameter $y$. The conditional distribution for $z$ given $x$ may be expressed as
\begin{align\*}
P\left(z|x\right) & =\int dy\, P\left(zy|x\right)\\\\
& =\int dy\, P\left(z|y\right)P\left(y|x\right),
\end{align\*}
where we have used the conditional independence relation $P\left(z|xy\right)=P\left(z|y\right)$ to obtain the second line.


## 4\. Linear model

Consider the simple linear model shown in Fig. 1\. We consider each parameter in turn and obtain the conditional distributions
\begin{align}
C_ {\mu} & \propto\prod_ {i}N\left(\mu,\Sigma;x_ {i}\right)\label{eq:C_ =00007Bmu=00007D}\\\\
C_ {\Sigma} & \propto\prod_ {i}N\left(\mu,\Sigma;x_ {i}\right)\label{eq:C_ =00007BSigma=00007D}\\\\
C_ {x_ {i}} & \propto N\left(\mu,\Sigma;x_ {i}\right)N\left(x_ {i},\sigma,\hat{x}_ {i}\right)\nonumber \\\\
& \quad\times N\left(ax_ {i}+b,\sigma;\hat{y}_ {i}\right)\label{eq:C_ =00007Bx_ i=00007D}\\\\
C_ {a} & \propto\prod_ {i}N\left(ax_ {i}+b,\sigma;\hat{y}_ {i}\right)\label{eq:C_ a}\\\\
C_ {b} & \propto\prod_ {i}N\left(ax_ {i}+b,\sigma;\hat{y}_ {i}\right),\label{eq:C_ b} \end{align}
where $N\left(\alpha,\beta;\gamma\right)\propto\exp\left[-\frac{1}{2}\left(\frac{\beta-\alpha}{\gamma}\right)^{2}\right]$ and we have assumed uniform priors for $\mu$, $\Sigma$, $a$ and $b$. We need to simplify the distributions to be able to sample from them efficiently. Consider Eq. (\ref{eq:C_ =00007Bmu=00007D})
\begin{align\*}
C_ {\mu} & \propto\exp\left[-\frac{1}{2\Sigma^{2}}\sum_ {i}\left(\mu^{2}-2x_ {i}\mu\right)\right]\\\\
& \propto\exp\left[-\frac{N}{2\Sigma^{2}}\left(\mu^{2}-2\mu\left\langle x\right\rangle \right)\right]\\\\
& =N\left(\left\langle x\right\rangle ,\frac{\Sigma}{\sqrt{N}};\mu\right),
\end{align\*}
where $N$ is the number of data points and $\left\langle x\right\rangle =\frac{1}{N}\sum_ {i=1}^{N}x_ {i}$ is the mean of the latent variables. For the sake of simplicity, we assume that $\Sigma$ is known. Consider Eq. (\ref{eq:C_ =00007Bx_ i=00007D})
\begin{align\*} C_ {x_ {i}} & \propto\exp\left[-\frac{x_ {i}^{2}-2x_ {i}\mu}{2\Sigma^{2}}-\frac{x_ {i}^{2}-2x_ {i}\hat{x}_ {i}}{2\sigma^{2}}\right.\\\\
& \qquad\left.-\frac{a^{2}x_ {i}^{2}-2x_ {i}a\left(\hat{y}_ {i}-b\right)}{2\sigma^{2}}\right]\\\\
& =N\left(\frac{\Sigma^{2}(a(\hat{y}_ {i}-b)+\hat{x}_ {i})+\mu\sigma^{2}}{\left(a^{2}+1\right)\Sigma^{2}+\sigma^{2}},\right.\\\\
& \qquad\left.\frac{\sigma^{2}\Sigma^{2}}{\left(a^{2}+1\right)\Sigma^{2}+\sigma^{2}};x_ {i}\right).
\end{align\*}
Consider Eq. (\ref{eq:C_ a}) and (\ref{eq:C_ b})
\begin{align\*} C_ {a,b} & \propto\exp\left[-\frac{1}{2\sigma^{2}}\sum_ {i}\left(a^{2}x_ {i}^{2}+2abx_ {i}\right.\right.\\\\
& \qquad\left.\left.-2ax_ {i}\hat{y}_ {i}+b^{2}-2b\hat{y}_ {i}\right)\right]\\\\
C_ {a} & =N\left(\frac{\left\langle x\hat{y}\right\rangle -b\left\langle x\right\rangle }{\left\langle x^{2}\right\rangle },\frac{\sigma^{2}}{N\left\langle x^{2}\right\rangle }\right)\\\\
C_ {b} & =N\left(\left\langle \hat{y}\right\rangle -a\left\langle x\right\rangle ,\frac{\sigma^{2}}{N}\right). \end{align\*}
 We can now sample from the conditional distributions.

Consider a synthetic dataset of $N=100$ data points generated from a population with mean $\mu=5$ and standard deviation $\Sigma=1$ as shown in Fig. 4}. The linear model is defined by $a=3$, $b=-1$ and we assume a measurement error with standard deviation $\sigma=0.1$. Running a Gibbs sampler for $10^{5}$ steps, we posterior densities for the linear model parameters $a$ and $b$ as shown in Fig. 5 and 6.


## References

1.  Mark Newman. _[Networks: An Introduction](http://www.amazon.co.uk/Networks-Introduction-Mark-Newman/dp/0199206651)_. OUP, 2010\. ISBN 0199206651.
2.  David J. C. MacKay. _[Information Theory, Inference and Learning Algorithms](http://www.amazon.co.uk/Information-Theory-Inference-Learning-Algorithms/dp/0521642981)_. CUP, 2003\. ISBN 0521642981.
