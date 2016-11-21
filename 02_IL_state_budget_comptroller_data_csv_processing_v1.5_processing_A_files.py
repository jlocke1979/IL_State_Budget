# -*- coding: utf-8 -*-
# Install libraries:
import pandas as pd
import os
import simplejson as json

# Possibly Needed llibraries 
# import numpy as np  
# import glob

### Summary of this script #####

# This script Cleans and Manipulates data.  
# It is to be run AFTER one performs the webscrape script on IL Comptroller website
# This script create compact and easily used Master Data file that ultimately is used to populate the data visualization




###################Switching over to create the file structure from top down first #######################################

# Manually create a reference for all Agencies and their names
agency_dict = {'210': 'Supreme Court Historic Preservation Commission', '664': 'Southern Illinois University', '131': 'General Assembly Retirement System', '620': 'Northeastern Illinois University',\
 '494': 'Department Of Transportation', '497': "Department Of Veterans' Affairs", '492': 'Department Of Revenue', '493': 'Illinois State Police', '692': 'Illinois Mathematics And Science Academy', \
 '693': 'State Universities Retirement System', '691': 'Illinois Student Assistance Commission', '695': 'State Universities Civil Service System', '542': 'Human Rights Commission', \
 '406': 'Department Of Agriculture', '540': 'Abraham Lincoln Presidential Library and Museum', '541': 'Illinois Historic Preservation Agency', '340': 'Office Of The Attorney General', \
 '402': 'Department On Aging', '548': 'Illinois Educational Labor Relations Board', '285': 'Judicial Inquiry Board', '676': 'University Of Illinois', '120': 'Legislative Ethics Commission',\
  '425': 'Department Of Juvenile Justice', '537': 'Illinois Guardianship And Advocacy Commission', '416': 'Department Of Central Management Services', '532': 'Illinois Environmental Protection Agency', \
  '370': 'Office Of The State Treasurer', '295': "Office Of The State's Attorneys Appellate Prosecutor", '418': 'Department Of Children And Family Services', '290': 'Office Of The State Appellate Defender', \
  '591': 'Illinois State Police Merit Board', '590': 'Illinois Labor Relations Board', '593': "Teachers' Retirement System", '592': 'Office Of The State Fire Marshal', \
  '310': 'Office Of The Governor', '115': 'Legislative Reference Bureau', '110': 'Legislative Printing Unit', '112': 'Legislative Research Unit', '524': 'Illinois Commerce Commission', \
  '525': 'Drycleaner Environmental Response Trust Fund Council', '526': 'Illinois Deaf And Hard Of Hearing Commission', '420': 'Department Of Commerce And Economic Opportunity',\
   '422': 'Department Of Natural Resources', '528': 'Court Of Claims', '529': 'East St. Louis Financial Advisory', '360': 'Office Of The State Comptroller', '426': 'Department Of Corrections',\
    '586': 'State Board Of Education', '587': 'State Board Of Elections', '585': 'Southwestern Illinois Development Authority', '580': 'Property Tax Appeal Board', '442': 'Department Of Human Rights', \
    '440': 'Department Of Financial And Professional Regulation', '446': 'Department Of Insurance', '445': 'Illinois Power Agency', '444': 'Department Of Human Services', '108': 'Legislative Information System',\
    '109': 'Legislative Audit Commission', '588': 'Illinois Emergency Management Agency', '103': 'Office Of The Auditor General', '101': 'General Assembly', \
    '105': 'Commission On Government Forecasting and Accountability', '644': 'Northern Illinois University', '511': 'Capital Development Board', \
    '510': 'Executive Ethics Commission', '517': 'Civil Service Commission', '458': 'Department Of The Lottery', '579': 'Illinois Racing Board', '578': 'Prisoner Review Board', '452': 'Department Of Labor', \
    '628': 'Western Illinois University', '330': 'Office Of The Lieutenant Governor', '574': 'Metropolitan Pier And Exposition Authority', '589': "State Employees' Retirement System", \
    '509': 'Office Of Executive Inspector General', '546': 'Illinois Criminal Justice Information Authority', '503': 'Illinois Arts Council', '569': 'Illinois Law Enforcement Training Standards Board', \
    '636': 'Illinois State University', '560': 'Illinois Finance Authority', '562': 'Procurement Policy Board', '466': 'Department Of Military Affairs', '564': 'Illinois Independent Tax Tribunal', \
    '565': 'Illinois Gaming Board', '507': "Governor's Office Of Management And Budget", '167': 'Joint Committee On Administrative Rules', '427': 'Department Of Employment Security', '275': 'Judges Retirement System', \
    '601': 'Board Of Higher Education', '558': 'Illinois Council On Developmental Disabilities', '156': 'Office Of The Architect Of The Capitol', '554': 'Illinois Sports Facilities Authority', \
    '608': 'Chicago State University', '201': 'Supreme Court', '563': "Workers' Compensation Commission", '612': 'Eastern Illinois University', '616': 'Governors State University', \
    '482': 'Department Of Public Health', '350': 'Office Of The Secretary Of State', '684': 'Illinois Community College Board', '478': 'Department Of Healthcare And Family Services', \
    '102': 'Legislative Inspector General','104': 'Citizens Assembly', '107': 'IL Commission on Intergovernmental Coop','140': 'Pension Laws Commission',\
    '155': 'Legislative Space Needs Comm','202': 'Attorney Regist & Discipl Comm','203': 'Board of Admission to the Bar','205': 'Clerk of the Supreme Court',\
    '215': 'Appellate Court District 1', '225': 'Appellate Court District 2','235': 'Appellate Court District 3','245': 'Appellate Court District 4',\
    '255': 'Appellate Court District 5', '331': 'IL Distance Learning Foundation','351': 'IL Literacy Foundation','399': 'Other Elected Officials','407': 'IL Grain Insurance', \
    '409': 'Alcoholism and Substance Abuse','423': 'IL Conservation Foundation','438': 'Financial Institutions','448': 'Innovation and Technology', \
    '462': 'Mental Health & Developmental Disabilities','473': 'Nuclear Safety','475': 'Professional Regulation','488': 'DORS (IW purposes only)', \
    '499': 'Other Code Departments','504': 'Other Agencies Boards & Auth','505': 'Banks & Real Estate','527': 'Comprehensive Health Insurance BD', \
    '530': 'E St. Louis Development Authority','531': 'Environmental Protection Trust Fund Com','533': "Governor's Purchase Care Rev BD",'534': 'Health Info Exchange Authority', \
    '535': 'IL Export Development Authority','536': 'IL Board of Examiners', '538': 'IL Farm Development Authority','539': 'IL Health Facilities Authority', \
    '549': 'IL Educational Facilities Authority','550': 'IL Development Finance Authority', '551': 'IL Housing Development Authority','553': 'IL Municipal Retirement Fund', \
    '555': 'IL State Board of Investments','556': 'IL Rural Bond Bank', '557': 'IL State Toll Highway Authority','559': 'IL Violence Prevenetion Authority',\
    '561': 'Tobacco Settlement Authority','567': 'Liquor Control Comm', '568': 'State Charter School Comm','570': 'City of Chicago',\
    '571': 'Medical District Comm','572': 'Mid-America Medical District Comm', '573': 'Roseland Medical District Comm','575': 'Prairie State 200 Authority', \
    '576': 'Regional Transportation Authority','577': 'Pollution Control Board', '581': 'Com Sav, Real Estate & Mort Fin','582': 'Quad Cities Reg Economic Development Authority', \
    '583': 'Sex Offender Management Board','584': 'Western IL Economic Development Authority', '594': "Teacher's Pension & Retirement System, C",'595': 'Summer School for the Arts ', \
    '596': 'Tri County River Valley Development Authority ','597': 'Southeastern IL Economic Development Authority', '598': 'Upper IL River Valley Development Authority', \
    '599': 'Will-Kankakee Regional Development Authority', '605': "Board of Governors'",'609': 'Chicago State University Foundation', '613': 'Eastern IL University Foundation', \
    '618': 'Governors State University Alumni Association', '621': 'Northereastern IL University Foundation','629': 'Western IL University Foundation', \
    '633': 'Board of Regents ','637': 'Illinois State University Foundation', '645': 'Northern IL University Foundation','646': 'Northern IL University Alumni Association', \
    '665': 'So Ill University - C Foundation','666': 'So Ill University - E Foundation', '667': 'So Ill University - C Alumni Association','668': 'So Ill University - E Alumni Association', \
    '677': 'University of Illinois Foundation','678': 'University of Illinois Alumni Association', '685': 'State Comm College - E St. Louis','799': 'Statutory Transfers', \
    '899': 'SAMS Administrative Agency'}



