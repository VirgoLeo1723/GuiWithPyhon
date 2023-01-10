from typing import Counter
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import smtplib
import json

f_account_read = open("Server/account.txt","r")
account={}
# set up flask server
app = Flask(__name__)
# apply flask cors
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/login', methods=['POST','GET'])
@cross_origin(origin='*')
def login_process():
    user_name = request.args.get('user')
    pass_word = request.args.get('pass')
    if user_name in account :
        if account[user_name][0] == pass_word: return "Login success"
        else: return "Wrong password"
    else: return "Login failed"

@app.route('/create', methods=['POST','GET'])
@cross_origin(origin='*')
def create_process():
    user_name = request.args.get('user')
    pass_word = request.args.get('pass')
    if user_name in account: return "Exist"
    else:
        email = request.args.get('mail')
        account[user_name]=[pass_word,email]
        f_account_load = open("Server/account.txt","a")
        f_account_load.write(f"{user_name}:{pass_word},{email}\n")
        f_account_load.close()
        return "Create Success"

@app.route('/forget', methods=['POST','GET'])
@cross_origin(origin='*')
def forget_process():
    user_name = request.args.get('user')
    email = request.args.get('mail')
    if user_name in account : 
        accountInfor="""User-name: %s\nPassword: %s""" %(user_name, account[user_name][0])
        mess =  """From: From Anxiety Disoders <anxietydisoders@gmail.com>
To: To You <%s>
Subject: [Account Information] 

%s
""" %(email,accountInfor)
        mail_server = smtplib.SMTP("smtp.gmail.com",587)
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()
        mail_server.login('anxietydisoders@gmail.com','yenkun1708')
        mail_server.sendmail('anxietydisoders@gmail.com', email, mess)  
    else: return "Cannot find user"
    return "Forget"

@app.route('/story', methods=['POST','GET'])
@cross_origin(origin='*')
def story_process():
    data_file = json.load(request.files['datas'])
    f_story_load = open("Server/story.txt","ab")
    for email in data_file:
        f_story_load.write(f"{email}:{data_file[email]}".encode("utf-8"))
    f_story_load.close()
        
    return "Story received"

@app.route('/feedback', methods=['POST','GET'])
@cross_origin(origin='*')
def feedback_process():
    data_file = json.load(request.files['datas'])
    f_fd_load = open("Server/feedback.txt","ab") 
    for email in data_file:
        f_fd_load.write(f"{email}:{data_file[email]}".encode("utf-8"))
    f_fd_load.close()
    return "Feedback received"

@app.route('/mail', methods=['POST','GET'])
@cross_origin(origin='*')
def mail_process():
    user_name = request.args.get('user')
    if user_name in account :
        return account[user_name][1]

def update_account():
    while True:
        temp=f_account_read.readline()
        if temp:
            if "\n" in temp:
                temp=temp[0:temp.index("\n")]
            pre1 = temp.split(":")
            pre2 = pre1[1].split(",")
            account[pre1[0]] = pre2
        else:  break
    f_account_read.close()
# start back-end
if __name__ == '__main__':
    update_account()
    app.run(host='0.0.0.0', port='9999')
    
