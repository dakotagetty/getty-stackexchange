from flask import render_template, flash, redirect, url_for, request
from app import app, requested_users
from app.forms import UsersForm
from stackapi import StackAPI
from datetime import datetime

@app.route('/requests')
def requests():
    temp_users = request.args.get('num_users', None)
    requested_users = int(temp_users)
    #requested_users = session.get('num_users', None)
    # Initialization method to connect to the host site.
    SITE = StackAPI('stackoverflow')
    # page_size will determine how many users are requested to the site.
    if requested_users > 100:  
        # fetch can only query 100 users in one hit.
        flash('Only 100 users may be requested at a time. Search defaulted to 100.')
        SITE.page_size = 100
    else:
        SITE.page_size = requested_users
    # max_pages set to 1 allows for control over request quota.
    SITE.max_pages = 1

    # Fetch the desired amount of users from stackoverflow on set date. Stored in dictionary object users.
    users = SITE.fetch('users', sort='creation', order='asc', fromdate=datetime(2021, 2, 1), todate=datetime(2021, 2, 2))

    # Dictionary to hold the user ID's as it's key and the value 
    # associated with each will be the number of questions each user has posted.
    user_questions = {}
    
    # Three counter variables storing counts necessary for later output
    num_questions = 0
    num_answered = 0
    num_users_questions = 0
    
    # Iterate over users['items'], which is a dictionary holding each user, 
    # to place the users' ID's into their unique list 'user_ids' for the questions fetch.
    user_ids = []
    for user in users['items']:
        user_ids.append(user['user_id'])
    
    # Fetch all questions asked by the previously fetched users, and store the resulting
    # dictionary into 'questions'. 
    questions = SITE.fetch('users/{ids}/questions', ids = user_ids)

    # First counter variable to store integer value of the total questions.
    num_questions = len(questions['items'])

    # Iterate over users['items'] a second time to check each user's (if any) questions.
    for user in users['items']:
        # Get user ID from user and add it to the user_questions dictionary.
        user_id = user['user_id']
        user_questions[user_id] = 0
        # Control boolean to accurately count how many users have asked questions. 
        first_question = True
        # Iterate through each question in the questions['items'] dictonary previously fetched. 
        for question in questions['items']:
            # Check to see if the user asking the question matches the user on current iteration.
            if question['owner']['user_id'] == user_id:
                # Conditional always suceeds on first iteration through questions
                if first_question:
                    # Increment number of users who have asked a question, flip conditional, 
                    # and set the value in the user_questions dictionary to one.
                    num_users_questions += 1
                    first_question = False
                    user_questions[user_id] = 1
                else:
                    # Increment for each successive question this current user has asked after the first.
                    user_questions[user_id] += 1
      
    # Iterate through each question and check if the question has been answered by another user.
    for question in questions['items']:
        if question['is_answered']:
            # Increment counter variable for each answered question.
            num_answered += 1

    # Flash statement providing client with number of users they have requested for specific timeline..
    flash('Client has requested information on the first {} users created on {}'.format(
        len(user_ids), datetime(2021, 2, 1)))

    # Flash statement to inform client of the data they requested on the aforementioned users.
    flash('There were {} total questions asked by {} users, and {} of them have been answered'.format(
        num_questions, num_users_questions, num_answered))

    # Render index.html with the appropriate data that will be used in the front-end output
    return render_template('requests.html', title="User Request", users=users, user_questions=user_questions, questions=questions)

# Home page routes to the request form
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UsersForm()
    if form.validate_on_submit():
        requested_users = form.num_users.data
        # Once valid submission provided, client is redirected to index page
        return redirect(url_for('requests', num_users = requested_users))
    return render_template('index.html', title='Home', form=form)
