#Installing Libraries
import pandas as pd
import simplejson as json
import numpy as np



### Introducation ####
# This script uses spreadsheets pulled down from the Illinois Office of Management and Budget (OMB).  
# The OMB is an alternate source of information than the Comptroller on IL Spending.
# The two data sources offer different Pros and Cons. 


# Pros of OMB
# Offers some detail in the data that the Comptroller does  (i.e. Approriation detail, including description and overall spend for given Approriation ID)


# Cons of OMB
# Only updated annually,  
# Forward looking numbers are only Governors Proposal (not enacted)
# Does not offer some views that the Comptroller offers 

# Presently, we decided to use Comptroller data for the more frequent updates to data, therefor this file is offered only in case one is interested in the detailed data provided by OMB 



############################################# For Reference: File Sources  #####################################################
## 2017:http://www.illinois.gov/gov/budget/Pages/default.aspx
## 2014 to 2016: http://www.illinois.gov/gov/budget/Pages/BudgetBooks.aspx
 # (See documents labled "Operating Budget Detail")


############################################# Beg Importing local CSV files   #####################################################

# Define location of local files 
# Note files are downloaded from web and stored locally
Enacted_Budget_2014 = r"..\\data\budgets\FY14EnactedTotalBudgetbyLineItem_JL_edited_Appr_ID.csv"
Enacted_Budget_2015 = r"..\data\budgets\Enacted_FY15_Budget_by_Line_Item.csv"
Enacted_Budget_2016 = r"..\data\budgets\FY2017BudgetbyLineItemDetail_2_entries_removed.csv"
## Note - THe 2016 data is pulled from a 2017 file as the 2016 "estimated expenditure" is likely more accurate (there was no enacted budget in 2016)
## Note 2 - See note under  2017
Enacted_Budget_2017 = r"..\data\budgets\FY2017BudgetbyLineItemDetail_2_entries_removed.csv"
# Note - In 2017 file  Two entries were left blank in the original source file, they weree causing errors (i.e. Nans), as such they were removed: 
	# a)  420-70-0555-49000000
	# b)  420-91-0611-44000026


# Read files
##Note = 'thousands' ensures the columns with numbers don't get converted to strings
##Note2 = not exactly sure why "encoding='latin-1" is needed but it works with it and threw and error without it :see post: http://stackoverflow.com/questions/5552555/unicodedecodeerror-invalid-continuation-byte

df_2014 = pd.read_csv(Enacted_Budget_2014, header = 0,thousands=',', 		
			dtype = {'Approp Code': str, 'Agency ID': str, \
			'Agency Name': str, ' Organization ID': str, 'Organization Name': str, 'Fund ID': str, \
			'Fund Name': str, ' FY14 Enacted ': np.longdouble, 'Capital Line?': str}, encoding='latin-1') 

df_2015 = pd.read_csv(Enacted_Budget_2015, header = 0,thousands=',', dtype = {'Approp Code': str, 'Agency ID': str, \
			'Agency Name':str,' Organization ID': str, 'Organization Name': str, 'Fund ID': str, 'Fund Name':str, \
			'Appropriation Line Item': str, 'Appropriation Type':str, 'Fund Category': str,'Capital Line?':str, \
			' FY15 Enacted ': np.longdouble},encoding='latin-1') 

df_2016 = pd.read_csv(Enacted_Budget_2016, header = 0,thousands=',', dtype = {'Approp Code': str, 'Agency ID': str, \
			'Agency Name': str,'Div ID': str,'Division Name': str, 'Appropriation Name': str, 'Appropriation ID': str, 'Fund Name': str, \
			'Fund ID': str,'Fund Category Name': str, 'Appropriation Type': str, 'Capital Line': str, \
			' FY15 Enacted Approp ': np.longdouble, ' FY15 Actual Expenditure ': np.longdouble, \
			' FY16 Enacted Approp ':np.longdouble,' FY16 Estimated Maintenance ':np.longdouble, \
			' FY16 Estimated Expend ':np.longdouble, ' FY17 Governors Proposed ': np.longdouble},encoding='latin-1')

df_2017 = pd.read_csv(Enacted_Budget_2017, header = 0,thousands=',', dtype = {'Approp Code': str, 'Agency ID': str, \
			'Agency Name': str,'Div ID': str,'Division Name': str, 'Appropriation Name': str, 'Appropriation ID': str, 'Fund Name': str, \
			'Fund ID': str,'Fund Category Name': str, 'Appropriation Type': str, 'Capital Line': str, \
			' FY15 Enacted Approp ': np.longdouble, ' FY15 Actual Expenditure ': np.longdouble, \
			' FY16 Enacted Approp ':np.longdouble,' FY16 Estimated Maintenance ':np.longdouble, \
			' FY16 Estimated Expend ':np.longdouble, ' FY17 Governors Proposed ': np.longdouble},encoding='latin-1')

############################################# End -Importing local CSV files   #####################################################


#########################################################  Beg - Rename Columns  ####################################################################

# # Rename Column Names where needed for consistency across dataframes
df_2014.rename(index=str,columns={'Approp Code':'Appropriation_Code','Agency ID':'Agency_ID',"Agency Name":"Agency_Name",\
		" Organization ID":"Division_ID","Organization Name":"Division_Name",'Fund ID':'Fund_ID','Fund Name':'Fund_Name',\
		"Line Item Appropriation":"Appropriation_Name",'Appropriation Type':'Appropriation_Type','Fund Category':'Fund_Category_Name',\
		" FY14 Enacted ":"Amount","Capital Line?":"Capital_Line"},inplace=True)
df_2015.rename(index=str,columns={'Approp Code':'Appropriation_Code','Agency ID':'Agency_ID',"Agency Name":"Agency_Name",
		"Organization ID":"Division_ID","Organization Name":"Division_Name",'Fund ID':'Fund_ID','Fund Name':'Fund_Name',\
		"Appropriation Line Item":"Appropriation_Name",'Appropriation Type':'Appropriation_Type','Fund Category':'Fund_Category_Name',\
		" FY15 Enacted ":"Amount","Capital Line?":"Capital_Line"},inplace=True)
df_2016.rename(index=str,columns={'Approp Code':'Appropriation_Code','Agency ID':'Agency_ID',"Agency Name":"Agency_Name",\
		'Div ID':'Division_ID','Division Name':'Division_Name','Appropriation Name':'Appropriation_Name',\
		'Appropriation ID':'Appropriation_ID','Fund Name':'Fund_Name','Fund ID':'Fund_ID','Fund Category Name':'Fund_Category_Name',\
		'Appropriation Type':'Appropriation_Type','Capital Line':'Capital_Line', " FY15 Enacted Approp ": "FY15_Enacted_Approp", \
		' FY15 Actual Expenditure ': 'FY15_Actual_Expenditure', ' FY16 Enacted Approp ': 'FY16_Enacted_Approp', \
		' FY16 Estimated Maintenance ':'FY16_Estimated_Maintenance', ' FY16 Estimated Expend ': 'Amount',\
		" FY17 Governors Proposed ":"FY17_Governors_Proposed"},inplace=True)
df_2017.rename(index=str,columns={'Approp Code':'Appropriation_Code','Agency ID':'Agency_ID',"Agency Name":"Agency_Name",\
		'Div ID':'Division_ID','Division Name':'Division_Name','Appropriation Name':'Appropriation_Name',\
		'Appropriation ID':'Appropriation_ID','Fund Name':'Fund_Name','Fund ID':'Fund_ID','Fund Category Name':'Fund_Category_Name',\
		'Appropriation Type':'Appropriation_Type','Capital Line':'Capital_Line', " FY15 Enacted Approp ": "FY15_Enacted_Approp", \
		' FY15 Actual Expenditure ': 'FY15_Actual_Expenditure', ' FY16 Enacted Approp ': 'FY16_Enacted_Approp', \
		' FY16 Estimated Maintenance ':'FY16_Estimated_Maintenance', ' FY16 Estimated Expend ': 'FY16_Estimated_Expend',\
		" FY17 Governors Proposed ":"Amount"},inplace=True)



# # Version 2 - Work in Progress - Not working yet but does read and rename at same time 

# df_2014 = pd.read_csv(Enacted_Budget_2014, header = 0,thousands=',', 
# 			names = ['Appropriation_Code','Agency_ID',"Agency_Name","Division_ID","Division_Name", \
# 			'Fund_ID','Fund_Name', "Appropriation_Name",'Appropriation_Type','Fund_Category_Name',"Amount","Capital_Line"],   \
# 			dtype = {'Appropriation_Code': str, 'Agency_ID': str, 'Agency_Name': str, \
# 			"Division_ID": str, 'Division_Name': str, 'Fund_ID': str, \
# 			'Fund_Name': str, "Appropriation_Name":str,'Appropriation_Type':str,'Fund_Category_Name':str, \
# 			'Amount': np.longdouble, 'Capital_Line': str}, \
# 			encoding='latin-1') 

