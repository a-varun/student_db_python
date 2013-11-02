from Tkinter import *
from ttk import *
import tkMessageBox
from random import *
import MySQLdb

def ret_val(a):
	if a in "aA": return 9;
	if a in "sS": return 10;
	if a in "bB": return 8;
	if a in "cC": return 7;
	if a in "dD": return 6;
	if a in "eE": return 5;
	if a in "uU": return 0;
	if a in "ab": return 0;
	


def check_name_present( rollno, name, age,phonenumber ):
	db=MySQLdb.connect(host="localhost", user="varun", passwd="raghav", db="test_db");
	allrows=db.cursor()
	allrows.execute(" select * from student")
	for k in allrows:
		if( k[0]==rollno):
			return True;
	return False;

def check_regno(a):
	return a.isalpha
def check_grade(s):
	if (len(s)==1 and s in "aAbBcCdDeEfFuU" )or (len(s)==2 and s=="ab"):
		return True
	return False

def putmessage(a,b):
	tkMessageBox.showinfo(a,b, )



#Here da 
def get_semester_subjects(semester):
	db = MySQLdb.connect(host="localhost", user="varun", passwd="raghav", db="test_db");
	all_rows=db.cursor();
	all_rows.execute("select code, credits from batch_info where batch=%s"%(semester))
	ar=[{}]
	for row in all_rows:
		ar.append(dict([('subj', row[0]), ('credits', int(row[1]))]))
	return ar


class Mark_entry(Frame):
	
	def __init__(self, parent, semester):
		Frame.__init__(self, parent)   
		parent.lift()
		self.semester=semester
		self.parent = parent
		
		self.initUI()
	def put_in_db (self) :
		roll_no=self.rt1.get()
		name=self.rt2.get()
		stri=""
		stri+=roll_no+","+self.semester
		gpa=0.0
		check_name_present( roll_no, name)    	    	
		for j in self.rowtext:
			p=j.get()
			q=ret_val(p)
			gpa+=q
			stri+=",'"+selv.v[j+1]['subj']+"'"+","+str(q)+","
		for j in range (len(v), 11):
			stri+=",'', -1"
		gpa/=len(self.v)
		gpa=str(gpa)

		db = MySQLdb.connect(host="localhost", user="varun", passwd="raghav", db="test_db");
		cur=db.cursor();
		cur.execute("insert into sample values(%s, %s)" %(stri, gpa));
		#print "Updated"
		db.commit();
		db.close();

	
	def initUI(self):
	  
		self.parent.title("Grades Entry")
		self.v=get_semester_subjects(self.semester)

		Style().configure("TLabel", padding=(0, 98, 0, 98), font='serif 20')
		Style().configure("TText", padding=(0, 98, 0, 98), font='serif 20')
		Style().configure("TButton", padding=(0,98, 0, 98), font='serif 20')
		for i in range(len(self.v)+10):
			self.rowconfigure(i, pad=12)

		self.columnconfigure(0, pad=12)
		self.columnconfigure(1, pad=12)

		self.r1 = Label(self, text="Roll number")
		self.r1.grid(row=0, column=0)
		self.rt1 = Entry(self)
		self.rt1.grid(row=0, column=1)
		self.r2 = Label(self, text="Name")
		self.r2.grid(row=1, column=0)
		self.rt2 = Entry(self)
		self.rt2.grid(row=1, column=1)
		self.rowsubj=[]
		self.rowtext=[]
		for j in range(len(self.v)-1):
			temp= Label(self ,text= self.v[j+1]['subj'])
			self.rowsubj.append( temp)
			self.rowsubj[len(self.rowsubj)-1].grid(row=j+2, column=0)
			self.rowtext.append(Entry(self))
			self.rowtext[len(self.rowtext)-1].grid(row=j+2, column=1)
		button_it= Button(self, text="Enter it in the database", command= self.put_in_db);
		button_it.grid(row=len(self.v)+4, columnspan=2)
		self.pack()




