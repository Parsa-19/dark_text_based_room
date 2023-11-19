import os
from main import area 


if __name__ == "__main__":
	 os.mkdir("Area")

	 rooms_name = ["black_room", "room2", "cafe", "clock_room", "laboratory", "murder_room", "wine_room"]
	 for meth_name in rooms_name:
	 	os.mkdir(f"Area/{meth_name}")

	