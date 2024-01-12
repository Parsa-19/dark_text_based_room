import time
import os


class area:
	def to_dic(self, *args):
		return {
			'starter' : args[0],
			'n' : args[1],
			's' : args[2],
			'e' : args[3],
			'w' : args[4]
		}

	def __init__(self):
		self.black_room_dic = self.to_dic("you open your eyes on a dark empty room with a cold bed which you are chained on!.. you cant remember anything and the only sound you hear is sth like someone's screaming", "black NORTH", "black SOUTH", "black EAST", "black WEST")
		self.room2_dic = self.to_dic("there are 10 doors in front of you", "room2 north", "room2 south", "room2 east", "room2 west")
		self.cafe_dic = self.to_dic("cafe is full of strainge people who doesnt look like a normal human except one who is the owner of the cafe", "N", "S", "E", "W")
		self.clock_room_dic = self.to_dic("there is clock on every where you look. each of them are showing you a different time!!", "clock NORTH", "clock SOUTH", "clock EAST", "clock WEST")
		self.laboratory_dic = self.to_dic("are two dead people on the ground. everywhere is foggy. you smell sth like a wierd strainge gass. its making you sick.", "N", "S", "E", "W")
		self.murder_room_dic= self.to_dic("its like you are entering to a wooden house.. you can see any kind of killing equipment such gun, kinfe, (tab here to see all)... you notice that there is a bloody eye looking at you every where you going on the wall, also three hanged girls and a little boy bleeding on the ground.", "N", "S", "E", "W")
		self.wine_room_dic = self.to_dic("you see large number of wines all around you, you can see racks in different categoriez are organized. in this room you're ganna get drunk by one of these wines which determines a seprated story line. there is a title on each of wines that shows you in which section you would like to continue..", "N", "S", "E", "W")

		self.all_rooms = ['black_room', 'room2', 'cafe', 'clock_room', 'laboratory', 'murder_room', 'wine_room']



	def black_room(self, direction):
		return self.black_room_dic[direction]

	def room2(self, direction):
		return self.room2_dic[direction]

	def cafe(self, direction):
		return self.cafe_dic[direction]

	def clock_room(self, direction):
		return self.clock_room_dic[direction]

	def laboratory(self, direction):
		return self.laboratory_dic[direction]

	def murder_room(self, direction):
		return self.murder_room_dic[direction]

	def wine_room(self, direction):
		return self.wine_room_dic[direction]
 


class player(area):  # cintains [player's information, player's commands]
	
	def __init__(self, player_bag=[], score=0, current_room='room2'): 
		super().__init__()
		self.player_bag = player_bag # list containing objects in it
		self.score = score
		self.current_room = current_room
		
	# getter (current_room)
	def get_current_room(self):
		return self.current_room

	# setter (current_room)
	def set_current_room(self, value):
		self.current_room = value

	def getter(self, variable):
		return self.variable

	def setter(self, variable, value):
		self.variable = value


	def handle_story(self, key): # gets the key and returns the value of the associated key. (the dictionary contains inherted methods as value)
		handle_story = {
			'black_room':self.black_room,
			'room2':self.room2,
			'cafe':self.cafe,
			'clock_room':self.clock_room,
			'laboratory':self.laboratory,
			'murder_room':self.murder_room,
			'wine_room':self.wine_room
		} 
		return handle_story[key]




	 



	
	# commands :

	def go(self, place): # place is room's name in string format (parameter)
		if place not in self.all_rooms and place not in ['n', 's', 'e', 'w']:
			return 'there is no room with this name :('

		''' if player wants to move in current room by sth like '>>>go N' or '>>>go E' ;
			first set the direction to one of ['n', 's', 'e', 'w']
			second set the place to the room that player is playing currently'''
		direction = 'starter' 
		if place in ['n', 's', 'e', 'w']: # if place was n s e w it means that we dont have the room's name in place itself. then we'll set the direction to 'direction' first and set the place to room's name by self.current room
			direction = place
			place = self.get_current_room() 

		# main function task:
		room_func = self.handle_story(place) # find the related function (which is inherted from 'area') 
		destination = room_func(direction) # execute the related room story function and store whole story in 'destination'

		self.set_current_room(place)
		return destination


	def get(self, stuff):
		pass

	def drop(self, stuff):
		pass

	def use(self, stuff):
		pass

	def bag(self): # shows what you have in bag
		pass

	def read(self, paper):
		pass

	def explain(self): # explains your current rooms 
		pass

	def talk(self, character):
		pass

	def unlock(self, obj):
		pass

	def help(self): # give you a hand to solve the problem
		pass

	def pass_(self): # give you the key to pass the room
		pass 

	def map_(self): # shows you the map 
		rooms_str = ''
		for i in self.all_rooms:
			rooms_str += (i+' | ')
		return rooms_str

	def command(self): 
		return '''
		command  |  followed_by  |  color  |  explained				 

		go          place           GREEN       go between rooms and directions
		get         stuff           BLUE        gain tools
		drop        stuff           BLUE        lose tools
		use         stuff           BLUE        you may need to use some of your tools
		bag           -               -	        shows you what tool you have in your bag
		read        paper           YELLOW      read papers
		explain       -               -         remind what is happening in the room again
		talk        character       PURPLE      you can talk to some one when you see him
		unlock       obj             RED        open the door
		help          -               -         when you got stuck you can get help
		pass          -               -         pass me the key
		map           -               -         what rooms are there
		command       -               -         what command can i use
		struc         -               -         how to use commands
		'''

	def struc(self):
		return '''
		structure / syntax

		(e.g.)>>> go black_room / go north / go n
		(e.g.)>>> get
		(e.g.)>>> drop
		(e.g.)>>> use
		(e.g.)>>> bag
		(e.g.)>>> read
		(e.g.)>>> explain
		(e.g.)>>> talk
		(e.g.)>>> unlock
		(e.g.)>>> help
		(e.g.)>>> pass
		(e.g.)>>> map
		(e.g.)>>> command
		(e.g.)>>> struc
		'''