# df_2015 = pd.read_csv(Enacted_Budget_2015, header = 0,thousands=',', \
# 			names = ['Appropriation_Code','Agency_ID',"Agency_Name","Division_ID","Division_Name", \
# 			'Fund_ID','Fund_Name',"Appropriation_Name",'Appropriation_Type','Fund_Category_Name',"Amount","Capital_Line"], \
# 			dtype = {'Appropriation_Code':str,'Agency_ID':str,"Agency_Name":str,\
# 			"Division_ID":str,"Division_Name":str, 'Fund_ID':str,\
# 			'Fund_Name':str,"Appropriation_Name":str,'Appropriation_Type':str,'Fund_Category_Name':str,\
# 			'Amount':np.longdouble,"Capital_Line":str}, \
# 			encoding='latin-1') 


#########################################################  End - Rename Columns  ####################################################################


#########################################################  Beg - Create a new field that combines Agency ID & Division ID  ####################################################################

# Create a Unique Identifier for Divison 
# Before this function, a particular Division_ID (for example 10) would exists in multiple agencies, but this mis-represents that data)
# To fix, we add Agency_ID & Division_ID together to get Agency-Divsision_ID 

def f(x):
	return str(x['Agency_ID'])+'_'+str(x['Division_ID'])

df_2014["Agency_and_Division_ID"] = df_2014.apply(f, axis =1)
df_2015["Agency_and_Division_ID"] = df_2015.apply(f, axis =1)
df_2016["Agency_and_Division_ID"] = df_2016.apply(f, axis =1)
df_2017["Agency_and_Division_ID"] = df_2017.apply(f, axis =1)

#########################################################  End - Create a new field that combines Agency ID & Division ID  ####################################################################


###########################################################  Beg - Connect "For Results to data" ###############################################################################################


results_outcomes_2015_file = r"..\\data\results\FY2015BudgetForResultsData.csv"
results_outcomes_2016_file = r"..\\data\results\FY2016BudgetForResults.csv"
results_outcomes_2017_file = r"..\\data\results\FY2017OperatingBudgetingforResultsDetail.csv"

######################### Read Files
# Note - before downloading make sure to manually change '-' to 0s!!

results_outcomes_2015 = pd.read_csv(results_outcomes_2015_file, header = 0,thousands=',', \
			names = ['Result_Name','Outcome_Name','Agency_Name', 'Division_Name', 'Fund_Name', 'Appropriation_Name', \
			'Appropriation_Code', 'Program_Name', 'FY13_Approp', 'FY13_Expend', 'FY14_Approp', \
			'FY14_Estimated', 'FY15_Proposed', 'FY15_Not_Recommneded', 'FY13_Approp_GF', \
			'FY13_Approp_OF', 'FY13_Approp_FF', 'FY13_Expend_GF','FY13_Expend_OF', 'FY13_Expend_FF', \
			'FY14_Approp_GF', 'FY14_Approp_OF', 'FY14_Approp_FF', 'FY14_Estimated_GF', 'FY14_Estimated_OF',\
			'FY14_Estimated_FF', 'FY15_Proposed_GF', 'FY15_Proposed_OF', 'FY15_Proposed_FF', \
			'FY15_Not_Recommended_GF', 'FY15_Not_Recommended_OF', 'FY15_Not_Recommended_FF'],
			dtype = {'Result_Name': str,'Outcome_Name':str,'Agency_Name':str, 'Division_Name':str, 'Fund_Name':str, \
			'Appropriation_Name':str, 'Appropriation_Code':str, 'Program_Name':str, \
			'FY13_Approp':str, 'FY13_Expend':np.longdouble, 'FY14_Approp':np.longdouble, 'FY14_Estimated':np.longdouble, \
			'FY15_Proposed':np.longdouble, 'FY15_Not_Recommneded':np.longdouble, 'FY13_Approp_GF':np.longdouble, \
			'FY13_Approp_OF':np.longdouble , 'FY13_Approp_FF':np.longdouble, 'FY13_Expend_GF':np.longdouble,\
			'FY13_Expend_OF':np.longdouble, 'FY13_Expend_FF':np.longdouble, 'FY14_Approp_GF':np.longdouble, \
			'FY14_Approp_OF': np.longdouble, 'FY14_Approp_FF':np.longdouble, 'FY14_Estimated_GF':np.longdouble, \
			'FY14_Estimated_OF':np.longdouble, 'FY14_Estimated_FF':np.longdouble, 'FY15_Proposed_GF':np.longdouble,\
			'FY15_Proposed_OF':np.longdouble, 'FY15_Proposed_FF':np.longdouble, 'FY15_Not_Recommended_GF':np.longdouble, \
			'FY15_Not_Recommended_OF':np.longdouble, 'FY15_Not_Recommended_FF':np.longdouble}, \
			encoding='latin-1')


results_outcomes_2016 = pd.read_csv(results_outcomes_2016_file, header=0, thousands= ",", \
			names = ['Result_Name','Outcome_Name','Agency_Name', 'Division_Name', 'Fund_Name', 'Appropriation_Name', \
			'Appropriation_Code', 'Program_Name',  \
			'FY14_Approp', 'FY14_Expend', 'FY15_Approp ', 'FY15_Estimated', 'FY16_Proposed ', 'FY14_Approp_GF ', \
			'FY14_Approp_OF', 'FY14_Approp_FF ', 'FY14_Expend_GF ', 'FY14_Expend_OF', 'FY14_Expend_FF ', \
			'FY15_Approp_GF ', 'FY15_Approp_OF', 'FY15_Approp_FF ', 'FY15_Estimated_GF ', 'FY15_Estimated_OF',\
			'FY15_Estimated_FF ', 'FY16 Proposed_GF ', 'FY16_Proposed_OF ', 'FY16_Proposed_FF'], \
			dtype = {'Result_Name': str,'Outcome_Name':str,'Agency_Name':str, 'Division Name':str, 'Fund Name':str, \
			'Appropriation Name':str, 'Appropriation_Code':str, 'Program Name':str, \
			'FY14_Approp':np.longdouble, 'FY14_Expend':np.longdouble, 'FY15_Approp':np.longdouble, 'FY15_Estimated':np.longdouble, \
			'FY16_Proposed':np.longdouble, 'FY14_Approp_GF':np.longdouble, 'FY14_Approp_OF':np.longdouble, \
			'FY14_Approp_FF':np.longdouble , 'FY14_Expend_GF':np.longdouble, 'FY14_Expend_OF':np.longdouble,\
			'FY14_Expend_FF':np.longdouble, 'FY15_Approp_GF':np.longdouble, 'FY15_Approp_OF':np.longdouble, \
			'FY15_Approp_FF':np.longdouble , 'FY15_Estimated_GF':np.longdouble, 'FY15_Estimated_OF':np.longdouble,\
			'FY15_Estimated_FF':np.longdouble, 'FY16_Proposed_GF':np.longdouble, 'FY16_Proposed_OF':np.longdouble, \
			'FY16_Proposed_FF':np.longdouble}, \
			encoding='latin-1')

# Note - had to repair line 9462 & 9461 in 2017 result document document (downloaded from web) used educated guess  

results_outcomes_2017 = pd.read_csv(results_outcomes_2017_file, header = 0,thousands=',', \
			names = ['Result_Name','Outcome_Name','Agency_Name', 'Division_Name','Fund_Name',\
			'Appropriation_Name', 'Appropriation_Code', 'Program_Name', 'FY15_Approp', 'FY15_Expend', 'FY16_Approp', \
			'FY16_Maintenance', 'FY16_Estimated ', 'FY17 Proposed ', 'FY15_Approp_GF', 'FY15_Approp_OF', \
			'FY15_Approp_FF', 'FY15_Expend_GF', 'FY15_Expend_OF', 'FY15_Expend_FF', 'FY16_Approp_GF', \
			'FY16_Approp_OF', 'FY16_Approp_FF', 'FY16_Maintenance_GF', 'FY16_Maintenance_OF', 'FY16_Maintenance_FF', \
			'FY16_Estimated_GF ', 'FY16_Estimated_OF', 'FY16_Estimated_FF', 'FY17_Proposed_GF ', 'FY17_Proposed_OF', \
			' FY17_Proposed_FF'],\
			dtype = {'Result_Name': str,'Outcome_Name':str,'Agency_Name':str, 'Division_Name':str, \
			'Fund_Name':str, 'Appropriation_Name':str, 'Appropriation_Code':str, 'Program_Name':str,  \
			'FY15_Approp':np.longdouble, 'FY15_Expend':np.longdouble, 'FY16_Approp':np.longdouble, \
			'FY16_Maintenance':np.longdouble, 'FY16_Estimated ':np.longdouble, 'FY17 Proposed ':np.longdouble, \
			'FY15_Approp_GF':np.longdouble, 'FY15_Approp_OF':np.longdouble, 'FY15_Approp_FF':np.longdouble, \
			'FY15_Expend_GF':np.longdouble, 'FY15_Expend_OF':np.longdouble, 'FY15_Expend_FF':np.longdouble, \
			'FY16_Approp_GF':np.longdouble, 'FY16_Approp_OF':np.longdouble, 'FY16_Approp_FF':np.longdouble, \
			'FY16_Maintenance_GF':np.longdouble, 'FY16_Maintenance_OF':np.longdouble, 'FY16_Maintenance_FF':np.longdouble, \
			'FY16_Estimated_GF ':np.longdouble, 'FY16_Estimated_OF':np.longdouble, 'FY16_Estimated_FF':np.longdouble, \
			'FY17_Proposed_GF ':np.longdouble, 'FY17_Proposed_OF':np.longdouble, ' FY17_Proposed_FF':np.longdouble},\
			encoding='latin-1')



