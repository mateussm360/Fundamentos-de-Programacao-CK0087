numero = 10
print(f"numero: {numero}")

# 10 + 2 = 12, numero = 12
numero += 2
print(f"{10} + {2} = {numero}")

# 12 - 2 = 10, numero = 10
numero -= 2
print(f"{12} - {2} = {numero}")

# 10 * 2 = 20, numero = 20
numero *= 2
print(f"{10} * {2} = {numero}")

# 20 / 2 = 10, numero = 10.0 (float)
numero /= 2
print(f"{20} / {2} = {numero}")

# 10.0 // 2 = 5, numero = 5.0 (float)
numero //= 2
print(f"{10.0} // {2} = {numero}")

# 5 = 2 * 2 + r => r = 5 - 4 => r = 1.0 (float)
numero %= 2
print(f"{5.0} % {2} = {numero}")

# 4 ** 2 = 16, numero = 16
numero = 4
numero **= 2
print(f"{4} ** {2} = {numero}")