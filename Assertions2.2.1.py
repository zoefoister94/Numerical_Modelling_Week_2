def solveByBisect(f, a, b, nmax=100, e=1e-6):
    "Solve function f by bisection method."
    "Solve to error e starting from a and b. Maximum nmax iterations."
    
    #Iterate until the solution is within the error or too many iterations
    for it in range(max):
        c = 0.5*(a+b)
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
            