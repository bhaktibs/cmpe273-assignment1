import sys
from flask import Flask
from github import Github


app = Flask(__name__)
#@app.route('/')
#def ind():
#    return "this is home page"
github_username=None
github_repo=None
output=None
def main_pr():
    arg=sys.argv[1]
    str_lst=arg.rsplit('/',2)
    global github_username
    github_username=str_lst[1]
    #print github_username
    global github_repo
    github_repo=str_lst[2]
    #print github_repo
@app.route('/v1/<username>')
def index(username):
    global github_repo
    global github_username
    g =Github() 
    repo = g.get_user(github_username).get_repo(github_repo) #get_user returns object of type name which in turn returns obj- repo.
    file_content = repo.get_file_contents(username)
    file_dec_content= file_content.decoded_content
    return file_dec_content


if __name__ == "__main__":
    main_pr()
    app.run(debug=True,host='0.0.0.0')