####################### Reduce the amount of text used to populate the Results_Name & Outcome_Name Field  


# Table for looking the Outcome_Name  # This was used to reduce the volume of data in the master_data.json file 
# Table reads as follows: {OutcomeID:  [Results_Name, Outcome_name] }

results_and_outcome_table = { 1: ['Enhanced Economic Well-Being of Residents and Communities','Increase Employment and Attract, Retain and Grow Businesses'],
	2: ['Improve Quality of Natural, Cultural, and Environmental Resources','Strengthen Cultural and Environmental Vitality'],
	3: ['Improved Access to and Cost Effectiveness of Healthcare','Improve Overall Health of Illinoisans'],
	4: ['Improved Efficiency and Stability of State Government','Support Basic Functions of Government'],
	5: ["Protection of Residents' Lives and Property",'Create Safer Communities'],
	6: ["Protection of Residents' Lives and Property",'Improve Infrastructure'],
	7: ["Protection of the Most Vulnerable of our Residents",'Increase Individual and Family Stability and Self-Sufficiency'],
	8: ["Protection of the Most Vulnerable of our Residents",'Meet the Needs of the Most Vulnerable'],
	9: ['Quality Education and Opportunities for Growth and Learning for all Illinois Students','Improve School Readiness and Student Success for All']
	}

# Create a function that replaced the text with Code:

def create_outcome_id(row):
	if row['Outcome_Name'] == "Increase Employment and Attract, Retain and Grow Businesses":
		return 1
	if row['Outcome_Name'] == "Strengthen Cultural and Environmental Vitality":
		return 2
	if row['Outcome_Name'] == "Improve Overall Health of Illinoisans":
		return 3
	if row['Outcome_Name'] == "Support Basic Functions of Government":
		return 4
	if row['Outcome_Name'] == "Create Safer Communities":
		return 5
	if row['Outcome_Name'] == "Improve Infrastructure":
		return 6
	if row['Outcome_Name'] == "Increase Individual and Family Stability and Self-Sufficiency":
		return 7
	if row['Outcome_Name'] == "Meet the Needs of the Most Vulnerable":
		return 8
	if row['Outcome_Name'] == "Improve School Readiness and Student Success for All":
		return 9
	else:
		return 'unknown'

## Run the code to replace the Outcome TExt with an ID:
results_outcomes_2015['Outcome_ID'] = results_outcomes_2015.apply (lambda row: create_outcome_id(row),axis=1)
results_outcomes_2016['Outcome_ID'] = results_outcomes_2016.apply (lambda row: create_outcome_id(row),axis=1)
results_outcomes_2017['Outcome_ID'] = results_outcomes_2017.apply (lambda row: create_outcome_id(row),axis=1)


# print results_outcomes_2015.head()

######################## Trim the Dataframe down to just the columns 1) Appropriation_Code count = 6 and 2) Outcome_ID = last column (drop the rest) also including Program name (count 7)
results_outcomes_trim_2015 = results_outcomes_2015.drop(results_outcomes_2015. \
	columns[[0,1,2,3,4,5,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]], axis=1) # Note: zero indexed  Choosing to keep all data for now
results_outcomes_trim_2016 = results_outcomes_2016.drop(results_outcomes_2016. \
	columns[[0,1,2,3,4,5,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]], axis=1) # Note: zero indexed  Choosing to keep all data for now
results_outcomes_trim_2017 = results_outcomes_2017.drop(results_outcomes_2017. \
	columns[[0,1,2,3,4,5,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]], axis=1) # Note: zero indexed  Choosing to keep all data for now



######################## Need to fix the Appro_Code in results to match the structure of  AppropCode in Budget docs

def fix_approp_code_order(df_to_repair):
	
	df_to_repair['First_Part'] = df_to_repair['Appropriation_Code'].str[5:8]
	df_to_repair['Second_Part'] = df_to_repair['Appropriation_Code'].str[8:10]
	df_to_repair['Third_Part'] = df_to_repair['Appropriation_Code'].str[:4]
	df_to_repair['Fourth_Part'] = df_to_repair['Appropriation_Code'].str[-8:]
	df_to_repair['New_Appropriation_Code'] = df_to_repair['First_Part']+"-"+df_to_repair['Second_Part']+"-"+df_to_repair['Third_Part']+"-"+df_to_repair['Fourth_Part']
	df_to_repair.drop(df_to_repair.columns[[3,4,5,6,7]],axis=1,inplace=True) # Note: zero indexed  Choosing to keep all data for now
	df_to_repair.rename(index=str,columns={'New_Appropriation_Code':'Appropriation_Code'},inplace=True)
	return df_to_repair


######################## Run the  Function to fix the order of Approp code 
results_outcomes_trim_2015 = fix_approp_code_order(results_outcomes_trim_2015)
results_outcomes_trim_2016 = fix_approp_code_order(results_outcomes_trim_2016)
results_outcomes_trim_2017 = fix_approp_code_order(results_outcomes_trim_2017)


######################## Merge the Results data into the new dataframe 

df_2015 = pd.merge(df_2015, results_outcomes_trim_2015, how = 'outer', on= 'Appropriation_Code')
df_2016 = pd.merge(df_2016, results_outcomes_trim_2016, how = 'outer', on= 'Appropriation_Code')
df_2017 = pd.merge(df_2017, results_outcomes_trim_2017, how = 'outer', on= 'Appropriation_Code')


###########################################################  End - Connect "For Results to data" ##############################################################################


########################################################### Beg - Connect "Performance Metrics" data ##########################################################################



############# Store the location of files
performance_2015_file = r"..\\data\\performance_measures\FY2015PerformanceMeasuresData_cleaned.csv"
performance_2016_file = r"..\\data\\performance_measures\FY2016PerformanceMeasuresData_cleaned.csv"
performance_2017_file = r"..\\data\\performance_measures\FY2017OperatingPerformanceMeasuresDetail_cleaned.csv"

################ Manual Cleaning ###################
#Notes - Had to manually clean the files doing following:
# 1) 2017 - Edited 
	#a) Dept of Transportation "Promote/Enforce Highway Safety" (shifted over 2 columns)
	#b) Dept of Transportation "Promote Motorcyclist Safety" (shifted over 2 columns)
	#c) Dept of Transportation "Promote/Enforce Motor Carrier Safety" (shifted over 2 columns)
# 2) Changed "-" to 0s
# 3) Changed "N/A" and "NULL" to blanks

######################### Read Files ########

performance_2015 = pd.read_csv(performance_2015_file, header = 0,thousands=',', \
			names = ['Agency_Name','Metric_Name','FY_2011_Actual','FY_2012_Actual','FY_2013_Actual','FY_2014_Estimated','FY_2015_Projected','Footnote',\
			'Program_Name','Outcome_Name','Result_Name'], \
			dtype = {'Agency_Name': str,'Metric_Name':str,'FY_2011_Actual':float,'FY_2012_Actual':float,'FY_2013_Actual':float,\
			'FY_2014_Estimated':float,'FY_2015_Projected':float,'Footnote':str,'Program_Name':str,'Outcome_Name':str,'Result_Name':str}, \
			encoding='latin-1')


performance_2017 = pd.read_csv(performance_2017_file, header = 0,thousands=',', \
			names = ['Agency_Name','Program_Name','Result_Name','Outcome_Name','Measure_Name','Measure_Footnote', \
			'FY_2013_Actual','FY_2014_Actual','FY_2015_Actual','FY_2016_Estimated','FY_2017_Projected','FY_2013_Footnote', \
			'FY_2014_Footnote','FY_2015_Footnote','FY_2016_Footnote','FY_2017_Footnote'], \
			dtype = {'Agency_Name':str,'Program_Name':str,'Result_Name':str,'Outcome_Name':str,'Measure_Name':str,\
			'Measure_Footnote':str, 'FY_2013_Actual':float,'FY_2014_Actual':float,'FY_2015_Actual':float,\
			'FY_2016_Estimated':float,'FY_2017_Projected':float,'FY_2013_Footnote':str,'FY_2014_Footnote':str,\
			'FY_2015_Footnote':str,'FY_2016_Footnote':str, 'FY_2017_Footnote':str}, \
			encoding='latin-1')



