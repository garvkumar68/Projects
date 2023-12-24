import mysql.connector
from csv import DictWriter
from csv import DictReader
import os

conn = mysql.connector.connect(host='localhost', username='root',password='garv', database='flights')
my_cursor = conn.cursor()

print("\n***********WELCOME TO FLIGHT BOOKING SYSTEM***********")

acc = input("\nDO YOU HAVE A ACCOUNT (Y/N): ")
e = []
if acc=='y' or acc=='yes' or acc=='Y' or acc=='YES':
    email = input("\nENTER YOUR EMAIL ID: ")
    e.append(email)
    pas = input("\nENTER YOUR PASSWORD: ")
    IN = " select * from userinfo1 where email='{}' and pass='{}'".format(email,pas)
    my_cursor.execute(IN)
    for user in my_cursor:
        print(user)
    print("\n-------------------------------")
    print("\n-------LOGIN SUCCESSFUL-------")
    print("\n-------------------------------")
    
else:
    nam = input("\nENTER YOUR FULL NAME: ")
    pn = int(input("\nENTER YOUR PHONE NO: "))
    city = input("\nENTER YOUR CITY NAME: ")
    state = input("\nENTER YOUR STATE: ")
    em = input("\nENTER YOUR EMAIL ID: ")
    e.append(em)
    passw = input("\nENTER YOUR PASSWORD: ")
    NAM = "INSERT INTO userinfo1(fullname,PhNo,city,state,email,pass) values('{}','{}','{}','{}','{}','{}')".format(nam,pn,city,state,em,passw)
    my_cursor.execute(NAM)
    conn.commit()
    query420 = "SELECT * FROM userinfo1 WHERE PhNo = '{}' ".format(pn)
    my_cursor.execute(query420)
    for z in my_cursor:
        print(z)
    print("\n--------------------------------------------------")
    print("\n-------YOUR ACCOUNT IS CREATED SUCCESSFULLY-------")
    print("\n--------------------------------------------------")    


print("\nhow do you want to search your flight by")
print("1.flight number")
print("2.manually")

ans = int(input("\nAnswer (1/2): "))


if ans==1:
    num = (input("\nENTER FLIGHT NUMBER: "))
    query85 = "SELECT AIRLINES_NAME FROM FLIGHTS WHERE FLIGHT_NO = '{}' ".format(num)
    query86 = "SELECT DEPARTURE FROM FLIGHTS WHERE FLIGHT_NO = '{}' ".format(num)
    query87 = "SELECT DESTINATION airlines_name FROM FLIGHTS WHERE FLIGHT_NO = '{}' ".format(num)
    query88 = "SELECT FLIGHT_NO FROM FLIGHTS WHERE FLIGHT_NO = '{}' ".format(num)
    query89 = "SELECT TIME_OF_DEPARTURE FROM FLIGHTS WHERE FLIGHT_NO = '{}' ".format(num)
    query90 = "SELECT TIME_OF_ARRIVAL FROM FLIGHTS WHERE FLIGHT_NO = '{}' ".format(num)
    query91 = "SELECT CHARGES FROM FLIGHTS WHERE FLIGHT_NO = '{}' ".format(num)
    print("\n----------------YOUR FLIGHT DATA----------------")   
    my_cursor.execute(query85)
    for a in my_cursor:
        print("AIRLINES_NAME:",a)
    
    my_cursor.execute(query86)
    for b in my_cursor:
        print("DEPARTURE:",b)
    my_cursor.execute(query87)
    for c in my_cursor:
        print("DESTINATION:",c)

    my_cursor.execute(query88)
    for d in my_cursor:
        print("FLIGHT NO:",d)
        
    my_cursor.execute(query89)
    for e in my_cursor:
        print("TIME OF DEPARTURE:",e)
        
    my_cursor.execute(query90)
    for d in my_cursor:
        print("TIME OF ARRIVAL:",d)
        
    my_cursor.execute(query91)
    for e in my_cursor:
        print("CHARGES:",e)

    for f in my_cursor:
        print(f)




deplo = []
arrlo = []
fli = []

def flight_data():   
    departure = input("\nENTER YOUR DEPARTURE LOCAION: ")
    arrival = input("\nENTER YOUR ARRIVAL LOCATION: ")
    query2 = "SELECT AIRLINES_NAME FROM FLIGHTS WHERE DEPARTURE = '{}' AND DESTINATION = '{}'".format(departure, arrival)
    deplo.append(departure)
    arrlo.append(arrival)
    my_cursor.execute(query2)
    print("\nYOUR REQUIRED FLIGHTS ARE------")
    for b in my_cursor:
        print(b) 
    fly = input("\nENTER A FLIGHT NAME YOU WANT: ")
    fli.append(fly)
    print("\nHEAR THE DETAILS OF YOUR FLIGHT--")
    query3 = "SELECT * FROM FLIGHTS WHERE AIRLINES_NAME = '{}' AND DEPARTURE = '{}' AND DESTINATION = '{}' ".format(fly, departure, arrival)
    my_cursor.execute(query3)
    for c in my_cursor:
        return print(c)
        
        

