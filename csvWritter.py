import csv

csvfile = open('LarvaBot/names.csv', 'w', newline='')
    #fieldnames = ['first_name', 'last_name']
    #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer = csv.writer(csvfile)
    #writer.writeheader()
for i in range(10):
    writer.writerow(['Baked','Beans1'])
    #writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    #writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})