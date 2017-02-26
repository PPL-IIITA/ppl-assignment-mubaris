class Boy:


	def __init__(self, name, attract, intelligence, budget, min_attr_req, type_):
		self.name = name
		self.attract = attract
		self.intelligence = intelligence
		self.budget = budget
		self.min_attr_req = min_attr_req
		self.status = "Single"
		self.happiness = 0
		self.girlfriend = ""
		self.type_ = type_

	def is_elligible(self, girl):
		if (self.budget >= girl.maintenance) and (girl.attract >= self.min_attr_req):
			return True
		else:
			return False

	def set_happiness(self, value):
		self.happiness = value

	def set_girlfriend(self, girl):
		self.girlfriend = girl

	def modify_budget(self, new_budget):
		self.budget = new_budget