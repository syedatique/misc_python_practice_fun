# THis is to import data to a csv file

# import csv, sys
# data = ( ['Sumon','is','doing','Good'] )
# # myfile = open(..., 'wb')
# # out = csv.writer(open("myfile.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
# # out.writerow(data)

# # open output file
# # outfile = open( "myfile.csv", "wb" )


# outfile = open(sys.argv[0], 'wt')

# # get a csv writer
# writer = csv.writer(outfile)

# # write header
# writer.writerow(['Alice'])

# # write data
# writer.writerow(data) # write.writer(row)

# # close file
# outfile.close()

import pandas as pd  # Google App Engine DOESN't Support PANDAS!!!!!

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
df.to_csv('~/Documents/example.csv')