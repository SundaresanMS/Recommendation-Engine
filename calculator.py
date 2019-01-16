class Calculator():
	def __init__(self,number_1,number_2):
		self.number_1 = number_1
		self.number_2 = number_2
	
	def add(self):
		return (self.number_1 +self.number_2)
		
	def subtract(self):
		return (self.number_1 - self.number_2)
		
	def multiply(self):
		return (self.number_1 * self.number_2)
		

	def exponent(self):
		return (self.number_1 ** self.number_2)
	
	
	
	def repeat_add(self):
		sum = 0
		
		for i in range(self.number_2):
			# sum = self.number_1 + sum  	
			sum = self.multiplier()+sum
		return (sum)
	
	def multiplier(self):
		return self.number_1
	
	
calculator= Calculator(5,6)

add = calculator.add() 
subtract = calculator.subtract() 
multiply = calculator.multiply() 
exponent = calculator.exponent() 
repeat_add =calculator.repeat_add()

		
print ('Addition Result',add)
print ('Subtraction Result',subtract)
print ('Multiplication Result',multiply)
print ('Exponent Result',exponent)
print ('Repeated Sum Result',repeat_add)


