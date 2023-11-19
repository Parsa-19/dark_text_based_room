import time



class area:

	def __init__(self):
		pass

	def to_dic(self, *args):
		return {
			'starter' : args[0],
			'N' : args[1],
			'S' : args[2],
			'E' : args[3],
			'W' : args[4]
		}


	def black_room(self): 
		return self.to_dic("dark empty room with a cold bed you chained on!", "black NORTH", "black SOUTH", "black EAST", "black WEST")

	def room2(self):
		return self.to_dic("there are 10 doors in front of you", "", "", "", "")

	def cafe(self):
		return self.to_dic("cafe is full of strainge people who doesnt look like a normal human except one who is the owner of the cafe", "", "", "", "")

	def clock_room(self):
		return self.to_dic("there is clock on every where you look. each of them are showing you a different time!!", "clock NORTH", "clock SOUTH", "clock EAST", "clock WEST",)

	def laboratory(self):
		return self.to_dic("are two dead people on the ground. everywhere is foggy. you smell sth like a wierd strainge gass. its making you sick.",  "", "", "", "")

	def murder_room(self):
		return self.to_dic("its like you are entering to a wooden house.. you can see any kind of killing equipment such gun, kinfe, (tab here to see all)... you notice that there is a bloody eye looking at you every where you going on the wall, also three hanged girls and a little boy bleeding on the ground.", "", "", "", "")

	def wine_room(self):
		return self.to_dic("you see large number of wines all around you, you can see racks in different categoriez are organized. in this room you're ganna get drunk by one of these wines which determines a seprated story line. there is a title on each of wines that shows you in which section you would like to continue..", "", "", "", "")

 


class player(area):
	
	def __init__(self, bag, score, current_room=""):
		self.bag = bag # list containing abjects in it
		self.score = score
		self.current_room = current_room
		
		self.handle_story = {
			'black_room':self.black_room,
			'cafe':self.cafe,
			'clock_room':self.clock_room,
			'laboratory':self.laboratory,
			'murder_room':self.murder_room,
			'wine_room':self.wine_room
		}
		


	def go(self, place, direc='starter'):
		destin_func = self.handle_story[place] # find the related function
		story_dic = destin_func() # execute the related room story function and store whole story in 'story dic'
		self.current_room = place # change the place you are 
		return story_dic[direc] # return the specific part of room's story

	def get(self, stuff):
		pass

	def drop(self, stuff):
		pass

	def use(self, stuff):
		pass

	def read(self, paper):
		pass

	def explain_situation(self, place):
		pass

	def talk(self, character):
		pass

	def unlock(self, obj):
		pass

	def get_help(self, place):
		pass

	def commands(self):
		commands_explained = """
		command  |  followed_by  |  color				 

		go 			place			GREEN	
		get 		stuff			RED
		drop 		stuff			RED
		use 		stuff			RED
		read		paper			YELLOW
		explain 	  _ 			  _ 
		talk 		character		BLUE
		unlock 		obj				PURPLE
		get_help      _ 			  _

		"""
		print(commands_explained)


class gameplay():

	def __init__(self):
		pass

	def write_story(self, story):
		for ch in story:
			print(ch, end='')
			time.sleep(0.003)






if __name__ == "__main__":


	mmd = player([], 0,'black_room')
	gameplay.write_story(gameplay, mmd.go('black_room', 'starter'))
	

	print("\n\n")

	mmd.commands()





















