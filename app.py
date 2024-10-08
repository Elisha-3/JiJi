from flask import*
import pymysql
from mpesa import*
from werkzeug.security import generate_password_hash, check_password_hash
app=Flask(__name__)
#session key
app.secret_key = "@pgaDmin4#0"
@app.route("/")
def Homepage():
    # establish connection to DB
    connection= pymysql.connect(host='localhost',user='root', password='',database='JIJI')
    sql = "SELECT * FROM products WHERE product_category = 'phones'"
    sql1 = "SELECT * FROM products WHERE product_category = 'electronics'"
    sql2 = "SELECT * FROM products WHERE product_category = 'appliances'"
    sql3 = "SELECT * FROM products WHERE product_category = 'Beauty'"
    sql4 = "SELECT * FROM products WHERE product_category = 'Shoes'"
    sql5 = "SELECT * FROM products WHERE product_category = 'furniture'"






    # execute the above querry
    # you need a cursor to execute it 
    cursor = connection.cursor()
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor4 = connection.cursor()
    cursor5 = connection.cursor()


    # execute
    cursor.execute(sql)
    cursor1.execute(sql1)
    cursor2.execute(sql2)
    cursor3.execute(sql3)
    cursor4.execute(sql4)
    cursor5.execute(sql5)




    # get all the phones
    phones= cursor.fetchall()
    electronics= cursor1.fetchall()
    appliances= cursor2.fetchall()
    beauty= cursor3.fetchall()
    shoes= cursor4.fetchall()
    furniture = cursor5.fetchall()

    # cursor.close()
    # connection.close()

    return render_template("index.html", phones = phones, electronics= electronics, appliances= appliances, beauty=beauty, shoes=shoes, furniture=furniture)

#route for a single product
@app.route("/single/<product_id>")
def Singleitem(product_id):
    connection= pymysql.connect(host='localhost',user='root', password='',database='JIJI')
    #create SQL query
    sql = "SELECT * FROM products WHERE product_id = %s "
    #create a cursor
    cursor = connection.cursor()
    #execute
    cursor.execute(sql,product_id)
    #get singleproduct
    product= cursor.fetchone()

    return render_template("single.html", product= product )

#upload products
@app.route("/upload",methods=['POST', 'GET'])
def Upload():
    if request.method=='POST':
        # user can add the products
        product_name = request.form['product_name']
        product_desc = request.form['product_desc']
        product_cost = request.form['product_cost']
        product_category = request.form['product_category']
        product_image_name = request.files['product_image_name']
        product_image_name.save('static/images/' + product_image_name.filename)

        # connect to DB
        connection= pymysql.connect(host='localhost',user='root', password='',database='JIJI')

        # create a cursor 
        cursor = connection.cursor()

        sql = "INSERT INTO products(product_name, product_desc, product_cost, product_category, product_image_name) values (%s, %s, %s, %s,%s)"

        #provide the data
        data = (product_name, product_desc, product_cost, product_category, product_image_name.filename)
        # execute
        cursor.execute(sql, data)
        # save changes
        connection.commit()

        return render_template("upload.html", message= "Product added successfully")

    else:
      return render_template("upload.html", error = "Please add a product")

#Fashion route 
# helps you to see all the fashions
@app.route("/fashion")
def fashion():
    # establish connection to DB
    connection= pymysql.connect(host='localhost',user='root', password='',database='JIJI')
    sql = "SELECT * FROM products WHERE product_category = 'dresses'"
    sql1 = "SELECT * FROM products WHERE product_category = 'handbags'"
    sql2 = "SELECT * FROM products WHERE product_category = 'socks'"
    sql3 = "SELECT * FROM products WHERE product_category = 'cap'"
    sql4 = "SELECT * FROM products WHERE product_category = 'belt'"
    #sql5 = "SELECT * FROM products WHERE product_category = 'furniture'"






    # execute the above querry
    # you need a cursor to execute it 
    cursor = connection.cursor()
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()
    cursor4 = connection.cursor()
    #cursor5 = connection.cursor()


    # execute
    cursor.execute(sql)
    cursor1.execute(sql1)
    cursor2.execute(sql2)
    cursor3.execute(sql3)
    cursor4.execute(sql4)
    #cursor5.execute(sql5)




    # get all the phones
    dresses= cursor.fetchall()
    handbags= cursor1.fetchall()
    socks= cursor2.fetchall()
    cap= cursor3.fetchall()
    belt= cursor4.fetchall()
    #furniture = cursor5.fetchall()

    return render_template("fashion.html",dresses=dresses, handbags=handbags, socks=socks, cap=cap, belt=belt)

