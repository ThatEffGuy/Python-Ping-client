import subprocess

out = subprocess.run(['ping' , 'google.com'], capture_output=True)
print (out.stdout.decode())

#declaring variables
target_address =" "
#getting target IP
target_address = input("enter the address to ping ")
#Giving the user the option to exit
subprocess.run(["ping", target_address])
