from system.core.controller import *
from time import gmtime, strftime, localtime
import re

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        # Note that we have to load the model before using it
        
        self.load_model('Course')

    def login(self):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
        session['date'] = strftime("%a, %d %b %Y ", localtime())
        session['time'] = strftime("%H:%M:%S", localtime()) 
        session['pokemonIds']=[]
        if request.form['email'] == "":
            flash("You must enter a valid email")
            return redirect('/')
            
        elif request.form['password'] == "":
            flash("You must enter a password")
            return redirect('/')
            
        else:
            user = self.models['Course'].login(request.form['email'], request.form['password'])
            print "user" + str(user)

            if user == []:
                flash("Email/Password combo does not match")
                return redirect('/')
            
            else:
                session['user'] = user
                # return redirect('/')
                return self.load_view('welcome.html', firstname=session['user'])
                
        
    def logout(self):
        session.clear()
        flash("You have successfully logged out.  Thank you come again")
        return self.load_view('index.html')

    def index(self):
        course = self.models['Course'].get_all_courses()
        return self.load_view('index.html', course=course)

    def choose(self,id):
        # declare an array to hold pics, once a picture is picked
        # this
        
        if len(session['pokemonIds']) < 10:
            session['pokemonIds'].append(id)
            print "pokenum" + str(session['pokemonIds'])
        return self.load_view('welcome.html', pokennum=session['pokemonIds'], firstname=session['user'], id=id)

    def dashboard(self):
        return self.load_view('welcome.html', firstname=session['user'])

    # This is how a method with a route parameter that provides the id would work
    # We would set up a GET route for this method
    def showAll_Courses(self):
        # Note how we access the model using self.models
        course = self.models['Course'].get_all_courses()
        
        return self.load_view('view_courses.html', firstname=session['user'], course=course)

    def showAll_Users(self):
        # Note how we access the model using self.models
        users = self.models['Course'].get_all_users()
        
        return self.load_view('view_users.html', firstname=session['user'], users=users)

    def del_course_confirm(self):
        session['id'] = request.form['CourseID']

        course = self.models['Course'].get_course_by_id(session['id'])
        return self.load_view('del_confirm.html', course=course, firstname=session['user'])

    def del_user_confirm(self):
        session['id'] = request.form['userID']
        print "session id: " + session['id']
        user = self.models['Course'].get_user_by_id(session['id'])
        print "user: " + str(user)
        return self.load_view('del_user_confirm.html',firstname=session['user'],user=user)
        # return self.load_view('del_user_confirm.html', user=user, firstname=session['user'])

    def show(self, id):
        # Note how we access the model using self.models
        course = self.models['Course'].get_course_by_id(id)
        return self.load_view('show.html', course=course)

    # This is how a method used to add a course would look
    # We would set up a POST route for this method
    def add_course(self):
        # add course details
        title = request.form['title']
        description = request.form['description']
        course = self.models['Course'].get_all_courses()
        
        if title == "":
            flash("Title Needed")
            return self.load_view('view_courses.html', title=title, description=description, firstname=session['user'], course=course)
        elif description == "":
            flash("Description Needed")
            return self.load_view('view_courses.html', title=title, description=description, firstname=session['user'], course=course)
        else:
            course_details = {
                'title': title,
                'description': description
            }
            self.models['Course'].add_course(course_details)
            course = self.models['Course'].get_all_courses()
            return self.load_view('view_courses.html', firstname=session['user'], course=course)
    
    def add_user(self):
        #add user
        token = int(request.form['token'])
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        if len(request.form['firstname']) < 2:
            flash("First Name must be more than 2 characters")
            if token == 1:
                users = self.models['Course'].get_all_users()
                return self.load_view('view_users.html', users=users, firstname=session['user'])
            elif token == 0:
                return self.load_view('index.html')
        elif len(request.form['lastname']) < 2:
            flash("Last Name must be more than 2 characters")
            if token == 1:
                users = self.models['Course'].get_all_users()
                return self.load_view('view_users.html', users=users, firstname=session['user'])
            elif token == 0:
                return self.load_view('index.html')
        elif not EMAIL_REGEX.match(request.form['email']):
            flash("Email format must have valid email format!")
            if token == 1:
                users = self.models['Course'].get_all_users()
                return self.load_view('view_users.html', users=users, firstname=session['user'])
            elif token == 0:
                return self.load_view('index.html')
        elif len(request.form['password']) < 1:
            flash("Password cannot be blank!")
            if token == 1:
                users = self.models['Course'].get_all_users()
                return self.load_view('view_users.html', users=users, firstname=session['user'])
            elif token == 0:
                return self.load_view('index.html')
        
        elif len(request.form['pwdconfirm']) < 1:
            flash("Confirm password must not be blank")
            if token == 1:
                users = self.models['Course'].get_all_users()
                return self.load_view('view_users.html', users=users, firstname=session['user'])
            elif token == 0:
                return self.load_view('index.html')
        
        elif len(request.form['password']) < 8:
            flash("Password must contain more than 8 characters")
            if token == 1:
                users = self.models['Course'].get_all_users()
                return self.load_view('view_users.html', users=users, firstname=session['user'])
            elif token == 0:
                return self.load_view('index.html')

        elif request.form['password'] != request.form['pwdconfirm']:
            flash("Passwords do not match")
            if token == 1:
                users = self.models['Course'].get_all_users()
                return self.load_view('view_users.html', users=users, firstname=session['user'])
            elif token == 0:
                return self.load_view('index.html')
        else:
            email_Check = self.models['Course'].get_firstname(request.form['email'])
            if email_Check:
                flash("User exists for that email, user NOT created")
                if token == 1:
                    users = self.models['Course'].get_all_users()
                    return self.load_view('view_users.html', users=users, firstname=session['user'])
                elif token == 0:
                    return self.load_view('index.html')
            else:
                user_details = {
                    'firstname': request.form['firstname'],
                    'lastname': request.form['lastname'],
                    'email': request.form['email'],
                    'password': request.form['password'],
                    }
                self.models['Course'].add_user(user_details)
                
                flash("User Added")
                if token == 1:
                    users = self.models['Course'].get_all_users()
                    return self.load_view('view_users.html', users=users, firstname=session['user'])
                elif token == 0:
                    return self.load_view('index.html')

        

    # This is how a method used to update a course would look
    # We would set up a POST route for this method
    def edit_course(self):
        CourseID = request.form['CourseID']
        course = self.models['Course'].get_course_by_id(CourseID)
        return self.load_view('edit_Course.html', firstname=session['user'], course=course)
        
    def edit_user(self):
        userID = request.form['userID']
        user = self.models['Course'].get_user_by_id(userID)
        return self.load_view('edit_user.html', firstname=session['user'], user=user)
    
    def update(self):
        course_details = {
            'title': request.form['course_title'],
            'description': request.form['description'],
            'course_id': request.form['CourseID']
            }
        self.models['Course'].update_course(course_details)
        flash("Course Updated")
        course = self.models['Course'].get_all_courses()
        
        return self.load_view('view_courses.html', firstname=session['user'], course=course)

    def update_user(self):
        user_details = {
            'firstname': request.form['firstname'],
            'lastname': request.form['lastname'],
            'password': request.form['password'],
            'userID': request.form['userID'],
            }
        self.models['Course'].update_user(user_details)
        flash("User Details Updated")
        users = self.models['Course'].get_all_users()
        return self.load_view('view_users.html', users=users, firstname=session['user'])

    def delete_course(self):
        self.models['Course'].delete_course(session['id'])
        flash("Course deleted")
        course = self.models['Course'].get_all_courses()
        return self.load_view('view_courses.html', course=course, firstname=session['user'])

    def delete_user(self):
        self.models['Course'].delete_user(session['id'])
        flash("User deleted")
        users = self.models['Course'].get_all_users()
        return self.load_view('view_users.html', users=users, firstname=session['user'])
        

    