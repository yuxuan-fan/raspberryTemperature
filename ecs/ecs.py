b=0.2
g=9.8
a=3.14159
E=2*10**11
Q=10
L=0.15
c=6.28318

g1 = b*g*a*E/Q/L/L/L/c/c
print(g1)

g1 = b*g*a*E/(Q/L/L/L/c/c)

print(g1)

g1 = b*g*a*E/(Q*L**3*c**2)
print(g1)

g1 = b*g*a*E/Q*L**3*c**2
print(g1)