########################################################### End - Connect "Performance Metrics" data ##########################################################################



#########################################################  Beg - Trim the files - Removes unnecessary columns ####################################################################
## Choosing to keep all data for now
df_2014_trim = df_2014.drop(df_2014.columns[[]], axis=1) # Note: zero indexed  Choosing to keep all data for now
df_2015_trim = df_2015.drop(df_2015.columns[[]], axis=1) # Note: zero indexed Choosing to keep all data for now
df_2016_trim = df_2016.drop(df_2016.columns[[6]], axis=1) # Note: zero indexed,hoosing to keep all data for now (except "Fund_Name" which is duplicative by "Fund_Category_Name")
# ## As Such I use ' FY16 Estimated Expend '  [Column Index of 16]
# print df_2017.head()
df_2017_trim = df_2017.drop(df_2017.columns[[6]], axis=1) # Note: zero indexed hoosing to keep all data for now

#########################################################  End - Trim the files - Removes unnecessary columns ####################################################################






######################################   Creating a dicitionary that contains Agency ID & Names and Division ID & Names for refernence   #################################################### 

## Create Agency ID & Agency Name Table 
#Note - Performed in reverse order (2017, 2016, 2015, 20140) so more recent names get priority
# Note - Time intensive operation so only do once per session (comment out otherwise)


# agency_dict = {}
# ## 
# # To iterate through CSVs (computationally intensive so only did once)
# for index, row in df_2017_trim.iterrows():
# 	if row['Agency_ID'] not in agency_dict:
# 		agency_dict[str(row['Agency_ID'])] = str(row['Agency_Name'])
# for index, row in df_2016_trim.iterrows():
# 	if row['Agency_ID'] not in agency_dict:
# 		agency_dict[str(row['Agency_ID'])] = str(row['Agency_Name'])
# for index, row in df_2015_trim.iterrows():
# 	if row['Agency_ID'] not in agency_dict:
# 		agency_dict[str(row['Agency_ID'])] = str(row['Agency_Name'])
# for index, row in df_2014_trim.iterrows():
# 	if row['Agency_ID'] not in agency_dict:
# 		agency_dict[str(row['Agency_ID'])] = str(row['Agency_Name'])

# Manual 


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
    '105': 'Commission On Government Forecasting and Accountability', '904': 'Continuing Appropriations', '644': 'Northern Illinois University', '511': 'Capital Development Board', \
    '510': 'Executive Ethics Commission', '517': 'Civil Service Commission', '458': 'Department Of The Lottery', '579': 'Illinois Racing Board', '578': 'Prisoner Review Board', '452': 'Department Of Labor', \
    '628': 'Western Illinois University', '330': 'Office Of The Lieutenant Governor', '574': 'Metropolitan Pier And Exposition Authority', '589': "State Employees' Retirement System", \
    '509': 'Office Of Executive Inspector General', '546': 'Illinois Criminal Justice Information Authority', '503': 'Illinois Arts Council', '569': 'Illinois Law Enforcement Training Standards Board', '636': \
    'Illinois State University', '560': 'Illinois Finance Authority', '562': 'Procurement Policy Board', '466': 'Department Of Military Affairs', '564': 'Illinois Independent Tax Tribunal', \
    '565': 'Illinois Gaming Board', '507': "Governor's Office Of Management And Budget", '167': 'Joint Committee On Administrative Rules', '427': 'Department Of Employment Security', '275': 'Judges Retirement System', \
    '601': 'Board Of Higher Education', '558': 'Illinois Council On Developmental Disabilities', '156': 'Office Of The Architect Of The Capitol', '554': 'Illinois Sports Facilities Authority', \
    '608': 'Chicago State University', '201': 'Supreme Court', '563': "Workers' Compensation Commission", '612': 'Eastern Illinois University', '616': 'Governors State University', \
    '482': 'Department Of Public Health', '350': 'Office Of The Secretary Of State', '684': 'Illinois Community College Board', '478': 'Department Of Healthcare And Family Services'}


## Iterating over to create division Dictionary
# division_dict = {}

# for index, row in df_2017_trim.iterrows():
# 	if row["Agency_and_Division_ID"] not in division_dict:
# 		division_dict[str(row["Agency_and_Division_ID"])] = row["Division_Name"].encode('utf-8')   #Using this because 524_20 "Chairman and Commissioners\xc2\x92 Office" kept throwing error
# 		#original code read as this: 		# str(row["Division_Name"])
# for index, row in df_2016_trim.iterrows():
# 	if row["Agency_and_Division_ID"] not in division_dict:
# 		division_dict[str(row["Agency_and_Division_ID"])] = row["Division_Name"].encode('utf-8')
# for index, row in df_2015_trim.iterrows():
# 	if row["Agency_and_Division_ID"] not in division_dict:
# 		division_dict[str(row["Agency_and_Division_ID"])] = row["Division_Name"].encode('utf-8')
# for index, row in df_2014_trim.iterrows():
# 	if row["Agency_and_Division_ID"] not in division_dict:
# 		division_dict[str(row["Agency_and_Division_ID"])] = row["Division_Name"].encode('utf-8')