if ans==2:
    flight_data()
    

con = input("\nWOULD YOU LIKE TO CONTINUE (Y/N): ")
while True:
    if con=='n' or con=='N' or con=='no' or con=='NO':
        flight_data()
    else:
        break

passenger = int(input("\nENTER THE NUMBER OF PASSANGERS: "))

nam=[]
ag=[]
gen=[]

def pass_data():
    name = input("\nENTER THE NAME OF A PASSENGER: ")
    age = int(input(f"\nENTER THE AGE OF {name}: "))
    gender = input("\nMALE/FEMALE: ")
    nam.append(name)
    ag.append(age)
    gen.append(gender)
    with open('userdata.csv', 'a', newline='') as csvfile:
        csvwriter = DictWriter(csvfile, fieldnames=['name', 'age', 'gender'])
        csvwriter.writeheader()
        csvwriter.writerow({'name':name, 'age':age, 'gender':gender})
    return print("\n-------DATA ENTERED SUCCESSFULLY-------")        

for d in range(passenger):
        pass_data()

def read_csv():
    with open('userdata.csv') as csvreader:
        reader = DictReader(csvreader)
        for row in reader:
            print(row)
    os.remove(r'userdata.csv')
    return print("------------------------------------")
read_csv()
print("\nCHECK YOUR DETAILS----")

ch = input("\nDO YOU WANT TO CONTINUE (Y/N): ")

while True:
    if ch=='n' or ch=='N' or ch=='no' or ch=='NO':
        for e in range(passenger):
            pass_data()
        read_csv()
    else:
        break

print("\nCHOOSE THE CLASS YOU WANT: ")
print("1.ECONOMY CLASS")
print("2.BUSINESS CLASS (+20% CHARGES)")
print("3.FIRST CLASS (+40% CHARGES)")

flo = []
tdep = []
tarr= []

def fl_nm():
    query4 = "SELECT FLIGHT_NO FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (fli[0], deplo[0], arrlo[0])
    my_cursor.execute(query4)
    for f in my_cursor:
        flo.append(f)

    query5 = "SELECT TIME_OF_DEPARTURE FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (fli[0], deplo[0], arrlo[0])
    my_cursor.execute(query5)
    for g in my_cursor:
        tdep.append(g)

    query6 = "SELECT TIME_OF_ARRIVAL FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (fli[0], deplo[0], arrlo[0])
    my_cursor.execute(query6)
    for h in my_cursor:
        tarr.append(h)

an = []
de = []
ds = []
td = []
ta = []

def fl_no():
    query7 = "SELECT AIRLINES_NAME FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(num)
    my_cursor.execute(query7)
    for i in my_cursor:
        an.append(i)

    query8 = "SELECT DEPARTURE FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(num)
    my_cursor.execute(query8)
    for j in my_cursor:
        de.append(j)

    query9 = "SELECT DESTINATION FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(num)
    my_cursor.execute(query9)
    for k in my_cursor:
        ds.append(k) 

    query10 = "SELECT TIME_OF_DEPARTURE FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(num)
    my_cursor.execute(query10)
    for l in my_cursor:
        td.append(l)

    query11 = "SELECT TIME_OF_ARRIVAL FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(num)
    my_cursor.execute(query11)
    for m in my_cursor:
        ta.append(m)

cl = int(input("\nENTER CLASS NO (1/2/3):-"))

payment = []

if ans==1 and cl==1:
    fl_no()
    query12 = "SELECT CHARGES*{} FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format(passenger, num)
    my_cursor.execute(query12)
    print("\nname = ", nam,"\nage = ", ag,"\ngender = ", gen)
    print("flight name = ", an,"\ndeparture = ", de,"\ndestination = ", ds)
    print("flight number = ", num,"\ndeparture time = ", td,"\narrival time = ", ta)
    print("class = economy class")
    for n in my_cursor:
        payment.append(n)
        print("f\nYOU HAVE TO PAY", n,"RUPEES")

elif ans==1 and cl==2:
    fl_no()
    query13 = "SELECT (CHARGES +CHARGES*0.2)*{} FROM FLIGHTS WHERE flight_no = '{}' ".format (passenger, num)
    my_cursor.execute(query13)
    print("\nname = ", nam,"\nage = ", ag,"\ngender = ", gen)
    print("flight name = ", an,"\ndeparture = ", de,"\ndestination = ", ds)
    print("flight number = ", num,"\ndeparture time = ", td,"\narrival time = ", ta)
    print("class = business class")
    for o in my_cursor:
        payment.append(o)
        print("f\nYOU HAVE TO PAY", {o},"RUPEES") 

