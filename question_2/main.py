#!/usr/bin/env python

import random 
import csv
import logging
import math
import pprint

from log import log_maker
from Couple import Couple
from Boy import Boy
from Girl import Girl
from Gift import Gift
from util import utility

class color:
	PURPLE = "\033[95m"
	CYAN = "\033[96m"
	DARKCYAN = "\033[36m"
	BLUE = "\033[94m"
	GREEN = "\033[92m"
	YELLOW = "\033[93m"
	RED = "\033[91m"
	BOLD = "\033[1m"
	UNDERLINE = "\033[4m"
	END = "\033[0m"


logging.basicConfig(filename="event_log.log", datefmt="%d/%m/%Y %I:%M:%S %p", format="%(asctime)s %(name)-6s %(levelname) s: %(message)s", level=logging.DEBUG, filemode="w")


def calc_happiness(H):
	with open("./gifts.csv", "r") as csvfile:
		ffp = csv.reader(csvfile, delimiter = ",")
		gifts = [Gift(row[0], int(row[1]), int(row[2]), row[3]) for row in ffp]
		csvfile.close()

	gifts = sorted(gifts, key=lambda item: item.cost)
	logging.warning("\n\nDetails of Gifts:\n")
	for i in H:
		if (i.boy.type_ == "Miser"):
			miser(gifts, i)

		if (i.boy.type_ == "Generous"):
			generous(gifts, i)

		if (i.boy.type_ == "Geek"):
			geek(gifts, i)

	gift_details(H)

def happy_couple(H, k):
	A = sorted(H, key=lambda item: item.happiness, reverse=True)
	B = sorted(H, key=lambda item: item.compatibility, reverse=True)

	print (color.BLUE + "\n\n" + str(k) + " most Compatible couples are as follows:" + color.END)
	for i in range(k):
		print (color.YELLOW + B[i].boy.name + " & " + B[i].girl.name + color.END)

	print (color.BLUE + "\n\n"+ str(k) + " most happy couples are as follows:" + color.END)
	for i in range(k):
		print (color.YELLOW + A[i].boy.name + " & " + A[i].girl.name + color.END)
	
def generous(gifts, p):
	b1 = 0
	b2 = 0

	for gift in gifts:
		if  (p.boy.budget - gift.cost > 0) and (p.boy.budget >= 0) and ((p.boy.budget- gift.cost <= 300) or (gift.cost == p.boy.budget) )  :
			if (gift.type_ == "Luxury"):
				b2 = b2 + 2 * gift.cost
			else:
				b2 = b2 + gift.cost
			b1 = b1 + gift.cost
			p.gifts = p.gifts + [gift]
			p.boy.budget = p.boy.budget - gift.cost
			logging.info(p.boy.name + "  gifted  " + p.girl.name + " a " + gift.name + " of price = Rs." + str(gift.cost) + "/-.")
	
	if (p.girl.type_ == "Choosy" and b2 > 0):
		p.girl.happiness = math.log10(b2)
	
	elif (p.girl.type_ == "Normal"):
		p.girl.happiness = b1
	
	else:
		p.girl.happiness = math.exp(b1)
	
	p.boy.happiness = p.girl.happiness
	p.set_happiness()
	p.set_compatibility()

def miser(gifts, x):
	b1 = 0
	b2 = 0
	for gift in gifts:
		if (x.boy.budget >= 0) and ( (gift.cost - x.girl.maintenance <= 100) or gift.cost == x.girl.maintenance) and (x.boy.budget - gift.cost > 0):
			if (gift.type_ == "Luxury"):
				b2 = b2 + 2 * gift.cost
			else:
				b2 = b2 + gift.cost
			b1 = b1 + gift.cost
			x.gifts = x.gifts + [gift]
			x.boy.budget = x.boy.budget - gift.cost
			log_maker(x.boy.name + " gifted " + x.girl.name + " a " + gift.name + " of price = Rs." + str(gift.cost) + "/-")

	if (x.girl.type_ == "Choosy" and b2 > 0):
		x.girl.happiness = math.log10(b2)
	
	elif (x.girl.type_ == "Normal"):
		x.girl.happiness = b1
	
	else:
		x.girl.happiness = math.exp(b1)
	x.boy.happiness = x.boy.budget
	x.set_happiness()
	x.set_compatibility()


