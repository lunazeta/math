from qmath import Function

language = input("EN/FR: ")

f = Function(input("function: "))

evaluateAt = float(input("evaluated at: "))

print(f.decomposition)

print(f"the function f(x) = {f.funct} evaluated at x = {evaluateAt}: {f.sub(evaluateAt)}")

print("integrate from 0.0 to 5.0: " + str(f.integrate(0.0, 5.0, 0.01)))