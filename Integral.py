def Trapezoid(f, a, b, n = 100000):
    """
    Calculate the integral with trapezoid method

    Parameters
    ----------
    f : function with one parameter
    a : float or int
        Lower bound of the integral
    b : float or int
        Upper bound of the integral
    n : int
        Number of subinterval
    """
    try:
        result = f(a) + f(b)
        d = (b-a) / n
        for i in range(1, n):
            result += 2 * f(a + i*d)
        result *= d/2
        return result
    except:
        raise ValueError("Error")
    
def Riemann(f, a, b, n = 100000, method = 'midpoint'):
    """
    Calculate the integral with left riemann, midpoint riemann or right riemann

    Parameters
    ----------
    f : function with one parameter
    a : float or int
        Lower bound of the integral
    b : float or int
        Upper bound of the integral
    n : int
        Number of subinterval
    method : str
        Method of riemann method, either left, midpoint or right
    """
    try:
        x = {'left' : 0, 'midpoint' : 0.5, 'right' : 1}[method]
    except:
        raise Exception(f'Method value \'{method}\' is not valid. Use either \'left\', \'right\' or \'midpoint\'')
    try:
        result = 0
        d = (b-a) / n
        for i in range(n):
            result += f(a + (x+i)*d)
        result *= d
        return result
    except:
        raise ValueError("Error")

def Simpson(f, a, b, n = 100000, method = '1/3'):
    """
    Calculate the integral with left riemann, midpoint riemann or right riemann

    Parameters
    ----------
    f : function with one parameter
    a : float or int
        Lower bound of the integral
    b : float or int
        Upper bound of the integral
    n : int
        Number of subinterval
    method : str
        Method of simpson method, either 1/3 or 3/8
    """
    try:
        x = {'1/3' : [2, 4, 1/3, 2], '3/8' : [2, 3, 3, 3/8, 3]}[method]
    except:
        raise Exception(f'Method value \'{method}\' is not valid. Use either \'1/2\' or \'3/8\'')
    try:
        result = f(a) + f(b)
        d = (b-a) / n
        for i in range(1, n):
            result += x[i % x[-1]] * f(a + i*d)
        result *= x[x[-1]] * d
        return result
    except:
        raise ValueError("Error")