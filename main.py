from qmath import Function

language = input("EN/FR: ")

f = Function(input("function: "))

evaluateAt = float(input("evaluated at: "))

print(f.decomposition)

print(f"the function f(x) = {f.funct} evaluated at x = {evaluateAt}: {f.sub(evaluateAt)}")