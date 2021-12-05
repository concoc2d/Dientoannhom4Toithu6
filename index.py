from urllib import request
import manage_dynamodb
from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    list_table= manage_dynamodb.list_table()
    return render_template("index.html",list_table=list_table);
@app.route("/add_student",methods=['get', 'post'])
def add_student():
    msg = "msg"
    if request.method == 'POST':
        studentid = request.form["studentid"]
        lastName = request.form["lastName"]
        email = request.form["email"]
        contact = request.form["contact"]
        address=request.form["address"]
        classsv = request.form["classsv"]
        faculty = request.form["faculty"]

        manage_dynamodb.put_item(studentid, lastName, email, contact, address, classsv, faculty)
        return redirect(request.args.get("next", "/"))

    return render_template("add_student.html")
@app.route("/saverecord")
def saveRecord():

    return render_template("success_record.html")
@app.route('/api/chuyenbay', methods=['post'])
def thoigianbay():
    data = request.json
    cart = {
        "Thoigianbatdau": data["Thoigianbatdau"]
    }
    session['tg'] = cart
    return cart

@app.route("/delete_student",methods=['get', 'post'])
def delete_student():
    if request.method == 'POST':
        studentid = request.form["studentid"]
        lastName = request.form["lastName"]
        manage_dynamodb.delete_item(studentid, lastName)
    return render_template("delete_student.html")
@app.route("/create_table",methods=['get', 'post'])
def create_table():
    manage_dynamodb.create_dynamodb_table()
@app.route("/info_sinhvien",methods=['get', 'post'])
def get_student():
    if request.method == 'POST':
        studentid = request.form["studentid"]
        lastName = request.form["lastName"]
        res= manage_dynamodb.get_item(studentid, lastName)
        return render_template("detailssv.html",res=res)
    return render_template("infostudent.html")

@app.route("/student_info",methods=['get', 'post'])
def student_info():

    if request.method == 'POST':
        studentid = request.form["studentid"]
        lastName = request.form["lastName"]
        email = request.form["email"]
        contact = request.form["contact"]
        address=request.form["address"]
        classsv = request.form["classsv"]
        faculty = request.form["faculty"]
        manage_dynamodb.up_item(studentid, lastName, email, contact, address, classsv, faculty)

        return redirect(request.args.get("next", "/"))


    return render_template("student_info.html")
if __name__ == '__main__':
    app.run(host='0.0.0.0')