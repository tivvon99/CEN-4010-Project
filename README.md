# Welcome to VolunteerNow

## Tools

* Python (Flask)
* MongoDB
* HTML/Bootstrap

## Directions

These are the directions for setting up your environment, and running the flask server on Windows. Mac and Linux will be added soon.

You will need to download MongoDB to see the data among your local server. Add the URI that is in the database.py file.

> After forking your repository to your computer, open your terminal. I recommend launching the terminal as administrator by right clicking it. After you open it navigate to your forked repo, last command should be.
>
>```shell
>cd CEN-4010-PROJECT
>```
>
> Create a virtual environment on your pc to avoid system dependencies with the required libraries. This keeps the version of flask you use here from downloading system wide on your pc.
>>```Python
>>python -m venv .venv
>>```
>
> Activate the environment
>>```shell
>> .venv\Scripts\Activate
>>```
>
> Download the application requirements
>>```
>>pip install -r requirements.txt
>>```
>
> Change into the Volunteer_Now directory and run the application
>>```Python
>> cd Volunteer_Now
>> python app.py
>>```
> To see it, enter the server link in your terminal in a web browser. just in case you have issues, be prepared to install Flask Session



# To Do

* FrontEnd
    * Begin Designing Web Page layouts
        * Bootstrap for responsiveness
        * Front end is separated from backend by keeping front end designs within the templates folder.
        * All current areas like the navbar and login form need to be rebuilt
        * messenger front end...

* Back End
    * Need to define many more app routes to handle http requests
    * Need to implement logic for form handling
    * Improve logic for user authentication and security
    * Make full use of session cookies
    * Make sure opportunity posts can iterate along a main page
    * messenger back end...

* FullStack
    * Currently, the database is configured to run on a local mongoDB database server. This will only reside and persist among your local server and will not be consistent with all of each others yet. It is important to configure the database to a cloud mongodb server so our database is consistent with each others in the meantime for testing.
        * Preferably, the entire application should be configured and deployed to a cloud server. Heroku?
    * The jinja library in Flask is used to integrate the backend and frontend. The HTTP routes will control what data is inputed into the frontend based on the HTTP Request (GET, POST, etc), and spit them back into the front end using jinja templating.