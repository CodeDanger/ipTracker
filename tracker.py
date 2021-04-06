################################
#       Scripted By            #
#       Code Danger            #
#       Ali Metwally           #
#        16/2/2021             #
################################

# pre requirements
    # 1- pip install colorama
    # 2- pip install pyfiglet
import socket
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from urllib.request import Request, urlopen
import webbrowser
import json
from pprint import pprint


author="Code Danger"
cprint(figlet_format(author, font="standard"), "red") 

def ask_for_host():
    while True:
        try:
            global ip4
            # let's ask for ip or host name
            host_name = input("Please Enter Host/Ip :  ")
            cprint("geting ip4 from host or ip ","yellow")
            # lets convert that host name to ipv 4 address
            ip4 = socket.gethostbyname(host_name)
            break

        except:
            # check if host name is exit then
            if host_name=="exit":
                cprint(figlet_format("Bye Bye", font="standard"), "blue") 
                exit()
                break
            cprint("please re enter valid host/ip like \n example.com / 127.1.1.9","red")
    # okay we got it here
    cprint("The ip is : " + ip4 ,"yellow")
    cprint("Fetching ip data " ,"green")

# run main
ask_for_host()

# api for fetching ip data
api = "https://ipinfo.io/{}/json"

# try to fetch data from api and convert json response to object(list)
try:
    call_request = Request(api.format(ip4), headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(call_request).read().decode()
    data = json.loads(response)
except e:
    # when connection or any error happen display it
    cprint("Fetcing data faild \n error :{} \n please try again later".format(e),"red")
    exit()

#api for open google maps
api_maps = "https://www.google.com/maps/search/?api=1&query={},{}"
# just printing da da
cprint("Fetcing data Success \n Ip data :","green")
# print list in pretty way
pprint(data)
# split location to long,lat
location = data["loc"].split(',',1)
# open final api link in default browser
webbrowser.open(api_maps.format(location[0],location[1]), new=2)
