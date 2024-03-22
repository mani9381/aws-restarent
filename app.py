from flask import Flask,render_template,request
import smtplib

app =Flask(__name__)
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/booktable',methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    restarent = request.form['restarent']
    phone = request.form['phone']
    date = request.form['date']
    time = request.form['time']
    count =request.form['people']
    message = request.form['message']
    server.login('akhilasuragani772@gmail.com','bvzbouwscjyikeyj')
    server.sendmail('akhilasuragani772@gmail.com',email,'yahoooo! '+name+'\nYour table bookes\n1.Restarant Name:'+restarent+'\nslot:'+date+'and'+time+'\nTotal peopele:'+count+'\n'+'Message you entered:'+message+'\nYour Phone number:'+phone)
    return render_template('index.html',ack="Booking confirmed")
@app.route('/sendmsg',methods=['post'])
def sendmsg():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    subject = request.form['subject']
    server.login('akhilasuragani772@gmail.com','bvzbouwscjyikeyj')
    server.sendmail('akhilasuragani772@gmail.com',email,'Thank your feed back!\n'+'Message that you sent: '+message)
    server.sendmail('akhilasuragani772@gmail.com','akhilasuragani772@gmail.com','You got a feed from: '+email+'\nName: '+name+"\nSubject: "+subject+'\n Message: '+message)
    return render_template('index.html',ackf="Thankyou for your feedback!")
   
if __name__=="__main__":
    app.run(debug=True)
