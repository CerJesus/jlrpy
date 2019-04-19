import jlrpy as jp
import sys
import pprint



def main():
    #Get login info from commandline
    email = sys.argv[1]
    password = sys.argv[2]

    #Create connection and get the ipace
    connect = jp.Connection(email=email,password=password)
    v = connect.vehicles[0]

    #do stuff
    stat = v.get_status()
    #pprint.pprint(stat)
    pprint.pprint(v.get_position())



if __name__ == '__main__':
	main()
