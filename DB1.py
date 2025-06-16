import sqlite3
import datetime

def getdate():
    a = datetime.date.today()
    dt = str(a.day) + "/" + str(a.month) + "/" + str(a.year)
    return dt

def issue_book():
    # accept details of enr number and book number.
    # we will fetch current system date for idate. And rdate will be null
    en = input("Enter Student's Enrollment Number to Borrow the Book : ")
    b = input("Enter Book Number to Borrow : ")
    idt = getdate()
    q = "insert into all_issued(enrnum, bnumber, idate, rdate) values(" + en + "," + b + ",'" + idt + "', 'NA')"
    con = sqlite3.connect("lib_proj.db")
    con.execute(q)
    con.commit()
    con.close()
    print("Book Issued Successfully....")
    input()


def return_book():
    # accept book number and update the Rdate on that book number's record
    b = input("Enter Book number to Return : ")
    rdt = getdate()
    q = "update all_issued set rdate='" + rdt + "' where bnumber=" + b + " and rdate='NA'"
    con = sqlite3.connect("lib_proj.db")
    con.execute(q)
    con.commit()
    con.close()
    print("Book Returned...")
    input()

def not_ret_books():
    q="select enrnum,bnumber,idate from all_issued where rdate='NA'"
    con=sqlite3.connect("lib_proj.db")
    cur = con.cursor()
    cur.execute(q)
    d = cur.fetchall()
    print("Enrollment no.|| Book no. || Issue date")
    for a,b,c in d:
        print(a,'\t\t\t\t\t',b,'\t',c)
    input()
def book_history():
    bnum= int(input("Enter Book Number, to print book history : "))
    con = sqlite3.connect("lib_proj.db")
    cur=con.cursor()
    q = "select * from all_issued"
    cur.execute(q)
    d = cur.fetchall()
    print("Enrnum   ||  idate      || rdate ")
    for i in d:
            if i[1] == bnum :
                print(i[0],"\t\t\t",i[2]," \t",i[3])
    input()
def stud_history():
    enr = int(input("Enter Student's Enrollment Number, to print History : "))
    con = sqlite3.connect("lib_proj.db")
    cur = con.cursor()
    q = "select * from all_issued"
    cur.execute(q)
    d=cur.fetchall()
    print("Book no. || Issue date ||   Return date ")
    for i in d:
        if i[0]==enr:
            print(i[1],"\t\t\t",i[2],"\t\t",i[3])
    input()

def add_new_stud():
    # accept details of student and then insert it into DB table "all_stud" by using insert-query
    '''q = 'create table all_stud ( en numeric, n varchar(20),c varchar(12),e varchar(20),m numeric(10))'
    con = sqlite3.connect('lib_proj.db')
    con.execute(q)'''
    enr = input("Enter Student Enrollment Number : ")
    nm = input("Enter Student Name : ")
    cl = input("Enter Student Class : ")
    em = input("Enter Student Email : ")
    mo = input("Enter Student Contact Number : ")

    q = "insert into all_stud(en,n,c,e,m) values(" + enr + ",'" + nm + "','" + cl + "','" + em + "'," + mo + ")"
    con = sqlite3.connect("lib_proj.db")
    con.execute(q);
    con.commit()
    print("New Student Added....!")
    input()


def add_new_book():
   #q='create table book_info ( bn numeric, name varchar(20),author varchar(12))'
   #con=sqlite3.connect('lib_proj.db')
   #con.execute(q)
   bn = input("Enter Book number:")
   c = input("Enter book name:")
   s = input("Enter author:")

   q = "insert into book_info(bn,name,author) values(" + bn + ",'" + c + "','" + s + "')"
   con = sqlite3.connect("lib_proj.db")
   con.execute(q)
   con.commit()
   print("New Book Added....!")
   input()

def search_stud():

    enr = int(input("Enter Student's Enrollment Number: "))
    con = sqlite3.connect("lib_proj.db")
    cur = con.cursor()
    q = "select * from all_stud"
    cur.execute(q)
    d = cur.fetchall()
    print("Name || Class || Email             || Mobile no.")
    for i in d:
        if i[0] == enr:
            print(i[1], "\t", i[2], "\t", i[3], "\t\t", i[4])
    input()
def search_book():


    bnm = (input("Enter Book Name: "))
    con = sqlite3.connect("lib_proj.db")
    cur = con.cursor()
    q = "select * from book_info"
    cur.execute(q)
    d = cur.fetchall()
    for i in d:
        if i[1] == bnm:
            print(" Book no.     ||  Author ")
            print("\t",i[0], "\t\t", i[2])
while True:
    print("Select an operation")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - Not Returned Books")
    print("4 - Book History")
    print("5 - Student History")
    print("6 - Add New Student")
    print("7 - Add New Book")
    print("8 - Search Student")
    print("9 - Search Book")
    print("0 - Exit")
    ch = int(input("Provide your choice : "))

    if ch==1:
        issue_book()
    elif ch==2:
        return_book()
    elif ch==3:
        not_ret_books()
    elif ch==4:
        book_history()
    elif ch==5:
        stud_history()
    elif ch==6:
        add_new_stud()
    elif ch==7:
        add_new_book()
    elif ch==8:
        search_stud()
    elif ch==9:
        search_book()
    else:
        exit(0)

