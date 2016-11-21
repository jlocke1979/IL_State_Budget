#Installing Libraries
# Needed:
import urllib2
import csv
import time 
import sys
from bs4 import BeautifulSoup

# Possibly needed libraries:
# from urllib2 import urlopen
# from urllib2 import HTTPError
# import pandas as pd
# import simplejson as json
# import numpy as np


################# Overview ####################
# This script is resonpsible for pulling information from the following site: 
# Source: http://ledger.illinoiscomptroller.gov/find-an-expense/statewide/
# and organizing and storing it for manipulation and visualization 



############################################## Beg - Tuturials / Research Referenced #################################################################################
"""
Research
Webscraping Tutorial: "Webscraping with Python 
Download file located here: "https://github.com/REMitchell/python-scraping"
"""
############################################## End - Tuturials / Research Referenced #################################################################################




############################################# Beg = What data are we interested in ?   #####################################################

"""StateWide Data (summarize Agency Category and Agencies):
Source: http://ledger.illinoiscomptroller.gov/find-an-expense/statewide/
Agency Category

A_2017 = Group By Agency Category; Year = 2017, Types of Spedning = Both, View Monthly Amounts = N, View Budget Amounts = Y, View Lapse Amounts = N
A_2016 = Group By Agency Category; Year = 2016, Types of Spedning = Both, View Monthly Amounts = N, View Budget Amounts = Y, View Lapse Amounts = N
A_2015 = Group By Agency Category; Year = 2015, Types of Spedning = Both, View Monthly Amounts = N, View Budget Amounts = Y, View Lapse Amounts = N

Agency 
B_2017 = Group By Agency; Year = 2017, Types of Spedning = Both, View Monthly Amounts = N, View Budget Amounts = Y, View Lapse Amounts = N
B_2016 = Group By Agency; Year = 2016, Types of Spedning = Both, View Monthly Amounts = N, View Budget Amounts = Y, View Lapse Amounts = N
B_2015 = Group By Agency; Year = 2015, Types of Spedning = Both, View Monthly Amounts = N, View Budget Amounts = Y, View Lapse Amounts = N



Agency Data (summarizes agency data grouping by Ojbect of Expenditure)
Source:  http://ledger.illinoiscomptroller.gov/find-an-expense/by-agency/
: Object of Expenditure for each Agency_ID

Title of files = C_2017_101
Agency = 101;
Group = Blank, 
Category = Blank, 
Type = Blank 
Group By Object of Expenditure; 
Year = 2017, 
Types of Spedning = Both, 
View Monthly Amounts = N, 
View Budget Amounts = Y, 
View Lapse Amounts = N

"""
############################################# End = What data are we interested in ?   #####################################################





######################### Beg -  Define the  Webpages we need to traverse ##########################################################

# For REference Human would go to this link first
# http://ledger.illinoiscomptroller.gov/index.cfm/find-an-expense/by-agency/


################ Compile Agency_ Lists ################################