def geek(gifts, c):
	b1 = 0
	b2 = 0
	for gift in gifts:
		if  (c.boy.budget >= 0)  and ((gift.cost - c.girl.maintenance <= 100) or (gift.cost == c.girl.maintenance))and (c.boy.budget - gift.cost > 0):
			if (gift.type_ == "Luxury"):
				b2 = b2 + 2 * gift.cost
			else:
				b2 = b2 + gift.cost
			b1 = b1 + gift.cost
			c.gifts = c.gifts + [gift]
			c.boy.budget = c.boy.budget - gift.cost
			log_maker(c.boy.name + " gifted " + c.girl.name + " a " + gift.name + " of price = Rs. " + str(gift.cost) + "/-.")

	for gift in gifts:
		if (gift not in c.gifts) and (gift.type_ == "Luxury") and (gift.cost <= c.boy.budget):
			b2 = b2 + 2 * gift.cost
			b1 = b1 + gift.cost
			c.gifts = c.gifts + [gift]
			c.boy.budget = c.boy.budget - gift.cost
			log_maker(c.boy.name + " gifted " + c.girl.name + " a " + gift.name + " of price = Rs. " + str(gift.cost) + "/-.")
			break


	if (c.girl.type_ == "Choosy" and b2 > 0):
		c.girl.happiness = math.log10(b2)
	
	elif (c.girl.type_ == "Normal"):
		c.girl.happiness = b1
	
	else:
		c.girl.happiness = math.exp(b1)
	c.boy.happiness = c.girl.intelligence
	c.set_happiness()
	c.set_compatibility()

def gift_details(H):
	for h in H:
		print (color.GREEN + "Gifts given from " + h.boy.name + " to " + h.girl.name + ":\n" + color.END)
		for gift in h.gifts:
			print (color.YELLOW + gift.name + "\tType: " + gift.type_ + color.END)
		print ("\n")
		k = random.randint(1, len(H))
	happy_couple(H, k)

def test():
	with open("./boys.csv", "r") as csvfile:
		fp1 = csv.reader(csvfile, delimiter = ",")
		boy_lists =[]
		for i in fp1:
			boy_lists += [Boy(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]), i[5])]
		csvfile.close()

	with open("./girls.csv", "r") as csvfile:
		fp2 = csv.reader(csvfile, delimiter = ",")
		girl_lists=[]
		for j in fp2:
			girl_lists += [Girl(j[0], int(j[1]), int(j[2]), int(j[3]), j[4])]
		csvfile.close()

	Couple_list = []

	logging.warning("\n\nGirls are looking for Boys.\n")
	for g in girl_lists:
		for b in boy_lists:
			log_maker(g.name + " is looking for " + b.name)
			if b.status == "Single" and g.status == "Single" and (g.is_elligible(b)) and (b.is_elligible(g)) :
				g.status = "Committed"
				b.status = "Committed"
				g.boyfriend = b
				b.girlfriend = g
				log_maker(g.name + " is in relationship with " + b.name)
				Couple_list = Couple_list + [(b, g)]
				break
	
	print (color.BLUE + "\n\nCouples in Relationship are :\n" + color.END)

	for g in girl_lists:
		if g.status != "Single":
			print (color.GREEN + g.name + " is in relationship with " + g.boyfriend.name + "\n" + color.END)
		else:
			print (color.RED + g.name + " is still single. Not commited with any boy.\n" + color.END)

	H=[]
	for i in Couple_list:
		H += [Couple(i[0],i[1])]
	calc_happiness(H)

utility()
test()