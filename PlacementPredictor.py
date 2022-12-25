import streamlit as st
import joblib
st.beta_set_page_config(page_title='College Placement Predictor')
st.title("PLACEMENT PREDICTION")

branch=st.selectbox("Select your branch",options=["CS","IT","EE","ECE","E","MECH","CIVIL","OTHER"])

hacks=st.selectbox("How many hackathons/contest you participated in",options=["0","1","2","3","4","5","6","7","8","9","10",">10"])

interns=st.selectbox("How many internships you completed",options=["0","1","2","3","4",">=5"])

projs=st.selectbox("How many projects you created",options=["0","1","2","3","4","5","6",">=7"])

interst=st.selectbox("Are you interested in programming",options=["Yes","No"])

att=st.selectbox("How much is your attendence",options=["less than 50%","between 50% and 60%","between 60% and 70%","between 70% and 80%","between 80% and 90%","more than 90%"])

backs=st.selectbox("How many backlogs do you have",options=["0","1","2","3","4",">4"])

campustrain=st.selectbox("Do you attend campus training",options=["Yes","No"])

certs=st.multiselect("Select what all certifications you have completed",["cis c++ beg", "cis c beg", "cis c++ adv", "cis c adv" , "cis js ess" , "cis net ess" , "ccna1" , "ccna2" , "ccna3" , "pckt tracer" , "machine learning" , "cisco python pcap" , "oracle" , "aws" , "microsoft" , "google" , "alibaba" , "cis cyber sec" , "cis iot" , "digital mark cert"])

hobbies=st.multiselect("Select your hobbies",["Computer Games", "Mobile Games", "Outdoor sports", "Indoor Sports", "Travelling", "Collecting something", "Sketching/ Painting/ Craft", "Dancing", "Singing", "Reading Books", "Youtube", "Content Creation"])

skills=st.multiselect("Select your skills",["HTML", "CSS", "Javascript", "C", "C++", "Python", "Java", "C#", "Go lang", "React JS", "Angular JS", "Node JS", "Express JS", "MongoDB", "DBMS", "Software", "Design Patterns", "AGILE framework", "MERN Stack Developement", "MEAN Stack Development", "Front End Web Development", "Back End Web Development", "Django Framework Python", "Flask Framework Python", "Linux", "Desktop Application Development", "Dot Net framework C#", "Mobile Application Developement", "Android Studio", "Game Development", "Unity", "Blender", "Video Editing", "Machine learning", "Neural Networks", "Wordpress", "Competitive Coding", "DSA", "Coding", "Problem Solving", "UI/UX Designing", "Figma", "Canva", "MS Excel", "React Native", "Git", "Animation", "Computer Vision", "Kotlin Language", "Cloud", "Project Management", "Hardware Programming", "Arduino", "Raspberry pi", "PHP", "Digital Marketing", "Aptitude", "Logical Reasoning", "English", "Content Creation", "Blockchain Developement", "Business", "entrepreneurship"])

x=103*[0]


actual_certs=["cis c++ beg", "cis c beg", "cis c++ adv", "cis c adv" , "cis js ess" , "cis net ess" , "ccna1" , "ccna2" , "ccna3" , "pckt tracer" , "machine learning" , "cisco python pcap" , "oracle" , "aws" , "microsoft" , "google" , "alibaba" , "cis cyber sec" , "cis iot" , "digital mark cert"]

actual_hobbies=["Computer Games", "Mobile Games", "Outdoor sports", "Indoor Sports", "Travelling", "Collecting something", "Sketching/ Painting/ Craft", "Dancing", "Singing", "Reading Books", "Youtube", "Content Creation"]

actual_skills=["HTML", "CSS", "Javascript", "C", "C++", "Python", "Java", "C#", "Go lang", "React JS", "Angular JS", "Node JS", "Express JS", "MongoDB", "DBMS", "Software", "Design Patterns", "AGILE framework", "MERN Stack Developement", "MEAN Stack Development", "Front End Web Development", "Back End Web Development", "Django Framework Python", "Flask Framework Python", "Linux", "Desktop Application Development", "Dot Net framework C#", "Mobile Application Developement", "Android Studio", "Game Development", "Unity", "Blender", "Video Editing", "Machine learning", "Neural Networks", "Wordpress", "Competitive Coding", "DSA", "Coding", "Problem Solving", "UI/UX Designing", "Figma", "Canva", "MS Excel", "React Native", "Git", "Animation", "Computer Vision", "Kotlin Language", "Cloud", "Project Management", "Hardware Programming", "Arduino", "Raspberry pi", "PHP", "Digital Marketing", "Aptitude", "Logical Reasoning", "English", "Content Creation", "Blockchain Developement", "Business", "entrepreneurship"]

actual_branch=[1,2,3,4,5,6,7,8]

for i in range(0,len(actual_certs)):
	for j in range(0,len(certs)):
		if actual_certs[i]==certs[j]:
			x[i+8]=1


for i in range(0,len(actual_hobbies)):
	for j in range(0,len(hobbies)):
		if actual_hobbies[i]==hobbies[j]:
			x[i+28]=1


for i in range(0,len(actual_skills)):
	for j in range(0,len(skills)):
		if actual_skills[i]==skills[j]:
			x[i+40]=1

actual_branch=["CS","IT","EE","ECE","E","MECH","CIVIL","OTHER"]

actual_hacks=["0","1","2","3","4","5","6","7","8","9","10",">10"]

actual_inters=["0","1","2","3","4",">=5"]

actual_projs=["0","1","2","3","4","5","6",">=7"]

actual_attend=["less than 50%","between 50% and 60%","between 60% and 70%","between 70% and 80%","between 80% and 90%","more than 90%"]

actual_backs=["0","1","2","3","4",">4"]

for i in range(0,len(actual_branch)):
	if branch==actual_branch[i]:
		x[0]=i+1
		
for i in range(0,len(actual_hacks)):
	if hacks==actual_hacks[i]:
		x[1]=i+1

for i in range(0,len(actual_inters)):
	if interns==actual_inters[i]:
		x[2]=i+1

for i in range(0,len(actual_projs)):
	if projs==actual_projs[i]:
		x[3]=i+1

for i in range(0,len(actual_attend)):
	if att==actual_attend[i]:
		x[5]=i+1

for i in range(0,len(actual_backs)):
	if backs==actual_backs[i]:
		x[6]=i+1

x[4]=1 if interst=="Yes" else 0
x[7]=1 if campustrain=="Yes" else 0

filename = 'placementmodel.sav'
clf = joblib.load(filename)

y=clf.predict([x])

st.title("Your placement chances are : "+str(round(y[0]*100))+"%")










