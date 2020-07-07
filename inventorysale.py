#import module
from tkinter import *
import tkinter.messagebox
import sqlite3

#class for frontend
class Product:
    def __init__(self,root):

        p=Database()
        p.conn()
        
        
        self.root=root
        self.root.title("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM")
        self.root.geometry("700x700")
        self.root.config(bg="grey")

        pID=StringVar()
        pName=StringVar()
        pPrice=StringVar()
        pQty=StringVar()
        pCompany=StringVar()
        pContact=StringVar()


        ''' lets call the database method to perform database operations'''
        def close():
            print("Product:closed method called")
            close=tkinter.messagebox.askyesno("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM","really........do you want to close the system")
            if close>0:
                root.destroy()
                print("Product:closed mehod finished\n")
                return

        def clear():
            print("Product:clear method called")
            self.txtpID.delete(0,END)
            self.txtpName.delete(0,END)
            self.txtpPrice.delete(0,END)
            self.txtpQty.delete(0,END)
            self.txtpCompany.delete(0,END)
            self.txtpContact.delete(0,END)
            print("Product:clear method finished")


        def insert():
            print("Product:insert method called")
            if (len(pID.get())!=0):
                p.insert(pID.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
                ProductList.delete(0,END)
                ProductList.insert(END,pID.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
                showInProductList() #called showproduct() method after inaerting the data 
            else:
                tkinter.messagebox.askyesno("WAREHOUSE INVENTORY SALES PURCHASE MANAGEMENT SYSTEM","really........Enter product id")
            
            print("Product:insert method called")


        def showInProductList():
            print("Product:showproduct method called")
            ProductList.delete(0,END)
            for row in p.show():
                ProductList.insert(END,row,str(""))
            print("Product:showproduct method called")


        def productrec(event):#func call from scroll bar
            print("Product:productrec method called")
            global pd
            searchpd= ProductList.curselection()[0]
            pd= ProductList.get(searchpd)
            self.txtpID.delete(0,END)
            self.txtpID.insert(END,pd[0])

            self.txtpName.delete(0,END)
            self.txtpName.insert(END,pd[1])
            
            self.txtpPrice.delete(0,END)
            self.txtpPrice.insert(END,pd[2])
            
            self.txtpQty.delete(0,END)
            self.txtpQty.insert(END,pd[3])
            
            self.txtpCompany.delete(0,END)
            self.txtpCompany.insert(END,pd[4])
            
            self.txtpContact.delete(0,END)
            self.txtpContact.insert(END,pd[5])
            print("Product:productrec method finished")

        def delete():
            
            print("Product:del method called")
            if(len(pID.get())!=0):
                p.delete(pd[0])
                clear()
                showInProductList()
            print("Product:del method finished")


        def search():
            
            print("Product:search method called")
            ProductList.delete(0,END)
            for row in p.search(pID.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get()):
                ProductList.insert(END,row,str(""))
            print("Product:search method finished")

        def update():
            print("Product:update method called:")
            if(len(pID.get())!=0):
               print("pd[0]","pd[p]")
               p.delete(pd[0])
            if(len(pID.get())!=0):
               p.insert(pID.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
               ProductList.delete(0,END)
            ProductList.insert(END,pID.get(),pName.get(),pPrice.get(),pQty.get(),pCompany.get(),pContact.get())
            print("Product:update method finished:")
            
                
        '''create frame'''
        MainFrame= Frame(self.root,bg="red")
        MainFrame.grid()

        HeadFrame=Frame(MainFrame,bd=1,padx=20,pady=20,bg='green',relief=RIDGE)
        HeadFrame.pack(side=TOP)

        self.ITitle=Label(HeadFrame,font=('arial',34,'bold'),fg='red',
                         text="WAREHOUSE INVENTORY SALES MANAGEMENT SYSTEM",bg='yellow')
        self.ITitle.grid()


        OperationalFrame=Frame(MainFrame,bd=2,width=1310,height=60,padx=17,pady=20,bg='white',relief=RIDGE)
        OperationalFrame.pack(side=BOTTOM)


        BodyFrame=Frame(MainFrame,bd=2,width=1310,height=500,padx=17,pady=20,bg='white',relief=RIDGE)
        BodyFrame.pack(side=BOTTOM)

        LBodyFrame=LabelFrame(BodyFrame,bd=2,width=500,height=500,padx=20,pady=10,bg='#5CB08F',relief=RIDGE,font=('arial',15,'bold'),
                              text='Product Items Details:')
        LBodyFrame.pack(side=LEFT)

        RBodyFrame=LabelFrame(BodyFrame,bd=2,width=600,height=380,padx=20,pady=10,bg='#5CB08F',relief=RIDGE,font=('arial',15,'bold'),
                              text='Product Items Information:')
        RBodyFrame.pack(side=RIGHT)


        '''add widget'''

        self.labelpID=Label(LBodyFrame,font=('arial',20,'bold'),text="Product Id:",padx=2,pady=2,bg='white',fg="blue")
        self.labelpID.grid(row=0,column=0,sticky=W)
        self.txtpID=Entry(LBodyFrame,font=('arial',20,'bold'),textvariable=pID,width=30)
        self.txtpID.grid(row=0,column=1,sticky=W)


        self.labelpName=Label(LBodyFrame,font=('arial',20,'bold'),text="Product Name:",padx=2,pady=2,bg='white',fg="blue")
        self.labelpName.grid(row=1,column=0,sticky=W)
        self.txtpName=Entry(LBodyFrame,font=('arial',20,'bold'),textvariable=pName,width=30)
        self.txtpName.grid(row=1,column=1,sticky=W)


        self.labelpPrice=Label(LBodyFrame,font=('arial',20,'bold'),text="Product Price:",padx=2,pady=2,bg='white',fg="blue")
        self.labelpPrice.grid(row=2,column=0,sticky=W)
        self.txtpPrice=Entry(LBodyFrame,font=('arial',20,'bold'),textvariable=pPrice,width=30)
        self.txtpPrice.grid(row=2,column=1,sticky=W)


        self.labelpQty=Label(LBodyFrame,font=('arial',20,'bold'),text="Product qunantity:",padx=2,pady=2,bg='white',fg="blue")
        self.labelpQty.grid(row=3,column=0,sticky=W)
        self.txtpQty=Entry(LBodyFrame,font=('arial',20,'bold'),textvariable=pQty,width=30)
        self.txtpQty.grid(row=3,column=1,sticky=W)


        self.labelpCompany=Label(LBodyFrame,font=('arial',20,'bold'),text="Mfg.Company:",padx=2,pady=2,bg='white',fg="blue")
        self.labelpCompany.grid(row=4,column=0,sticky=W)
        self.txtpCompany=Entry(LBodyFrame,font=('arial',20,'bold'),textvariable=pCompany,width=30)
        self.txtpCompany.grid(row=4,column=1,sticky=W)


        self.labelpContact=Label(LBodyFrame,font=('arial',20,'bold'),text="Company Contact:",padx=2,pady=2,bg='white',fg="blue")
        self.labelpContact.grid(row=5,column=0,sticky=W)
        self.txtpContact=Entry(LBodyFrame,font=('arial',20,'bold'),textvariable=pContact,width=30)
        self.txtpContact.grid(row=5,column=1,sticky=W)

        self.labelpC1=Label(LBodyFrame,padx=2,pady=2)
        self.labelpC1.grid(row=6,column=0,sticky=W)
        
                          
        self.labelpC2=Label(LBodyFrame,padx=2,pady=2)
        self.labelpC2.grid(row=7,column=0,sticky=W)

        self.labelpC3=Label(LBodyFrame,padx=2,pady=2)
        self.labelpC3.grid(row=8,column=0,sticky=W)
        self.labelpC4=Label(LBodyFrame,padx=2,pady=2)
        self.labelpC4.grid(row=9,column=0,sticky=W)
        

        '''right widget'''
        scroll=Scrollbar(RBodyFrame)
        scroll.grid(row=0,column=1,sticky='ns')
        
        ProductList=Listbox(RBodyFrame,width=40,height=16,font=('arial',12,'bold'),yscrollcommand=scroll.set)
        ProductList.bind('<<ListboxSelect>>',productrec)
        ProductList.grid(row=0,column=0,padx=9)

        scroll.config(command=ProductList.yview)
                        
        '''button'''
        self.buttonSave=Button(OperationalFrame,text='Save',font=('arial',20,'bold'),height=1,width='10',bd=4,command=insert)
        self.buttonSave.grid(row=0,column=0)

        self.buttonShow=Button(OperationalFrame,text='Show',font=('arial',20,'bold'),height=1,width='10',bd=4,command=showInProductList)
        self.buttonShow.grid(row=0,column=1)

        self.buttonClear=Button(OperationalFrame,text='Reset',font=('arial',20,'bold'),height=1,width='10',bd=4,command=clear)
        self.buttonClear.grid(row=0,column=2)

        self.buttonDel=Button(OperationalFrame,text='Del',font=('arial',20,'bold'),height=1,width='10',bd=4,command=delete)
        self.buttonDel.grid(row=0,column=3)

        self.buttonSearch=Button(OperationalFrame,text='Search',font=('arial',20,'bold'),height=1,width='10',bd=4,command=search)
        self.buttonSearch.grid(row=0,column=4)

        self.buttonUpd=Button(OperationalFrame,text='Update',font=('arial',20,'bold'),height=1,width='10',bd=4,command=update)
        self.buttonUpd.grid(row=0,column=5)

        self.buttonClose=Button(OperationalFrame,text='Close',font=('arial',20,'bold'),height=1,width='10',bd=4,command=close)
        self.buttonClose.grid(row=0,column=6)
        
'''backend database operations'''

class Database:
    def conn(self):
        print("Database: connection method called")
        con=sqlite3.connect("inventory.db")
        cur=con.cursor()
        query="create table if not exists product(pid integer primary key,\
             pname text,price text,qty text,company text,contact text)"
        cur.execute(query)
        con.commit()
        con.close()
        print("Database:Connection method finished\n")

    def insert(self,pid,name,price,qty,company,contact):
        print("Database: insert method called")
        con=sqlite3.connect("inventory.db")
        cur=con.cursor()
        query="insert into product values(?,?,?,?,?,?)"
        cur.execute(query,(pid,name,price,qty,company,contact))
        con.commit()
        con.close()
        print("Database:insert method finished\n")

    def show(self):
        print("Database: insert method called")
        con=sqlite3.connect("inventory.db")
        cur=con.cursor()
        query="select * from Product"
        cur.execute(query)
        rows=cur.fetchall()
        con.close()
        print("Database:show method finished\n")
        return rows


    def delete(self,pid):
        print("Database: delete method called")
        con=sqlite3.connect("inventory.db")
        cur=con.cursor()
        cur.execute("delete from Product where pid=?",(pid,))
        con.commit()
        con.close()
        print("Database:Delete method finished\n",pid)


    def search(self,pid="",name="",price="",qty="",company="",contact=""):
        print("Database: search method called",pid)
        con=sqlite3.connect("inventory.db")
        cur=con.cursor()
        cur.execute("select * from Product where pid=? or pname=? or price=? or qty=? or company=? or contact=?",(pid,name,price,qty,company,contact))
        row=cur.fetchall()
        con.close()
        print(pid,"Database:search method called\n")
        return row


    def update(self,pid="",name="",price="",qty="",company="",contact=""):
        print("Database: update method called")
        con=sqlite3.connect("inventory.db")
        cur=con.cursor()
        cur.execute("update Product set pid=? or pname=? or price=? or qty=? or company=? or contact=? where pid=?",((pid,name,price,qty,company,contact,pid)))
        con.commit()
        con.close()
        print(pid,"Database:search method called\n")
        

if __name__=='__main__':
    root=Tk()
    application=Product(root)
    root.mainloop()
