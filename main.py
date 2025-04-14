import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import os

#starting title of the project
print("Welcome to academic Tracker and Resource Recommander")
print("*"*30)
print("\n\n")

#csv file variable
user_csv='users.csv'
resource_csv='resources.csv'

#ask user to enter name for checking there previous data
s_name=input("Your Name:").strip().title()

# Check if user already exists
if os.path.exists(user_csv):
    df_existing = pd.read_csv(user_csv)
    if s_name in df_existing['Student Name'].values:  # checking from csv file if user exist with name
      print("\nUser Found! Welcome back, here is your data:\n")
      print(df_existing[df_existing['Student Name'] == s_name].to_string(index=False)) #displaying the data 
      exit()
    else:
      print("\nUser not found. Let's enter your details.\n")
else:
  print("\nPlease Enter Your details:\n")  
  
  #loop for inputting the details and helping in further checking
while True:
    scores = {} #using dictionary for insertion in csv
    percentage={} # for calculating the percentage of subjects  
  
  #Inputting the details of the user  
    no_of_sub=int(input("Enter the No.of.Subject:"))
    
  # using loop to add all subjects marks
    for i in range(no_of_sub):
      subject_name=input(f"Enter Subject {i+1}: ").strip().lower()
      score_got = int(input(f"Enter the marks you scored in {subject_name}: "))
      score_total=int(input(f"Enter the total marks in {subject_name}: "))
      
      #adding values in dictionary
      scores[subject_name]=(score_got, score_total)
      percentage[subject_name]=round((score_got/score_total)*100,2)
  
  # attendance input
    attendance=float(input("Enter your Overall Attendance Percentage:"))
    
  # printing the inputted details for confirmation
    print("\nYour Entered Details:\n")
    for subject, percent in percentage.items():
      print(f"{subject}: {percent}%")
    print(f"Attendance: {attendance}%")
      
  #   #confirming with the user
    confrim_msg=input("\nType yes to confirm or no to re-enter your details:").strip().lower()

    if (confrim_msg=="yes"):
      print("\nDetails Confirmed and Saved.\n")
      break
    else:
      print("\nRe-enter your Details.\n") #user will re enter the details

#calculating ovaerall percentage using numpy
all_scores=np.array(list(percentage.values()))
overall_percentage=round(np.mean(all_scores),2)  
  
#checking for the weak subject   
weak_subject=[] 
for subject,perc in percentage.items():
  if perc<33:
    weak_subject.append(subject) 

#making the list of weak subjects in comma separated fromat  
if weak_subject:
    weak_subject_str = ", ".join(weak_subject)
else:
    weak_subject_str = "None"
    
  
  
data={
  'Student Name':s_name,
  'Attedance (%)':attendance,
  **percentage, #unpacking the percentage{} (dictionary)
  'Overall (%)':overall_percentage,
  'Weak Subject':weak_subject_str
}  
    
#storing the data in csv file  
if os.path.exists(user_csv):
  df = pd.read_csv(user_csv)
  df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
else:
  df = pd.DataFrame([data])

df.to_csv(user_csv, index=False)     
      
#after storing data we will display the progress
print("*"*30)
print("Calculating your Progress....")   
print("Your Updated Academic Report:\n")

#printing the data from the csv file 
print(pd.DataFrame([data]).to_string(index=False))
  
#displaying graph related to the progress   
pl.figure(figsize=(10, 6))
pl.bar(percentage.keys(), percentage.values(), color='skyblue')
pl.xlabel("Subjects")
pl.ylabel("Score Percentage")
pl.title(f"{s_name}'s Subject Performance")
pl.ylim(0, 100)
pl.axhline(y=33, color='red', linestyle='--', label='Pass Threshold')
pl.legend()
pl.grid(axis='y', linestyle='--', alpha=0.7)
pl.tight_layout()
pl.show()

if os.path.exists(resource_csv):
    resources_df = pd.read_csv(resource_csv)

    print("\nPersonalized Recommendations:\n")
    for subject in percentage:
        score = percentage[subject]
        if subject in resources_df['Subject'].values:
            recs = resources_df[resources_df['Subject'] == subject]

            for _, row in recs.iterrows():
                cond = row['Condition'].strip().lower()
                if score < 33 and attendance < 75 and cond == 'score<40 & attendance<75':
                    print(f"{subject}: {row['Recommendation']}")
                elif score < 33 and attendance >= 75 and cond == 'score<40 & attendance>=75':
                    print(f"{subject}: {row['Recommendation']}")
                elif score >= 33 and attendance < 75 and cond == 'score>=40 & attendance<75':
                    print(f"{subject}: {row['Recommendation']}")
                elif score >= 33 and attendance >= 75 and cond == 'score>=40 & attendance>=75':
                    print(f"{subject}: {row['Recommendation']}")
else:
    print("\nNo resource recommendations found. Make sure resources.csv exists with Subject, Condition, and Recommendation columns.")
