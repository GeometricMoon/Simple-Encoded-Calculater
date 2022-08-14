class Calculater:
    def __init__(self):
        pass
    
    def Calculate(self,calculate):
        # GET VALUES
        inputs = self.get_input(calculate)

        # CALCULATE ANSWER
        answer = self.calculate(inputs)

        # OUTPUT TO THE OUTSIDE
        return answer        

    def get_input(self,calculate):
        # RESET ALL VALUES
        l = []
        l += calculate
        n1 = ""
        n2 = ""
        oper = ""
        oper_char = 0

        # GET FIRST NUMBER
        for char in range(len(l)):
            op =self.check_if_operator(l[char])
            if not op:
                n1 = str(n1) + l[char]
            else:
                oper = l[char]
                oper_char = char
                break

        # GET OPERATOR
        if oper == "":
            for char in range(len(l)):
                op =self.check_if_operator(l[char])
                if op:
                    oper = l[char]
                    oper_char = char
                    break

        # GET SECOND NUMBER
        for char in range(oper_char + 1,len(l)):
            op =self.check_if_operator(l[char])
            n2 = str(n2) + l[char]

        # RETURN VALUES IN COMPACT LIST
        compact = [n1,oper,n2]
        return compact
        

    def check_if_operator(self,char):
        # CHECK IF CHARACTER IS A OPERATOR
        if char == "+":
            return True
        elif char == "-":
            return True
        elif char == "*":
            return True
        elif char == "/":
            return True
        else:
            return False

    def calculate(self,data):
        # UNPACK DATA
        n1 = data[0]
        oper = data[1]
        n2 = data[2]

        # SET INIATIAL VARIABLES
        answer = 0

        # FIND RIGHT OPERATOR TO CALCULATE AND CALCULATE IT
        if oper == "+":
            answer = int(n1) + int(n2)
        elif oper == "-":
            answer = int(n1) - int(n2)
        elif oper == "*":
            answer = int(n1) * int(n2)
        elif oper == "/":
            answer = int(n1) / int(n2)
        else:
            AttributeError()

        # OUTPUT ANSWER COMPACTLY
        return answer