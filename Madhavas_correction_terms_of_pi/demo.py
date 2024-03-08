import math

# Madhava Leibniz series for pi
def pi(n, c):
    sum, i, sign  = 0, 0, 1
    while(i<n):
        sum += sign*4.0/(2*i+1)
        sign *= -1
        i += 1
    if(c == 1):
        sum += correction_term_1(n)
    elif(c == 2):  
        sum += correction_term_2(n)
    elif(c == 3):
        sum += correction_term_3(n)
    return sum

# correction terms in increasing accuracy

# c1 = 1/n
def correction_term_1(n):
    sign = 1 if n%2 == 0 else -1
    return sign/n

# c2 = 4n/(4n^2+1)
def correction_term_2(n):
    sign = 1 if n%2 == 0 else -1
    return sign*4.0*n/(4*n*n+1) 

# c3 = 4(n^2+1)/(4n^3+5n)
def correction_term_3(n):
    sign = 1 if n%2 == 0 else -1
    return sign*4.0*(n*n+1)/(4*n*n*n+5*n)

print("Deviation from pi for n = 10, 100, 1000 terms in the approximation series with the three correction terms:")

print("\nCorrection term 1:")
print("n = 10: ", pi(10, 1) - math.pi)
print("n = 100: ", pi(100, 1) - math.pi)
print("n = 1000: ", pi(1000, 1) - math.pi)

print("\nCorrection term 2:")
print("n = 10: ", pi(10, 2) - math.pi)
print("n = 100: ", pi(100, 2) - math.pi)
print("n = 1000: ", pi(1000, 2) - math.pi)

print("\nCorrection term 3:")
print("n = 10: ", pi(10, 3) - math.pi)
print("n = 100: ", pi(100, 3) - math.pi)
print("n = 1000: ", pi(1000, 3) - math.pi)