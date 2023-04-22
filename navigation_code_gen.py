import os 
import json 
import requests 
from itertools import count

Account_data = "kornbot380@hotmail.com"
account_payload = {Account_data:"token_payload_input"} 
print(account_payload)
for i in count(0):

            try:
                  
                  resq_dat = requests.post("https://roboreactor.com/gen_nav_code",json=account_payload)
                  print("Current_status json input ",resq_dat.json())  # Get the json input data from the json input 
                  #Generat the  navigation type to send back the navigation component code into the system  
                  nav_gen_code = resq_dat.json() # Get the json data of the api to get the code gen 
                  status_nav = nav_gen_code.get('status') # Get the status navigation code data 
                  if status_nav == "ON":
                               print("Activate the code generator features function ")
                               #First classify the hardware name on the system 
                               board_name_onboard = list(nav_gen_code.get("navigation_payload"))[0] 
                               print(board_name_onboard)  
                               # Check if the computer onboard selected is on the selected function then begin function to generate the code 
                  if status_nav == "OFF":
                               print("Finish generating code of the navigation function algorithm") 
                                                
              
    
            except:
                 print("Error cannot connect to the server")
