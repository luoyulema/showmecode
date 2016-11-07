import MySQLdb
conf = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'mydream5',
    'port': 3306,
    'db': 'testdb',
}


class save_DB:
    """docstring for Save_DB"""

    def __init__(self, path):
        self.path = path
        print path

    def __conn(self, **conf):
        try:
            conn = MySQLdb.connect(**conf)
        except MySQLdb.Error as e:
            print "There is something wrong"

        return conn

    def save_data_todb(self, **conf):
        conn = self.__conn(**conf)
        path = self.path
        cur = conn.cursor()
        cur.execute('drop table if exists data')
        cur.execute(
            'create table data (id int(10) primary key auto_increment,data varchar(20))')

        with open(path, 'r+') as f:
            for line in f.readlines():
                line = line.rstrip()
                cur.execute('insert into data(data) values(%s)', [line])
        conn.commit()
        cur.close()
        conn.close()

    def see_data(self, **conf):
        conn = self.__conn(**conf)
        cur = conn.cursor()
        cur.execute('select * from data')
        values=cur.fetchall()
        print values
        cur.close()
        conn.close()

