from flask import Flask, render_template, request
app=Flask(__name__)
notes=list() # take list
@app.route('/',methods=['POST','GET'])
def home():
   if request.method=='POST':
     new_note={"title":request.form['title'],"content":request.form['description']}
     notes.append(new_note)
   return render_template('index1.html',notes=notes)

@app.route('/delete',methods=['POST','GET'])
def delete():

   if request.method=='POST':
    new_index=int(request.form['new_index'])
    notes.pop(new_index)
   return render_template('index1.html',notes=notes) 

if __name__=='__main__':
    app.run(debug=True)
