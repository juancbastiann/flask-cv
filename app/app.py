from flask import Flask, render_template
from functions import edad_actual, fecha_letras

app = Flask(__name__)

@app.route('/')
def index():

    skills = ['HTML', 'PYTHON', 'JAVA']
    projects_html = ['Proyecto Solutions']
    projects_python = ['Proyecto Plantas de Energía']
    projects_java = ['Online Chat']

    links={
        'java_project_1' : 'https://github.com/juancbastiann/Messagechat',
        'python_project_1' : 'https://github.com/juancbastiann/proyecto-plantas-de-energia',
        'html_project_1' : 'https://juancbastiann.github.io/SOLUTIONS/'
    }

    personal_data={
        'full_name' : 'Juan Sebastian Altamirano Carrión',
        'age' : edad_actual,
        'date' : fecha_letras,
        'phone_number' : '0994013903',
        'email' : 'jsebastianaltamirano@gmail.com',
        'school' : 'Colegio de Bachillerato Arenillas, 2018',
        'university' : 'Universidad de Guayaquil',
        'image' : 'Screenshot 2023-06-05 081507.png'
    }

    data_projects={
        'skills' : skills,
        'projects_html' : projects_html,
        'projects_python' : projects_python,
        'projects_java' : projects_java
    }

    data={
        'title' : 'Curriculum Vitae'
    }
    return render_template('index.html', data=data, personal_data=personal_data, data_projects=data_projects, links=links)

if __name__ == '__main__':
    app.run(debug=True, port=5000)