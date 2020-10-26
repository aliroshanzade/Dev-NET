from netmiko import ConnectHandler
import getpass

user = input("please enter your username: ")
passwd = getpass.getpass()
file = input("please enter your directory: ")
files = open(file , "r")
IP = files.readlines()
files.seek(0)

for i in range(len(IP)) :
    j = IP[i]
  

    device= {
        "device_type" : "cisco_ios",
        "host": str(j) ,
        "username": user,
        "password": passwd
            }
    net_connect = ConnectHandler(**device)
    output= net_connect.send_command("sho ip arp 192.168.20.139" ,use_textfsm=True )

    if "mac" in output[0] :
        print("This SW is Gateway")
    else:
        print("This Sw is not Gateway")

    mac_1 = output[0].get("mac")
    

    output_2= net_connect.send_command(f"sho mac add add {mac_1}" ,use_textfsm=True )
    print(output_2)

    Interface = output_2[0].get(destinatio_port)
    print(f"\n" , device["host"] ,"\n" , "this mac {mac_1} is learn in Interface {Interface} :)")

    
