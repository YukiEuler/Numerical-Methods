def ForwardDiff(f, x, h = 0.00001):
    """
    Check the differential of f(x) with forward differential

    Parameters
    ----------
    f : function with one parameter
    x : float or int
    h : float, default = 0.00001
    """
    try:
        return (f(x+h) - f(x)) / h
    except:
        raise ValueError("Error")

def BackwardDiff(f, x, h = 0.00001):
    """
    Check the differential of f(x) with backward differential

    Parameters
    ----------
    f : function with one parameter
    x : float or int
    h : float, default = 0.00001
    """
    try:
        return (f(x) - f(x-h)) / h
    except:
        raise ValueError("Error")

def CenteredDiff(f, x, h = 0.00001):
    """
    Check the differential of f(x) with centered differential

    Parameters
    ----------
    f : function with one float or int parameter
    x : float or int
    h : float, default = 0.00001
    """
    try:
        return (f(x+h) - f(x-h)) / (2*h)
    except:
        raise ValueError("Error")