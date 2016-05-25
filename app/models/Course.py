from system.core.model import Model
from datetime import datetime
import md5

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def get_all_courses(self):
        return self.db.query_db("SELECT * FROM courses")

    def get_all_users(self):
        return self.db.query_db("SELECT * FROM students")

    def get_course_by_id(self, course_id):
        # pass data to the query like so
        query = "SELECT * FROM courses WHERE id = :course_id"
        data = { 'course_id': course_id}
        return self.db.query_db(query, data)

    def get_user_by_id(self, course_id):
        # pass data to the query like so
        query = "SELECT * FROM students WHERE id = :course_id"
        data = { 'course_id': course_id}
        return self.db.query_db(query, data)

    def add_course(self, course):
      # Build the query first and then the data that goes in the query
      query = "INSERT INTO courses (title, description, created_at) VALUES (:title, :description, NOW())"
      data = { 'title': course['title'], 'description': course['description'] }
      return self.db.query_db(query, data)

    def add_user(self, user):
      # hashed_pw = md5.new(user['password']).hexdigest()
      # user['password'] = hashed_pw
      hashed_pw = self.bcrypt.generate_password_hash(user['password'])
      query = "INSERT INTO students (first_name, last_name, email, password, created_at, updated_at) VALUES (:firstname, :lastname, :email, :password, NOW(), NOW())"
      # we'll then create a dictionary of data from the POST data received
      data = {
          'firstname': user['firstname'],
          'lastname': user['lastname'],
          'email': user['email'],
          'password': hashed_pw
          }
      return self.db.query_db(query, data)

    def login(self, email, password):
      # works for hd5 password
      # password = md5.new(password).hexdigest()
      user_query = "SELECT * FROM students WHERE email = :email LIMIT 1"
      user_data = {'email': email }
      user = self.db.query_db(user_query, user_data)
      
      if user:
           # check_password_hash() compares encrypted password in DB to one provided by user logging in
        if self.bcrypt.check_password_hash(user[0]['password'], password):
          return user
        # Whether we did not find the email, or if the password did not match, either way return False
      else:
        return False

    def get_firstname(self, email, password):
      query = "SELECT first_name FROM students WHERE email = :email AND password = :password"
      data = {
          'email': email,
          'password': password
          }
      return self.db.query_db(query, data)

    def get_firstname(self, email):
      query = "SELECT first_name FROM students WHERE email = :email"
      data = {
          'email': email
          }
      return self.db.query_db(query, data)

    def update_course(self, course):
      # Building the query for the update
      query = "UPDATE courses SET title=:title, description=:description, updated_at=:updated_at WHERE id = :course_id"
      # we need to pass the necessary data
      data = { 'title': course['title'], 'description': course['description'], 'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'course_id': course['course_id']}
      # run the update
      return self.db.query_db(query, data)

    def update_user(self, user):
      # Building the query for the update
      print "id: " + str(user['lastname'])
      query = "UPDATE students SET first_name=:firstname, last_name=:lastname, password=:password, updated_at=:updated_at WHERE id = :course_id"
      # we need to pass the necessary data
      data = { 'firstname': user['firstname'], 'lastname': user['lastname'], 'password': user['password'], 'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'course_id': user['userID'] }
      # run the update
      return self.db.query_db(query, data)

    def delete_course(self, course_id):
      query = "DELETE FROM courses WHERE id = :course_id"
      data = { "course_id": course_id }
      return self.db.query_db(query,data)

    def delete_user(self, user_id):
      query = "DELETE FROM students WHERE id = :user_id"
      data = { "user_id": user_id }
      return self.db.query_db(query,data)
