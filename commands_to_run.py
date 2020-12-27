# By Harshit Gupta (University of petroleum and energy studies)

#here are the commands to demonstrate how to access and perform operations on a main file


#run the MODULE of MAIN FILE and import mainfile as a library 

import main_code as xyz 
#importing the main file("main_code" is the name of the file I have used) as a library 


xyz.create("age",22)
#to create a key with key_name,value given and with no time-to-live property


xyz.create("name","harshit_gupta",3600) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


xyz.read("age")
#it returns the value of the respective key in Jsonobject format 'key_name:value'


xyz.read("name")
#it returns the value of the respective key in Jsonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


xyz.create("name","harshit")
#it returns an ERROR since the key_name already exists in the database

 
xyz.delete("age")
#it deletes the respective key and its value from the database(memory is also freed)


#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB

