class Girl:


	def __init__(self, name, attract, intelligence, maintenance, type_):
		self.name = name
		self.attract = attract
		self.intelligence = intelligence
		self.maintenance = maintenance
		self.status = "Single"
		self.happiness= 0
		self.boyfriend = ""
		self.type_= type_

	def is_elligible(self, boy):
		if (self.maintenance <= boy.budget):
			return True
		else:
			return False

	def set_happiness(self, value):
		self.happiness = value

	def set_boyfriend(self, boy):
		self.boyfriend = boy
