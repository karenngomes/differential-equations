import numpy

n = numpy.zeros(5)
n[0] = 20.
n[4] = 99.

print(n)
print(n[-1])

z = numpy.zeros([2, 3])

z[0, 1] = 7.
z[1, 2] = 8.

print(z)
z = 1. + 2. * z
print(z)
print(z[0])
print('line')
q = z
q[0, 0] = 42.
print(z)
