from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
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
    content1 = db.Column(db.String(120), nullable=False)
    content2 = db.Column(db.String(120), nullable=False)

    content3 = db.Column(db.String(120), nullable=False)
    content4 = db.Column(db.String(120), nullable=False)

    content5 = db.Column(db.String(120), nullable=False)
    content6 = db.Column(db.String(120), nullable=False)

    content7 = db.Column(db.String(120), nullable=False)
    content8 = db.Column(db.String(120), nullable=False)

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
    flash("Stay home, stay safe!", "danger")
    posts = Posts.query.filter_by().all()
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
    flash("Let us know if you have any query or suggestion. Thank-you!", "primary")
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)

@app.route("/about")
def about():
    return render_template('about.html', params=params)



@app.route("/dshboard", methods=['GET', 'POST'])
def dashboard():
    if ('user' in session and session['user'] == params['admin_user']):
        posts = Posts.query.all()
        return render_template('dshboard.html', params=params, posts=posts)

    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username==params['admin_user'] and userpass==params['admin_password']):
            session['user'] = username
            posts = Posts.query.all()
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
            content1 = request.form.get('content1')
            content2 = request.form.get('content2')

            content3 = request.form.get('content3')
            content4 = request.form.get('content4')

            content5 = request.form.get('content5')
            content6 = request.form.get('content6')

            content7 = request.form.get('content7')
            content8 = request.form.get('content8')

            conclusion = request.form.get('conclusion')
            href_link = request.form.get('href_link')
            post_link = request.form.get('post_link')
            img_file = request.form.get('img_file')
            credit = request.form.get('credit')
            post_img = request.form.get('post_img')
            date = datetime.now()

            if sno=='0':
                post = Posts(title=box_title, slug=slug, content1=content1, content2=content2, content3=content3, content4=content4,content5=content5, content6=content6, content7=content7, content8=content8,conclusion=conclusion, href_link=href_link,post_link=post_link ,img_file=img_file, tagline=tline, date=date, credit=credit, post_img = post_img)
                db.session.add(post)
                db.session.commit()

            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title=box_title
                post.slug=slug

                post.content1 =content1
                post.content2= content2

                post.content3 = content3
                post.content4 = content4

                post.content5 = content5
                post.content6 = content6

                post.content7 = content7
                post.content8 = content8

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
            return "Uploaded successfully"

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
                          body=message + "\n" + phone
                          )

        flash("Thanks for submitting your details. We will get back to you soon.", "success")

    return render_template('contact.html', params=params)

if __name__ == '__main__':
    app.run(debug=True)
