# import sqlite3

# class DatabaseConnection:
#     def __init__(self):
#         self.connection = sqlite3.connect("example.db")

#     def execute_query(self, query):
#         cursor = self.connection.cursor()
#         cursor.execute(query)
#         self.connection.commit()

# # Utilisation
# db1 = DatabaseConnection()
# db1.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# db2 = DatabaseConnection()
# db2.execute_query("INSERT INTO users (name) VALUES ('Alice')")

# print(db1 is db2)  # False : Chaque module a sa propre connexion
























import sqlite3
import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()  # Sécurité pour les environnements multi-thread

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
                cls._instance.connection = sqlite3.connect("example.db")
        return cls._instance

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()



# Module A
db1 = DatabaseConnection()
db1.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# Module B
db2 = DatabaseConnection()
db2.execute_query("INSERT INTO users (name) VALUES ('Alice')")

# Vérification
print(db1 is db2)  # True : Une seule instance de connexion est utilisée
