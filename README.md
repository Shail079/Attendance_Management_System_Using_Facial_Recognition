# Attendance_Management_System_Using_Facial_Recognition

## Setup Prerequisitives for project

##### 1) Python 3.7 or later. Download at "https://www.python.org/downloads/".
##### 2) Download XAMPP server @ "https://www.apachefriends.org/download.html".


## How to run 

#### 1) Download the Zip file of project from  "code" tab. Or clone the repository using "git clone https://github.com/Shail079/Attendance_Management_System_Using_Facial_Recognition.git" into your local host.

#### 2) Now open your command prompt and cd to your project directory.

#### 3) Create and activate a virtual Environment in your Project directory.
##### Steps to create Virtual Env
 * Type the command "py -m venv myenv" in your command prompt.
 * Now cd in myenv using "cd myenv".
 * Next in Scripts folder activate venv using "Scripts\activate".
 * Move back to project directory using "cd.." command.

#### 4) Now download the required libraries for running this project using "pip install -r requirements.txt".
* This will install all libraries required for the project.

#### 5) Start your XAMPP server and login to your "MyPHP" and Create a blank database "Face_db" in your MyPHP server.

#### 6) Next run command "python manage.py migrate" to make all migrations to "Face_db" database.

#### 7) Once migration is completed load your "MyPHP" admin and you will find that the tables are created.

#### 8) Now in "admin_details" table add details (eg: Username and Password) for your admin login in for your project.

#### 9) Next in your command prompt run command "python manage.py runserver" and copy the link "http://127.0.0.1:8000/" in your browser.

#### 10) Enjoy our "Attendance_Management_System_Using_Facial_Recognition" project and contribute more by adding more features to the app.

