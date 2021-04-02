from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     #return 'Hello, Apurv!'
#     #print(url_for('static', filename='sand_castle_icon.ico'))
#     return render_template('./index.html', name=username, post_id=post_id)

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', newline='',mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]  #newline='',TypeError: 'newline' is an invalid keyword argument for this function 
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
        
@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
	if request.method == 'POST':
		try:
		    data = request.form.to_dict()
		    write_to_csv(data)		
		    return redirect('/thankyou.html')
		except:
			return 'did not save to database'
	else:
		return 'something went wrong, try again'


# @app.route('/')
# def my_home():
#     #return 'Hello, Apurv!'
#     #print(url_for('static', filename='sand_castle_icon.ico'))
#     return render_template('./index.html')

# @app.route('/about.html')
# def about():
#     return render_template('./about.html')

# @app.route('/index.html')
# def index():
#     return render_template('./index.html')

# @app.route('/work.html')
# def work():
#     return render_template('./work.html')

# @app.route('/works.html')
# def works():
#     return render_template('./works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('./contact.html')

# # @app.route('/favicon.ico')
# # def about():
# #     return render_template('./about.html')

# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs!'

# @app.route('/blog')
# def blog2():
#     return 'this is my dog'