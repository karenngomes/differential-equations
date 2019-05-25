import math

radius_of_earth = 6.371e6  # m

f = math.sqrt(4)  # 4 ** 0.5
g = radius_of_earth * math.sin(math.pi /
                               180.0 * 23.4)  # in radians, not in degrees

print(f, g)


