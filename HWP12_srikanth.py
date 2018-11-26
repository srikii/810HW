from flask import Flask, render_template
import sqlite3  

db_file=r'D:\college\ssw 810\repo\database\810database.db'

app= Flask(__name__)

@app.route('/')
def hello():
    return "hello world, this is flask typing"

@app.route('/goodbye')
def see_ya():
    return "see you later buddy."

@app.route('/sample_template')
def template_demo():
    return render_template('parameters.html',
                            title="Stevens repository",
                            my_header="My Stevens Repository",
                            my_param="my custom parameters")

@app.route('/students')
def students_summary():
    students=[
        {'cwid': '11658',
        'name': 'Kelly, P',
        'major': 'SYEN', 
        'taken': ['SSW 540'],
        'remain':['SYS 621','SYS 671','SYS 672','SYS 673','SYS 674','SYS 800']
        },
        {'cwid': '11714',
        'name': 'Morton, A',
        'major': 'SYEN', 
        'taken': ['SYS 611', 'SYS 645'],
        'remain':['SYS 612','SYS 671','SYS 672','SYS 673','SYS 674','SYS 800']
        }
    ]
    return render_template('student_table.html',
                            title="Stevens Repository",
                            table_title="student summary",
                            students=students)
                            
@app.route('/instructor_courses')
def instructors():
    query='''select i.NAME, i.CWID, i.Dept, g.Course, count(g.student_CWID) as total_students 
    from instructors i join grades g on i.CWID=g.instructor_CWID
    group by i.cwid, g.course;'''

    db=sqlite3.connect(db_file)
    result=db.execute(query)

    data=[{'name': name, 'cwid': cwid, 'Dept': Dept, 'course':course, 'count':count}
        for name, cwid, Dept, course, count in result]
    
    db.close()

    return render_template('instructors_details.html',
                            title= 'Stevens Repository',
                            table_title='Number of students by course and instructors',
                            instructors=data)


app.run(debug=True)