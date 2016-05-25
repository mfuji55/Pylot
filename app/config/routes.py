"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes
    
    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter 
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Courses'
routes['POST']['/add_course'] = 'Courses#add_course'
routes['POST']['/get_all_courses'] = 'Courses#showAll_Courses'
routes['POST']['/get_all_users'] = 'Courses#showAll_Users'
# routes['/delete'] = 'Courses#delete'
routes['POST']['/courses/destroy'] = 'Courses#del_course_confirm'
routes['POST']['/user/destroy'] = 'Courses#del_user_confirm'
routes['POST']['/delete/course'] = 'Courses#delete_course'
routes['POST']['/delete/user'] = 'Courses#delete_user'
routes['POST']['/login'] = 'Courses#login'
routes['POST']['/logout'] = 'Courses#logout'
routes['POST']['/add_user'] = 'Courses#add_user'
routes['POST']['/edit/course'] = 'Courses#edit_course'
routes['POST']['/edit/user'] = 'Courses#edit_user'
routes['POST']['/course/update'] = 'Courses#update'
routes['POST']['/user/update'] = 'Courses#update_user'
routes['POST']['/dashboard'] = 'Courses#dashboard'
routes['GET']['/choose/<int:id>'] = 'Courses#choose'

    
"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.
    
    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path). 
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