# manual Storage
division_dict = {'524_20': 'Chairman and Commissioners\xc2\x92 Office', '420_31': 'Local Projects', '440_70': 'Professions Indirect Cost', '426_68': 'Graham Correctional Center', \
	'330_1': 'General Office', '112_1': 'Operations', '497_1': 'Central Office', '494_1': 'Central Administration and Planning', '444_41': 'Treatment and Detention Program', \
	'444_40': 'Program Administration-Disabilities And Behavioral Health', '360_99': 'Table I-A Adjustment', '494_70': 'Highway Safety Program - Traffic Safety', '406_32': \
	'Marketing', '492_10': 'Government Services', '560_1': 'General Office', '564_1': 'General Office', '586_33': 'Internal Audit', '422_94': 'State Museum', '101_10': 'Senate Expenses', \
	'586_32': 'Governmental Relations', '406_49': 'DuQuoin Buildings and Grounds', '406_48': 'State Fair/Buildings and Grounds', '458_1': 'General Office', '406_43': 'Weights and Measures', \
	'406_42': 'Medicinal Plants', '406_47': 'Environmental Programs', '406_46': 'Land and Water Resources', '406_45': 'Meat and Poultry Inspection', '406_44': 'Animal Industries', '580_10': 'General Office',\
	 '586_44': 'Early Childhood', '586_46': 'Title IV Grants, Safe and Drug Free Schools', '586_47': 'Title II Grants, Eisenhower Professional Development', '524_40': 'Transportation', \
	 '586_48': 'McKinney Homeless Grants', '587_30': 'General Counsel', '110_1': 'Operations', '420_15': 'General Administration', '478_15': 'Office Of Inspector General', \
	 '201_1': 'Ordinary Operations of the Supreme Court', '402_33': 'Division of Home and Community Services OAF', '482_20': 'Epidemiology And Health System Development', '425_29': 'IYC - Kewanee', \
	 '425_21': 'IYC - Chicago', '425_24': 'IYC - Harrisburg', '494_17': 'Department of Natural Resources', '494_16': 'Highway Safety Program - Illinois Liquor Control Commission', \
	 '494_10': 'Division of Transportation Safety', '494_19': 'Highway Safety Program - Department of Human Services', '494_18': 'Day Labor', '420_43': 'Local Projects', '511_16': \
	 'Governors State University', '420_41': 'Local Projects', '511_12': 'Eastern Illinois University', '420_45': 'Business Development', '420_44': 'Local Projects', '517_1': \
	 'General Office', '440_39': 'Thrift Regulation', '427_59': 'Trust Fund Unit', '444_87': 'Federal Stimulus', '444_80': 'Human Capital Development', '493_73': 'Financial Fraud And Forgery Unit', \
	 '440_89': 'Shared Services', '532_20': 'Laboratory Services', '532_60': 'Bureau of Water', '420_36': 'Local Projects', '452_1': 'General Office', '420_34': 'Local Projects', \
	 '420_35': 'Technology and Industrial Competitiveness', '420_32': 'Local Projects', '420_33': 'Local Projects', '420_30': 'Workforce Development', '425_4': 'School District', \
	 '494_6': 'Department-wide Operations', '494_5': 'Central Offices, Division of Highways', '494_3': 'Bureau of Information Processing', '494_2': 'Permanent Improvements', '420_38': \
	 'Local Projects', '420_39': 'Local Projects', '492_1': 'General Office', '444_30': 'Rehabilitation Services Bureau', '444_31': 'Client Assistance Project', '444_32': \
	 'DRS Program Administrative Support', '511_8': 'Chicago State University', '511_6': 'Agriculture', '511_5': 'Central Management Services', '511_1': 'General Office', \
	 '422_70': 'Office of Oil and Gas Resource Management', '587_70': 'Electronic Data Processing', '478_60': 'Cost Recoveries', '478_65': 'Medical', '586_80': 'Federal Grants', \
	 '524_30': 'Public Utilities', '586_87': 'Federal Stimulus', '628_1': 'General Operations', '494_87': 'Federal Stimulus', '452_10': 'Public Safety', '418_77': 'Inspector General',\
	  '418_76': 'Office of The Guardian', '418_73': 'Budget, Legal and Compliance', '676_20': 'Illinois Fire Services Institute', '418_78': 'Regulation and Quality Control', \
	  '426_88': 'Sheridan Correctional Center', '426_85': 'Shawnee Correctional Center', '426_84': 'Robinson Correctional Center', '426_83': 'Pontiac Correctional Center', \
	  '426_82': 'Pinckneyville Correctional Center', '593_1': 'Retirement', '541_20': 'Preservation Services Division', '586_18': 'Grants D', '620_1': 'General Operations', '586_14': 'Grants C', \
	  '586_13': 'Grants B', '586_12': 'Human Resources', '586_11': 'Special Funds', '586_10': 'Administration - Human Resources', '591_1': 'General Office', '416_10': 'Strategic Sourcing', \
	  '156_1': 'Space Needs', '493_20': 'Bureau Of Information Services', '482_58': 'Public Health Laboratories', '497_30': 'State Approving Agency', '482_50': 'Office Of Health Protection', \
	  '482_51': 'Office Of Health Protection: AIDS', '587_5': 'Administration', '340_50': "Crime Victims' Assistance", '406_5': 'Computer Services', '420_42': 'Local Projects', \
	  '360_10': 'Inspector General', '406_1': 'Administrative Services', '494_28': 'District 8, Collinsville Office', '494_29': 'District 9, Carbondale Office', '494_26': 'District 6, Springfield Office', \
	  '494_27': 'District 7, Effingham Office', '494_24': 'District 4, Peoria Office', '494_25': 'District 5, Paris Office', '494_22': 'District 2, Dixon Office', '494_23': 'District 3, Ottawa Office', \
	  '494_21': 'District 1, Schaumburg Office', '691_1': 'Executive Division Administration', '588_35': 'Nuclear Facility Safety', '440_69': 'Professional Evidence', '440_68': 'Nurse', '440_67': 'Certified Public Accountants', \
	  '511_27': 'Corrections, New Facilities', '440_65': 'Pharmacy', '440_64': 'Design', '511_22': 'Natural Resources', '440_62': 'Medical', '511_20': 'Northeastern Illinois University', \
	  '440_60': 'General Professions', '579_1': 'General Office', '526_1': 'General Office', '444_70': 'Illinois Center for Rehabilitation And Education', '537_1': 'General Office', \
	  '695_1': 'General Office', '420_87': 'Federal Stimulus', '420_80': 'Energy and Recycling', '579_89': 'Shared Services', '350_1': 'Executive Group', '541_50': 'Abraham Lincoln Presidential Library and Museum', \
	  '402_1': 'Direct Senior Services', '418_74': 'Clinical Services', '290_1': 'General Operations', '492_27': 'Tax Operations', '422_81': 'Water Resources Capital', '422_80': 'Water Resources', \
	  '275_1': 'Operations', '542_1': 'General Office', '422_88': "Governor's Discretionary Appropriation", '608_1': 'General Operations', '446_20': 'Insurance Producer Administration', '446_22': 'Insurance Financial Regulation', \
	  '446_25': 'Public Pension', '446_27': "Workers' Compensation Anti-Fraud", '418_38': 'Office of Quality Assurance', '586_27': 'School Construction Maintenance Grants', \
	  '418_30': 'Central Administration', '420_4': 'Local Projects', '586_50': 'Special Education - Administration', '586_57': 'IDEA Preschool Grants', '420_10': 'Local Projects', \
	  '420_11': 'Local Projects', '420_12': 'Local Projects', '546_87': 'Federal Stimulus', '422_30': 'Coastal Management', '420_14': 'Local Projects', '402_22': 'Division of Finance and Administration OAF', \
	  '402_26': 'Senior Health Insurance', '425_39': 'IYC - St. Charles', '210_1': 'General Operations', '420_16': 'Local Projects', '482_15': 'Division Of Information Technology', \
	  '420_17': 'Local Projects', '482_10': 'Finance And Administration', '425_36': 'IYC - Pere Marquette', '426_74': 'Lawrence Correctional Center', '426_75': 'Lincoln Correctional Center', \
	  '426_77': 'Logan Correctional Center', '426_70': 'Hill Correctional Center', '426_71': 'Jacksonville Correctional Center', '546_1': 'Operations', '426_79': 'Menard Correctional Center', \
	  '420_6': 'Local Projects', '420_7': 'Local Projects', '494_60': 'Aeronautics', '420_5': 'Agency wide Operations', '420_2': 'Local Projects', '420_3': 'Local Projects', \
	  '586_20': 'School Support Services for All Schools', '420_1': 'Local Projects', '548_1': 'General Office', '420_8': 'Local Projects', '420_9': 'Local Projects', '426_4': 'Education Services', \
	  '426_1': 'General Office', '588_40': 'Disaster Assistance Preparedness', '426_9': 'Field Services', '511_62': 'Mental Health', '511_61': 'Board Of Higher Education', \
	  '511_66': 'Military Affairs', '511_64': 'Southern Illinois University', '511_69': 'Mathematics And Science Academy', '588_89': 'Shared Services', '528_1': 'Claims Adjudication', \
	  '482_87': 'Federal Stimulus', '427_62': 'Workforce Development', '532_10': 'Bureau of Air', '370_1': 'General Office', '592_1': 'General Office', '493_60': 'Division Of Operations', \
	  '590_1': 'General Office', '440_56': 'Community Association Manager Licensing and Disciplinary', '420_24': 'Local Projects', '440_54': 'Cemetery Oversight Licensing and Disciplinary', \
	  '420_26': 'Local Projects', '420_21': 'Local Projects', '440_53': 'Medical Marijuana', '420_23': 'Local Projects', '420_22': 'Local Projects', '420_29': 'Local Projects', \
	  '420_28': 'Local Projects', '478_58': 'Legal Representation', '478_55': 'Child Support Services', '444_26': 'Addiction Treatment', '444_24': 'DD Grants-in-aid and Purchase of Care', \
	  '444_23': 'Office of The Inspector General', '444_22': 'Mental Health Grants and Administration', '444_21': 'Home Services Program', '444_20': 'Bureau of Disability Determination Services',\
	   '587_60': 'Campaign Financing', '422_60': 'Mines and Minerals', '458_89': 'Shared Services', '692_1': 'General Office', '440_1': 'Financial Institutions', '440_3': 'Credit Union', \
	   '440_8': 'Transmitters of Money Act', '578_1': 'General Office', '442_1': 'Administration', '601_1': 'General Office', '418_40': 'Child Welfare', '574_1': 'General Office', \
	   '452_20': 'Fair Labor Standards', '558_1': 'General Office', '563_10': 'Electronic Data Processing', '541_5': 'Executive Office', '492_88': "Governor's Lump Sum", '492_89': 'Shared Services', \
	   '586_68': 'Educational Investments', '586_69': 'Career & Technical Education Grants', '586_63': 'IDEA Improvement Grants', '586_60': 'Teaching and Learning Services for All Children', \
	   '586_66': 'Deaf-Blind Grants', '586_64': 'Student Assessment', '554_1': 'General Office', '494_80': 'Division of Public and Intermodal Transportation', '494_81': 'Rail Passenger and Rail Freight',\
	    '444_1': 'Direct Support to Individuals', '425_47': 'IYC - Warrenville', '565_89': 'Shared Services', '497_23': "Illinois Veterans' Home At LaSalle", '497_20': "Illinois Veterans' Home At Quincy", \
	    '497_25': "Illinois Veterans' Home At Manteno", '442_10': 'Charge Processing', '466_1': 'Office of the Adjutant General', '340_20': 'Enforcement', '340_25': 'Asbestos Litigation', \
	    '360_20': "State Officers' Salaries And Other Expenditures", '109_1': 'General Office', '494_32': 'Highway Safety Program - Illinois States Attorney Appellate Prosecutors', \
	    '511_38': 'Office Of The Attorney General', '511_35': 'Secretary Of State', '511_36': 'Illinois State University', '420_65': 'Illinois Trade Office', \
	    '444_60': 'Community and Residential Services for Blind And Visually Impaired', '525_1': 'General Office', '416_20': 'Benefits', '541_40': 'Historic Sites Division', '406_10': 'Agriculture Regulation',\
	     '446_89': 'Shared Services', '285_1': 'General Office', '101_30': 'Joint Committees', '529_1': 'General Office', '511_82': 'Public Health', '511_84': 'Illinois Community College Board',\
	      '511_86': 'State Board Of Education', '444_16': 'Management Information Services', '444_17': 'DHS Operations', '444_15': 'Administrative and Program Support', '585_1': 'General Office', \
	      '482_40': 'Office Of Health Care Regulation', '416_89': 'Shared Services', '422_50': 'Land Management', '420_37': 'Local Projects', '588_15': 'Operations', '587_10': 'Elections Operations', \
	      '360_12': 'Statewide Fiscal Operations', '904_1': 'Initiative', '440_35': 'Medical Cannabis', '492_35': 'Liquor Control Commission General Office', '422_20': 'Resource Conservation', \
	      '482_1': "Director's Office", '509_1': 'Operations', '426_63': 'East Moline Correctional Center', '588_20': 'Radiation Safety', '426_65': 'Southwestern Illinois Correctional Center', \
	      '360_65': 'Court Reporting Services', '426_69': 'Illinois River Correctional Center', '503_1': 'General Office', '350_10': 'General Administrative Group', '420_25': 'Tourism', \
	      '586_37': 'Advanced Placement Grants', '494_72': 'Highway Safety Program - Secretary of State', '494_75': 'Highway Safety Program - Department of State Police', '494_74': 'Highway Safety Program - Department of Public Health', \
	      '494_77': 'Highway Safety Program - Law Enforcement Training Standards Board', '440_57': 'Athletics', '494_79': 'Highway Safety Program - Administrative Office of the Illinois Courts', \
	      '420_27': 'Local Projects', '420_20': 'Local Projects', '511_71': 'Medical District Commission', '511_76': 'University Of Illinois', '511_24': 'Juvenile Justice', '482_70': 'Office of Public Health Preparedness',\
	       '497_18': "Illinois Veterans' Home At Anna", '507_1': 'General Office', '497_15': "Veterans' Field Services", '644_1': 'General Operations', '636_1': 'General Operations', \
	       '540_50': 'Abraham Lincoln Presidential Library and Museum', '295_1': 'General Office', '440_45': 'Real Estate Research and Education', '440_44': 'Appraisal Administration', \
	       '440_47': 'Home Inspector Administration', '420_13': 'Local Projects', '440_41': 'Pawnbrokers Regulation', '440_40': 'Bank and Trust Company', '440_43': 'Real Estate License Administration', \
	       '440_42': 'Savings and Residential Finance', '420_18': 'Local Projects', '420_19': 'Local Projects', '445_1': 'General Office', '440_48': 'Real Estate Audit', '108_1': 'General Office', \
	       '532_70': 'Pollution Control Board', '444_50': 'Illinois School for the Deaf', '444_51': 'Illinois School for the Visually Impaired', '416_55': 'Communications and Computer Services', \
	       '422_18': 'Office of Grant Management and Assistance', '511_28': 'Western Illinois University', '103_1': 'General Office', '422_12': 'Office of Realty and Capital Planning', \
	       '422_13': 'Real Estate and Environmental Planning', '422_10': 'General Office', '422_11': 'Capital', '422_16': 'Sparta World Shooting and Recreational Complex', '422_14': 'Strategic Services', \
	       '511_26': 'Corrections, Upgrade Facilities', '105_1': 'General Office', '440_66': 'Podiatry', '420_70': 'Office of Energy Assistance', '466_15': 'Facilities Operations', '511_25': 'Corrections', \
	       '120_1': 'General Office', '290_20': 'Illinois Criminal Justice Information Grants', '440_63': 'Optometric', '440_61': 'Dental', '420_75': 'Community Development', '587_3': 'The Board', \
	       '406_52': 'DuQuoin State Fair', '406_53': 'County Fairs and Horseracing', '589_5': 'Social Security Division', '350_51': 'Motor Vehicle Group', '589_1': 'Central Office', '418_50': 'Child Protection', \
	       '416_1': 'Administrative Operations', '416_5': 'Information Services', '691_31': 'Student Grant Programs', '563_1': 'General Office', '478_5': 'Program Administration', '586_76': 'State Charter School Commission', \
	       '693_1': 'Retirement', '482_30': 'Office Of Health Promotion', '586_75': 'Community Residential Services Authority', '494_90': 'Motor Fuel Tax Administration and Grants', '426_58': 'Dixon Correctional Center',\
	        '588_45': 'Environmental Safety', '426_52': 'Big Muddy River Correctional Center', '426_56': 'Danville Correctional Center', '426_57': 'Decatur Correctional Center', '426_54': 'Centralia Correctional Center', \
	        '511_44': 'Northern Illinois University', '569_1': 'General Office', '420_55': 'Illinois Film Office', '416_45': 'Bureau of Agency Services', '420_50': 'Coal Development and Marketing', '416_40': 'Property Management', \
	        '612_1': 'General Operations', '511_41': 'Historic Preservation', '511_43': 'Human Services', '616_1': 'General Operations', '684_1': 'Central Office', '565_1': 'General Office', \
	        '167_1': 'General Operations', '416_30': 'Personnel', '416_35': 'Business Enterprise Program', '676_1': 'General Operations', '532_30': 'Bureau of Land', '101_20': 'House Expenses', \
	        '340_1': 'General Office', '310_1': 'Executive Office', '511_97': "Veterans' Affairs", '511_95': 'Supreme Court', '511_93': 'Department Of State Police', '511_92': 'Revenue', '532_1': 'Administration', \
	        '422_40': 'Law Enforcement', '360_5': 'Merit Commission', '360_1': 'Administration', '426_98': 'Correctional Industries', '426_96': 'Vienna Correctional Center', '426_97': 'Western Illinois Correctional Center', \
	        '426_94': 'Vandalia Correctional Center', '426_92': 'Stateville Correctional Center', '426_93': 'Taylorville Correctional Center', '494_44': 'Construction, Bond Fund A', '494_46': 'Grade Crossing Protection', \
	        '494_42': 'Construction (Grants)', '131_1': 'General Office', '586_5': 'Fiscal Support Services', '418_17': 'Regional Offices', '586_1': 'General Office', '420_98': 'Local Projects', '420_99': 'Local Projects', \
	        '115_1': 'General Office', '664_1': 'General Operations', '420_90': 'Historic Preservation', '420_91': 'Infrastructure Investments', '420_92': 'Local Projects', '420_93': 'Local Projects', '420_94': 'Local Projects', \
	        '420_95': 'Local Projects', '420_96': 'Local Projects', '420_97': 'Local Projects', '562_1': 'General Office', '493_2': 'Division Of Administration', '588_5': 'Management and Administrative Support',\
	         '482_60': "Office Of Women's Health", '592_89': 'Shared Services', '510_1': 'General Office', '541_30': 'Building and Grounds Maintenance Services', '425_1': 'General Office', '493_88': "Governor's Lump Sum",\
	          '493_85': 'Division Of Internal Investigation', '493_80': 'Division Of Forensic Services And Identification', '425_6': 'Aftercare Services'}
