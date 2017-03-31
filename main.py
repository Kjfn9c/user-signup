import webapp2
import cgi
import re
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>

"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    def get(self):
        signup_header = "<h2>Signup</h2>"

        signup_buildpage = """
        <form action="/add" method="post">
            <input type='text' name='username' placeholder='Enter A Username'/>
            <br>
            <input type='password' name='password' placeholder='Enter A Password'/>
            <br>
            <input type='password' name='Vpassword' placeholder='Verify Password'/>
            <br>
            <input type='text' name='email' placeholder='Email Address (optional)'/>
            <br>
            <input type='Submit'/>
        </form>"""

        error = self.request.get("error")
        if error:
            error_esc = cgi.escape(error, quote=True)
            error_element = '<p class="error">' + error_esc + '</p>'
        else:
            error_element = ''

        main_content =  signup_header + signup_buildpage + error_element
        content = page_header + main_content + page_footer
        self.response.write(content)

class AddUsername(webapp2.RequestHandler):
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        Vpassword = self.request.get("Vpassword")
        email = self.request.get("email")
        if username == '':
            error = "Enter a Username".format(username)
            self.redirect("/?error=" + error)

        if username != '':
            if password == '':
                error = "You must create a password".format(password)
                self.redirect("/?error=" + error)

        if username != '':
            if password != '':
                if Vpassword != password:
                    if Vpassword == '':
                        error = "You must verify your password".format(Vpassword)
                        self.redirect("/?error=" + error)
                    else:
                        error = "Your passwords must be identical".format(Vpassword)
                        self.redirect("/?error=" + error)

        username = cgi.escape(username)
        username_sentence = "Thanks for signing up, " + username
        content = page_header + "<p>" + username_sentence + "</p>" + page_footer
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/add', AddUsername)
], debug=True)