############################ Create function that creates a skeleton of a dictionary for the first layer (Agencies)

def create_agency_ID_Name_skeleton(Agency_dictionary_lookup):
	result = []
	temp_list = Agency_dictionary_lookup.items()
	for kk, vv in temp_list:
		temp_dictionary = {"Agency_ID": kk, "Agency_Name": vv}
		result.append(temp_dictionary)
	return result


# run the function
master_dictionary = create_agency_ID_Name_skeleton(agency_dict)


###################### Create skeleton spot in dictionary for Agency Category and Agency Category ID:

def create_agency_category_name_id_skelton(master_dictionary_to_add_to):
	result = master_dictionary_to_add_to
	for entry in result:
		entry["Agency_Category_Name"] = "None"
		entry["Agency_Category_ID"] = "None"
		
	return result

# Run the function 
master_dictionary = create_agency_category_name_id_skelton(master_dictionary)




####################### # Define each Agency_Category Groupings;
elementary_and_secondary_ed = ['586']  # id here is 1000
higher_education = ['691','676','684','664','644','636','628','601','608','612','616','620','692','695'] # id here is 1500
human_services = ['478','444','402','418','482','497','537','534','558','527','526'] # id here is 2000
public_safety = ['426','493','588','425','546','466','592','569','578','560','591']   # id here is  3000
environmental_and_business_regulation = ['532','422','565','440','446','524','563','442','579','525','542']    # id here is 4000
economic_development_and_infrastructure = ['494','557','420','427','574','406','554','445','541','452','503','585']   # id here is 5000
govt_services_elected_officials = ['360','370','350','340','310','330','553']   # id here is 6000
govt_services_judicial_agencies = ['201','275','290','295','210','285']   # id here is 6200
govt_services_legislative_agencies = ['131','101','103','108','112','105','115','110','156','167','564','120','109']   # id here is 6400
govt_services_other = ['416','448','458','492','507','509','510','511','517','528','548','555','562','580','583','587','589','590','593','594','693']   # id here is 6600
statutory_transfer_out = ['799']   # id here is 8000
unknown = []

