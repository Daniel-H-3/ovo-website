from flask import Flask
from flask import abort
from flask import render_template
from flask import url_for
from jinja2 import  FileSystemLoader
from jinja2 import Environment


app = Flask(__name__)


@app.route('/')
def homepage():
    workers_list = ['dan', 'joe', 'michal', 'will']
    workers_dict = {'dan': 15, 'joe': 25, 'michal': 32, 'will': 25}

    return render_template('homepage.html', workers_list=workers_list, workers_dict=workers_dict)


@app.route('/people/<name>')
def peoplepage(name):
    available_people = ['michal', 'dan', 'will', 'joe']
    name = name.lower()
########## Dummy variables - practices ##################################################################################
    new_var = 'abcd'
    new_string = 'this is value for new_var: {new_var}'.format(new_var=new_var)
    another_string = f'this is value for new_var: {new_var}'
    url_for_this_project = 'C:\projects\dan'
    another_url = r'\\ovoflow\OvoForecasting\OvoForecasting Data\new\\'
    print(url_for_this_project)
    print(another_url)
########################################################################################################################

    print(new_string)
    print(another_string)
    if name in available_people:
        name = name[0].upper() + name[1:]
        return f"""
        <h1>Welcome To {name}'s Profile Page</h1>
        <a href="/people/{name}/page">{name}'s Profile</a>
        """

    else:
        abort(404)


@app.route('/people/<name>/page')
def personpage(name):
        return render_template(f'{name}.html')

@app.errorhandler(404)
def pagenotfound(e):
    return render_template('404error.html'), 404

if __name__ == '__main__':
    app.run()
