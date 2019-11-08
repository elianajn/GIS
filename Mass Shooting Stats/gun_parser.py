import csv

def parse(filename, output):
	file_arr = []
	file = 'gun_stats_2014.csv'
	with open(filename) as file_object:
		for line in file_object:
			line = line.replace(' ','');
			line = line.replace('||','|');
			file_arr = line.split("|")
	with open (output, 'w',newline='') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		spamwriter.writerow(['Lat'] + ['Long']+ ['Incident_Number'])
		# for row in range(len(file_arr)):
		# 	spamwriter.writerow(file_arr[row])
		x = 0
		while x < (len(file_arr)):
			try:
				spamwriter.writerow([file_arr[x]] + [file_arr[x+1]] + [file_arr[x+2]])
			except:
				csvfile.close()
			x += 3


parse("gun_2014.txt", 'gun_stats_2014.csv')
parse("gun_2015.txt", "gun_stats_2015.csv")
parse("gun_2016.txt", "gun_stats_2016.csv")
parse("gun_2017.txt", "gun_stats_2017.csv")