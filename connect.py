import mysql.connector  
     
myconn = mysql.connector.connect(host = "ec2-34-202-88-122.compute-1.amazonaws.com", user = "ovrbzhegwiovax",passwd = "bd3e9f211a40013ae748ff9d49d86c8efe164b6b24bac372916cf71642eef78c", database = "dbqjer5r92drnr")
    
print(myconn)