def update_Agency_Category(master_dictionary_to_add_to,agency_category_list,text_to_use,id_to_use):
	for entry in master_dictionary_to_add_to:
		if entry["Agency_ID"] in agency_category_list:
			entry["Agency_Category_Name"] = text_to_use
			entry["Agency_Category_ID"] = id_to_use
	return



############### Run the function to update Agency Category Name and ID 
update_Agency_Category(master_dictionary,elementary_and_secondary_ed,"Elementary and Secondary Education",'1000')
update_Agency_Category(master_dictionary,higher_education,"Higher Education",'1500')
update_Agency_Category(master_dictionary,human_services,"Human Services",'2000')
update_Agency_Category(master_dictionary,public_safety,"Public Safety",'3000')
update_Agency_Category(master_dictionary,environmental_and_business_regulation,"Environmental and Business Regulation",'4000')
update_Agency_Category(master_dictionary,economic_development_and_infrastructure,"Economic Development and Infrastructure",'5000')
update_Agency_Category(master_dictionary,govt_services_elected_officials,"Government Services: Elected Officials",'6000')
update_Agency_Category(master_dictionary,govt_services_judicial_agencies,"Government Services: Judicial Agencies",'6200')
update_Agency_Category(master_dictionary,govt_services_legislative_agencies,"Government Services: Legislative Agencies",'6400')
update_Agency_Category(master_dictionary,govt_services_other,"Government Services: Other",'6600')
update_Agency_Category(master_dictionary,statutory_transfer_out,"Statutory Transfer Out",'8000')




