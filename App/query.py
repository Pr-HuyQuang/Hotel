import pyodbc as pyodbc

def Connect():
    try:
        connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                    "Server=HUYQUANG;"
                                    "Database=QL_TEST;"
                                    "Trusted_Connection=yes;")
        print('Success')
        return connection
    except:
        return "Lỗi"
def getGV(id, pas):
    try:
        conn = Connect()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM GIANGVIEN WHERE MAGV =N'"+id+"' AND MATKHAU='" +pas+"'"
            print(sql)
            cursor.execute(sql)
            for row in cursor:
                # Format
                a = {'MANV':row[0], 'MatKhau':row[1], 'TenNV':row[2] +" "+ row[3], 'GioiTinh':row[4], 'NgaySinh':row[5].strftime("%d/%m/%Y"), 'ChucVu':row[6], 'hinhAnh':row[7]}
                print(a)
        return a
    except:
        return 'Lỗi'

def Login(id, passw):
    try:
        get = getGV(id,passw)
        if(get[0] == id and get[1] == passw):
            return 1
    except:
        return 0
def BaoGiang(id):
    print("Chưa làm")

if __name__ == "__main__":
    print(getGV('NVDQ','123456'))
    #print(Login('NVDQ','123456'))