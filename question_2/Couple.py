class Couple:


	def __init__(self, boy, girl):
		self.happiness = 0
		self.girl = girl
		self.boy = boy
		self.gifts = []
		self.compatibility = 0
		
	def set_compatibility(self):
		a = self.boy.budget - self.girl.maintenance
		b = abs(self.boy.attract - self.girl.attract)
		c = abs(self.boy.intelligence - self.girl.intelligence)
		self.compatility = a+b+c	

	def set_happiness(self):
		self.happiness = self.boy.happiness + self.girl.happiness

	