agency_name_dict = {'210': 'Supreme Court Historic Preservation Commission', '664': 'Southern Illinois University', '131': 'General Assembly Retirement System', '620': 'Northeastern Illinois University',\
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


agency_list = ['101','102','103','104','105','107','108','109','110','112','115','120','131','140','155','156','167','201','202','203','205','210','215','225','235','245','255',\
    '275','285','290','295','310','330','331','340','350','351','360','370','399','402','406','407','409','416','418','420','422','423','425','426','427','438','440','442','444','445',\
    '446','448','452','458','462','466','473','475','478','482','488','492','493','494','497','499','503','504','505','507','509','510','511','517','524','525','526','527','528','529',\
    '530','531','532','533','534','535','536','537','538','539','540','541','542','546','548','549','550','551','553','554','555','556','557','558','559','560','561','562','563','564',\
    '565','567','568','569','570','571','572','573','574','575','576','577','578','579','580','581','582','583','584','585','586','587','588','589','590','591','592','593','594','595',\
    '596','597','598','599','601','605','608','609','612','613','616','618','620','621','628','629','633','636','637','644','645','646','664','665','666','667','668','676','677','678',\
    '684','685','691','692','693','695','799','899']

agency_category_mapping = {'586': '1000','691': '1500','676': '1500','684': '1500','664': '1500','644': '1500','636': '1500','628': '1500','601': '1500',
    '478': '2000','444': '2000','402': '2000','418': '2000','482': '2000','497': '2000','537': '2000','534': '2000', \
    '558': '2000','527': '2000','526': '2000','426': '3000','493': '3000','588': '3000','425': '3000','546': '3000', \
    '466': '3000','592': '3000','569': '3000','578': '3000','560': '3000','591': '3000','532': '4000','422': '4000', \
    '565': '4000','440': '4000','446': '4000','524': '4000','563': '4000','442': '4000','579': '4000','525': '4000', \
    '542': '4000','494': '5000','557': '5000','420': '5000','427': '5000','574': '5000','406': '5000','554': '5000', \
    '445': '5000','541': '5000','452': '5000','503': '5000','585': '5000','360': '6000','370': '6000','350': '6000', \
    '340': '6000','310': '6000','330': '6000','201': '6200','275': '6200','290': '6200','295': '6200','210': '6200', \
    '285': '6200','131': '6400','101': '6400','103': '6400','108': '6400','112': '6400','105': '6400','115': '6400', \
    '110': '6400','156': '6400','167': '6400','564': '6400','120': '6400','109': '6400','416': '6600','448': '6600', \
    '458': '6600','492': '6600','507': '6600','509': '6600','510': '6600','511': '6600','517': '6600','528': '6600', \
    '548': '6600','555': '6600','562': '6600','580': '6600','583': '6600','587': '6600','589': '6600','590': '6600', \
    '593': '6600','594': '6600','693': '6600','799': '8000','608': '1500','612': '1500','616': '1500','620': '1500', \
    '692': '1500','695': '1500','553': '6000'}

# ############### Validate Data ####### Only have to do this once
# # Cross Check these two lists against each other

# not_in_agency_list_check = []
# for index, value in agency_dict.items():
#     if index not in agency_list:
#         not_in_agency_list_check.append(index)

# # print not_in_agency_list_check

# not_in_agency_dict = []
# for instance in agency_list:
#     if instance not in agency_dict:
#         not_in_agency_dict.append(instance)

# # print not_in_agency_dict

# # # Only one not showing up is "904":"Continuting Approriations" (removed from Agency_dictionary)
# # Conclusion = Go with COmptroller Data



############## Define a function that gets 1 URL given an agency and a year ######################################
def create_url(AgcySel, AgcyGrpSel, AgcyCatSel, AgcyTypeSel, GroupBy, FY, Type, ShowBudg):
    # Store Base URl for webscraper
    base_url_text = "http://ledger.illinoiscomptroller.gov/index.cfm/find-an-expense/by-agency/"
    
    # Add inputs into the output webpage
    selected_url_text = base_url_text \
        +"?AgcySel="+AgcySel \
        +"&AgcyGrpSel="+AgcyGrpSel \
        +"&AgcyCatSel="+AgcyCatSel \
        +"&AgcyTypeSel="+AgcyTypeSel \
        +"&GroupBy="+GroupBy \
        +"&FY="+FY \
        +"&Type="+Type \
        +"&ShowBudg="+ShowBudg \
        +"&submitted="
    return selected_url_text

# Test the function 
# test_101 = create_url('101', "0", "0", "0", "Obje", "17", "B", "Yes")
# print test_101



########################################################## Beg - Check Summary Text at top of Page Functions ##############################################################################
# Create a Function that prints off the text at the top of the webpage. This is largely for verification purposes to see I'm returning the right page
def print_summary_text(url, tag):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        interesting_text = bsObj.findAll("",tag)
        result = interesting_text[0].get_text()
    except AttributeError as e:
        return None
    return result


# # Run print_summary_text function
# # Example of getting Summary Text using Agency 101
# summary_text = print_summary_text(selected_url_text,{"class":"col-md-3 col-md-offset-3"})
# print summary_text




########################################################## End - Check Summary Text at top of Page Functions ##############################################################################




###################### Create a Function that creates BSObject #################### 


def get_BeautifulSoup_Object(url):
    # This portion inserts information about me to the scraper, so admins can monitor my usage and / or reach out
    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36 ; Justin R. Locke / Peoria, IL justin@wearenortherly.com'}
    request = urllib2.Request(url, headers=headers)

    html = urllib2.urlopen(request)

    BeautifulSoup_Object = BeautifulSoup(html.read(),"lxml")
    return BeautifulSoup_Object


###################### Create a Function that pulls header names from datatable on desired  webpage #########
def get_column_header_names(BSObject):
    thead = BSObject.find("thead")
    headers= []
    
    if thead == None:
        headers= None
        return headers
    else:
        headers= []
        # Find & Store  thead section
        # Run through each column header and append to array
        for header in thead.tr.findAll('th'):
            value = header.get_text()
            headers.append(value)
        return headers

#Example:
# test_bsObj = get_BeautifulSoup_Object(url_list_all_text[0])
# print get_column_header_names(test_bsObj)




###################### Beg - Create a Function that pulls data from datatable and writes to CSV 



def capture_and_write_to_CSV(AgcySel, AgcyGrpSel, AgcyCatSel, AgcyTypeSel, GroupBy, FY, Type, ShowBudg):
    print AgcySel
    url = create_url(AgcySel, AgcyGrpSel, AgcyCatSel, AgcyTypeSel, GroupBy, FY, Type, ShowBudg)

    bsObj = get_BeautifulSoup_Object(url)

    # Find & Store the body section
    tbody = bsObj.tbody

    # Get the headers row
    headers = get_column_header_names(bsObj)

    if headers == None:
        None_returned = ["No information returned"]
        with open('20%s_%s_%s_%s_%s_%s_%s_%s.csv' % (FY, AgcySel, AgcyGrpSel, AgcyCatSel, AgcyTypeSel, GroupBy, Type, ShowBudg), 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(None_returned)
    else: 
        with open('20%s_%s_%s_%s_%s_%s_%s_%s.csv' % (FY,AgcySel, AgcyGrpSel, AgcyCatSel, AgcyTypeSel, GroupBy, Type, ShowBudg), 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            records = [] # store all of the records in this list
            # header =  get_column_header_names(url)
            writer.writerow(headers)


            for row in tbody.findAll('tr'):
                records = []
                col = row.findAll('td')
                code_col = col[0].string.strip()
                obj_of_exp_col = col[1].string.strip()
                # 5 Step process here: 1) replace $ with "", 2) then "," with "" 3) then ) with "" 4) then convert "(" to "-" 5) then convert to float)

                appropriated_col = col[2].string.replace( '$','')   # step 1
                appropriated_col = appropriated_col.replace(")","")
                appropriated_col = appropriated_col.replace(",","")
                appropriated_col = appropriated_col.replace( '(','-')
                appropriated_col = float(appropriated_col)
                
                expended_ytd_col = col[3].string.replace( '$','')
                expended_ytd_col = expended_ytd_col.replace(')',"")   
                expended_ytd_col = expended_ytd_col.replace(',',"")
                expended_ytd_col = expended_ytd_col.replace('(',"-") 
                expended_ytd_col = float(expended_ytd_col) 
                
                unexpended_col = col[4].string.replace( '$','')
                unexpended_col = unexpended_col.replace(')',"")   
                unexpended_col = unexpended_col.replace(',',"")
                unexpended_col = unexpended_col.replace('(',"-") 
                unexpended_col = float(unexpended_col)

                record = [code_col, obj_of_exp_col,appropriated_col,expended_ytd_col,unexpended_col] # store the record with a ',' between
                records.append(record)

                # Write each row to 
                writer.writerow(record)


        return

# Validation 
# Works!
# capture_and_write_to_CSV('101', "0", "0", "0", "Obje", "17", "B", "Yes")


def pull_datatables_en_mass(agency_input_list, AgcyGrpSel, AgcyCatSel, AgcyTypeSel, GroupBy, FY, Type, ShowBudg, seconds_to_wait_between_web_hits):
    num_of_agencies = len(agency_input_list)
    
    for agency in agency_input_list:
        capture_and_write_to_CSV(agency, AgcyGrpSel, AgcyCatSel, AgcyTypeSel, GroupBy, FY, Type, ShowBudg)
        # This function inserts a pause in between hits to give the servers a break and so I don't get kicked out
        time.sleep( seconds_to_wait_between_web_hits )
    return




########################  Beg -  Scale up to ALL 185 Agencies ############################
## Note - Initially had trouble running at home, possible they throttled my home IP address, went to 30/30 and it ran fine

###### #2017
### Worked, (although script failed on last agency 899, reran for that single one and worked fine)
### Files stored here:
# pull_datatables_en_mass(agency_list, "0", "0", "0", "Obje", "17", "A", "Yes", 5)

###### 2016
# pull_datatables_en_mass(agency_list, "0", "0", "0", "Obje", "16", "A", "Yes", 5)

###### 2015
# pull_datatables_en_mass(agency_list, "0", "0", "0", "Obje", "15", "A", "Yes", 5)



# Small Problem: Keeps failing on agency 899 not sure why,..but works when I run individually 
# Running an individual Agency
# capture_and_write_to_CSV('899', "0", "0", "0", "Obje", "17", "A", "Yes")
# capture_and_write_to_CSV('899', "0", "0", "0", "Obje", "16", "A", "Yes")
# capture_and_write_to_CSV('899', "0", "0", "0", "Obje", "15", "A", "Yes")
#
# Otherwise Successfull


###################### End - Create a Function that pulls data from datatable





    