## 

######################################   End - Creating a dicitionary that contains Agency ID & Names and Division ID & Names for refernence   #################################################### 


####################################### Establish Querying Functions useful for more complex functions later ###############################################################################################


############  Finding Agency ID (or Division ID) when you have a Name [BOTH Agency and Division] 

def find_id(dict_to_look_thru, name_to_find):
	result = []
	for k in dict_to_look_thru:
		# print dict_to_look_thru[k]
		if dict_to_look_thru[k] == name_to_find:
			result.append(k)
		else:
			pass
	return result

## Examples
# print find_id(agency_dict, 'Continuing Appropriations' )
# print find_id(division_dict, 'Public Safety' )


############ Finding Agency Name (No Function needed just direct query a dictionary 
## Example:
# print agency_dict['103']



############  Finding Division Name when you have a Agency ID and Division ID (ONLY applicable for Divisions)
# Option A
def get_division_name(dict_to_look_thru, agency_ID, division_ID):
	text_full = agency_ID+"_"+division_ID
	return dict_to_look_thru[text_full] 
## Example:
# text1 = '103'
# text2 = '1'
# print get_division_name(division_dict, text1, text2)

# Option B - Direct query of dictionary 
#print division_dict['103_1']



####################################### Establish Querying Functions useful for more complex functions later ###############################################################################################




######################################################  Beg - Create Dataframe Groupings ####################################

##By AppropIDs
###skipped for AppropID, just use file named. df_2014_trim,...etc

