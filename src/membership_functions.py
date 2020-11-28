
def Gamma(x, a, m):
    if x <= a:
        return 0
    if x >= m:
        return 1
    return (x-a)/(m-a)

def L(x , a, m):
    if x <= a:
        return 1
    if x >= m:
        return 0
    return (m-x)/(m-a)

def Lambda(x, a, b, m):
    if a < x <= m:
        return (x-a)/(m-a)
    if m < x <= b:
        return (b-x)/(m-x)
    return 0

def Pi(x ,a ,b ,c ,d):
    if a < x <= b:
        return (x-a)/(b-a)
    if b < x <= c:
        return 1
    if c < x <= d:
        return (d-x)/(b-c)
    return 0

def S(x , a , c):
    if a < x <= (a+c)/2:
        return 2*((x-a)/(c-a))**2
    if (a+c)/2 < x < c:
        return 1 - (2 * ((x-a)/(c-a))**2)
    if x >= c:
        return 1
    return 0

def Z(x , a , c):
    if a < x <= (a+c)/2:
        return 1 - (2 *((x-a)/(c-a))**2)
    if (a+c)/2 < x < c:
        return 2 * ((x-a)/(c-a))**2
    if x >= c:
        return 1
    return 0

def Gaussiana(x , b , d):
    if x <= b:
        return S(x , b - d , b)
    return Z(x , b, b + d)