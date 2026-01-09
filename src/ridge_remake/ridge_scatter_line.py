def ridge_scatter_line(ax, x_line, y_line, *, line_kwargs=None, label=None):
    """
    Overlay a precomputed regression line onto an existing scatter plot.

    This function assumes another function has already created the scatter plot
    on the provided Matplotlib Axes object, and that the regression line has
    already been computed and stored as coordinate arrays. It adds the line to
    the same axes so both elements appear in a single plot.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes containing the existing scatter plot.
    x_line : array-like of shape (n_points,)
        X-coordinates of the regression line (typically sorted).
    y_line : array-like of shape (n_points,)
        Y-coordinates of the regression line. Must be the same length as x_line.
    line_kwargs : dict, optional
        Keyword arguments forwarded to Matplotlib's plot() to style the line
        (e.g., {"linewidth": 2, "linestyle": "--"}). If None, defaults are used.
    label : str, optional
        Legend label for the regression line.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The same axes, with the regression line added.
    line : matplotlib.lines.Line2D
        The line artist created by Matplotlib.

    Notes
    -----
    This function does not compute the regression line and does not recreate the
    scatter plot; it only overlays the provided line on the existing axes.
    """
    pass
