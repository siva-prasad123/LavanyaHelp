from django.shortcuts import render
import pymysql

# Create your views here.
def login(request):
    return render(request,'sk/Login.html')


def SKRegister(request):
    return render(request,'sk/SKRegister.html')

def RegAction(request):
    email=request.POST['email']
    shopname=request.POST['shopname']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['password']
    mobile=request.POST['mobile']

    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from skregister where shopname='"+shopname+"' and email='"+email+"' and mobile='"+mobile+"'")
    d=cur.fetchone()
    if d is not None:

     context={'msg':'Already Exist These Details...!!'}
     return render(request,'sk/SKRegister.html', context)
    else:
        cur=con.cursor()
        cur.execute("insert into skregister values(null,'"+shopname+"','"+email+"','"+address+"','"+mobile+"','"+username+"','"+password+"')")
        con.commit()
        context={'msg':'Successfully Registered Your Details...!!'}
        return render(request,'sk/SKRegister.html', context)

def LogAction(request):
    uname=request.POST['username']
    pwd=request.POST['password']

    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from skregister where username='"+uname+"' and password='"+pwd+"'")
    d=cur.fetchone()
    if d is not None:
        request.session['userid']=d[0]
        request.session['shopname']=d[1]
        request.session['email']=d[2]
        return render(request,'sk/SKHome.html')
    else:
        context={'msg':'Login Failed...!!'}
        return render(request,'sk/Login.html', context)


def SKHome(request):
    return render(request,'sk/SKHome.html')

def addProducts(request):
    return render(request,'sk/AddProduct.html')

def ProductAction(request):
    pname=request.POST['pname']
    available=request.POST['available']
    price=request.POST['price']
    usage=request.POST['usage']

    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from product where pname='"+pname+"'")
    d=cur.fetchone()
    if d is not None:

     context={'msg':'Product Already Exist...!!'}
     return render(request,'sk/AddProduct.html', context)
    else:
        sid=request.session['userid']
        shop_id=str(sid)
        cur=con.cursor()
        cur.execute("insert into product values(null,'"+shop_id+"','"+pname+"','"+price+"','"+available+"','"+usage+"')")
        con.commit()
        context={'msg':'Successfully Product Added...!!'}
        return render(request,'sk/AddProduct.html', context)

def viewproducts(request):
    sid=request.session['userid']
    shop_id=str(sid)
    print("shopid::"+shop_id)
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from product where shop_id='"+shop_id+"'")
    data=cur.fetchall()
    table="<table><tr><th>ID</th><th>Product Name</th><th>Product Price</th><th>No.of Availability</th><th>Product Usage</th></tr>"
    for d in data:
        table+="<tr><td>"+str(d[0])+"</td><td>"+str(d[2])+"</td><td>"+str(d[3])+"</td><td>"+str(d[4])+"</td><td>"+str(d[5])+"</td></tr>"
    table+="</table>"
    context={'data':table}
    return render(request,'sk/ViewProducts.html', context)

def viewbookings(request):
    u_id=request.session['userid']
    spid=str(u_id)
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("select * from product_book pb, register r where pb.user_id=r.id and pb.shop_id='"+spid+"'")
    data=cur.fetchall()
    table="<table><tr><th><center>Customer Name</center></th><th><center>Email</center></th><th><center>Mobile No.</center></th><th><center>Booked Date</center></th><th><center>Status</center></th></tr>"
    for d in data:
        status=d[5]
        if status=='waiting':
            table+="<tr><td>"+str(d[7])+"</td><td>"+str(d[8])+"</td><td>"+str(d[9])+"</td><td>"+str(d[4])+"</td><td><a href='AcceptProduct?sid="+str(d[0])+"'>Accept</a></td></tr>"
        else:
            table+="<tr><td>"+str(d[7])+"</td><td>"+str(d[8])+"</td><td>"+str(d[9])+"</td><td>"+str(d[4])+"</td><td>"+str(d[5])+"</td></tr>"
    table+="</table>"
    context={'data':table}
    return render(request,'sk/ViewBooking.html', context)
def AcceptProduct(request):
    sid=request.GET['sid']
    u_id=request.session['userid']
    spid=str(u_id)
    con=pymysql.connect(host='localhost', user='root',password='root', database='service_portal', charset='utf8')
    cur=con.cursor()
    cur.execute("update product_book set status='Accepted' where id='"+sid+"'")
    cur=con.cursor()
    con.commit()
    cur=con.cursor()
    cur.execute("select * from product_book pb, register r where pb.user_id=r.id and pb.shop_id='"+spid+"'")
    data=cur.fetchall()
    table="<table><tr><th>Customer Name</th><th>Email</th><th>Mobile</th><th>Booked Date</th><th>Status</th></tr>"
    for d in data:
        status=d[5]
        if status=='waiting':
            table+="<tr><td>"+str(d[7])+"</td><td>"+str(d[8])+"</td><td>"+str(d[9])+"</td><td>"+str(d[4])+"</td><td><a href='AcceptProduct?sid="+str(d[0])+"'>Accept</a></td></tr>"
        else:
            table+="<tr><td>"+str(d[7])+"</td><td>"+str(d[8])+"</td><td>"+str(d[9])+"</td><td>"+str(d[4])+"</td><td>"+str(d[5])+"</td></tr>"
    table+="</table>"
    context={'data':table}
    return render(request,'sk/ViewBooking.html', context)
