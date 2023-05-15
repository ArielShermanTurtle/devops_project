import pymysql

host_url = "sql12.freemysqlhosting.net"
db_uamer = "sql12615069"
db_pass = "ya2sVF11QE"

schema_name = "sql12615069"
tbl_name = "users"
temp_sch = "{user_id:1111,username:'turtle'}"
#conn = pymysql.connect(host=host_url, port=3306, user=db_uamer, passwd=db_pass, db=schema_name)
#conn.autocommit(True)
#cursor = conn.cursor()


# Inserting data into table
#def insert_user_into_db(user_id):
    #statementToExecute = "INSERT INTO TABLE `"+schema_name+"`.`"+tbl_name+"`(user_id` INT NOT NULL,`name` INT, NOT NULL, PRIMARY KEY (`user_id`));"
    #cursor.execute(statementToExecute)
    ##cursor.close()
    #conn.close()
    #return "DB insert_user_into_db"

# Pull Data from table
def get_user_name_from_db(user_id):
    #statementToExecute = "SELECT user_name FROM `"+schema_name+"`.`"+tbl_name+"` where user_id = " + user_id +";"
    #myresult = cursor.fetchall()
    #user_name = "no user"
    #if myresult.length > 0
        #for x in myresult:
        #    user_name = x

    # cursor.close()
    # conn.close()
    #return user_name
    return temp_sch

# Update Data on DB
#def update_user_name_db(user_id, user_name=""):
    # statementToExecute = "update `"+schema_name+"`.`"+tbl_name+"` set user_name = " + user_name + " where user_id = " + user_id +";"
    #cursor.execute(statementToExecute)
    #user_name = ge_user_name_from_db(user_id)
    #cursor.close()
    #conn.close()
    #return user_name


# Delete Data on DB
#def delete_user_name_db(user_id):
    # statementToExecute = "delete from `"+schema_name+"`.`"+tbl_name+"` where user_id = " + user_id +";"
    #cursor.execute(statementToExecute)

    #cursor.close()
    #conn.close()
    # user_name = "user was deleted"
    #return user_name