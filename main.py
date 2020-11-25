from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from datetime import datetime
from flask_mail import Mail
from werkzeug.utils import secure_filename
import json
import os
import math

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

server = 'prod'
app=Flask(__name__)

app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = 'True',
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password']
)
mail = Mail(app)

if server == 'local':
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
db.init_app(app)
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), unique=True, nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), unique=True, nullable=False)
    content = db.Column(db.String(120), nullable=False)
    para = db.Column(db.String(120), nullable=False)
    cont_one = db.Column(db.String(120), nullable=False)
    para_one = db.Column(db.String(120), nullable=False)

    cont_two = db.Column(db.String(120), nullable=False)
    para_two = db.Column(db.String(120), nullable=False)

    cont_three = db.Column(db.String(120), nullable=False)
    para_three = db.Column(db.String(120), nullable=False)

    cont_four = db.Column(db.String(120), nullable=False)
    para_four = db.Column(db.String(120), nullable=False)

    cont_five = db.Column(db.String(120), nullable=False)
    para_five = db.Column(db.String(120), nullable=False)

    conclusion = db.Column(db.String(120), nullable=False)
    href_link = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    post_link = db.Column(db.String(120), nullable=False)
    img_file = db.Column(db.String(12), nullable=False)
    tagline = db.Column(db.String(120), nullable=False)
    credit = db.Column(db.String(120), nullable=False)
    post_img = db.Column(db.String(12), nullable=False)

@app.route("/terms-conditions")
def tnc():
    return  render_template('tnc.html', params=params)

@app.route("/privacy-policy")
def privacypolicy():
    return  render_template('privacypolicy.html', params=params)

@app.route("/")
def home():
    # flash("Stay home, stay safe!", "danger")
    posts = Posts.query.filter_by().order_by(desc(Posts.sno)).all()
    last = math.ceil(len(posts)/int(params['no_of_posts']))


    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts']) + int(params['no_of_posts'])]
    if (page==1):
        prev = "#"
        next = "/?page="+ str(page + 1)
    elif (page==last):
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)


    return render_template('index.html', params=params, posts=posts, prev=prev, next=next)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post(post_slug):
    # flash("Let us know if you have any query or suggestion. Thank-you!", "primary")
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)

@app.route("/about")
def about():
    return render_template('about.html', params=params)



@app.route("/dshboard", methods=['GET', 'POST'])
def dashboard():
    if ('user' in session and session['user'] == params['admin_user']):
        posts = Posts.query.order_by(desc(Posts.sno)).all()
        return render_template('dshboard.html', params=params, posts=posts)

    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username==params['admin_user'] and userpass==params['admin_password']):
            session['user'] = username
            posts = Posts.query.order_by(desc(Posts.sno)).all()
            return render_template('dshboard.html', params=params, posts=posts)
        else:
            return "Please enter valid username or password."
    return render_template('login.html', params=params)

@app.route("/edit/<string:sno>", methods = ['GET', 'POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')

            content = request.form.get('content')
            para = request.form.get('para')
            
            cont_one = request.form.get('cont_one')
            para_one = request.form.get('para_one')

            cont_two = request.form.get('cont_two')
            para_two = request.form.get('para_two')

            cont_three = request.form.get('cont_three')
            para_three = request.form.get('para_three')

            cont_four = request.form.get('cont_four')
            para_four = request.form.get('para_four')

            cont_five = request.form.get('cont_five')
            para_five = request.form.get('para_five')

            conclusion = request.form.get('conclusion')
            href_link = request.form.get('href_link')
            post_link = request.form.get('post_link')
            img_file = request.form.get('img_file')
            credit = request.form.get('credit')
            post_img = request.form.get('post_img')
            date = datetime.now()

            if sno=='0':
                post = Posts(title=box_title, slug=slug, content=content, para=para, cont_one=cont_one, para_one=para_one, cont_two=cont_two, para_two=para_two, cont_three=cont_three, para_three=para_three, cont_four=cont_four, para_four=para_four, cont_five=cont_five, para_five=para_five, conclusion=conclusion, href_link=href_link, post_link=post_link ,img_file=img_file, tagline=tline, date=date, credit=credit, post_img = post_img)
                db.session.add(post)
                db.session.commit()

            else:
                post = Posts.query.filter_by(sno=sno).order_by(desc(Posts.sno)).first()
                post.title=box_title
                post.slug=slug
                post.content = content
                post.para = para
                post.cont_one = cont_one
                post.para_one = para_one
                post.cont_two = cont_two
                post.para_two = para_two
                post.cont_three = cont_three
                post.para_three = para_three
                post.cont_four = cont_four
                post.para_four = para_four
                post.cont_five = cont_five
                post.para_five = para_five
                post.conclusion=conclusion
                post.href_link = href_link
                post.post_link = post_link
                post.tagline=tline
                post.img_file=img_file
                post.date=date
                post.credit=credit
                post.post_img=post_img
                db.session.commit()
                return redirect('/edit/'+sno)

    post = Posts.query.filter_by(sno=sno).first()
    return render_template('edit.html', params=params, post=post, sno=sno)


@app.route("/uploader", methods = ['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if (request.method == 'POST'):
            f= request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return """<h1 style="color: green";>UPLOADED SUCCESSFULLY</h1>"""

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dshboard')

@app.route("/delete/<string:sno>", methods = ['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dshboard')

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        #add entry to the database
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        entry = Contacts(name = name, phone_num = phone, email = email, msg = message, date = datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from: ' + name,
                          recipients = [params['gmail-user']],
                          sender=email,
                          body='Message: ' + message + "\n" + 'Contact: ' + phone
                          )

        flash("Thanks for submitting your details. We will get back to you soon.", "success")

    return render_template('contact.html', params=params)

if __name__ == '__main__':
    app.run(debug=True)
