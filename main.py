
import pandas as pd

#starting title of the project
print("Welcome to academic Tracker and Resource Recommander\n\n")
print("*"*30)

while True:
  print("Please Input the Necessary Details to Track your Progress:\n\n")

#Inputting the details of the user
  s_name=input("Your Name:")
  no_of_sub=int(input("Enter the No.of.Sunject:"))

  scores = {} #using dictionary for easy insertion in csv  

# using loop to add all subjects marks
  for i in range(no_of_sub):
    subject_name=input(f"Enter Subject {i+1}: ")
    score_got = int(input(f"Enter the mark you scored in {subject_name}: "))
    
    #adding values in dictionary
    scores[subject_name]=score_got  

  attendance=float(input("Enter your Overall Attendance Percentage:"))

#printing the inputted details for confirmation
#for confirmation show it in the table form


  data = []
  for subject, score in scores.items():
      data.append({
          'Student Name': s_name,
          'Subject': subject,
          'Score': score,
          'Attendance (%)': attendance
          })
  df = pd.DataFrame(data)
  print(df)
  confrim_msg=input("Click yes to confirm or click No to modify the data:")

  if confrim_msg=="yes":
     print("Data confirmed and saved")
     break
  else:
    print("Re-enter the data.")
  




# max_score = sum(scores) 
# print("Total Marks:", max_score)
