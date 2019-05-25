answer = 42
radius_of_earth = 6.371e6  # m

# Basic arithmetics
a = 3 * answer + 4
b = radius_of_earth ** 2 + (a + 3) ** 0.5

answer += 7

c = 5 // 4
d = 5 / 4  # or 4.
e = 1.0 * 5 / 4

print(radius_of_earth)
print(a, b, answer, c, d, e)

for h in range(7):
    i = h ** 2
    print(i)

k = 42
m = 43

while (k < 130 or m == 140):
    k += 1
    m += k

print(k, m)

if (k > 42):
    print('Hi')
elif (m > 43):
    print('Hello')
else:
    print('Bye')


def three_times(u):
    r = 2 * u
    return r + u


print(three_times(1), three_times(7))