##By Agency
## For Exporting (Arbitrary index) - Not sure but works if I keep both
df_2014_by_agency_temp = df_2014_trim.groupby("Agency_ID", as_index = False )
df_2015_by_agency_temp = df_2015_trim.groupby("Agency_ID", as_index = False )
df_2016_by_agency_temp = df_2016_trim.groupby("Agency_ID", as_index = False )
df_2017_by_agency_temp = df_2017_trim.groupby("Agency_ID", as_index = False )
df_2014_by_agency = df_2014_by_agency_temp.aggregate(np.sum)
df_2015_by_agency = df_2015_by_agency_temp.aggregate(np.sum)
df_2016_by_agency = df_2016_by_agency_temp.aggregate(np.sum)
df_2017_by_agency = df_2017_by_agency_temp.aggregate(np.sum)

### For INternal Calculations (Index = Agency_ID) - Not sure but works if I keep both
# df_2014_by_agency_temp_calcs = df_2014_trim.groupby("Agency_ID")
# df_2015_by_agency_temp_calcs = df_2015_trim.groupby("Agency_ID")
# df_2016_by_agency_temp_calcs = df_2016_trim.groupby("Agency_ID")
# df_2017_by_agency_temp_calcs = df_2017_trim.groupby("Agency_ID")
# df_2014_by_agency_calcs = df_2014_by_agency_temp_calcs.aggregate(np.sum)
# df_2015_by_agency_calcs = df_2015_by_agency_temp_calcs.aggregate(np.sum)
# df_2016_by_agency_calcs = df_2016_by_agency_temp_calcs.aggregate(np.sum)
# df_2017_by_agency_calcs = df_2017_by_agency_temp_calcs.aggregate(np.sum)

# ##By Div

df_2014_by_div_temp = df_2014_trim.groupby("Agency_and_Division_ID", as_index = False )
df_2015_by_div_temp = df_2015_trim.groupby("Agency_and_Division_ID", as_index = False )
df_2016_by_div_temp = df_2016_trim.groupby("Agency_and_Division_ID", as_index = False )
df_2017_by_div_temp = df_2017_trim.groupby("Agency_and_Division_ID", as_index = False )
df_2014_by_div = df_2014_by_div_temp.aggregate(np.sum)
df_2015_by_div = df_2015_by_div_temp.aggregate(np.sum)
df_2016_by_div = df_2016_by_div_temp.aggregate(np.sum)
df_2017_by_div = df_2017_by_div_temp.aggregate(np.sum)


# ####################################################  End - Create Dataframe  Groupings ####################################

# ####################################################  Beg - Convert dataframes to dictionaries ####################################

# # #
# ##By AppropID
dict_2014_by_appropID = df_2014_trim.to_dict(orient ='records')
dict_2015_by_appropID = df_2015_trim.to_dict(orient ='records')
dict_2016_by_appropID = df_2016_trim.to_dict(orient ='records')
dict_2017_by_appropID = df_2017_trim.to_dict(orient ='records')


##By Agency
dict_2014_by_agency = df_2014_by_agency.to_dict(orient ='records')
dict_2015_by_agency = df_2015_by_agency.to_dict(orient ='records')
dict_2016_by_agency = df_2016_by_agency.to_dict(orient ='records')
dict_2017_by_agency = df_2017_by_agency.to_dict(orient ='records')


##By Division
dict_2014_by_div = df_2014_by_div.to_dict(orient ='records')
dict_2015_by_div = df_2015_by_div.to_dict(orient ='records')
dict_2016_by_div = df_2016_by_div.to_dict(orient ='records')
dict_2017_by_div = df_2017_by_div.to_dict(orient ='records')



# ####################################################  End - Convert dataframes to dictionaries ####################################



# # ####################################################  Beg  - Create Multi-Year Dataframes   ####################################

# ##  By Agency

# #Rename Amount to Years
# df_2014_by_agency_calcs_renamed = df_2014_by_agency_calcs.rename(index=str,columns={'Amount':'2014'})
# df_2015_by_agency_calcs_renamed = df_2015_by_agency_calcs.rename(index=str,columns={'Amount':'2015'})
# df_2016_by_agency_calcs_renamed = df_2016_by_agency_calcs.rename(index=str,columns={'Amount':'2016'})
# df_2017_by_agency_calcs_renamed = df_2017_by_agency_calcs.rename(index=str,columns={'Amount':'2017'})

# #Trim Columns not needed
# df_2014_by_agency_calcs_renamed_trim  = df_2014_by_agency_calcs_renamed.drop(df_2014_by_agency_calcs_renamed.columns[[]], axis=1) #For some reason no columns to trime, not sure why but it works
# df_2015_by_agency_calcs_renamed_trim  = df_2015_by_agency_calcs_renamed.drop(df_2015_by_agency_calcs_renamed.columns[[0]], axis=1)
# df_2016_by_agency_calcs_renamed_trim  = df_2016_by_agency_calcs_renamed.drop(df_2016_by_agency_calcs_renamed.columns[[0]], axis=1)
# df_2017_by_agency_calcs_renamed_trim  = df_2017_by_agency_calcs_renamed.drop(df_2017_by_agency_calcs_renamed.columns[[0]], axis=1)

# #append to Multi-Year by Agency Dataframe
# df_multi_year_by_agency = pd.concat([df_2014_by_agency_calcs_renamed_trim, 
# 	df_2015_by_agency_calcs_renamed_trim,
# 	df_2016_by_agency_calcs_renamed_trim,
# 	df_2017_by_agency_calcs_renamed_trim], axis=1)

# # Create Percentage Change Calculations
# df_multi_year_by_agency['2015v2014'] = ((df_multi_year_by_agency['2015'] / df_multi_year_by_agency['2014'])-1)*100
# df_multi_year_by_agency['2016v2015'] = ((df_multi_year_by_agency['2016'] / df_multi_year_by_agency['2015'])-1)*100
# df_multi_year_by_agency['2017v2016'] = ((df_multi_year_by_agency['2017'] / df_multi_year_by_agency['2016'])-1)*100
# df_multi_year_by_agency['2017v2015'] = (((df_multi_year_by_agency['2017'] / df_multi_year_by_agency['2015'])**(1/2.0))-1)*100  # Annualized Percentage Change over 2 year period

# df_multi_year_by_agency_percentages = df_multi_year_by_agency.drop(df_multi_year_by_agency.columns[[0,1,2,3]], axis=1)


# # ####################################################  End  - Create Multi-Year Dataframes   ####################################





######################################### ############   Beg - Created a Nested JSON called "Master Dictionary" ##############################################


# Create a location for final data
file_name_master_data = r'C:\Users\Justin\Development\ILStateBudget\output\master_data.json'


# Create function that creates a skeleton of a dictionary for the first layer (Agencies)

def create_agency_ID_Name_skeleton(Agency_dictionary_lookup):
	result = []
	temp_list = Agency_dictionary_lookup.items()
	for kk, vv in temp_list:
		temp_dictionary = {"Agency_ID": kk, "Agency_Name": vv}
		result.append(temp_dictionary)
	return result

# run the function
master_dictionary = create_agency_ID_Name_skeleton(agency_dict)

	
### Attached Meta Tags to master dictionary #####

# define Meta Tags
elementary_and_secondary_education_agencies = ['586', '593']
higher_education_agencies = ['601', '608', '612', '616', '620', '628', '636', '644', '664', '676', '684', '691', '692', '693', '695']
all_education_agencies = ['586', '593', '601', '608', '612', '616', '620', '628', '636', '644', '664', '676', '684', '691', '692', '693', '695']
governor_agencies_1 = [ '402', '406', '416', '418', '420', '422', '425', '426','427', '440', '442', '444', '446', '452','458', '466', '478', '482','492', '493', '494', '497', '503', '507', '511']
governor_agencies_2 = [ '517' ,'524', '525' ,'526' ,'532', '537','540','542','546', '548', '554', '558', '560', '562', '563','564','565','569','574','578','579','580','585','588','589','590','591','592']
governor_agencies_all = governor_agencies_1 + governor_agencies_2
judicial_agencies = ['201','210', '275','285','290','295','310','330','340','350','360','370','445','509','528','587']
legislative_agencies = ['101','103','105','108','109','110','112','115','120','131','156','167','510']
unknown_agencies = ['529','541','904']


# test each entry and apply the meta Tags

def update_Agency_tag(master_dictionary_to_add_to,agency_meta_tag_list,text_to_use):
	for entry in master_dictionary_to_add_to:
		if str(entry["Agency_ID"]) in agency_meta_tag_list:
			entry["Agency_Tag"] = text_to_use
	return

