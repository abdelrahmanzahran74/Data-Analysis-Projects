# File_Handling
# f = open('employers.json','r') #open file "Upload to RAM", 'r' > read, write > 'w'

# print(f.read())4


# f = open('employers.json','w') #open file "Upload to RAM", 'r' > read, write > 'w'

# print(f.write()) #overwrite

# f = open('employers.json','a') #open file, 'a' append

import json
#######write a program to get new emp from user, and this employer#######

# read employers file
employers_file = open('employers.json')  # by default flag is read
employers = employers_file.read()

#close after asign to list
employers_file.close()

#transform to list use json.loads
employers = json.loads(employers) 


# get new employer from user
name = input("enter employer name: \n")

employer = { "id": employers[-1]["id"] + 1,  "name" : name }

# append this employer to the list of employers
employers.append(employer)

#open the json file
employers_file = open('employers.json', 'w')

#insert (overwrite) #transform from list to json "sring" 
employers_file.write(json.dumps(employers))
