class Calculator:
        
    def __init__(self,first_number,operator,second_number):
        # print("This is initializing.....")
        self.first_number =first_number
        self.second_number = second_number
        self.operator =operator
    
    def result(self):
        if self.operator =="+":
            return self.add()
        
        elif self.operator == "-":
            return self.sub()
        
        elif self.operator == "*":
            return self.mul()
        
        elif self.operator=="/":
            return self.div()
        
    def add(self):
        return self.first_number+self.second_number
    
    def sub(self):
        return self.first_number-self.second_number
    
    def mul(self):
        return self.first_number*self.second_number
    
    def div(self):
        return self.first_number/self.second_number

 