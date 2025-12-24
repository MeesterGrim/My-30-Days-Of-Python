import subprocess

# execute system command to get python version
try:
    result = subprocess.run(
        ['python3', '--version'],
        capture_output=True,  # Captures stdout and stderr
        text=True,            # Returns strings instead of bytes
        check=True            # Raises exception if command fails
    )
    print(result.stdout)
except Exception as e:
    print("Unable to get Python version")
    print({e})

print(3 + 4)   # addition(+)
print(3 - 4)   # subtraction(-)
print(3 * 4)   # multiplication(*)
print(3 / 4)   # division(/)
print(3 ** 4)  # exponential(**)
print(3 % 4)   # modulus(%)
print(3 // 4)  # Floor division operator(//)

# text can be contained either in ' or "
print()
print('Your name')
print("Your family name")
print('Your country')
print("I am enjoying 30 days of python")

# check the data types of the specified values
print()
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Your name'))
print(type("Your family name"))
print(type('Your country'))

# Find an Euclidian distance between (2, 3) and (10, 8)
# In the Euclidean plane, let point p have Cartesian coordinates (p1 , p2) and let point q 
# have coordinates (q1 , q2). Then the distance between p and q by:
# d (p , q) = sqrt ((p1 − q1) ^ 2 + (p2 − q2)^2).
print()
distance = (((2 - 10) ** 2) + ((3 - 8) ** 2)) ** .5
print (distance)