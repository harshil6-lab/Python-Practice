# find the GCD(A,B).

def gcd(m,n):
    cf = []

    for i in range(1,min(m,n)+1):
        if(m%i)==0 and (n%i)==0 :
            cf.append(i)
    
    return (cf[-1])


# print(gcd(1,2))
# print(gcd(14,12))
# print(gcd(5,6))
# print(gcd(6,12))


#improved GDC(m,n)

def gcd(m,n):
    mrcf = 0
    for i in range(1,min(m,n) + 1):

        if(m%i)==0 and (n%i)==0 :
            mrcf = i
    
    return mrcf

print(gcd(1,2))
print(gcd(14,12))
print(gcd(5,6))
print(gcd(6,12))


# further improvement ( NO LIST )
#if we can start from last to first then the things are same but iteration is may be less.

def gcd(m,n):

    i = min(m,n)

    while i>=0:
        if(m%i)==0 and (n%i)==0:
            return i
        else:
            i = i-1


print(gcd(1,2))
print(gcd(14,12))
print(gcd(5,6))
print(gcd(6,12))


#Euclide Algoritham ...
