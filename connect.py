import mysql.connector  
     
myconn = mysql.connector.connect(host = "ec2-52-20-248-222.compute-1.amazonaws.com", user = "yizavtynwgjfcs",passwd = "aff6e5ec08f5035f2152457497cd4da56d6cecce2d7e0f83b94f1121b8af3f8b", database = "dcot1pjik8e8oj")
    
print(myconn)
