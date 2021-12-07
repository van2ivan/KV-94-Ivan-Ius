import psycopg
import Database
from View import Menu

try:
    Menu.mainmenu()
except (Exception , psycopg.Error) as error:
        print ("Database Error: ",error)
finally:
    print("Database connection is closed")