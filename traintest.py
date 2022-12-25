import pandas as pd
import joblib

df=pd.read_csv("placement.csv")

x=df[["BRANCH","HACKATHONS","INTERNSHIPS","PROJECTS","INTEREST","ATTENDENCE","BACKLOGS","CAMPUSTRAINING","cis c++ beg", "cis c beg", "cis c++ adv", "cis c adv" , "cis js ess" , "cis net ess" , "ccna1" , "ccna2" , "ccna3" , "pckt tracer" , "machine learning" , "cisco python pcap" , "oracle" , "aws" , "microsoft" , "google" , "alibaba" , "cis cyber sec" , "cis iot" , "digital mark cert","Computer Games", "Mobile Games", "Outdoor sports", "Indoor Sports", "Travelling", "Collecting something", "Sketching/ Painting/ Craft", "Dancing", "Singing", "Reading Books", "Youtube", "Content Creation",
"HTML", "CSS", "Javascript", "C", "C++", "Python", "Java", "C#", "Go lang", "React JS", "Angular JS", "Node JS", "Express JS", "MongoDB", "DBMS", "Software", "Design Patterns", "AGILE framework", "MERN Stack Developement", "MEAN Stack Development", "Front End Web Development", "Back End Web Development", "Django Framework Python", "Flask Framework Python", "Linux", "Desktop Application Development", "Dot Net framework C#", "Mobile Application Developement", "Android Studio", "Game Development", "Unity", "Blender", "Video Editing", "Machine learning", "Neural Networks", "Wordpress", "Competitive Coding", "DSA", "Coding", "Problem Solving", "UI/UX Designing", "Figma", "Canva", "MS Excel", "React Native", "Git", "Animation", "Computer Vision", "Kotlin Language", "Cloud", "Project Management", "Hardware Programming", "Arduino", "Raspberry pi", "PHP", "Digital Marketing", "Aptitude", "Logical Reasoning", "English", "Content Creation", "Blockchain Developement", "Business", "entrepreneurship"]]

y=df["PLACED"]

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

from sklearn.linear_model import LinearRegression

clf=LinearRegression()
clf.fit(x_train,y_train)

filename = 'placementmodel.sav'
joblib.dump(clf, filename)

for i in clf.predict(x_test):
	print(i)

print(y_test)


