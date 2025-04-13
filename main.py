#create 2 csv files
#1) User.csv
#2) Reccomdation.csv

import pandas as pd
import numpy as np
import matplotlib as mb

#starting title of the project
print("Welcome to academic Tracker and Resource Recommander\n\n")
print("*"*30)

#ask user to enter name for checking there previous data
s_name=input("Your Name:")

#condition to check user
if(s_name=="abc"): #need to change condition for csv file to check name
  print("User Exist\nWelcome Back :)\n Displaying your data")
  #csv code to display data

else:
  print("User Not Exist :(\nlease Enter the Necessary Details to Track your Progress:\n\n")
  
  #loop for inputting the details and helping in further checking
  
  while True:
    scores = {} #using dictionary for insertion in csv  
  
  #Inputting the details of the user
    #no need for re-enter name will take from above
    
    no_of_sub=int(input("Enter the No.of.Subject:"))
    
  # using loop to add all subjects marks
    for i in range(no_of_sub):
      subject_name=input(f"Enter Subject {i+1}: ")
      score_got = int(input(f"Enter the marks you scored in {subject_name}: "))
      
      #adding values in dictionary
      scores[subject_name]=score_got  

    attendance=float(input("Enter your Overall Attendance Percentage:"))

  #printing the inputted details for confirmation
    data = []
    for subject, score in scores.items():
        data.append({
            'Student Name': s_name,
            'Subject': subject,
            'Score': score,
            'Attendance (%)': attendance
            })
    df = pd.DataFrame(data)
    df.to_csv('details.csv',index=False)#detail.csv is a csv file where data is stored in csv format.
    df_check=pd.read_csv('details.csv')
    print(df_check)#its just to check the data have been stored in csv format or not.
    
    #printing all the details
    print()
    print(df.to_string())
    
    #confirming with the user
    confrim_msg=input("\nType yes to confirm or no to re-enter your details:")

    if (confrim_msg.lower()=="yes"):
      print("\nDetails Confirmed and Saved.\n")
      #code for saving data in csv file
      break
    else:
      print("\nRe-enter your Details.\n") #user will re enter the details
      
  #after storing data we will calculate the progress
  print("*"*30)
  print("Calculating your Progress....")   
  
  #calculate the progress

  #will display the progress