class Batch_entry(Frame):
	
	def __init__(self, parent, semester):
		Frame.__init__(self, parent)   
		parent.lift()
		self.semester=semester
		self.parent = parent
		
		self.initUI()
	def put_in_db (self) :
		code=self.code.get()
		credit=self.credit.get()
		db = MySQLdb.connect(host="localhost", user="varun", passwd="raghav", db="test_db");
		cur=db.cursor();
		cur.execute("insert into batch_info values(%s, %s, %s)" %(str(self.semester), code, credit));
		print "Updated"
		db.commit();
		db.close();

	
	def initUI(self):
	  
		self.parent.title("Semester Subject Entry")
		self.v=get_semester_subjects(self.semester)

		Style().configure("TLabel", padding=(0, 98, 0, 98), font='serif 20')
		Style().configure("TText", padding=(0, 98, 0, 98), font='serif 20')
		Style().configure("TButton", padding=(0,98, 0, 98), font='serif 20')
		for i in range(len(self.v)+10):
			self.rowconfigure(i, pad=12)

		self.columnconfigure(0, pad=12)
		self.columnconfigure(1, pad=12)
		self.r2 = Label(self, text="Subject code")
		self.r2.grid(row=1, column=0)
		self.code = Entry(self)
		self.code.grid(row=1, column=1)
		self.r2 = Label(self, text="Credits")
		self.r2.grid(row=3, column=0)
		self.credit = Entry(self)
		self.credit.grid(row=3, column=1)
		button_it= Button(self, text="Enter it in the database", command= self.put_in_db);
		button_it.grid(row=len(self.v)+4, columnspan=2)
		self.pack()


class Mark_entry(Frame):
	
	def __init__(self, parent, semester):
		Frame.__init__(self, parent)   
		parent.lift()
		self.semester=semester
		self.parent = parent
		self.initUI()

	def put_in_db (self) :
		roll_no=self.rt1.get()
		db = MySQLdb.connect(host="localhost", user="varun", passwd="raghav", db="test_db");
		cur=db.cursor();
		tenum=1
		for j in self.rowtext:
			p=j.get()
			q=ret_val(p)
			cur.execute("insert into marks values(%s, %s, '%s', %s)" %(str(self.semester), roll_no, self.v[tenum]['subj'], str(q)));
			tenum+=1;
		print "Updated"
		db.commit();
		db.close();

	
	def initUI(self):
	  
		self.parent.title("Grades Entry")
		self.v=get_semester_subjects(self.semester)

		Style().configure("TLabel", padding=(0, 98, 0, 98), font='serif 20')
		Style().configure("TText", padding=(0, 98, 0, 98), font='serif 20')
		Style().configure("TButton", padding=(0,98, 0, 98), font='serif 20')
		for i in range(len(self.v)+10):
			self.rowconfigure(i, pad=12)

		self.columnconfigure(0, pad=12)
		self.columnconfigure(1, pad=12)

		self.r1 = Label(self, text="Roll number")
		self.r1.grid(row=0, column=0)
		self.rt1 = Entry(self)
		self.rt1.grid(row=0, column=1)
		self.r2 = Label(self, text="Name")
		self.r2.grid(row=1, column=0)
		self.rt2 = Entry(self)
		self.rt2.grid(row=1, column=1)
		self.rowsubj=[]
		self.rowtext=[]
		for j in range(len(self.v)-1):
			temp= Label(self ,text= self.v[j+1]['subj'])
			self.rowsubj.append( temp)
			self.rowsubj[len(self.rowsubj)-1].grid(row=j+2, column=0)
			self.rowtext.append(Entry(self))
			self.rowtext[len(self.rowtext)-1].grid(row=j+2, column=1)
		button_it= Button(self, text="Enter it in the database", command= self.put_in_db);
		button_it.grid(row=len(self.v)+4, columnspan=2)
		self.pack()



class find_result(Frame):
	
	def __init__(self, parent, semester):
		Frame.__init__(self, parent)   
		parent.lift()
		self.semester=semester
		self.parent = parent
		self.initUI()

	def get_values (self) :
		self.db = MySQLdb.connect(host="localhost", user="varun", passwd="raghav", db="test_db");
		self.cur=self.db.cursor();
		stud = self.rollno.get()
		self.cur.execute("select code,grade from marks where batch=%s and stud_id= %s"%(self.semester, stud));
		j=3
		Style().configure("TLabel", padding=(0, 98, 0, 98), font='serif 20')
		Style().configure("TText", padding=(0, 98, 0, 98), font='serif 20')
		Style().configure("TButton", padding=(0,98, 0, 98), font='serif 20')
		st=""
		gpa=0.0
		count=0
		for row in self.cur:
			st+=row[0]+'\t'
			st+=str(row[1])+'\n'
			gpa+=row[1]*randint(1,5)
			j+=1
			count+=1			
		st+="Gpa"+ '\t'+  str(gpa/count)+'\n'
		putmessage("Result",st)	
	def initUI(self):
	  
		self.parent.title("Result Display")
		self.v=get_semester_subjects(self.semester)

		Style().configure("TLabel", padding=(0, 98, 0, 98), font='serif 20')
		Style().configure("TText", padding=(0, 98, 0, 98), font='serif 20')
		Style().configure("TButton", padding=(0,98, 0, 98), font='serif 20')
		for i in range(110):
			self.rowconfigure(i, pad=2)

		self.columnconfigure(0, pad=2)
		self.columnconfigure(1, pad=2)

		self.r1 = Label(self, text="Student id")
		self.r1.grid(row=0, column=0)
		self.rollno = Entry(self)
		self.rollno.grid(row=0, column=1)
		button_it= Button(self, text="Find the Result", command= self.get_values);
		button_it.grid( row=2, column=1)
		self.pack()







