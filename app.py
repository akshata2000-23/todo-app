from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# with app.app_context():
#     db=SQLAlchemy(app)
    #db.session.add(Todo(title="example",desc="My example"))
    #db.session.commit()
    #users=db.session.execute(db.select(Todo)).scalars()
    #users=User.query.all()

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == "POST":
        title= request.form['title']
        desc= request.form['desc']
        print(title)
        print(desc)
        todo=Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    
    allTodos=Todo.query.all()
    #print(allTodos)
    return render_template('index.html',allTodos=allTodos)


@app.route('/show')
def products():
    allTodo= Todo.query.all()
    print(allTodo)
    return 'this is Products page'
if __name__ =="__main__":
    app.run(debug=True, host='0.0.0.0',port=5000)