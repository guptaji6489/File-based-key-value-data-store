import threading 
#this is for python 3.0 and above. use import thread for python2.0 versions
from threading import*
import time

dict1={}    #'dict1' is the dictionary in which we store data

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional
#you can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in dict1:
        print("Error: this key already exists! Try another one")     #error message1 if key already exists
    else:
        if(key.isalpha()):
            if len(dict1)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jsonobject value less than 16KB 
                if timeout==0:
                    ll=[value,timeout]
                else:
                    ll=[value,time.time()+timeout]
                if len(key)<=32:    #constraints for input key_name capped at 32chars
                    dict1[key]=ll
            else:
                print("Error: Memory limit exceeded!! ")    #error message2 if Memory limit exceeded!!
        else:
            print("Error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")  #error message3



#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in dict1:
        print("Error: given key does not exist in database. Please enter a valid key or another Key") #Error message4
    else:
        bb=dict1[key]
        if bb[1]!=0:
            if time.time()<bb[1]:  #comparing the present time with expiry time
                s=str(key)+" : "+str(bb[0])  #to return the value in the format of JsonObject i.e.,"key_name:value"
                return s
            else:
                print("Error: time-to-live of",key,"has expired") #Error message time-to-live of key has expired
        else:
            s=str(key)+" : "+str(bb[0])
            return s



#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in dict1:
        print("Error: given key does not exist in database. Please enter a valid key or another Key") #Error message4
    else:
        bb=dict1[key]
        if bb[1]!=0:
            if time.time()<bb[1]: #comparing the current time with expiry time
                del dict1[key]
                print("key is successfully deleted")
            else:
                print("Error: time-to-live of",key,"has expired") #Error message time-to-live of key has expired
        else:
            del dict1[key]
            print("key is successfully deleted")

