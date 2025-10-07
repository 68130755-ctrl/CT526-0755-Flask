from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')
    

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/myid')
def myid():
    return "รหัสนักศึกษา: 0755"

@app.route('/draw/<int:num>')
def draw(num):
    output = ""
    for i in range(num):
        output += "mmmm<br>"
    return f"<h3>การแสดงผล {num} แถว</h3><p>{output}</p>"

if __name__ == '__main__':
   app.run(debug=True)
