import random
import csv

def utility():
	boys=[]
	girls=[]
	gifts=[]

	boy_names = ["Max", 	"Buddy", 	"Charlie", 	"Jack", 	"Cooper", 	"Rocky", 	"Toby", 	"Tucker", 	"Jake", 	"Bear", 	"Duke", 	"Teddy", 	"Oliver", 	"Riley", 	"Bailey", 	"Bentley", 	"Milo", 	"Buster", 	"Cody", 	"Dexter", 	"Winston", 	"Murphy", 	"Leo", 	"Lucky", 	"Oscar", 	"Louie", 	"Zeus", 	"Henry", 	"Sam", 	"Harley", 	"Baxter", 	"Gus", 	"Sammy", 	"Jackson", 	"Bruno", 	"Diesel", 	"Jax", 	"Gizmo", 	"Bandit", 	"Rusty", 	"Marley", 	"Jasper", 	"Brody", 	"Roscoe", 	"Hank", 	"Otis", 	"Bo", 	"Joey", 	"Beau", 	"Ollie", 	"Tank", 	"Shadow", 	"Peanut", 	"Hunter", 	"Scout", 	"Blue", 	"Rocco", 	"Simba", 	"Tyson", 	"Ziggy", 	"Boomer", 	"Romeo", 	"Apollo", 	"Ace", 	"Luke", 	"Rex", 	"Finn", 	"Chance", 	"Rudy", 	"Loki", 	"Moose", 	"George", 	"Samson", 	"Coco", 	"Benny", 	"Thor", 	"Rufus", 	"Prince", 	"Chester", 	"Brutus", 	"Scooter", 	"Chico", 	"Spike", 	"Gunner", 	"Sparky", 	"Mickey", 	"Kobe", 	"Chase", 	"Oreo", 	"Frankie", 	"Mac", 	"Benji", 	"Bubba", 	"Champ", "Brady", "Elvis", "Copper", "Cash", "Archie", "Walter"]
	girl_names = [	"Bella",	"Lucy",	"Daisy",	"Molly",	"Lola",	"Sophie",	"Sadie",	"Maggie",	"Chloe",	"Bailey",	"Roxy",	"Zoey",	"Lily",	"Luna",	"Coco",	"Stella",	"Gracie",	"Abby",	"Penny",	"Zoe",	"Ginger",	"Ruby",	"Rosie",	"Lilly",	"Ellie",	"Mia",	"Sasha",	"Lulu",	"Pepper",	"Nala",	"Lexi",	"Lady",	"Emma",	"Riley",	"Dixie",	"Annie",	"Maddie",	"Piper",	"Princess",	"Izzy",	"Maya",	"Olive",	"Cookie",	"Roxie",	"Angel",	"Belle",	"Layla",	"Missy",	"Cali",	"Honey",	"Millie",	"Harley",	"Marley",	"Holly",	"Kona",	"Shelby",	"Jasmine",	"Ella",	"Charlie",	"Minnie",	"Willow",	"Phoebe",	"Callie",	"Scout",	"Katie",	"Dakota",	"Sugar",	"Sandy",	"Josie",	"Macy",	"Trixie",	"Winnie",	"Peanut",	"Mimi",	"Hazel",	"Mocha",	"Cleo",	"Hannah",	"Athena",	"Lacey",	"Sassy",	"Lucky",	"Bonnie",	"Allie",	"Brandy",	"Sydney",	"Casey",	"Gigi",	"Baby",	"Madison",	"Heidi",	"Sally",	"Shadow",	"Cocoa",	"Pebbles",	"Misty",	"Nikki",	"Lexie",	"Grace",	"Sierra"]
	gift_names = ["Flowers", "Chocolate", "Laptop", "Books", "Bracelet", "Sunglasses", "Smartphone", "Watch", "T-Shirt", "Mug", "Scarf", "Keychain", "Necklace", "Earrings", "Teddy", "Perfume", "Sneakers", "Disney Princess", "Pouch", "Friends DVD"]
	gift_name_types = ["Luxury", "Luxury", "Luxury", "Utility", "Essential", "Utility", "Utility", "Utility", "Essential", "Luxury", "Essential", "Utility", "Luxury", "Essential", "Luxury", "Utility", "Essential", "Luxury", "Utility", "Utility"]


	boy_types = ["Miser", "Generous", "Geek"]
	girl_types = ["Choosy", "Normal", "Desperate"]
	gift_types = ["Essential", "Luxury", "Utiltiy"]

	for i in range (0, 100):
		boys+= [(boy_names[i], random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), boy_types[random.randint(0,2)])]

	for j in range (0, 60):
		girls+=[(girl_names[j], random.randint(0,20), random.randint(0,20), random.randint(0,20), girl_types[random.randint(0,2)])]

	for k in range (0,20):
		gifts += [(gift_names[k], random.randint(0,40), random.randint(0,100), gift_name_types[k])]

	csvfile("./boys.csv", boys)
	csvfile("./girls.csv", girls)
	csvfile("./gifts.csv", gifts)


def csvfile(file_name, list_name):
	fp = open(file_name, "w")
	writer = csv.writer(fp, delimiter = ",")

	for i in list_name:
		writer.writerow(i)	

utility() 