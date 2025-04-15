import pandas as pd

data = [
    ["Python", "score<33 & attendance<75", "You're struggling with both attendance and understanding. Start with this Python crash course: https://youtu.be/rfscVS0vtbw?si=B497zE5XH5xKqiWD"],
    ["Python", "score<33 & attendance>=75", "You're trying but need better clarity. Try this interactive Python tutorial: https://www.learnpython.org/"],
    ["Python", "score>=33 & attendance<75", "Good score but low attendance. Revise with this cheat sheet: https://gto76.github.io/python-cheatsheet/"],
    ["Python", "score>=33 & attendance>=75", "Great job! Try building projects from here: https://realpython.com/"],

    ["Java", "score<33 & attendance<75", "Low performance and poor attendance. Start with Java basics: https://youtu.be/grEKMHGYyns"],
    ["Java", "score<33 & attendance>=75", "You’re attending but struggling. Try this hands-on Java site: https://www.tpointtech.com/java-tutorial"],
    ["Java", "score>=33 & attendance<75", "Good performance, attend more! Use this summary guide: https://quickref.me/java.html"],
    ["Java", "score>=33 & attendance>=75", "Excellent work! Practice with real coding challenges: https://www.hackerrank.com/domains/tutorials/10-days-of-java"],

    ["OS", "score<33 & attendance<75", "Both performance and attendance are low. Watch this OS intro: https://www.youtube.com/playlist?list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O"],
    ["OS", "score<33 & attendance>=75", "You’re present but need clarity. Try: https://www.geeksforgeeks.org/operating-systems/"],
    ["OS", "score>=33 & attendance<75", "You’re doing okay, attend classes to strengthen understanding. Summary here: https://www.geeksforgeeks.org/last-minute-notes-operating-systems/"],
    ["OS", "score>=33 & attendance>=75", "Good progress! Solve OS questions here: https://www.geeksforgeeks.org/operating-systems-interview-questions/"],

    ["DSA", "score<33 & attendance<75", "Weak performance and low attendance. Start from basics: https://youtu.be/8hly31xKli0"],
    ["DSA", "score<33 & attendance>=75", "You’re attending, keep practicing: https://www.geeksforgeeks.org/data-structures/"],
    ["DSA", "score>=33 & attendance<75", "Keep it up! Focus more on class participation. Use: https://csvistool.com/"],
    ["DSA", "score>=33 & attendance>=75", "Awesome! Improve further here: https://leetcode.com/explore/"],

    ["DBMS", "score<33 & attendance<75", "You need help with DBMS basics. Start here: https://youtu.be/HXV3zeQKqGY?si=4u9uAYe-2v08f9i-"],
    ["DBMS", "score<33 & attendance>=75", "You’re regular but need conceptual clarity. Try this: https://www.geeksforgeeks.org/dbms/"],
    ["DBMS", "score>=33 & attendance<75", "You know the concepts, improve consistency. Use this: https://www.studytonight.com/dbms/"],
    ["DBMS", "score>=33 & attendance>=75", "You're doing great! Build a mini project: https://github.com/topics/dbms-project"],

    ["C", "score<33 & attendance<75", "You need help with C basics. Start here: https://www.youtube.com/watch?v=87SH2Cn0s9A"],
    ["C", "score<33 & attendance>=75", "You’re regular but need conceptual clarity. Try this: https://www.geeksforgeeks.org/c-programming-language/"],
    ["C", "score>=33 & attendance<75", "Good performance, attend more! Use this summary guide: https://quickref.me/c.html"],
    ["C", "score>=33 & attendance>=75", "You're doing great! Build a mini project: https://www.codewithc.com/c-projects-with-source-code/"]

]

df = pd.DataFrame(data, columns=["Subject", "Condition", "Recommendation"])
df.to_csv("resources.csv", index=False)
