# Pitch
####  This is a web app that allows users to view submit and comment on various categories of one minuite pitches,15-Sep-2019
#### By **Kingecha Kevin Nyota**
## Link to live site
You can view the site here ---> https://the-pitch1.herokuapp.com

## Description
This is a web app that allows users to view submit and comment on various categories of one minuite pitches.The main reson behind this site is to allow users see various pitches and use them wisely to impress since it only takes one minuite to impress somebody
## User Stories
- [x] User can see various one minuite pitches from various categories on the homepage of the application.
- [x] User can add a pitch to any category
- [x] User can add a comment on any pitch
- [x] User can login into the application 

## Setup/Installation Requirements
* Ensure that Python is installed on your machine if not please visit the python website and download the latest version python 3.6
* Fork the repository and either download the project or clone it to your machine
* Create a virtual environment using the following command
```
python3.6 -m venv --without-pip virtual
```
* then install the latest version of pip
```
curl https://bootstrap.pypa.io/get-pip.py | python
```
* Register the secret key as an environment variable in your terminal as follows
```
export SECRET_KEY=<your-secret-key>
```
* Regester your Email as follows in the environment
```
export MAIL_USERNAME=<Your-email>
```
* Regester your Email Password as follows in the environment
```
export MAIL_PASSWORD=<Your-email-password>
```
* run the application from your terminal using the following command
```
python3.6 manage.py server
```
* To edit the code if you will need any dependancys you will need to navigate to the virtual environment in order to install them from there to avoid version conflicts
```
source virtual/bin/activate
```
## Known Bugs
There are no known bug if any dont hesitate to contact me
## Technologies Used
1. Python Version 3.6
2. Flask Framework
3. Html
4. Bootstrap
5. Css
## Support and contact details
if you run into any issues please contact knyota66@gmail.com
### License
*MIT*
Copyright (c) 2019 **Kingecha Kevin Nyota**