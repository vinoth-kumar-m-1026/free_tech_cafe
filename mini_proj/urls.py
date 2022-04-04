from mini_proj import app
from mini_proj.views import *

#register route
app.add_url_rule("/register", methods=["POST"], view_func=register_view)

#login route
app.add_url_rule("/login", methods=["POST"], view_func=login_view)

#home page route
app.add_url_rule("/home",methods=["GET"],view_func=home)

#logout route
app.add_url_rule("/logout",methods=["POST"],view_func=logout_view)