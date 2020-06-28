#9-readcsv.py
import csv

def ReadCSV():
	with open('treeview.csv',newline='',encoding='utf-8') as file:
		#fr = file reader
		fr = csv.reader(file)
		#print(list(fr))
		data = list(fr)
	return data
	
expense = ReadCSV()
print(expense[0][1])