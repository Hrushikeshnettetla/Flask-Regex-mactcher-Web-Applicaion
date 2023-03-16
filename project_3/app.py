from flask import Flask, request,render_template
import re
app = Flask(__name__)

@app.route('/')
def home_page():
    return "welcome to homePage"

@app.route('/search')
def search_page():
    return "welome to the search"

@app.route('/add')
def add_fun():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a) + int(b))
 
@app.route('/upper')
def convert_to_uppercase():
    input_str = request.args.get('input_str')
    words = input_str.split()
    uppercase_words = [word.upper() for word in words]
    output_str = " ".join(uppercase_words)  
    return output_str

##creating regex Matcher using Flask

###Create a route that will handle the form submission and display the matches

@app.route('/regex_page', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex = request.form['regex']
        matches = re.findall(regex, test_string)
        return render_template('index.html', test_string=test_string, regex=regex, matches=matches)
    else:
        return render_template('index.html')

##Run the flask app
if __name__ =='__main__':
    app.run(debug=True)