### Creat and Fill the data structure with both Years and empty field (preparing for import of real data


def fill_year_with_skeleton(master_dictionary_to_add_to, year_reference):
	for i in master_dictionary_to_add_to:
		i[year_reference]  = { \
		'Agency_Appropriated_Amount': None,
		'Agency_Expended_Amount': None,
		'Agency_Unexpended_Amount': None,	
		'Object_of_Expenditure':[],
		}
	return


fill_year_with_skeleton(master_dictionary, '2015')
fill_year_with_skeleton(master_dictionary, '2016')
fill_year_with_skeleton(master_dictionary, '2017')



# Store the location of the summary amounts for all agencies (i.e. For each Agency was was its Approriations, expended, & unexpended)
agency_summary_file_2017 = r"..\\data\\comptroller_webscrape\\Statewide_By_Agency\\2017_AllAgency_A_Yes.csv"
agency_summary_file_2016 = r"..\\data\\comptroller_webscrape\\Statewide_By_Agency\\2016_AllAgency_A_Yes.csv"
agency_summary_file_2015 = r"..\\data\\comptroller_webscrape\\Statewide_By_Agency\\2015_AllAgency_A_Yes.csv"



############### A Function that read's Agency Summary  CSVs and stores to  df

def all_agency_summary_csv_to_df(file_path):

	df = pd.read_csv(file_path, 
		header = 0,
		thousands=',', 
		names = ['code','agency_name','appropriated','expended','unexpended'],
		dtype = {'code':str},
		encoding = 'latin-1')

	df['appropriated'] = df['appropriated'].str.replace('[$,]','')
	df['appropriated'] = df['appropriated'].str.replace('(', '-').astype(float)

	df['expended'] = df['expended'].str.replace('[$,]','')
	df['expended'] = df['expended'].str.replace('(', '-').astype(float)
	
	df['unexpended'] = df['unexpended'].str.replace('[$,]','')
	df['unexpended'] = df['unexpended'].str.replace('(', '-').astype(float)

	return df

# Run the function

agency_summary_df_2017 = all_agency_summary_csv_to_df(agency_summary_file_2017)
agency_summary_df_2016 = all_agency_summary_csv_to_df(agency_summary_file_2016)
agency_summary_df_2015 = all_agency_summary_csv_to_df(agency_summary_file_2015)








############### A Function that updates Agency Amount using Dataframe


def fill_agency_amounts(master_dictionary_to_add_to, df_to_reference, year):
	for index, row in df_to_reference.iterrows():
		for instance in master_dictionary_to_add_to:
			if instance["Agency_ID"] == row["code"]:
				instance[year]["Agency_Appropriated_Amount"] = row["appropriated"]
				instance[year]["Agency_Expended_Amount"] = row["expended"]
				instance[year]["Agency_Unexpended_Amount"] = row["unexpended"]
	return

## Run the function to update master data with Agency summary amounts
fill_agency_amounts(master_dictionary, agency_summary_df_2017, "2017") 
fill_agency_amounts(master_dictionary, agency_summary_df_2016, "2016") 
fill_agency_amounts(master_dictionary, agency_summary_df_2015, "2015") 









###################### BEG - Fills OBJECT OF EXPENDITURE into data structure #################################################


# Store Folder Locations
csvs_2017_folder = "..\\data\\comptroller_webscrape\\Object_of_expenditure_By_Agency\\Pulled_2016-08-09\\2017\\"
csvs_2016_folder = "..\\data\\comptroller_webscrape\\Object_of_expenditure_By_Agency\\Pulled_2016-08-09\\2016\\"
csvs_2015_folder = "..\\data\\comptroller_webscrape\\Object_of_expenditure_By_Agency\\Pulled_2016-08-09\\2015\\"

# Store names of each files in the above directories 
file_names_2017 = os.listdir(csvs_2017_folder)
file_names_2016 = os.listdir(csvs_2016_folder)
file_names_2015 = os.listdir(csvs_2015_folder)


