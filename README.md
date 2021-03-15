# StackExchange API Tool 
A simple python web application to scrape and output data from StackOverflow using the wrapper class StackAPI for the StackExchange API. User's have the ability to query StackOverflow and recieve information on the users who have recently created accounts.

## Setup
To run the application, I installed Python3, and then I ran the following:\
```python3 -m venv venv``` to create my virtual environment then I activated it with ```source venv/bin/activate```\
Next run
```pip install flask``` to install 
Flask 1.1.2,\
```pip install flask-wtf``` to install 
Flask-WTF 0.14.3, and\
```pip install stackapi``` to install
StackAPI 0.2\
This provided me access to each necessary package to run the application


## Usage
The user of this web application has the ability to submit a form requesting up to 100 users that created thier accounts on February 1st, 2021.
Once the form is submitted, it will output each user, and the number of questions they have asked. Next, it outputs every question that has been asked
and prints the title of the question, the author, and whether or not the question has been answered.

## Author
Dakota Getty

## External Resources
To setup the web application, I utilized part 1, 2, and 3 of this tutorial https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world 
to assist in ensuring the skeleton of the application was setup correctly. Also, I used the documentation in https://api.stackexchange.com/ and https://stackapi.readthedocs.io/en/latest/index.html to acclimate myself to the StackExchangeAPI and the wrapper StackAPI class.

## Future Extensions
A few concepts I am looking into for future releases are to allow the client to choose what day the users were created, instead of the static February 1st, 2021 date.
Similarly, more paramters can be added to the search form such as the option to only output questions that have or have not been answered. This could let the web user to either view questions that they may need answered, or it can allow them redirect to an unanswered question on stackoverflow where they can answer it themselves.
