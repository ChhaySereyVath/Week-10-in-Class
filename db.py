import mysql.connector

'''
State your group member name and id here:
ex: 1. 2023001chea - Joe Chea

'''


# TODO:
# host can be 'localhost' or '127.0.0.1'
# if you are using mamp, password is root
# and port is 8889
# use cat_db as database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cat_db",
    port="3306"
)


cursor = mydb.cursor()


def register_cat(cat_info):
    '''
    TODO:
    cat_info is in a form of list ex: ["rose", "f", "Siberian", "2020-03-08", "smart one"], that register_cat function will insert the provided
    list to cats table as an insert record.
    '''
    sql = "INSERT INTO cats (name, gender, breed, dob, description) VALUES (%s, %s, %s, %s, %s)"
    
    cursor.execute(sql, cat_info)

    mydb.commit()
    print(cursor.rowcount, "record inserted.")
    
test_data = ["rose", "f", "Siberian", "2020-03-08", "smart one"]
# register_cat(test_data)

def get_cats():
    '''
    TODO:
    this function will get all cat from cats table 
    '''
    sql = "SELECT * FROM cats"
    cursor .execute(sql)
    myresult = cursor.fetchall()
    
    return myresult


# get_cats()


def get_cat(id):
    '''
    TODO:
    '''
    sql = f"SELECT * FROM cats WHERE id = {id}"
    cursor.execute(sql)
    myresult = cursor.fetchone()

    return myresult

print(get_cat(5))

def update_cat(cat_info):
    '''
    TODO:
    cat_info is in a form of list ex: [1,"rose", "f", "Siberian", "2020-03-08", "smart one"], that update_cat function will use as 
    an update record for specific cat information where equal to cat_info[0]
    '''
    id, name, gender, breed, dob, description = cat_info

    sql = f"UPDATE cats SET name = '{name}', gender = '{gender}', breed = '{breed}', dob = '{dob}', description = '{description}' WHERE id = {id}"
    cursor.execute(sql)
    mydb.commit()

# test_data = [7, "Rosie", "m", "Cambodian", "2020-03-08", "like a dog"]
# update_cat(test_data)

def remove_cat(id):
    '''
    TODO:
    this function will remove record from cat table base on id parameter.
    '''
    sql = f"DELETE FROM cats WHERE id = {id}"

    cursor.execute(sql)

    mydb.commit()

print(cursor.rowcount, "record(s) deleted")

remove_cat(7)