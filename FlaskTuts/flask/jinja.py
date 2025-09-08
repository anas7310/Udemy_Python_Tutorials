##Building URL dynamically
##Variable rule
##Jinja 2 Template Engine


##Jinja2 template engine
'''
{{}} expressions to print output in HTML
{%....%} conditional statements such as conditions, for loops
{#....#} this is for comments
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form["name"]
        return f"Hello {name}!"
    return render_template('form.html')

##Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template('result.html',results=res)


@app.route('/successresults/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    exp={'score':score, 'res':res}

    return render_template('result1.html',results=exp)


##If condition
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html',results=score)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',results=score)

@app.route('/submitmarks', methods=['POST','GET'])
def submitmarks():
    average=0
    if request.method=='POST':
        science = float(request.form['science'])
        maths= float(request.form['maths'])
        cpp = float(request.form['cpp'])
        datascience= float(request.form['datascience'])

        total_marks = maths+science+cpp+datascience
        average=total_marks/4
    else:
        return render_template('getresult.html')

    return redirect(url_for('successres', score=average))

if __name__ == "__main__":
    app.run(debug=True)




