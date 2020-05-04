from flask import Flask,request
from flask import render_template
import jinja2


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
	if request.method == 'POST' and 'name' in request.form and 'age' in request.form:
		name = request.form.get("name")
		age = request.form.get("age")
		templateLoader = jinja2.FileSystemLoader(searchpath="./")
		templateEnv = jinja2.Environment(loader=templateLoader)
		TEMPLATE_FILE = "name.html"
		template = templateEnv.get_template(TEMPLATE_FILE)

		outputText = template.render(name=name,age=age)
		html_file = open(str('certificate' + '.html'), 'w')
		html_file.write(outputText)
		html_file.close()

		import pdfkit
		pdfkit.from_file('certificate' + '.html', 'certific' + '.pdf')
	return render_template("index.html")

app.run()
