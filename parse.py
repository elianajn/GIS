import numpy
import csv

def parse_file(filename):
	"""
		Within each line look for title:, lat:, lng:
		Append each as a row in the array
	"""
	arr = []
	n = 0
	name = ''
	lat = ''
	lng = ''
	with open(filename) as file_object:
		for line in file_object:
			if 'title\":' in line:
				name = line.split(":")[-1]
				name = name.replace('"','')
				name = name.replace(',','')
			if 'lat\":' in line:
				lat = line.split(":")[-1]
				lat = lat.replace('"','')
				lat = lat.replace(',','')
			if 'lng\":' in line:
				lng = line.split(":")[-1]
				lng = lng.replace('"','')
				lng = lng.replace(',','')
				n += 1
				arr.append([name, lat, lng])
		return arr

def main():
	"""
		Parse the file to get a 2d array of title, lat, longs
		create a new csv file
		write the headers

	"""
	arr = []
	arr = parse_file("/Users/ellaneurohr/Desktop/GIS Lab/CPC.html")
	with open ('/Users/ellaneurohr/Desktop/CPC.csv', 'w',newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(['Name'] + ['Lat']+ ['Long'])
		for row in range(len(arr)):
			spamwriter.writerow(arr[row])

if __name__ == '__main__':
	main()