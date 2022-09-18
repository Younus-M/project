import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="atm"
)
mycursor=mydb.cursor()

print("welcome to atm")
choose_your_choice=int(input("press 1 for login & 0 for registe:"))
password=""
myname=""
depo=""
id=""


if choose_your_choice==0:
    name=input("enter your name:")
    account_number=int(input("ente your account number:"))
    amount=int(input("enter starting amount u want to depasite:"))
    password=int(input("set your password"))
    
    myname=name
    password=password
    depo=amount
    id=account_number

    val=(myname,password,depo,id)

    sql="insert into atm_register(my_name,pass_word,de_po,i_d) values (%s,%s,%s,%s)"
    mycursor.execute(sql,val)
    print("sucessfully")
    mydb.commit()


    
if choose_your_choice==1:
    info=int(input("enter your id:"))
    password=int(input("enter password:"))
    mycursor.execute(f"select * from atm_register where i_d='%s'"%{info}) 
    row=mycursor.fetchone()
    print("sucessfully")
    if mycursor.rowcount==1:

        mycursor.execute(f"select * from atm_resiter where pass_wod='%s'"%{password})
        row=mycursor.fetchone()
        if mycursor.rowcount==1:
            print("login successful")
            
            d=int(input("enter 1 withdrawl or 2 for depasit & 3 for exit:"))
            
            if d==1:
                a=int(input("hoe much you want to withdrawl:"))
                mycursor.execute("""select de_po from atm_regiter where pass_wors='%s'"""%{password})
                col=mycursor.fetchone()
                x=list(col)
                for i in x:
                    z=(int(i))
                    c=z-a
                mycursor.execute("""update atm_regiter set de_po='%s' whare pass_word='%s'"""%{c,password})


            if d==2:
                a=int(input("how much you want to depasite:"))
                mycursor.execute("""select de_po from atm_register where pass_word='%s'"""%{password})
                col=mycursor.fetchone()
                x=list(col)
                for i in x:
                    z=(int(i))
                    c=z+a
                mycursor.execute("""update atm_regiter set de_po='%s' where'%s'"""%{c,password})



            if d==3:
                    exit(0)
            else:
                print("invalid password")
        else:
            print("account doesn't exist")
            mydb.commit()
