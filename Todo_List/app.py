# from flask import Flask, render_template, request, url_for

# app=Flask(__name__)
# tasks=[]
# @app.route('/' , methods=['POST','GET'])

# def home():
#     new_task=request.form('task')
#     tasks.append(new_task)
#     return render_template('index1.html',tasks=tasks)   


# if __name__=='__main__':
#     app.run(debug=True)




# from flask import Flask, render_template, request

# app = Flask(__name__)

# tasks = []  # keep tasks globally

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         new_task = request.form['task']
#         tasks.append(new_task)
#     return render_template('index1.html', tasks=tasks) # it display index.html page and tasks=tasks dend 

# if __name__ == '__main__':
#     app.run(debug=True)






from flask import Flask , render_template, request
app=Flask(__name__)
tasks=[]
@app.route('/',methods=['POST','GET'])  # "/" as actoion because donot want to add extra page such as write a root as /add so my url will be 127.0.0.1:5000/add otherwise 127.0.0.1:5000 it open as locaaly without manual typing in seaechbar
def home():
    if request.method=='POST':
        new_task=request.form['task'] # task is submit buton in html file  when user clik + or "ADD" it goes to request and app.py python get the of html data  whenever user click of submit button. and python fetch the data from request by request.form('task') and then store that value in new_task 
        tasks.append(new_task)  # data from new_task, added to our actual list "tasks".
    # elif request.method=='POST'and request.value=='Delete':
    #    new_task=request.form['task']
    #    tasks.remove(new_task)
       
       
    return render_template('index1.html', tasks=tasks)   # shoes or display our index1. html and transfer the data from python(tasks-rightside) to html(tasks-leftside)



@app.route('/delete',methods=['POST','GET'])
def delete_task():
     if request.method=='POST':
       new_task=int(request.form['task_index'])
       tasks.pop(new_task)
           
     return render_template('index1.html',tasks=tasks)       
    
if __name__=='__main__' :
  app.run(debug=True)   