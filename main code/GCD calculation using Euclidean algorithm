def gcd(a, b):
    """Calculate the Greatest Common Divisor (GCD) using the Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def modular_inverse(a, m):
    """Calculate the modular inverse of a under modulo m using the Extended Euclidean Algorithm."""
    if m <= 1:
        raise ValueError("Modulus must be greater than 1.")

    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0  # No modular inverse if m is 1
    while a > 1:
        # q is quotient
        q = a // m
        m, a = a % m, m  # Update a and m
        x0, x1 = x1 - q * x0, x0  # Update x0 and x1
    if x1 < 0:
        x1 += m0  # Ensure x1 is positive
    return x1

# Task 1: Calculate GCD and modular inverse for 1547 and 560
a, b = 1547, 560
gcd_result = gcd(a, b)

if gcd_result == 1:  # Only compute modular inverse if GCD is 1
    mod_inverse = modular_inverse(a, b)
    print(f"{a} ve {b} 1547 ve 560 sayıların EBOB (GCD): {gcd_result}")
    print(f"Modular inverse of {a} mod {b}:------ {mod_inverse}")
else:
    print(f"{a} ve {b} 1547 ve 560 sayıların EBOB (GCD): {gcd_result}.------ sayıların modüler tersini bulunmamatadır (not coprime).")

# Task 2: GCD and modular inverse calculations for three more pairs of numbers
pairs = [(103, 200), (1297,2017), (300, 125)]

for x, y in pairs:
    gcd_result = gcd(x, y)
    if gcd_result == 1:  # Only compute modular inverse if GCD is 1
        try:
            mod_inverse = modular_inverse(x, y)
            print(f"{x} ve {y} 1547 ve 560 sayıların EBOB (GCD): {gcd_result},------- {x} ve {y} sayıların modüler tersini: {mod_inverse}")
        except Exception as e:
            print(f"{x} ve {y} 1547 ve 560 sayıların EBOB (GCD): {gcd_result},------- {x} ve {y} sayıların modüler tersini bulunmamatadır: Not defined ({e})")
    else:
        print(f"{x} ve {y} 1547 ve 560 sayıların EBOB (GCD): {gcd_result}.------- sayıların modüler tersini bulunmamatadır (not coprime).")


#outputs
1547 ve 560 1547 ve 560 sayıların EBOB (GCD): 7.------ sayıların modüler tersini bulunmamatadır (not coprime).
103 ve 200 1547 ve 560 sayıların EBOB (GCD): 1,------- 103 ve 200 sayıların modüler tersini: 167
1297 ve 2017 1547 ve 560 sayıların EBOB (GCD): 1,------- 1297 ve 2017 sayıların modüler tersini: 1213
300 ve 125 1547 ve 560 sayıların EBOB (GCD): 25.------- sayıların modüler tersini bulunmamatadır (not coprime).
