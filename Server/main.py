import time
import server
import pyodbc as pyodbc

HOST_NAME = 'localhost'
PORT = 8000

if __name__ == "__main__":
    print(server.Connect())
    print(server.getGV('NVDQ','123456'))