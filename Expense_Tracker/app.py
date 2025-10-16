from flask import Flask , render_template, request

app=Flask(__name__)

expenses=list()
@app.route('/', methods=['POST','GET'])
def home():
  if request.method=='POST':
    new_expen={'detail':request.form['detail'],'price':int(request.form['price'])}
    expenses.append(new_expen)
  total_sum=sum(expens['price'] for expens in expenses)
  return render_template('index1.html',expenses=expenses, total_sum=total_sum)  

@app.route('/delete',methods=['POST'])
def delete():
  if request.method=='POST':
   new_index=int(request.form['new_index'])
   expenses.pop(new_index)
  total_sum=sum(expens['price'] for expens in expenses)
  return render_template('index1.html', expenses=expenses, total_sum=total_sum) 


if __name__=='__main__':
   app.run(debug=True)