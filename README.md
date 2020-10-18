# sms_chemical_module 
# Django Rest Api with Postgres Database

INTRODUCTION

The metallics optimizer calculates the cheapest charge mix for an electric arc furnace (EAF)
in a steel plant. The charge materials are different scrap types and virgin material. In summary
those materials are called commodities. The optimization algorithm uses the chemical
composition of commodities as input values to guarantee that the chemical composition of the
tapped melt is within a specific range. The melt is tapped after the melting process in the EAF
is finished. One complete melting process as well as tapping the melt into a ladle is called a
heat.

1 step:-

Download and Install Postgres Database
https://www.postgresql.org/download/
and download the pgadmin tool(UI Tool) for access postgres database and create the database , the database name is sms_db_1
  note:- please remembere the password

2 step:- Python 3.8.6 on windows

please follow the below link
https://github.com/pettarin/python-on-windows/blob/master/README.md

3:- download the module from github https://github.com/Azhar-Shelia/sms_chemical_module

4:- step 4
      Installing PIP On Windows

      Step 1: Download PIP get-pip.py => https://bootstrap.pypa.io/get-pip.py
              Download the file to the desired folder in Windows. You can save the file to any location, but remember the path so you can use it later.

      step:- 2 Launch Windows Command Line
             Open the Command Prompt. Use the cd command followed by a folder name to navigate to the location of the get-pip.py file.
             To install PIP type in the following in cmd console:
             python get-pip.py

             Verify Installation and Check the Pip Version
             pip --version

5:- downlaod the requirements.txt from github

        Download the file to the desired folder in Windows. You can save the file to any location, but remember the path so you can use it later.
        Use the cd command followed by a folder name to navigate to the location of the requirements.txt file.
        To install the package of python 
        run the the command on command prompt (pip install -r requirements.txt)
  
6:- after the step 5:
        please go to project location 
        Use the cd command followed by a folder name to navigate to the location of the project.

        step 1 :- cd project folder_name.  ex (cd sms)
        step 2 :- cd folder_name.  ex(cd sms_exam)
  
 7:- please follow the below step to connect your project to database
      
        step 1: open the setting file on text editor tool ex(sublime, pycharm, notepad), setting file location sms_exam -> seeting.py
        step 2: please find the DATABASES keyword in setting.py and fill the requirement in database section, put yoyr password against the PASSWORD key with single quotes ''.
            
            
              DATABASES = {
                       'default': {
                           'ENGINE': 'django.db.backends.postgresql',
                           'NAME': 'sms_db_1', on step we create the sms_db_1 , so dont touch Name section
                           'USER': 'postgres',
                           'PASSWORD': 'your password',  please add the password remember the password on step 1, 
                           'HOST': '127.0.0.1',
                           'PORT': '5432',
                       }
                    }
        step 3:- save the file
        step 4 :- run the command on command prompt: manage.py runserver
        step 5 :- goto the browse and past this url on url bar (http://127.0.0.1:8000/all_chemical_elements) you will se all the elements of chemical. 

