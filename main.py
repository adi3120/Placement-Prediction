import csv
import pandas as pd
from utils import *

branch_chances=[35,25,10,10,7,6,4,3]

a=1
n=10000
branch_result=[]

for i in branch_chances:
	i=i*(n//100)
	for j in range(0,i):
		branch_result.append(a)
	a+=1

data_list=[]

rows=["BRANCH","CERTS","HACKATHONS","INTERNSHIPS","PROJECTS","SKILLS","HOBBIES","INTEREST","ATTENDENCE","BACKLOGS","CAMPUSTRAINING","PLACED","PACKAGE","cis c++ beg", "cis c beg", "cis c++ adv", "cis c adv" , "cis js ess" , "cis net ess" , "ccna1" , "ccna2" , "ccna3" , "pckt tracer" , "machine learning" , "cisco python pcap" , "oracle" , "aws" , "microsoft" , "google" , "alibaba" , "cis cyber sec" , "cis iot" , "digital mark cert","Computer Games", "Mobile Games", "Outdoor sports", "Indoor Sports", "Travelling", "Collecting something", "Sketching/ Painting/ Craft", "Dancing", "Singing", "Reading Books", "Youtube", "Content Creation",
"HTML", "CSS", "Javascript", "C", "C++", "Python", "Java", "C#", "Go lang", "React JS", "Angular JS", "Node JS", "Express JS", "MongoDB", "DBMS", "Software", "Design Patterns", "AGILE framework", "MERN Stack Developement", "MEAN Stack Development", "Front End Web Development", "Back End Web Development", "Django Framework Python", "Flask Framework Python", "Linux", "Desktop Application Development", "Dot Net framework C#", "Mobile Application Developement", "Android Studio", "Game Development", "Unity", "Blender", "Video Editing", "Machine learning", "Neural Networks", "Wordpress", "Competitive Coding", "DSA", "Coding", "Problem Solving", "UI/UX Designing", "Figma", "Canva", "MS Excel", "React Native", "Git", "Animation", "Computer Vision", "Kotlin Language", "Cloud", "Project Management", "Hardware Programming", "Arduino", "Raspberry pi", "PHP", "Digital Marketing", "Aptitude", "Logical Reasoning", "English", "Content Creation", "Blockchain Developement", "Business", "entrepreneurship"]

for i in branch_result:
	data={
		"BRANCH":0,
		"CERTS":[],
		"HACKATHONS":0,
		"INTERNSHIPS":0,
		"SKILLS":[],
		"PROJECTS":0,
		"PLACED":1,
		"INTEREST":1,
		"BACKLOGS":0,
		"HOBBIES":[],
		"ATTENDENCE":3,
		"CAMPUSTRAINING":0,
		"PACKAGE":0,
		"cis c++ beg":0,
		"cis c beg":0, 
		"cis c++ adv":0, 
		"cis c adv":0 ,
		"cis js ess":0 ,
		"cis net ess":0 ,
		"ccna1":0 ,
		"ccna2":0 ,
		"ccna3":0 ,
		"pckt tracer":0 ,
		"machine learning":0 ,
		"cisco python pcap":0 ,
		"oracle":0 ,
		"aws":0 ,
		"microsoft":0 ,
		"google":0 ,
		"alibaba":0 ,
		"cis cyber sec":0 ,
		"cis iot":0 ,
		"digital mark cert":0,
		"Computer Games":0,
		"Mobile Games":0,
		"Outdoor sports":0,
		"Indoor Sports":0,
		"Travelling":0,
		"Collecting something":0,
		"Sketching/ Painting/ Craft":0,
		"Dancing":0,
		"Singing":0,
		"Reading Books":0,
		"Youtube":0,
		"Content Creation":0,
		"HTML":0,
		"CSS":0,
		"Javascript":0,
		"C":0,
		"C++":0,
		"Python":0,
		"Java":0,
		"C#":0,
		"Go lang":0,
		"React JS":0,
		"Angular JS":0,
		"Node JS":0,
		"Express JS":0,
		"MongoDB":0,
		"DBMS":0,
		"Software":0,
		"Design Patterns":0,
		"AGILE framework":0,
		"MERN Stack Developement":0,
		"MEAN Stack Development":0,
		"Front End Web Development":0,
		"Back End Web Development":0,
		"Django Framework Python":0,
		"Flask Framework Python":0,
		"Linux":0,
		"Desktop Application Development":0,
		"Dot Net framework C#":0,
		"Mobile Application Developement":0,
		"Android Studio":0,
		"Game Development":0,
		"Unity":0,
		"Blender":0,
		"Video Editing":0,
		"Machine learning":0,
		"Neural Networks":0,
		"Wordpress":0,
		"Competitive Coding":0,
		"DSA":0,
		"Coding":0,
		"Problem Solving":0,
		"UI/UX Designing":0,
		"Figma":0,
		"Canva":0,
		"MS Excel":0,
		"React Native":0,
		"Git":0,
		"Animation":0,
		"Computer Vision":0,
		"Kotlin Language":0,
		"Cloud":0,
		"Project Management":0,
		"Hardware Programming":0,
		"Arduino":0,
		"Raspberry pi":0,
		"PHP":0,
		"Digital Marketing":0,
		"Aptitude":0,
		"Logical Reasoning":0,
		"English":0,
		"Content Creation":0,
		"Blockchain Developement":0,
		"Business":0,
		"entrepreneurship":0
	}
	data["BRANCH"]=i
	data_list.append(data)

for i in range(0,n):
	if data_list[i]["BRANCH"]==1:
		mn,mx=1,8
		data_list[i]["CERTS"]=get_certificates(mn,mx)
		mn,mx=1,12
		data_list[i]["HACKATHONS"]=get_hackathons(mn,mx)
		mn,mx=1,6
		data_list[i]["INTERNSHIPS"]=get_internships(mn,mx)
		mn,mx=4,16
		data_list[i]["SKILLS"]=get_skills(mn,mx)
		mn,mx=1,8
		data_list[i]["PROJECTS"]=get_projects(mn,mx)

	elif data_list[i]["BRANCH"]==2:
		mn,mx=4,7
		data_list[i]["CERTS"]=get_certificates(mn,mx)
		mn,mx=1,12
		data_list[i]["HACKATHONS"]=get_hackathons(mn,mx)
		mn,mx=1,6
		data_list[i]["INTERNSHIPS"]=get_internships(mn,mx)
		mn,mx=4,16
		data_list[i]["SKILLS"]=get_skills(mn,mx)
		mn,mx=1,8
		data_list[i]["PROJECTS"]=get_projects(mn,mx)
	
	elif data_list[i]["BRANCH"]==3:
		mn,mx=1,6
		data_list[i]["CERTS"]=get_certificates(mn,mx)
		mn,mx=1,9
		data_list[i]["HACKATHONS"]=get_hackathons(mn,mx)
		mn,mx=1,4
		data_list[i]["INTERNSHIPS"]=get_internships(mn,mx)
		mn,mx=3,14
		data_list[i]["SKILLS"]=get_skills(mn,mx)
		mn,mx=1,7
		data_list[i]["PROJECTS"]=get_projects(mn,mx)
	
	elif data_list[i]["BRANCH"]==4:
		mn,mx=1,6
		data_list[i]["CERTS"]=get_certificates(mn,mx)
		mn,mx=1,9
		data_list[i]["HACKATHONS"]=get_hackathons(mn,mx)
		mn,mx=1,4
		data_list[i]["INTERNSHIPS"]=get_internships(mn,mx)
		mn,mx=3,14
		data_list[i]["SKILLS"]=get_skills(mn,mx)
		mn,mx=1,7
		data_list[i]["PROJECTS"]=get_projects(mn,mx)
	
	elif data_list[i]["BRANCH"]==5:
		mn,mx=1,6
		data_list[i]["CERTS"]=get_certificates(mn,mx)
		mn,mx=1,9
		data_list[i]["HACKATHONS"]=get_hackathons(mn,mx)
		mn,mx=1,4
		data_list[i]["INTERNSHIPS"]=get_internships(mn,mx)
		mn,mx=3,14
		data_list[i]["SKILLS"]=get_skills(mn,mx)
		mn,mx=1,7
		data_list[i]["PROJECTS"]=get_projects(mn,mx)
	
	elif data_list[i]["BRANCH"]==6:
		mn,mx=4,6
		data_list[i]["CERTS"]=get_certificates(mn,mx)
		mn,mx=1,7
		data_list[i]["HACKATHONS"]=get_hackathons(mn,mx)
		mn,mx=1,4
		data_list[i]["INTERNSHIPS"]=get_internships(mn,mx)
		mn,mx=4,13
		data_list[i]["SKILLS"]=get_skills(mn,mx)
		mn,mx=1,6
		data_list[i]["PROJECTS"]=get_projects(mn,mx)
	
	elif data_list[i]["BRANCH"]==7:
		mn,mx=1,5
		data_list[i]["CERTS"]=get_certificates(mn,mx)
		mn,mx=1,4
		data_list[i]["HACKATHONS"]=get_hackathons(mn,mx)
		mn,mx=1,3
		data_list[i]["INTERNSHIPS"]=get_internships(mn,mx)
		mn,mx=3,10
		data_list[i]["SKILLS"]=get_skills(mn,mx)
		mn,mx=1,6
		data_list[i]["PROJECTS"]=get_projects(mn,mx)
	
	elif data_list[i]["BRANCH"]==8:
		mn,mx=1,5
		data_list[i]["CERTS"]=get_certificates(mn,mx)
		mn,mx=1,4
		data_list[i]["HACKATHONS"]=get_hackathons(mn,mx)
		mn,mx=1,3
		data_list[i]["INTERNSHIPS"]=get_internships(mn,mx)
		mn,mx=1,8
		data_list[i]["SKILLS"]=get_skills(mn,mx)
		mn,mx=1,6
		data_list[i]["PROJECTS"]=get_projects(mn,mx)
	
	data_list[i]["INTEREST"]=get_interest_in_programming(data_list[i])
	data_list[i]["BACKLOGS"]=get_backlogs(data_list[i])
	data_list[i]["HOBBIES"]=get_hobbies()
	data_list[i]["ATTENDENCE"]=get_attendance(data_list[i])
	data_list[i]["CAMPUSTRAINING"]=get_campus_training(data_list[i])
	data_list[i]["PLACED"]=placed_or_not(data_list[i])
	data_list[i]["PACKAGE"]=get_package_range(data_list[i])
	

for i in data_list:
	i["SKILLS"]=set(i["SKILLS"])
	i["CERTS"]=set(i["CERTS"])
	i["HOBBIES"]=set(i["HOBBIES"])

# for i in data_list:
# 	if i["PLACED"]==0:
# 		print(i)

for i in data_list:
	# i["BRANCH"]=branch_name_from_number(i["BRANCH"])
	i["CERTS"]=cert_name_from_number(i["CERTS"])
	# i["HACKATHONS"]=hackathons_number_from_number(i["HACKATHONS"])
	# i["INTERNSHIPS"]=internships_number_from_number(i["INTERNSHIPS"])
	# i["PROJECTS"]=projects_number_from_number(i["PROJECTS"])
	# i["ATTENDENCE"]=attendence_value_from_number(i["ATTENDENCE"])
	i["HOBBIES"]=hobbies_value_from_number(i["HOBBIES"])
	i["PLACED"]=placed_value_from_number(i["PLACED"])
	# i["BACKLOGS"]=backlogs_value_from_number(i["BACKLOGS"])
	i["INTEREST"]=interest_value_from_number(i["INTEREST"])
	# i["PACKAGE"]=package_value_from_number(i["PACKAGE"])
	i["SKILLS"]=skills_value_from_number(i["SKILLS"])

for i in range(0,n):
	data_list[i]=value_to_num(data_list[i])

with open('placement.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=rows)
    writer.writeheader()
    writer.writerows(data_list)

placements=pd.read_csv("placement.csv")

data_min=placements[["BRANCH","HACKATHONS","INTERNSHIPS","PROJECTS","INTEREST","ATTENDENCE","BACKLOGS","CAMPUSTRAINING","cis c++ beg", "cis c beg", "cis c++ adv", "cis c adv" , "cis js ess" , "cis net ess" , "ccna1" , "ccna2" , "ccna3" , "pckt tracer" , "machine learning" , "cisco python pcap" , "oracle" , "aws" , "microsoft" , "google" , "alibaba" , "cis cyber sec" , "cis iot" , "digital mark cert","Computer Games", "Mobile Games", "Outdoor sports", "Indoor Sports", "Travelling", "Collecting something", "Sketching/ Painting/ Craft", "Dancing", "Singing", "Reading Books", "Youtube", "Content Creation",
"HTML", "CSS", "Javascript", "C", "C++", "Python", "Java", "C#", "Go lang", "React JS", "Angular JS", "Node JS", "Express JS", "MongoDB", "DBMS", "Software", "Design Patterns", "AGILE framework", "MERN Stack Developement", "MEAN Stack Development", "Front End Web Development", "Back End Web Development", "Django Framework Python", "Flask Framework Python", "Linux", "Desktop Application Development", "Dot Net framework C#", "Mobile Application Developement", "Android Studio", "Game Development", "Unity", "Blender", "Video Editing", "Machine learning", "Neural Networks", "Wordpress", "Competitive Coding", "DSA", "Coding", "Problem Solving", "UI/UX Designing", "Figma", "Canva", "MS Excel", "React Native", "Git", "Animation", "Computer Vision", "Kotlin Language", "Cloud", "Project Management", "Hardware Programming", "Arduino", "Raspberry pi", "PHP", "Digital Marketing", "Aptitude", "Logical Reasoning", "English", "Content Creation", "Blockchain Developement", "Business", "entrepreneurship","PLACED","PACKAGE"]]

# print(data_min.head())

data_min.to_csv('placement.csv')