class Batch_entry(Frame):
	
	def __init__(self, parent, semester):
		Frame.__init__(self, parent)   
		parent.lift()
		self.semester=semester
		self.parent = parent
		
		self.initUI()
	def put_in_db (self) :
		code=self.code.get()
		credit=self.credit.get()
		db = MySQLdb.connect(host="localhost", user="varun", passwd="raghav", db="test_db");
		cur=db.cursor();
		cur.execute("insert into batch_info values(%s, '%s', %s);" %(str(self.semester), code, credit));
		print "Updated"
		db.commit();
		db.close();

	
	def initUI(self):
	  
		self.parent.title("Semester Subject Entry")
		self.v=get_semester_subjects(self.semester)

		Style().configure("TLabel", padding=(0, 98, 0, 98), font='serif 20')
		Style().configure("TText", padding=(0, 98, 0, 98), font='serif 20')
		Style().configure("TButton", padding=(0,98, 0, 98), font='serif 20')
		for i in range(len(self.v)+10):
			self.rowconfigure(i, pad=12)

		self.columnconfigure(0, pad=12)
		self.columnconfigure(1, pad=12)
		self.r2 = Label(self, text="Subject code")
		self.r2.grid(row=1, column=0)
		self.code = Entry(self)
		self.code.grid(row=1, column=1)
		self.r2 = Label(self, text="Credits")
		self.r2.grid(row=3, column=0)
		self.credit = Entry(self)
		self.credit.grid(row=3, column=1)
		button_it= Button(self, text="Enter it in the database", command= self.put_in_db);
		button_it.grid(row=len(self.v)+4, columnspan=2)
		self.pack()
class Mainframe(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)   
		 
		self.parent = parent
		
		self.initUI()
	def getdataval(self):
		root1= Tk()
		p=self.sem.get()
		if p.isalpha() or len(p)==0:
			putmessage("Invalid Semester", "Please enter a correct Semester Value")
			return
		print p
		semester=int(p)
		if semester>8:
			putmessage("Invalid Semester", "Please enter a correct Semester Value")
			return

		root1.geometry("300x300")
		app1=Mark_entry(root1, semester)

	def getsemsubj (self):
		
		root1=Tk()
		p=self.sem.get()
		if p.isalpha() or len(p)==0:
			putmessage("Invalid Semester", "Please enter a correct Semester Value")
			return
		print p
		semester=int(p)
		if semester>8:
			putmessage("Invalid Semester", "Please enter a correct Semester Value")
			return
		root1.geometry("300x300")
		app1=Batch_entry(root1, semester)
	def findresult (self):
		
		root1=Tk()
		p=self.sem.get()
		if p.isalpha() or len(p)==0:
			putmessage("Invalid Semester", "Please enter a correct Semester Value")
			return
		print p
		semester=int(p)
		if semester>8:
			putmessage("Invalid Semester", "Please enter a correct Semester Value")
			return
		root1.geometry("300x300")
		app1=find_result(root1, semester)

	def initUI(self):
	  
		self.parent.title("Grades Entry")
		Style().configure("TLabel", padding=(0, 28, 0, 28), font='serif 20')
		Style().configure("TText", padding=(0, 28, 0, 28), font='serif 20')
		Style().configure("TButton", padding=(0, 28, 0, 28), font='serif 20')
		self.rowconfigure(0, pad=8)
		self.rowconfigure(1, pad=8)
		self.rowconfigure(2, pad=8)
		self.rowconfigure(3, pad=8)
		self.rowconfigure(4, pad=8)
		self.rowconfigure(5, pad=8)
		self.rowconfigure(6, pad=8)
		self.columnconfigure(0, pad=8)
		self.columnconfigure(1, pad=8)
		root1 = Tk()      
		self.sem=Entry(self)
		self.sem.grid(row=1, columnspan=2)
		button_for_batch=Button(self, text="Enter subjects for a Semester", command= self.getsemsubj);
		button_for_batch.grid(row=2,columnspan=2)
		button_it= Button(self, text="Enter values in the database", command= self.getdataval);
		button_it.grid(row=3, columnspan=2)
		button_it= Button(self, text="Find out the results of a student ", command= self.findresult);
		button_it.grid(row=4, columnspan=2)

		self.pack()



root = Tk()
root.geometry("3000x3000")
app = Mainframe(root)
root.mainloop() 
