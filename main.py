import random
import csv
import pandas as pd
from utils import *

branch_choices=[1,2,3,4,5,6,7,8]
branch_chances=[40,20,10,10,5,5,5,5]

a=1
n=100
branch_result=[]


for i in branch_chances:
	i=i*(n//100)
	for j in range(0,i):
		branch_result.append(a)
	a+=1


data_list=[]
rows=["BRANCH","CERTS","HACKATHONS","INTERNSHIPS","PROJECTS","SKILLS","HOBBIES","INTEREST","ATTENDENCE","BACKLOGS","CAMPUSTRAINING","PLACED","PACKAGE"]
for i in branch_result:
	data={
		"BRANCH":0,
		"CERTS":[],
		"HACKATHONS":0,
		"INTERNSHIPS":0,
		"SKILLS":[],
		"PROJECTS":0,
		"PLACED":True,
		"INTEREST":True,
		"BACKLOGS":0,
		"HOBBIES":[],
		"ATTENDENCE":3,
		"CAMPUSTRAINING":False,
		"PACKAGE":0
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

for i in data_list:
	if i["PLACED"]==False:
		print(i)

for i in data_list:
	i["BRANCH"]=branch_name_from_number(i["BRANCH"])
	i["CERTS"]=cert_name_from_number(i["CERTS"])
	i["HACKATHONS"]=hackathons_number_from_number(i["HACKATHONS"])
	i["INTERNSHIPS"]=internships_number_from_number(i["INTERNSHIPS"])
	i["PROJECTS"]=projects_number_from_number(i["PROJECTS"])
	i["ATTENDENCE"]=attendence_value_from_number(i["ATTENDENCE"])
	i["HOBBIES"]=hobbies_value_from_number(i["HOBBIES"])
	i["PLACED"]=placed_value_from_number(i["PLACED"])
	i["BACKLOGS"]=backlogs_value_from_number(i["BACKLOGS"])
	i["INTEREST"]=interest_value_from_number(i["INTEREST"])
	i["PACKAGE"]=package_value_from_number(i["PACKAGE"])
	i["SKILLS"]=skills_value_from_number(i["SKILLS"])

with open('placement.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=rows)
    writer.writeheader()
    writer.writerows(data_list)

# placements=pd.read_csv("placement.csv")

# print(placements.head())
