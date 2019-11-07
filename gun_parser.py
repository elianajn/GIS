import csv

def parse(filename):
	file_arr = []
	with open(filename) as file_object:
		for line in file_object:
			line = line.replace(' ','');
			line = line.replace('||','|');
			file_arr = line.split("|")
	with open ('gun_stats.csv', 'w',newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(['Lat'] + ['Long']+ ['Incident_Number'])
		# for row in range(len(file_arr)):
		# 	spamwriter.writerow(file_arr[row])
		for x in range(len(file_arr)):
			try:
				spamwriter.writerow([file_arr[x]] + [file_arr[x+1]] + [file_arr[x+2]])
				x += 3
			except:
				csvfile.close()


parse("gun.txt")