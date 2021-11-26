from flask import Flask 
from flask import request 
import csv

def login() 
	if request.method == 'POST': 
		name = request.form['fname'] 
		surname = request.form['fsurname']
    		companyName = request.form['fcompany']
    		companyDesc = request.form['fcomment']
    		email = request.form['femail']
    		number = request.form['fnumber']
  	full_info = name + ',' + surname + ',' + companyName + ',' + companyDesc + ',' + email + ',' + number 
  
  	fname = "surveyinfo.csv"
  
  	with open(fname, 'w') as f:
    		writer = csv.writer(f)
    		writer.writerow(full_info)
    
     
    
    
