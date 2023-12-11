How to Run Project


1. Create a Virtual Environment using following command.I strongly recommend to use git bash to run commands, and makesure you have python installed properly in your system.
git bash download link: https://git-scm.com/downloads.For mac you have to install manually.
for mac how to create virtual envionment: https://github.com/codingforentrepreneurs/Guides/blob/master/all/install_django_mac_linux.md

python -m venv myvenv

myvenv= replace this with your virtual environment name.if you don't want to change virtual environment name then keep as it is.

2. After,we have to activate this environment using following command
source myvenv/Scripts/activate (For Windows)
source myvenv/bin/activate (For Mac)

3. Now, we need required packages to run this project.so install required packages using following command.
pip install -r requirements.txt

4.now,we have to type following command to run server.
python manage.py runserver

for Admin login use following url:
https://127.0.0.1:8000/admin

username: admin@gmail.com
password: admin

You can create superuser using following command:
python manage.py createsuperuser

if any difficulties to run project email me on: u2405445@uel.ac.uk

Thank you.



