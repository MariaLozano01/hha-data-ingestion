import pandas as pd 
import xlrd
import requests
import json
#pip installed for all modules needed and then imported modules that were appropriate for the assignment (aka. import pandas, import request, import JSON)
import pandas as pd # used this line to import the pandas command 
tab1 = pd.read_excel('data/xls.py.xlsx')
tab2 = pd.read_excel('data/xls.py.xlsx', sheet_name= 1) #Used the same command as tab 1 but needed to figure out which table to use so used command "sheet_name"
#use pandas to read file 
tab1
tab2 
import requests #call requests package
apidataset = 'https://data.cms.gov/data-api/v1/dataset/332846e4-ea55-4641-8307-59ea4e59a5a0/data'
data = apidataset
data = requests.get(apidataset)
data = data.json()

## Section 3
from google.cloud import bigquery # import bigquery
GOOGLE_APPLICATION_CREDENTIALS = 'hha-data-ingestion-361019-30da82e962c4.json'
client = bigquery.Client.from_service_account_json('/Users/marialozano/Downloads/hha-data-ingestion HW FILES/hha-data-ingestion-361019-30da82e962c4.json')




