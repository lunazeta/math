class Function():
    from math import pow

    #Decomposes a function string by separating it into parts and return a list of those parts
    #Parts include: Any numerals in the function, any x's in the function, and any operators in the function
    def __functionDecomposition(self, f: str):
        if not isinstance(f, str): raise TypeError(f"Expected {str(str)} for f but got type : " + str(type(f)))
          
        parts = []
        lookingAt = ""
        previousIsNumeric = False
        for i in range(0, len(f)):
            char = f[i]
            if char.isnumeric() or char == ".":
                previousIsNumeric = True
                lookingAt += char
                if i == len(f) - 1: parts.append(float(lookingAt))
                
            else:
                if previousIsNumeric:
                    parts.append(float(lookingAt))
                    lookingAt = ""

                if i == len(f) - 1 and char != "x": raise TypeError(self.errorCodes[self.language]["OperatorAtEnd"])
                if char != "x" and (f[i + 1] == "+"): raise TypeError(self.errorCodes[self.language]["SequentialOperators"])
                if char not in self.currentOperators: raise TypeError(self.errorCodes[self.language]["InvalidOperator"])

                parts.append(char)
                previousIsNumeric = False

        return parts

    def updateFunction(self, f: str):
        self.funct = f
        self.decomposition = self.__functionDecomposition(f)

    #Inititates Function object with a given function
    def __init__(self, f: str, lang: str = "en"):
        self.funct = f
        
        #Change to add new operators, must also add into sub(x: int)
        self.currentOperators = ["x", "+", "*", "/", "^"]
        self.errorCodes = {"EN": {"OperatorAtEnd":"Function given is invalid: A function cannot end with an operator", "SequentialOperators":"Function given is invalid: A function cannot have two sequential operators", "InvalidOperator":"Function given is invalid: The given function uses invalid operator type"},"FR": {"OperatorAtEnd":"La fonction donnée est non valide: Une fonction ne peut pas finir avec un opérateur", "SequentialOperators":"La fonction donnée est non valide: Une fonction ne peut pas avoir deux opérateurs séquentiels", "InvalidOperator":"La fonction donnée est non valide: La fonction utilise un opérateur non valide"}}
        self.supportedLanguages = ["EN", "FR"]

        #Language support (for errors only)
        #Note: did language with my own limited knowledge of french so be wary of translation errors
        try:
            if lang.upper() in self.supportedLanguages: self.language = lang.upper()
            else: self.language = "EN"
        except:
            self.language = "EN"

        self.decomposition = self.__functionDecomposition(f)

    #Takes x and subs it into the function
    def sub(self, x: float):
        if not isinstance(x, float): raise TypeError(f"Expected {str(float)} for x but got type : " + str(type(x)))
        
        decomposition = self.decomposition

        lookingAt = []
        newLookingAt = []
        for i in decomposition:
            lookingAt.append(i)
            newLookingAt.append(i)

        for part in lookingAt:
            if part == "x":
                lookingAt[lookingAt.index(part)] = x

        while len(lookingAt) != 1:

            part = lookingAt[0]
            
            #Defining all operators
            if isinstance(part, float):
                if lookingAt[1] == "+":
                    newLookingAt[0] = part + lookingAt[2]
                    newLookingAt.pop(2)
                    newLookingAt.pop(1)
                elif lookingAt[1] == "*":
                    newLookingAt[0] = part * lookingAt[2]
                    newLookingAt.pop(2)
                    newLookingAt.pop(1)
                elif lookingAt[1] == "/":
                    newLookingAt[0] = part / lookingAt[2]
                    newLookingAt.pop(2)
                    newLookingAt.pop(1)
                elif lookingAt[1] == "/":
                    newLookingAt[0] = part / lookingAt[2]
                    newLookingAt.pop(2)
                    newLookingAt.pop(1)
                elif lookingAt[1] == "^":
                    newLookingAt[0] = pow(part, lookingAt[2])
                    newLookingAt.pop(2)
                    newLookingAt.pop(1)
                else:
                    newLookingAt[0] = part * lookingAt[1]
                    newLookingAt.pop(1)
            
            lookingAt = newLookingAt

        return lookingAt[0]
    
    def integrate(self, lowerBound: float, upperBound: float, deltaX: float = 0.01):
        if not isinstance(lowerBound, float): raise TypeError(f"Expected {str(float)} for lowerBound but got type : " + str(type(lowerBound)))
        if not isinstance(upperBound, float): raise TypeError(f"Expected {str(float)} for upperBound but got type : " + str(type(upperBound)))
        if not isinstance(deltaX, float): raise TypeError(f"Expected {str(float)} for deltaX but got type : " + str(type(deltaX)))

        #Iterate over x with step size deltaX until x > upperBound
        x = lowerBound
        total = 0
        while x < upperBound:
            total += self.sub(x) * deltaX
            x += deltaX

        return total  