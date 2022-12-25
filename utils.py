import random
def branch_name_from_number(base):
	actual=["CS","IT","EE","ECE","E","MECH","CIVIL","OTHER"]
	data=actual[base-1]
	return data

def cert_name_from_number(base):
	actual=["cis c++ beg",
	"cis c beg", 
	"cis c++ adv", 
	"cis c adv" ,
	"cis js ess" ,
	"cis net ess" ,
	"ccna1" ,
	"ccna2" ,
	"ccna3" ,
	"pckt tracer" ,
	"machine learning" ,
	"cisco python pcap" ,
	"oracle" ,
	"aws" ,
	"microsoft" ,
	"google" ,
	"alibaba" ,
	"cis cyber sec" ,
	"cis iot" ,
	"digital mark cert"]
	data=[]
	for i in base:
		data.append(actual[i-1])
	return data

def hackathons_number_from_number(base):
	if base==12:
		return "more than 10"
	return base-1

def internships_number_from_number(base):
	if base==6:
		return "more than 5"
	return base-1

def projects_number_from_number(base):
	if base==8:
		return "more than 7"
	return base-1

def attendence_value_from_number(base):
	actual=["less than 50%","between 50% and 60%","between 60% and 70%","between 70% and 80%","between 80% and 90%","more than 90%"]
	return actual[base-1]

def placed_value_from_number(base):
	if base:
		return "PLACED"
	else:
		return "NOT PLACED"

def interest_value_from_number(base):
	if base:
		return "INTERESTED"
	else:
		return "NOT INTERESTED"

def backlogs_value_from_number(base):
	if base==6:
		return "more than 4"
	else:
		return base-1

def hobbies_value_from_number(base):
	actual=[
		"Computer Games",
		"Mobile Games",
		"Outdoor sports",
		"Indoor Sports",
		"Travelling",
		"Collecting something",
		"Sketching/ Painting/ Craft",
		"Dancing",
		"Singing",
		"Reading Books",
		"Youtube",
		"Content Creation"
	]
	data=[]
	for i in base:
		data.append(actual[i-1])
	return data

def package_value_from_number(base):
	actual=[
		"less than 2 lac",
		"2 - 4 lac",
		"4 - 7 lac",
		"7 - 10 lac",
		"10 -15 lac",
		"more than 15 lac",
		"0(not placed)"
	]

	return actual[base-1]

def skills_value_from_number(base):
	actual=[
		"HTML",
		"CSS",
		"Javascript",
		"C",
		"C++",
		"Python",
		"Java",
		"C#",
		"Go lang",
		"React JS",
		"Angular JS",
		"Node JS",
		"Express JS",
		"MongoDB",
		"DBMS",
		"Software",
		"Design Patterns",
		"AGILE framework",
		"MERN Stack Developement",
		"MEAN Stack Development",
		"Front End Web Development",
		"Back End Web Development",
		"Django Framework Python",
		"Flask Framework Python",
		"Linux",
		"Desktop Application Development",
		"Dot Net framework C#",
		"Mobile Application Developement",
		"Android Studio",
		"Game Development",
		"Unity",
		"Blender",
		"Video Editing",
		"Machine learning",
		"Neural Networks",
		"Wordpress",
		"Competitive Coding",
		"DSA",
		"Coding",
		"Problem Solving",
		"UI/UX Designing",
		"Figma",
		"Canva",
		"MS Excel",
		"React Native",
		"Git",
		"Animation",
		"Computer Vision",
		"Kotlin Language",
		"Cloud",
		"Project Management",
		"Hardware Programming",
		"Arduino",
		"Raspberry pi",
		"PHP",
		"Digital Marketing",
		"Aptitude",
		"Logical Reasoning",
		"English",
		"Content Creation",
		"Blockchain Developement",
		"Business",
		"entrepreneurship"
	]
	data=[]
	for i in base:
		data.append(actual[i-1])
	return data

def get_certificates(mn,mx):
	n=random.randint(mn,mx)
	certs=[]
	for i in range(0,n):
		ele=random.randint(1,20)
		certs.append(ele)
	return certs

def get_hackathons(mn,mx):
	n=random.randint(mn,mx)
	return n

def get_internships(mn,mx):
	n=random.randint(mn,mx)
	return n

def get_skills(mn,mx):
	n=random.randint(mn,mx)
	skills=[]
	for i in range(0,n):
		ele=random.randint(1,63)
		skills.append(ele)
	return skills

def get_projects(mn,mx):
	n=random.randint(mn,mx)
	return n

def placed_or_not(data):
	if len(data["CERTS"])<6:
		if len(data["SKILLS"])<9:
			if data["PROJECTS"]<3:
				if data["ATTENDENCE"]<4:
					if data["BACKLOGS"]>1:
						if data["CAMPUSTRAINING"]==False:
							return False
					return False
				return False
	return True

def get_interest_in_programming(data):
	if len(data["CERTS"])<7:
		if data["PROJECTS"]<4:
			return False
	return True

def get_backlogs(data):
	if data["INTEREST"]==False:
		if len(data["SKILLS"])<5:
			if data["PROJECTS"]<4:
				return random.randint(2,6)
	if random.randint(1,5)==3:
		return random.randint(1,3)
	else:
		return 1

def get_hobbies():
	hobbies=[]
	n=random.randint(1,6)
	for i in range(0,n):
		hobbies.append(random.randint(1,12))
	return hobbies

def get_attendance(data):
	if data["BACKLOGS"]>3:
		if data["HACKATHONS"]<2:
			return 1
		return 2
	if len(data["SKILLS"])>8:
		if data["HACKATHONS"]>=4:
			return random.randint(5,6)
		return random.randint(4,6)
	return random.randint(3,4)
	
def get_campus_training(data):
	if len(data["SKILLS"])>7 or data["ATTENDENCE"]>2:
		return True
	return False

def get_package_range(data):
	if data["PLACED"]:
		if len(data["CERTS"])>5:
			if len(data["SKILLS"])>9:
				if data["PROJECTS"]>5:
					if data["ATTENDENCE"]>2:
						if data["BACKLOGS"]==1:
							if data["INTERNSHIPS"]>=3:
								return 6
							return random.randint(5,6)
						return random.randint(4,5)
					return random.randint(3,4)
				return random.randint(2,3)
			return random.randint(1,3)
		return random.randint(0,3)
	return 7
				