# a route to upload fashion
@app.route("/uploadfashion",methods=['POST', 'GET'])
def UploadFashion():
    if request.method=='POST':
        # user can add the products
        product_name = request.form['product_name']
        product_desc = request.form['product_desc']
        product_cost = request.form['product_cost']
        fashion_category = request.form['product_category']
        product_image_name = request.files['product_image_name']
        product_image_name.save('static/images/' + product_image_name.filename)

        # connect to DB
        connection= pymysql.connect(host='localhost',user='root', password='',database='JIJI')

        # create a cursor 
        cursor = connection.cursor()

        sql = "INSERT INTO products(product_name, product_desc, product_cost, product_category, product_image_name) values (%s, %s, %s, %s,%s)"

        #provide the data
        data = (product_name, product_desc, product_cost, fashion_category, product_image_name.filename)
        # execute
        cursor.execute(sql, data)
        # save changes
        connection.commit()

        return render_template("uploadfashion.html", message= "Fashion added successfully")

    else:
      return render_template("uploadfashion.html", error = "Please add a fashion")

@app.route("/about")
def About():
    return "This is about"

@app.route("/register", methods=['POST','GET'])
def Register():
    if request.method=='POST':
        # user can add the products
        username = request.form['username']
        email = request.form['email']
        gender = request.form['gender']
        phone = request.form['phone']
        password = request.form['password']
        
        #hashed security
        #hashed_password = generate_password_hash(password, method= 'sha256', salt_length=int=16)
        # connect to DB
        connection= pymysql.connect(host='localhost',user='root', password='',database='JIJI')

        # create a cursor 
        cursor = connection.cursor()

        sql = "INSERT INTO users(username, email, gender, phone, password) values (%s, %s, %s, %s,%s)"

        #provide the data
        data = (username, email, gender, phone, password)
        # execute
        cursor.execute(sql, data)
        # save changes
        connection.commit()

        return render_template("register.html", message= "user registered successfully")

    else:
      return render_template("register.html", error = "Please add a user")
    
@app.route("/login", methods=['POST','GET'])
def Login():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']

        # connect to DB
        connection= pymysql.connect(host='localhost',user='root', password='',database='JIJI')
        cursor = connection.cursor()
        # check if user exists in the DB
        sql = "select * from users WHERE email = %s and password =%s"
        
        data = (email,password)
    
        #execute
        cursor.execute(sql, data)
    
        # check if any result found
        if cursor.rowcount==0:
            #it means the username and password not found
            return render_template("login.html", error = "Invalid login credentials")

        else:
            session['key']= email
            return redirect("/")


    else:
        return render_template("login.html")
#Mpesa
    # implent STK PUSH 
@app.route("/mpesa", methods=['POST'])
def mpesa():
    phone= request.form["phone"]
    amount = request.form["amount"]

    # use mpesa_payment function from mpesa.py
    # it accepts the phone and amount as arguments
    mpesa_payment(amount,phone)
    return '<h1> Please complete payment in your phone</h1>' \
    '<a href="/" class= "btn btn-outline-muted btn-sm"> Back to Products</a>'

@app.route("/logout")
def Logout():
    session.clear()

    return redirect("/login")

if __name__ == '__main__':
    app.run(debug=True, port=4003)