elif ans==1 and cl==3:
    fl_no()
    query14 = "SELECT (CHARGES +CHARGES*0.4)*{} FROM FLIGHTS WHERE FLIGHT_NO = '{}'".format (passenger, num)
    my_cursor.execute(query14)
    print("\nname = ", nam,"\nage = ", ag,"\ngender = ", gen)
    print("flight name = ", an,"\ndeparture = ", de,"\ndestination = ", ds)
    print("flight number = ", num,"\ndeparture time = ", td,"\narrival time = ", ta)
    print("class = first class")
    for p in my_cursor:
        payment.append(p)
        print("f\nYOU HAVE TO PAY", p,"RUPEES")


elif ans==2 and cl==1:
    fl_nm()
    query15 = "SELECT CHARGES*{} FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (passenger, fli[0], deplo[0], arrlo[0])
    my_cursor.execute(query15)
    print("\nname = ", nam,"\nage = ", ag,"\ngender = ", gen)
    print("flight name = ", an,"\ndeparture = ", de,"\ndestination = ", ds)
    print("flight number = ", num,"\ndeparture time = ", td,"\narrival time = ", ta)
    print("class = economy class")
    for q in my_cursor:
        payment.append(q)
        print("f\nYOU HAVE TO PAY", q,"RUPEES") 

elif  ans==2 and cl==2:
    fl_nm()
    query16 = "SELECT (CHARGES +CHARGES*0.2)*{} FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (passenger, fli[0], deplo[0], arrlo[0])
    my_cursor.execute(query16)
    print("\nname = ", nam,"\nage = ", ag,"\ngender = ", gen)
    print("flight name = ", an,"\ndeparture = ", de,"\ndestination = ", ds)
    print("flight number = ", num,"\ndeparture time = ", td,"\narrival time = ", ta)
    print("class = business class")
    for r in my_cursor:
        payment.append(r)
        print("f\nYOU HAVE TO PAY", r," RUPEES")  

elif ans==2 and cl==3:
    fl_nm()
    query17 = "SELECT (CHARGES +CHARGES*0.4)*{} FROM FLIGHTS WHERE airlines_name = '{}' and DEPARTURE = '{}' and DESTINATION = '{}' ".format (passenger, fli[0], deplo[0], arrlo[0])
    my_cursor.execute(query17)
    print("\nname = ", nam,"\nage = ", ag,"\ngender = ", gen)
    print("flight name = ", an,"\ndeparture = ", de,"\ndestination = ", ds)
    print("flight number = ", num,"\ndeparture time = ", td,"\narrival time = ", ta)
    print("class = first class")
    for s in my_cursor:
        payment.append(s)
        print("f\nYOU HAVE TO PAY", s," RUPEES")

pay = input("\nTO PAY PRESS (P):-")

if pay=='p' or pay=='P':
    print("\nHOW YOU WANT TO PAY ?")
    print("1.GOOGLE PAY")
    print("2.AMAZON PAY")
    print("3.PAYPAL")
    print("4.APPLE PAY")
    print("5.CREDIT CARD")
    print("6.DEBIT CARD")
    print("7.BANK TRANSFER")

pay2 = int(input("\nENTER YOUR PAYMENT METHOD (1/2/3/4/5/6/7): "))

if pay2==1:
    print("\n-------------------GOOGLE PAY---------------------------")
    print("PAY", payment[0], "RUPEES")
    pay3 = input("\nTO CONTINUE PAYMENT PRESS (P): ")
    print("\nTRANSACTION SUCCESSFUL------------")
    print("\n**********THANK YOU***********")

if pay2==2:
    print("\n-------------------AMAZON PAY---------------------------")
    print("PAY", payment[0], "RUPEES")
    pay3 = input("\nTO CONTINUE PAYMENT PRESS (P): ")
    print("\nTRANSACTION SUCCESSFUL------------")
    print("\n**********THANK YOU***********")
    
if pay2==3:
    print("\n-------------------PAYPAL---------------------------")
    print("PAY", payment[0], "RUPEES")
    pay3 = input("\nTO CONTINUE PAYMENT PRESS (P): ")
    print("\nTRANSACTION SUCCESSFUL------------")
    print("**********THANK YOU***********")

if pay2==4:
    print("\n-------------------APPLE PAY---------------------------")
    print("PAY", payment[0], "RUPEES")
    pay3 = input("\nTO CONTINUE PAYMENT PRESS (P): ")
    print("\nTRANSACTION SUCCESSFUL------------")
    print("**********THANK YOU***********")

if pay2==5 or pay2==6 or pay2==7:
    print("\n-------------------CARD PAYMENT---------------------------")
    print("PAY", payment[0], "RUPEES")
    c_no = int(input("\nENTER YOUR CARD NO: "))
    cvv = int(input("\nENTER YOUR CVV:-"))
    print("\nTRANSACTION SUCCESSFUL------------")
    print("**********THANK YOU***********")

print("\n--------THANKS FOR USING FLIGHT BOOKING SYSTEM--------------")
print("\nYOUR TICKETS ARE SENT TO YOUR EMAIL: ", em)
print("\nSEE YOU LATER :)")



conn.close()
