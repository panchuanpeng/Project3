import sqlite3

DbName = "Card"


class Cdb:
	def __init__(self, dbName):
		self.dbName = dbName
		self.conn = None
		self.cursor = None
		self.__connect()

	def __connect(self):
		try:
			self.conn = sqlite3.connect(self.dbName)
			self.cursor = self.conn.cursor()
		except:
			print("conn db err!")

	def exec_query(self, sql, *parms):
		try:
			self.cursor.execute(sql, parms)
			values = self.cursor.fetchall()
		except:
			print("exec_query error,sql is=", sql)
			return None
		return values

	def exec_cmd(self, sql, *parms):
		try:
			self.cursor.execute(sql, parms)
			self.conn.commit()
		except:
			print("exec_cmd error,sql is=", sql)

	def close_connect(self):
		try:
			self.cursor.close()
			self.conn.close()
		except:
			print("close db err!")


def initcard():
	cdb = Cdb(DbName)
	sql = """create table if not exists card(id integer primary key autoincrement not null,zk varchar(100), 
	sn varchar(100),nsi varchar(100),vd varchar(100),yz varchar(100),sy varchar(100),cp varchar(100),yj integer,
	td integer,wz varchar(100),bz varchar(100))""".replace("\n", "")
	cdb.exec_cmd(sql)
	cdb.close_connect()


def deletecard(id):
	cdb = Cdb(DbName)
	sql1 = "delete from card where id=?"
	cdb.exec_cmd(sql1, id)
	cdb.close_connect()


def addcard(zk, sn, nsi, vd, yz, sy, cp, yj, td, wz, bz):
	cdb = Cdb(DbName)
	sql1 = "insert into card (zk, sn, nsi, vd, yz, sy, cp, yj, td, wz, bz) values (?,?,?,?,?,?,?,?,?,?,?)"
	cdb.exec_cmd(sql1, zk, sn, nsi, vd, yz, sy, cp, yj, td, wz, bz)
	sql2 = "select max(id) from card"  # "select max(id) from user"
	res = cdb.exec_query(sql2)
	cdb.close_connect()
	return res[0][0]


def editcard(id, zk, sn, nsi, vd, yz, sy, cp, yj, td, wz, bz):
	cdb = Cdb(DbName)
	sql1 = "update card set zk=?, sn=?, nsi=?, vd=?, yz=?, sy=?, cp=?, yj=?, td=?, wz=?, bz=? where id=?"
	cdb.exec_cmd(sql1, zk, sn, nsi, vd, yz, sy, cp, yj, td, wz, bz, id)
	cdb.close_connect()

def takeoutcard(id, sy):
	cdb = Cdb(DbName)
	sql1 = "update card set sy=? where id=?"
	cdb.exec_cmd(sql1, sy, id)
	cdb.close_connect()

def getData(table):
	cdb = Cdb(DbName)
	sql2 = f"select * from {table}"
	res = cdb.exec_query(sql2)
	cdb.close_connect()
	print(res)
	return res


def inituser():
	cdb = Cdb(DbName)
	sql = "create table if not exists user(id integer primary key autoincrement not null, user varchar(30), password varchar(30), admin varchar(30))"
	cdb.exec_cmd(sql)
	sql2 = f"select * from user"
	res = cdb.exec_query(sql2)
	res = [i[1] for i in res]
	if "admin" not in res:
		sql1 = "insert into user (user, password, admin) values (?,?,?)"
		cdb.exec_cmd(sql1, "admin", "admin", "admin")
	cdb.close_connect()


def adduser(user, password, admin):
	cdb = Cdb(DbName)
	sql1 = "insert into user (user, password, admin) values (?,?,?)"
	cdb.exec_cmd(sql1, user, password, admin)
	sql2 = "select max(id) from user"  # "select max(id) from user"
	res = cdb.exec_query(sql2)
	cdb.close_connect()
	return res[0][0]


def edituser(user, password, admin):
	cdb = Cdb(DbName)
	sql1 = "update user set password=?,admin=? where user=?"
	cdb.exec_cmd(sql1, password, admin, user)
	cdb.close_connect()

# if __name__ == '__main__':
#     cdb = Cdb(DbName)
#     delSql = "drop table user"
#     #cdb.exec_cmd(delSql)
#     sql1 = "insert into user (name,password) values (?,?)"
#     cdb.exec_cmd(sql1,'sam','8888')
#     sql2 = "select * from user where name=?"
#     res = cdb.exec_query(sql2,'sam8')
#     for item in res:
#         print(item)
#         print(item[0],item[1],item[2])
#         id = item[0]
#         name = item[1]
#         password = item[2]
#     cdb.close_connect()
