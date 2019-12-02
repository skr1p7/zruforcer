import zipfile 

name = raw_input("Enter the name of your zip file : ") 
myfile = name 
w_list = 'list.txt' 
 
password = None 
file = zipfile.ZipFile(myfile) 
with open(w_list, 'r') as f: 
   for line in f.readlines(): 
         password = line.strip('\n') 
         try: 
               file.extractall(pwd=password) 
               password = 'Pass is : %s' % password 
               print password 
         except: 
               pass 