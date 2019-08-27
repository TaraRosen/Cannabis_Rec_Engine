from flask import Flask, render_template, request
from forms import *
from strains import strains_list


# lst = strains_list
current_selection =  ''
strain = '----'
strains = ['----','----','----','----','----']

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template('home.html', Recommendations=strains, strains=strains_list, your_strain=strain)

@app.route("/result", methods=['GET', 'POST'])
def result():
	if request.method == 'POST':
		strain = request.form['strains']
	strains = recommended_strains(strain)
	print(strain)
	return render_template('home.html', Recommendations=strains, strains=strains_list, your_strain=strain)


if __name__ == '__main__':
    app.run(debug=True)