################ A Function that create a SINGLE file_path (given a folder location & file name)

def create_file_path(folder,file_name):
	result = folder+file_name
	return result	



################ A Function that creates a MULTIPLE file_paths (given a folder location and an array of file name)

def create_file_paths_en_mass(folder,file_paths_array):
	result =[]
	for file_path in file_paths_array:
		final_path = create_file_path(folder, file_path) 	
		result.append(final_path)
	return result 



# Run Function that creates all file paths for a given year
full_file_paths_2017 = create_file_paths_en_mass(csvs_2017_folder,file_names_2017)
full_file_paths_2016 = create_file_paths_en_mass(csvs_2016_folder,file_names_2016)
full_file_paths_2015 = create_file_paths_en_mass(csvs_2015_folder,file_names_2015)




############### A Function that read's file to csv read file 

def object_of_expend_csv_to_df(file_path):
	df = pd.read_csv(file_path, 
		header = 0,
		thousands=',', 
		names = ['code','object_of_expenditure','appropriated','expended','unexpended'],
		dtype = {'code':str, 'object_of_expenditure':str,'appropriated':float,'expended':float,'unexpended':float},
		encoding = 'latin-1')
	return df




######################## Create function that goes through each file and updates the master dictionary with needed infor for Object of Expenditure ##########


def cycle_thru_file_path_update_and_update_master_dictionary(file_paths_array, master_dictionary_to_add_to):
	for file_path in file_paths_array:
		df = object_of_expend_csv_to_df(file_path)
		agency_id = file_path[90:93]			#### Be careful with this line (if the file path changes you'll need to update this)
		# print agency_id
		year = file_path[85:89]					#### Be careful with this line (if the file path changes you'll need to update this)
		# print year

		for instance in master_dictionary_to_add_to:
			if instance["Agency_ID"] == agency_id:
				for index, row in df.iterrows():
					instance[year]["Object_of_Expenditure"].append({ \
						"Obj_Exp_Name": row['object_of_expenditure'],
						"Obj_Exp_Appropriated": row['appropriated'],
						"Obj_Exp_Expended": row['expended'],
						"Obj_Exp_Unxpended": row['unexpended'],
						})

	return



# Run the function that populated master dictionary with Object of Expenditure data 
cycle_thru_file_path_update_and_update_master_dictionary(full_file_paths_2017, master_dictionary)
cycle_thru_file_path_update_and_update_master_dictionary(full_file_paths_2016, master_dictionary)
cycle_thru_file_path_update_and_update_master_dictionary(full_file_paths_2015, master_dictionary)





####################### Cleanup anything with Null values#################

# # Version 1 Works!
# no_category_list = []

# count = 0 
# for i in xrange(len(master_dictionary)):
# 	# print entry 
# 	if master_dictionary[i]["Agency_Category_ID"] == "None":
# 		no_category_list.append(count)
# 		# no_category_list.append(entry["Agency_ID"]
# 		# print entry 
# 		# master_dictionary.pop(entry) 

# 	count +=1 

# print no_category_list


# print len(master_dictionary)



# for each in reversed(no_category_list):
# 	# print each
# 	master_dictionary.pop(each)


# Version 2 -

def function_to_remove_null_agency_category_id(master_dictionary_to_add_to):
	no_category_list = []
	count = 0 
	for i in xrange(len(master_dictionary_to_add_to)):
		if master_dictionary_to_add_to[i]["Agency_Category_ID"] == "None":
			no_category_list.append(count)
		count +=1 

	for each in reversed(no_category_list):
		master_dictionary_to_add_to.pop(each)

	return master_dictionary_to_add_to


# Run the function to take out any null Agency_

trimmed_master_dictionary = function_to_remove_null_agency_category_id(master_dictionary)








########################################### Beg - Export master dictionary to JSON  ########################################################################################

# Create a location for final data
file_name_master_data = r'C:\Users\Justin\Development\ILStateBudget\output\master_data_v15.2.json'


with open(file_name_master_data,'w') as outfile:
	json.dump(trimmed_master_dictionary, outfile)

########################################### End - Export  master dictionary to JSON  ########################################################################################


