from bottle import Bottle, request
import csv

app = Bottle()
##Should pull out info but idk
@app.route('/form.py', method="POST")
def formhandler():

  name = request.forms.get('fname')
  surname = request.forms.get('fsurname')
  company_name = request.forms.get('fcompany')
  company_desc = request.forms.get('fcomment')
  phone_num = request.forms.get('fnumber')
  email = request.forms.get('femail')
  full_info = name + ',' + surname + ',' + company_name + ',' + company_desc + ',' + phone_num + ',' + email + '\n'
  
  fname = 'surveyinfo.csv'
  with open('path/to/csv_file', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(full_info)
    
    
     
    
    
