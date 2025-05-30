import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import os


class AcademicTracker():
  def __init__(self):
    
    #csv file variable
    self.user_csv='users.csv'
    self.resource_csv='resources.csv'
    #all declared variables
    self.s_name=''
    self.scores = {}
    self.percentage = {}
    self.attendance = 0.0
    self.weak_subjects = ''
    self.overall_percent = 0.0
    
  def input_student_details(self):
      #ask user to enter name for checking there previous data
      self.s_name=input("Your Name:").strip().title()

      # Check if user already exists
      if os.path.exists(self.user_csv):
          df_existing = pd.read_csv(self.user_csv)
          if self.s_name in df_existing['Student Name'].values:  # checking from csv file if user exist with name
            print("\nUser Found! Welcome back, here is your data:\n")
            print(df_existing[df_existing['Student Name'] == self.s_name].to_string(index=False)) #displaying the data 
            exit()
          else:
            print("\nUser not found. Let's enter your details.\n")
      else:
        print("\nPlease Enter Your details:\n")  
  
        #loop for inputting the details and helping in further checking
      while True:
          self.scores = {} #using dictionary for insertion in csv
          self.percentage={} # for calculating the percentage of subjects  
        
        #Inputting the details of the user  
          no_of_sub=int(input("Enter the No.of.Subject:"))
          
        # using loop to add all subjects marks
          for i in range(no_of_sub):
            subject_name=input(f"Enter Subject {i+1}: ").strip().title()
            score_got = int(input(f"Enter the marks you scored in {subject_name}: "))
            score_total=int(input(f"Enter the total marks in {subject_name}: "))
            
            #adding values in dictionary
            self.scores[subject_name]=(score_got, score_total)
            self.percentage[subject_name]=round((score_got/score_total)*100,2)
        
        # attendance input
          self.attendance=float(input("Enter your Overall Attendance Percentage:"))
    
        # printing the inputted details for confirmation
          print("\nYour Entered Details:\n")
          for subject, percent in self.percentage.items():
            print(f"{subject}: {percent}%")
          print(f"Attendance: {self.attendance}%")
            
        #   #confirming with the user
          confrim_msg=input("\nType yes to confirm or no to re-enter your details:").strip().lower()
          if (confrim_msg=="yes"):
            print("\nDetails Confirmed and Saved.\n")
            break
          else:
            print("\nRe-enter your Details.\n") #user will re enter the details

  def calculate_progress(self):
    #calculating ovaerall percentage using numpy
    all_scores=np.array(list(self.percentage.values()))
    self.overall_percentage=round(np.mean(all_scores),2)  

  def data_saving(self):
    #storing the user entered data in data list    
    data=[]
    for subject,percent in self.percentage.items():  
      data.append({
        'Student Name':self.s_name,
        'Subject': subject,
        'Score (%)': percent,
        'Attendance (%)': self.attendance,
        'Overall (%)': self.overall_percentage,
        'Weak Subject': 'Yes' if percent < 33 else 'No'
      })
      
    #storing the data in csv file  
    self.df_new = pd.DataFrame(data)
    if os.path.exists(self.user_csv):
      df = pd.read_csv(self.user_csv)
      df_combined = pd.concat([df, self.df_new], ignore_index=True)
    else:
      df_combined=self.df_new

    df_combined.to_csv(self.user_csv, index=False)     
          
    #after storing data we will display the progress
    print("*"*50)
    print("Calculating your Progress....")   
    print("Your Updated Academic Report:\n")

    #printing the data from the csv file 
    print(self.df_new.to_string(index=False))
  
  def show_graph(self):  
    #displaying graph related to the progress   
    pl.figure(figsize=(10, 6))
    pl.bar(self.percentage.keys(), self.percentage.values(), color='green')
    pl.xlabel("Subjects")
    pl.ylabel("Score Percentage")
    pl.title(f"{self.s_name}'s Subject Performance")
    pl.ylim(0, 100)
    pl.axhline(y=33, color='yellow', linestyle='--', label='Minimum')
    pl.legend()
    pl.grid(axis='y', linestyle='--', alpha=0.7)
    pl.tight_layout()
    pl.show()

  def recommendation(self):
    #displaying recommendations 
    if os.path.exists(self.resource_csv):
      resources_df = pd.read_csv(self.resource_csv)

      print("\nPersonalized Recommendations:\n")
      for _, row in self.df_new.iterrows():  #iterating over each subject row
        subject = row['Subject']
        score = row['Score (%)']

        if subject in resources_df['Subject'].values:
          recs = resources_df[resources_df['Subject'] == subject]

          for _, res_row in recs.iterrows():
            cond = res_row['Condition'].strip().lower()
            if score < 33 and self.attendance < 75 and cond == 'score<33 & attendance<75':
              print(f"{subject}: {res_row['Recommendation']}")
            elif score < 33 and self.attendance >= 75 and cond == 'score<33 & attendance>=75':
              print(f"{subject}: {res_row['Recommendation']}")
            elif score >= 33 and self.attendance < 75 and cond == 'score>=33 & attendance<75':
              print(f"{subject}: {res_row['Recommendation']}")
            elif score >= 33 and self.attendance >= 75 and cond == 'score>=33 & attendance>=75':
              print(f"{subject}: {res_row['Recommendation']}")
            
#MAIN FUNCTION
if __name__=="__main__":
  #starting title of the project
  print("Welcome to academic Tracker and Resource Recommander")
  print("*"*50)
  print("\n\n")
  
  tracker=AcademicTracker()
  tracker.input_student_details()
  tracker.calculate_progress()
  tracker.data_saving()
  tracker.show_graph()
  tracker.recommendation() 
