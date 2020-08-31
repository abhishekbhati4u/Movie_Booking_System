import sqlite3
import sqlite3
Movie=sqlite3.connect('movies.db')
movies_curs=Movie.cursor()

#A function to show the data present in the tables
def show_data():
	print("The data in the ticket table is as follows: ")
	print("\nTicketID,User Name,Phone No, Starting Time, Ending Time,Status")
	query="SELECT * FROM ticket"
	movies_curs.execute(query)
	rec=movies_curs.fetchall()
	for r in rec:
		print(r[0],",",r[1],",",r[2],",",r[3],":",r[4],",",r[5],":",r[6],",",r[7])
	query2="SELECT * FROM ticket_status"
	movies_curs.execute(query2)
	rows=movies_curs.fetchall()
	print("\nThe status of the various movie slots in the theatre is as follows: ")
	print("\nStarting Time,Ending Time,No. of tickets")
	for row in rows:
		print(row[1],":",row[2],",",row[3],":",row[4],",",row[0])

#Function to reserve a ticket for a user after checking the available slots
def reserve_ticket(usr_name,strt_hrs,strt_mins,end_hrs,end_mins):
	qu="SELECT * FROM ticket"
	movies_curs.execute(qu)
	res=movies_curs.fetchall()
	ticket_id=0
	if len(result)!=0:
		ticket_id=res[len(res)-1][0]+1
	st="Active"
	phone=input("Enter your phone number: ")
	movies_curs.execute("INSERT INTO ticket (TicketID,user_name,phone_no,start_hrs,start_mins,end_hrs,end_mins,status) VALUES (?,?,?,?,?,?,?,?);",(ticket_id,usr_name,phone,strt_hrs,strt_mins,end_hrs,end_mins,st))
	Movie.commit()

#Function to view the show times
def view_show_times():
	li=[[(10,00),(12,00)],
		[(12,30),(14,30)],
		[(15,00),(17,00)],
		[(17,30),(19,30)],
		[(20,00),(22,00)],]
	print("The available show times for the movie theatre are as follows:")
	for i in len(li):
		print(li[i][0][0],":",li[i][0][1],"-",li[i][1][0],":",li[i][1][1])
		movies_curs.execute("INSERT INTO ticket_status (no, start_hrs, start_mins, end_hrs, end_mins) VALUES (?,?,?,?,?);",(0,li[i][0][0],li[i][0][1],li[i][1][0],li[i][1][1]))
		movies_curs.commit()

#The calling function to book the ticket
def book_ticket():
	view_show_times()
	usr_name=input("Enter the name of the user: ")
	strt_hrs=int(input("Enter the starting time (hrs) of the movie: "))
	strt_mins=int(input("Enter the starting time (mins) of the movie: "))
	end_hrs=int(input("Enter the end time (hrs) of the movie: "))
	end_mins=int(input("Enter the end time (mins) of the movie: "))
	q="SELECT * FROM ticket_status"
	movies_curs.execute(q)
	result=movies_curs.fetchall()
	for record in result:
		if record[1]==start_hrs and record[2]==start_mins and record[3]==end_hrs and record[4]==end_mins and record[0]<20:
			reserve_ticket(usr_name,strt_hrs,strt_mins,end_hrs,end_mins)
		elif record[0]==20:
			print("Sorry, there are no tickets available in this slot.")
		else:
			print("Sorry, the slot you entered does not exist.")

#The main code of the program
print("Welcome to the movie ticket booking system")
print("Enter a choice from one of the following:")
print("1. Book a new ticket.")
print("2. View the status of the user tables.")
num=int(input("Enter your choice:"))
if num==1:
	book_ticket()
elif num==2:
	show_data()
else:
	print("You have enetered a wrong choice.")