# /usr/bin/python 

location = -1 # No Match 

try:
    while 1:
        location = BB.index('Bob', location + 1) 
        print "match at", location 
    except ValueError:
        pass 


# but having this every time, would be tediuous, so lets write a
# helper function to make it easier to see. 

def findall(lst, value, start=0):
    
