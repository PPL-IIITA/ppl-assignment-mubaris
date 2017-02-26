#!/usr/bin/env python

from Girl import Girl
from Boy import Boy
from util import utility
import csv
from log import log_maker

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

utility()
boys = open('./boys.csv')
girls = open('./girls.csv')
getboy = csv.reader(boys, delimiter = ',')
getgirl = csv.reader(girls, delimiter = ',')
boy_list=[]
girl_list=[]

for i in getboy:
	boy_list += [Boy(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]), i[5])] 

for j in getgirl:
	girl_list += [Girl(j[0], int(j[1]), int(j[2]), int(j[3]), j[4])]

for g in  girl_list:
	for b in  boy_list:
		log_maker(g.name + '  is looking for  ' + b.name)
		if b.is_elligible(g) and g.is_elligible(b) and g.status=='Single' and b.status=='Single':
			g.status = 'Commited'
			b.status= 'Commited'
			g.set_boyfriend(b)
			b.set_girlfriend(g)
			print(color.BLUE + g.name + color.END + color.YELLOW + '  is in relationship with ' + color.END + color.BLUE + b.name + color.END)
			log_maker(g.name + '  is in relationship with ' + b.name)
			break
