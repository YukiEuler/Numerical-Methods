def bisection(f, a, b, e = 1e-5):
    if f(a)*f(b) > 0:
        raise ValueError(f"Bisection methods fails for x in range {a} and {b}")
    x = a
    y = b
    m = (a+b)/2
    while abs(y-x) > e:
        f_m = f(m)
        if f(x)*f_m < 0:
            y = m
        elif f(y)*f_m < 0:
            x = m
        else:
            raise ValueError(f"Bisection methods fails for x in range {a} and {b}")
        m = (x+y)/2
    return m

def fixed_point(g, x, e = 1e-5):
    x_n = g(x)
    x_n1 = g(x_n)
    while abs(x_n1 - x_n) > e:
        x_n = x_n1
        x_n1 = g(x_n)
    return x_n1

def newton_raphson(f, f1, x, e = 1e-5):
    x_n = x
    x_n1 = x - f(x)/f1(x)
    while abs(x_n-x_n1) > e:
        x_n = x_n1
        x_n1 = x_n - f(x_n)/f1(x_n)
    return x_n1