class gameplay(player):  # contains [gameplay functional methods]

	commands = ['go', 'get', 'drop', 'use', 'bag', 'read', 'explain', 'talk', 'unlock', 'help', 'pass', 'map', 'command', 'struc'] # calss variable

	def __init__(self):
		super().__init__()

	def command_handle(self, command):
		command_dic = {
			'go':self.go,
			'get':self.get,
			'drop':self.drop,
			'use':self.use,
			'bag':self.bag,
			'read':self.read,
			'explain':self.explain,
			'talk':self.talk,
			'unlock':self.unlock,
			'help':self.help,
			'pass':self.pass_,
			'map':self.map_,
			'command':self.command,
			'struc':self.struc
		}
		return command_dic[command]


	def get_req(self, user_input): # returns lst [command, parameter] or lst just [command]
		user_input = user_input.lower()
		words = user_input.split()

		# check the len of words: 
		if len(words) == 1:
			# words.append('')
			return words # words be like --> [command]

		if len(words) == 2:
			''' (prepare for 'go' command in a special situation) 
				if parameter was compelete directions '''
			command = words[0]
			parameter = words[1]
			directions = {
				'north':'n',
				'south':'s',
				'east':'e',
				'west':'w'
			}
			if parameter in list(directions.keys()): # if user inputed parameter was compelete word then change it to letters --> n e w s
				words[1] = directions[parameter] # change ['go', 'south'] to --> ['go', 's']  

			return words # got what user say as request and returns it as 2 word

		return False


	def process(self, requ):
		
		command = requ[0] 
		parameter = requ[1] if len(requ) >= 2 else False

		# check the command
		if command not in gameplay.commands:
			return "unknown command!"

		command_respond_func = self.command_handle(command)
		try:
			return command_respond_func(parameter) # execute the commamd function within inputs e.g.--> go(parameter) , get(parameter) , read(parameter)
		except:
			return command_respond_func() # execute the commamd function wihtout inputs e.g.--> explain() , bag(parameter) , help(parameter), pass(), map()respond



	def write(self, story):
		for ch in story:
			print(ch, end='', flush=True)
			time.sleep(0.02)
		print('\n')


	
		






class initial(area):

	def __init__(self):
		pass

	def Ready_ask(self): 
		ready_ans = None 
		ready_ans = input('ready to start?').lower()

		while ready_ans != 'y' and ready_ans != 'n':
			print("plz just type Y for yes or N for no...")
			ready_ans = input('ready to start?').lower()
		print(ready_ans)

		if ready_ans == 'n':
			while ready_ans != 'y':
				ready_ans = input('dont make me ask again (Y/N)!?').lower()

		os.system('clear')


	# def start(self):
	# 	mmd = player()
	# 	print(mmd.go('black_room'))
	# 	# gameplay.write_story(gameplay, you.go('black_room'))


	def introduce(self, player_ins): # gets	player_ins to --> introduce to the player
		intro_game = gameplay()
		intro_game.write("Hi..\nThis is a adventure_text_baesed Game where\nyou can search and solve different problems!")
		self.Ready_ask()
		
		
	def get_name(self):
		name = input("What's your name? ")

		







if __name__ == "__main__":

	mmd = player()
	game1 = gameplay()
	intro = initial()

	# intro.introduce(mmd)

	while True:
		# gets the request and ensures that the value you entered is in the correct format --> 'command' 'parameter'
		requ = game1.get_req(input(f"({game1.get_current_room()})>>>"))  # this game works on [>>>"command" "parameter"] structure
		if not requ: # if it was false then execute it
			game1.write("invalid input: extra space or out of structure!")


		# process the request choose the best answer for it
		elif requ:
			answer = game1.process(requ) # requ is a list
			if answer:
				game1.write(answer)
			else:
				game1.write(f"couldnt get any answer from game1.process --> {answer}")


		
		





















