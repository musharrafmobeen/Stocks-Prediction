from flask import Flask, request, render_template, make_response, session
from StocksData import prediction, return_graph_url
from FacialRecognition import SignIn_With_FacialId, SignUp_With_FacialId
from flask_mysqldb import MySQL
import database as db
import FR
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'musharrafmobeen@gmail.com'
app.config['MAIL_PASSWORD'] = 'blackviking125125'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'stockslab'

mysql = MySQL(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

global eml


@app.route('/')
def index():
    
    if 'Agree' in request.cookies:
        if 'User' in request.cookies:
            username = request.cookies.get('User')
            return render_template('home.html', username = username)

        else:
            return render_template('home2.html')

    else:
        return render_template('index.html')            


@app.route('/setCookie')
def setCookie():
    res = make_response(render_template('home2.html') )
    res.set_cookie('Agree', 'welcome to website' , max_age=60*60*24*365)
    return res    

@app.route('/MessageToDeveloper_LoggedIn', methods=['GET', 'POST'])
def MessageToDeveloper_LoggedIn():
    if request.method == 'POST':
        username = request.form['nameloggedin']
        email = request.form['mailloggedin']
        comments = request.form['review']
        if email != None and username != None:
            msg = Message(f'From {username} : Comment about the website ', sender = email, recipients=['musharrafmobeen8@gmail.com','mmq.25524@gmail.com'])
            msg.body = f'{comments}'
            mail.send(msg)
            return render_template('home.html') 

        else:
            return render_template('home.html', message = "fill all forms") 

    return render_template('home.html', message = "Something Went Wrong")         

@app.route('/MessageToDeveloper_LoggedOff', methods=['GET', 'POST'])
def MessageToDeveloper_LoggedOff():
    if request.method == 'POST':
        username = request.form['nameloggedoff']
        email = request.form['mailloggedoff']
        comments = request.form['review']
        if email != None and username != None:
            msg = Message(f'From {username} : Comment about the website ', sender= email, recipients=['musharrafmobeen8@gmail.com','mmq.25524@gmail.com'])
            msg.body = f'{comments}'
            msg.attachments
            mail.send(msg)
            return render_template('home2.html') 

        else:
            return render_template('home2.html', message = "fill all forms")

    return render_template('home2.html', message = "Something Went Wrong") 

@app.route('/SignIn')
def SignIn():
    return render_template('SignIN.html')

@app.route('/SignUp')
def SignUp():
    return render_template('SignUP.html')

@app.route('/LogIn', methods=['GET', 'POST'])
def LogIn():
    if request.method == 'POST':
        if 'User' in request.cookies:
            return render_template('home.html', result = "Already Logged In")  

        else:    
            Email = request.form['Email']
            Password = request.form['Password']
            result = db.read(mysql,Email,Password)
            if result[0] != None:
                res = make_response(render_template('home.html', username = result[0]))
                res.set_cookie('User', result[0] , max_age=60*60*24*365)
                if not 'User' in session:
                    session['User'] = result
                    session['Email'] = Email
                eml = True    
                return res

            else:
                return render_template('SignIN.html', result = "Account Not Found")         

@app.route('/LogOut')
def LogOut():
    res = make_response(render_template('home2.html') )
    res.set_cookie('User', '' , max_age=0)
    session.clear()
    return  res  

@app.route('/updateordelete',methods=['GET','POST'])
def updateordelete():
    if request.method == 'POST':
        if 'Email' in session:
            Email = session['Email']
            UserName = request.form['username']
            Password = request.form['password']
            selector = request.form['btn']
            if selector == 'Delete':
                try:
                    db.delete(mysql,Email)
                    res = make_response(render_template('home2.html', message = "Account Deleted"))
                    res.set_cookie('User', '' , max_age=0)
                    session.clear() 
                    return  res
                except:
                    return render_template('home.html', message = "Something Went Wrong 1")
            elif selector == 'Update':
                if UserName != None and Password != None:
                    try:
                        db.update(mysql,UserName,Email,Password)
                        res = make_response(render_template('home.html', username = UserName ,message= "Successfullt Updated"))
                        res.set_cookie('User', '' , max_age=0)
                        res.set_cookie('User', UserName , max_age=60*60*24*365)
                        session['User'] = UserName
                        return res
                    except:
                        return render_template('home.html', message = "Something Went Wrong 2")
                else:
                    return render_template('home.html', message = "Something Went Wrong 3")     
            return render_template('home.html', message = "Something Went Wrong 3")                 
        return render_template('home.html', message = "Something Went Wrong 4") 

                

@app.route('/Register', methods=['GET', 'POST'])
def Registor():
    if request.method == 'POST':
        UserName = request.form['UserName']
        Email = request.form['Email']
        Password = request.form['Password']
        Password2 = request.form['Password2']
        try:
            result = db.insert(mysql,UserName,Email,Password,Password2)
            if result == "Success":
                msg = Message('Welcome you have successfully registered', sender='musharrafmobeen8@gmail.com', recipients=[Email])
                mail.send(msg)
                res = make_response(render_template('home.html', username = UserName))
                res.set_cookie('User', UserName , max_age=60*60*24*365)
                if not 'User' in session:
                    session['User'] = UserName
                    session['Email'] = Email
                eml = True    
                return res

            elif result == "AlreadyExists":
                return render_template('SignUP.html',result = "Email Already Registered")

            elif result == "PasswordError":
                return render_template('SignUP.html',result = "Password Mismatch")

        except TypeError:
              return render_template('SignUP.html',result = "Email Already Registered")
        return render_template('SignUP.html',result = "Email Already Registered")

    else:
        return render_template('SignUP.html',result = "Email Already Registered")               

      

@app.route('/Policy')
def Policy():
    return render_template('policy.php')      

@app.route('/LogIn_With_Facial_ID')
def LogIn_With_Facial_ID():
    try:
        picname = FR.getPic()
        if picname != "No Capture Device Available": 
            text = SignIn_With_FacialId(picname)
            if text != 'More Than One person in Image' and text != 'NO person in image' and text != 'Sign Up First' and text != None:
                User = db.readFID(mysql,text)
                if User != None:
                    if  not 'User' in request.cookies:
                        res = make_response(render_template('home.html', username = User[0]))
                        res.set_cookie('User', User[0] , max_age=60*60*24*365)
                        if not 'User' in session:
                            session['User'] = User[0]
                            session['Email'] = User[1]
                            eml = False    
                        return res

                return render_template('SignIN.html',result = "User Not Found")    

            else:
                return render_template('SignUP.html',result = "Register First")

        else:
            return render_template('SignIN.html',result = "No Camera Available")        

        return render_template('SignIN.html',result = "User Not Found")
  
    except ValueError:
        pass    

@app.route('/Register_With_Facial_ID', methods=['GET', 'POST'])
def Register_With_Facial_ID():
    if request.method == 'POST':
        UserName = request.form['username']
        Email = request.form['email']
        if not UserName and not Email:
            return render_template('SignUP.html',result = "Fiil all fields Empty")
        else:
            try:
                picname = FR.getPic() 
                if picname != "No Capture Device Available":    
                    text = SignUp_With_FacialId(picname)
                    if text == 'Person Saved':
                        try:
                            msg = Message('Welcome you have successfully registered', sender='musharrafmobeen8@gmail.com', recipients=[Email])
                            mail.send(msg)
                            db.insertFID(mysql,UserName,picname,Email)
                            res = make_response(render_template('home.html', username = UserName))
                            res.set_cookie('User', UserName , max_age=60*60*24*365)
                            if not 'User' in session:
                                session['User'] = UserName
                                session['Email']= Email
                            eml = False    
                            return res
                        except:
                            render_template('SignUP.html',result = "Something Went Wrong")    

                else:
                    return render_template('SignIN.html',result = "No Camera Available")   
                           
            except TypeError as e:
                return render_template('SignUP.html', result = e)        
 
            else:
                return render_template('SignUP.html',result = text)
                
            return render_template('SignUP.html',result = "Something Went Wrong")    

        return render_template('SignUP.html',result = "")   

    else:
        return render_template('SignUP.html',result = "something went wrong")        

@app.route('/PredictStocks')
def PredictStocks():
    return render_template('StocksPrediction.html') 

@app.route('/Predict', methods=['GET', 'POST'])
def foo():
    if request.method == 'POST':
        Company_Name = request.form['Company_Name']
        Date = request.form['Date']
        predictions = prediction(Company_Name,Date)
        graph_name = return_graph_url()
        if 'Email' in session:
            reciever = session['Email']
            msg = Message('Result To The Stocks Prediction', sender = 'musharrafmobeen8@gmail.com', recipients=[reciever])
            msg.body = f'Opening value of stocks={predictions[0][0]}, Highest value of stocks={predictions[0][1]}, Lowest value of stocks={predictions[0][2]}, Closing value of stocks={predictions[0][3]}, Volume of stocks={predictions[0][4]}'
            with app.open_resource(f"static/graphs/{graph_name}") as fp:  
                msg.attach("galexy.jpg","image/png",fp.read())  
                mail.send(msg)  
        return render_template('Prediction.html', Open=predictions[0][0], High=predictions[0][1], Low=predictions[0][2], Close=predictions[0][3], Volume=predictions[0][4], graph= f'graphs/{graph_name}' )
      

if __name__ == '__main__':
    app.debug = True
    app.run()
   


