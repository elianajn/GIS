from geopy.geocoders import Nominatim

def geocode(filepath):
	data = []
	geolocator = Nominatim(user_agent="my_application")
	with open(filepath) as file_object:
		# line = file_object.readline()
		for line in file_object:
			# print(line)
			# address = file_object.readline()
			# address = line
			location = geolocator.geocode(line)
			print(location.address)
			print((location.latitude, location.longitude))


def main():
	geocode("/Users/ellaneurohr/Desktop/CPC2.txt")

if __name__ == '__main__':
	main()