update_Agency_tag(master_dictionary,elementary_and_secondary_education_agencies,"Education: Elementary and Secondary")
update_Agency_tag(master_dictionary,higher_education_agencies,"Education: Higher")
update_Agency_tag(master_dictionary,governor_agencies_all,"Governor's Agencies")
update_Agency_tag(master_dictionary,judicial_agencies,"Judicial")
update_Agency_tag(master_dictionary,legislative_agencies,"Legislative")
update_Agency_tag(master_dictionary,unknown_agencies,"Unknown")



### Creat and Fill  the Year Object  #####

# Appends the Year Data with Agency Amount (initially set to 0) and Divisions holder (empty)

def fill_year_with_skeleton(master_dictionary_to_add_to, year_reference):
	for i in master_dictionary_to_add_to:
		i[year_reference]  = {'Agency_Amount': 0,'Divisions':[]}
	return


fill_year_with_skeleton(master_dictionary, '2014')
fill_year_with_skeleton(master_dictionary, '2015')
fill_year_with_skeleton(master_dictionary, '2016')
fill_year_with_skeleton(master_dictionary, '2017')

		
# Fills the Years for "Amount" (cycle's through dictionary created for JSON Export) 

def fill_agency_amount(master_dictionary_to_add_to,  data_source,year_reference):
	for j in data_source:
		for k in master_dictionary_to_add_to:
			if j["Agency_ID"] == k["Agency_ID"]:
				k[year_reference]["Agency_Amount"] = j["Amount"]
	return 


fill_agency_amount(master_dictionary,dict_2014_by_agency, '2014')
fill_agency_amount(master_dictionary,dict_2015_by_agency, '2015')
fill_agency_amount(master_dictionary,dict_2016_by_agency, '2016')
fill_agency_amount(master_dictionary,dict_2017_by_agency, '2017')


### Create and Fill the Divisions holder Object  #####



########################################### Beg - Function to find the children of Agency (i.e. division_ID)  ##################################

def get_divisions(dict_to_look_thru, agency_ID):
	result = []
	for a,b in dict_to_look_thru.iteritems(): # a: agency_division_id,...b: division_name
		agency_code = a[0:3]    #stores first 3 characters of agency_division_id (equal to Agency_ID) 
		division_code = a[4:]   #stores all characters after 4 of agency_division_id (equal to Division_ID) 
		if a[0:3] == agency_ID:  
			result.append(division_code)
	return result
	# text_full = agency_ID
	# print dict_to_look_thru[0]
	# return dict_to_look_thru[text_full] 

# print get_divisions(division_dict, '103')
# print get_divisions(division_dict, '586')

########################################### End - Function to find Agency Children ##################################

########################################### Beg - Function too Find Amount given an Agency_ID and Division_ID ############################################

def get_division_amount(summary_division_dictionary,agency_id,division_id):
	agency_division_id = agency_id+"_"+division_id
	for entry in summary_division_dictionary:
		if entry['Agency_and_Division_ID'] == agency_division_id:
			return entry['Amount']

# print get_division_amount(dict_2014_by_div,'586','57')

########################################### End - Function too Find Amount given an Agency_ID and Division_ID ############################################



#################################  Beg -  Fills the "Divisions" part of "Year"#######################################


def fill_divisions(master_dictionary_to_add_to, division_dictionary_to_lookup, division_data_source,year_of_interest):
	for m in master_dictionary_to_add_to:
		agency_of_interest = m["Agency_ID"]	
		division_array = get_divisions(division_dictionary_to_lookup, agency_of_interest)	
		for division_of_interest in division_array:
			temp_container = {
				'Division_ID':division_of_interest,
				'Division_Name': get_division_name(division_dictionary_to_lookup, agency_of_interest, division_of_interest),
				'Division_Amount': get_division_amount(division_data_source,agency_of_interest,division_of_interest),
				'Division_Tag': 'test',
				'Appropriations': []

			}
			m[year_of_interest]["Divisions"].append(temp_container)
	return

fill_divisions(master_dictionary, division_dict,dict_2014_by_div,'2014')
fill_divisions(master_dictionary, division_dict,dict_2015_by_div,'2015')
fill_divisions(master_dictionary, division_dict,dict_2016_by_div,'2016')
fill_divisions(master_dictionary, division_dict,dict_2017_by_div,'2017')

#################################  End -  Fills the "Divisions" part of "Year"#######################################




#################################  Beg -  Fills the "Appropriations" part of "Year"#######################################


def fill_appropriations(master_dictionary_to_add_to, appropriations_data_source,year_of_interest):
	for q in master_dictionary_to_add_to:											# Cycles through each entry in master dictionary  q= top level of dictionary (agency level)
		agency_id_of_interest = q["Agency_ID"]										# Track which agency your interested in 
		# print q['2014']['Divisions']
		for r in q[year_of_interest]['Divisions']:											# Reference the "Divisions" level of dictionary (preparing for inputting into master Dictionary)
			# print r
			# print r['Division_ID']													# print the division_id to double check
			division_id_of_interest = r['Division_ID'] 									#Store the division_ID
			agency_division_id_of_interest = agency_id_of_interest+"_"+division_id_of_interest						#Create the agency_division_ID
			# print r
			# print r["Appropriations"]
		
			temp_appropriations_container = []
			for appro in appropriations_data_source:										# Go and reference the detail approriations dictionary (preparing for inputting into master Dictionary)
			
				if appro["Agency_and_Division_ID"] == agency_division_id_of_interest:		# If agency and Division both match, then store the detail appropriation information into a temp dictionary
					
					if year_of_interest == '2014':												# this if clause is sued because we don't have result_name and outome_name for 2014
						temp_dictionary = {
							"Fund_Name": appro["Fund_Name"],
							"Fund_Category_Name": appro["Fund_Category_Name"],
							"Appropriation_Amount": appro["Amount"],
							"Appropriation_Type": appro["Appropriation_Type"],
							"Fund_ID": appro["Fund_ID"],
							"Appropriation_Name": appro["Appropriation_Name"],
							"Appropriation_Code": appro["Appropriation_Code"],
							"Capital_Line": appro["Capital_Line"],
							"Outcome_ID": None
							#########################NEED TO CHECK TO SEE IF THIS WORKS how to incorprate Program_Name???  ##################
							
						}							
					else:
						temp_dictionary = {
							"Fund_Name": appro["Fund_Name"],
							"Fund_Category_Name": appro["Fund_Category_Name"],
							"Appropriation_Amount": appro["Amount"],
							"Appropriation_Type": appro["Appropriation_Type"],
							"Fund_ID": appro["Fund_ID"],
							"Appropriation_Name": appro["Appropriation_Name"],
							"Appropriation_Code": appro["Appropriation_Code"],
							"Capital_Line": appro["Capital_Line"],
							"Outcome_ID": appro["Outcome_ID"]
						}
					temp_appropriations_container.append(temp_dictionary)					# Append the temp dictionary
			r['Appropriations'] = temp_appropriations_container
	return

# do the procedure for each  year

fill_appropriations(master_dictionary,dict_2014_by_appropID,'2014')
fill_appropriations(master_dictionary,dict_2015_by_appropID,'2015')
fill_appropriations(master_dictionary,dict_2016_by_appropID,'2016')
fill_appropriations(master_dictionary,dict_2017_by_appropID,'2017')



#################################  End -  Fills the "Appropriations" part of "Year"#######################################





##################################  Beg - Helper Functions to Query the Master Dictionary   ##########################################################
# Other functions were used in creation of Master JSON, not these

##################  Retun the Agency name from Agency ID ##########################

def agency_name_lookup(master_dictionary_to_reference, agency_ID):
	for agency_example in master_dictionary_to_reference:
		if agency_example['Agency_ID'] == agency_ID:
			return agency_example["Agency_Name"]



#################  Return Agency amount from Agency ID ####################################

def agency_amount_lookup(master_dictionary_to_reference, agency_ID, year_of_interest):
	for agency_example in master_dictionary_to_reference:
		if agency_example['Agency_ID'] == agency_ID:
			print agency_ID	
			return agency_example[year_of_interest]["Agency_Amount"]

# print agency_amount_lookup(master_dictionary,'478','2014')


########### Return Agency Name, it's Division Children (Names) and heir Amounta, from an Agency ID ########

def division_amount(master_dictionary_to_reference, agency_id, year_of_interest):
	print agency_name_lookup(master_dictionary_to_reference, agency_id)
	for agency_example in master_dictionary:
			if agency_example['Agency_ID'] == agency_id:
				for division_example in agency_example[year_of_interest]['Divisions']:
					print division_example['Division_Name'] 
					print division_example['Division_Amount']
					# print '\v'
	return

# print division_amount(master_dictionary,'478','2014')


##################################  End - Helper Functions to Query the Master Dictionary  ##########################################################



########################################### Beg - Export master dictionary to JSON  ########################################################################################
with open(file_name_master_data,'w') as outfile:
	json.dump(master_dictionary, outfile)

########################################### End - Export  master dictionary to JSON  ########################################################################################




