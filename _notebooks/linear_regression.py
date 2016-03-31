import numpy as np
from matplotlib import pyplot as plt


def generate_data(n=1000, p=2, seed=1, theta=None, theta_mean=1, theta_std=1, X_mean=3, X_std=1):
    """
    Generate synthetic data for linear regression. Default parameters are chosen for illustration purposes.

    Parameters
    ----------
    n : int
        number of observations
    p : int
        number of features including bias
    noise_precision : float
        inverse variance of the observations
    seed : int
        seed for the random number generator
    theta : np.ndarray
        regression coefficients
    theta_mean : float
        mean of regression coefficients if randomly generated
    theta_std : float
        std of regression coefficients if randomly generated
    X_mean : float
        mean of features
    X_std : float
        std of features

    Returns
    -------
    (X, y, theta)
    """
    # Use a seed for reproducibility
    np.random.seed(seed)

    # Generate a design matrix
    X = np.hstack([np.ones((n, 1)), np.random.normal(X_mean, X_std, (n, p - 1))])
    # Define regression coefficients
    if theta is None:
        theta = np.random.normal(theta_mean, theta_std, p)
    # Generate observations
    y = np.dot(X, theta) + np.random.normal(0, 1, n)

    return X, y, theta


def plot_data(X, y, theta, ax=None):
    """
    Plot synthetic data for linear regression.

    Parameters
    ----------
    X : np.ndarray
        regression features
    y : np.ndarray
        observations
    theta : np.ndarray
        regression coefficients
    """
    ax = ax or plt.gca()
    # Plot the synthetic data
    ax.scatter(X[:, 1], y, marker='.', alpha=.5)

    # Plot the underlying relationship
    x = np.linspace(np.min(X[:, 1]), np.max(X[:, 1]))
    ax.plot(x, theta[0] + theta[1] * x, color='r', lw=2)
    ax.set_ylabel('Observations')
    ax.set_xlabel('Covariates')


def plot_parameter_trace(trace, reference=None, X=None, sigma=3, step=1, ax=None):
    """
    Plot a trace of parameter values.

    Parameters
    ----------
    trace : np.ndarray
        trace of parameter values as a matrix
    reference : np.ndarray
        vector of true values for comparison
    X : np.ndarray
        design matrix used to calculate uncertainties
    sigma : float
        how many standard deviations to plot
    """
    ax = ax or plt.gca()
    trace = np.asarray(trace)

    # Iterate over all parameters
    for j, x in enumerate(np.transpose(trace[::step])):
        # Plot the line
        line, = ax.plot(x, marker='.')
        # Plot the reference value
        if reference is not None:
            ax.axhline(reference[j], color=line.get_color(), ls=':')
        # Plot the uncertainty
        if X is not None:
            err = np.sum(X[:, j] ** 2) ** -0.5
            ax.fill_between(np.arange(len(x)), x - sigma * err,
                            x + sigma * err, color=line.get_color(), alpha=.2)

    ax.set_xlabel('Iteration')
    ax.set_ylabel(r'Parameter $\mu$')


def plot_elbo_trace(elbos, ax=None):
    """
    Plot a trace of the evidence lower bound.

    Parameters
    ----------
    elbos : np.ndarray
    """

    ax = ax or plt.gca()

    ax.plot(elbos, color='r', marker='.')
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    ax.set_ylabel(r'ELBO $\mathcal{L}$')
    ax.set_xlabel('Iteration')


def plot_trace(elbos, trace, reference=None, X=None, sigma=3, step=1):
    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, True)

    # Plot
    plot_parameter_trace(trace, reference, X, sigma, step, ax1)
    plot_elbo_trace(elbos, ax2)

    fig.tight_layout()
    return fig, (ax1, ax2)


def evaluate_elbo(X, y, mu):
    """
    Evaluate the ELBO up to additive constants.
    """
    predictor = np.dot(X, mu)
    return -0.5 * np.dot(predictor, predictor) + np.dot(y, predictor)


def evaluate_elbo_landscape(X, y, mu1, mu2):
    """
    Evaluate the ELBO over a grid of values.
    """
    return np.reshape([evaluate_elbo(X, y, (_mu1, _mu2)) for _mu1 in mu1 for _mu2 in mu2],
                      (len(mu1), len(mu2))).T


def plot_trajectory(X, y, trace, reference=None, ax=None, **kwargs):
    ax = ax or plt.gca()
    trace = np.asarray(trace)

    # Plot the trajectory
    ax.plot(trace[:, 0], trace[:, 1], marker='.')
    ax.set_xlabel(r'$\mu_1$')
    ax.set_ylabel(r'$\mu_2$')

    # Add the reference point
    if reference is not None:
        ax.scatter(*reference)

    # Plot the landscape
    mu1 = np.linspace(*ax.get_xlim())
    mu2 = np.linspace(*ax.get_ylim())
    landscape = evaluate_elbo_landscape(X, y, mu1, mu2)
    ax.contour(mu1, mu2, landscape, **kwargs)
