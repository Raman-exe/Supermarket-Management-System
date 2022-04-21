import pymssql
import generaloperat
from basic import Basic
from frontdesk import FrontDesk
from purchasemanage import PurchaseManage
from adminmanage import AdminManage
import os
def link():
    conn = pymssql.connect(host="127.0.0.1",  # Connect to the database
                           user="sa",
                           password="123",
                           database="supermarket",  # Suppermarket
                           charset="utf8")
    return conn
def meta():
    while True:
        os.system("cls")
        print("------------------------------------------------")
        print("1: Salesperson interface")
        print("2: Buyer interface")
        print("3: Admin interface")
        print("                                     other numbers exit")
        print("------------------------------------------------")
        cmd = input("Please enter options:").strip()
        if cmd=="1":
            front_desk=FrontDesk()
            front_desk.meta()
        elif cmd=="2":
            purchase_manage = PurchaseManage()
            purchase_manage.meta()
        elif cmd=="3":
            admin_manage = AdminManage()
            admin_manage.meta()
        else:
            break
        os.system("pause")

if __name__ == '__main__':
    try:
        conn=link()
        Basic.setConn(conn)
        meta()
    except Exception as e:
        print("An error occurred, the reason：",e)
