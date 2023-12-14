import time
import math

start_time = time.time()

def cis(y):
    if y[0] == 0:
        if y[1] > 0:
            return math.pi/2
        return 3*math.pi/2
    if y[0] > 0:
        if y[1] >= 0:
            return math.atan(y[1]/y[0])
        return 2*math.pi + math.atan(y[1]/y[0])
    return math.pi + math.atan(y[1]/y[0])

def nrm(y):
    return math.sqrt(y[0]**2 + y[1]**2)

def sfilt(theta):
    if theta < 0:
        return theta + math.pi*2
    return theta

def coins_for_loops(loops_given):
    loops = 0
    yn = [1, 0]
    n = 0
    A = 0
    theta = 0
    while loops < loops_given:
        n += 1
        tau = cis(yn)
        rho = math.sqrt(yn[1]**2 + yn[0]**2)
        alpha = math.acos(rho/2)
        theta1 = alpha + tau
        A += sfilt(theta1 - theta)
        theta = theta1
        yn = [(n*yn[0] + math.cos(theta))/(n+1), (n*yn[1] + math.sin(theta))/(n+1)]
        #y += [yn]
        #print("rho = ", rho)
        #print("tau = ", tau)
        #print("alpha = ", alpha)
        #print(A)
        loops = math.floor(A /( math.pi*2))
    return n+1
#print("1 - ",coins_for_loops(1))
#print("2 - ",coins_for_loops(2))
#print("10 - ",coins_for_loops(10))
#print("200 - ",coins_for_loops(200))
#print(" --- %s seconds --- "%(time.time() - start_time))
#print("400 - ",coins_for_loops(400))
#print(" --- %s seconds --- "%(time.time() - start_time))
#print("800 - ",coins_for_loops(800))
#print(" --- %s seconds --- "%(time.time() - start_time))
#print("1200 - ",coins_for_loops(1200))
#print(" --- %s seconds --- "%(time.time() - start_time))
#print("1600 - ",coins_for_loops(1600))
#print(" --- %s seconds --- "%(time.time() - start_time))
print("2020 - ",coins_for_loops(2020))
print(" --- %s seconds --- "%(time.time() - start_time))
