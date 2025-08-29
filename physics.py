# Predefined variables
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# 1. Function to convert Fahrenheit to Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

# 2. Test f_to_c with 100 Fahrenheit
f100_in_celsius = f_to_c(100)
print("100 Fahrenheit in Celsius is:", f100_in_celsius)

# 3. Function to convert Celsius to Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

# 4. Test c_to_f with 0 Celsius
c0_in_fahrenheit = c_to_f(0)
print("0 Celsius in Fahrenheit is:", c0_in_fahrenheit)

# 5. Function to calculate force (Newton's second law)
def get_force(mass, acceleration):
    return mass * acceleration

# 6. Test get_force with train variables
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies", train_force, "Newtons of force.")

# 8. Function to calculate energy (Einstein's equation)
def get_energy(mass, c=3*10**8):
    return mass * (c ** 2)

# 9. Test get_energy with bomb_mass
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies", bomb_energy, "Joules.")

# 11. Function to calculate work (Force × Distance)
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance

# 12. Test get_work with train variables
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")
