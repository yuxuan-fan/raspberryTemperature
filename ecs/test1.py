# import socket
# import pymysql
# import time


# # 打开数据库连接
# db = pymysql.connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     passwd='111111FYXfyx!',
#     db='centosdb',
#     charset='utf8'
# )
# print("数据库打开")

# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()

while True:
    import socket
    import pymysql
    import time


    # 打开数据库连接
    db = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='111111FYXfyx!',
        db='centosdb',
        charset='utf8'
    )
    print("数据库打开")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()







    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    HOST = '172.24.130.60'
    PORT = 2222
    #绑定socket
    s.bind((HOST, PORT))
    s.listen(10)
    
    
    # 接收客户端连接
    print("等待连接...")
    client, address = s.accept()

    while True:
        print("新连接")
        print("IP is %s" % address[0])
        print("port is %d\n" % address[1])


        # 读取消息
        msg = client.recv(1024)
        
        # 把接收到的数据进行解码
        print(msg.decode("utf-8"))
        print("读取完成")
        sqltime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # SQL 插入语句
        sql = "INSERT INTO magnetism(TESTTIME , MFLAG) VALUES ('%s', '%s')" % (sqltime, msg.decode('utf-8'))



        try:
            # 执行sql语句
            cursor.execute(sql)


            # 提交到数据库执行
            db.commit()
            print("insert success!")
        except:
            # 如果发生错误则回滚
            db.rollback()
            print("insert fail!")
        
        # time.sleep(5)


        # if msg == "over":
        #     client.close()
        #     s.close()
        #     # 关闭数据库连接
        #     db.close()
        #     print("程序结束\n")
        #     exit()

        client.close()
        s.close()
        # 关闭数据库连接
        db.close()
        print("程序结束\n")
        break
        # exit()












