-- Creates a MySQL server with:
--   Database hbnb_dev_db.
--   User hbnb_dev with password hbnb_dev_pwd in localhost with all previleges.

db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root'
)

-- Create a cursor object to execute queries
cursor = db.cursor()

-- Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS hbnb_dev_db")

-- Create the user
cursor.execute("CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'")

-- Grant all privileges
cursor.execute("GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost'")

-- Grant performance_schema to hbnb_dev
cursor.execute("GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'")

cursor.execute("FLUSH PRIVILEGES")

-- Close the cursor
cursor.close()
db.close()
