#codeing=utf-8

import MySQLdb as mdb


class py_mysql:
	host=""
	port=""
	user=""
	password=""
	dbname=""
	conn=""
	cursor=""

	def __init__(self,host,port,dbname,user,password):
		self.host=host
		self.port=port
		self.dbname=dbname
		self.user=user
		self.password=password

	def mysql_connect(self,ismaster=0):
		self.conn = mdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.password)
		self.cursor=self.conn.cursor()
		self.conn.select_db(self.dbname)

	def execute(self,sql):
		return self.cursor.execute(sql)

	def query(self,sql):
		try:
			self.cursor.execute(sql)
			return self.cursor.fetchall()
		except mdb.Error,e:
			print "Error %d:%s" % (e.args[0],e.args[1])

	def insert(self,tablename,dataarr):
		try:
			sql = self.dealinsertdata(tablename,dataarr)
			re.self.execute(sql)
			return re
		except mdb.Error,e:
			print "Erro %d:%s" % (e.args[0],e.args[1])

	def update(self,tablename,dataarr,where):
		try:
			sql = self.dealupdatedata(tablename,dataarr,where)
			re = self.execute(sql)
			return re
		except mdb.Error,e:
			print "Error %d:%s" % (e.args[0],e.args[1])

	def delete(self,tablename,where):
		try:
			sql = "DELETE FROM " + tablename + " WHERE " + where 	
			re = self.execute(sql)
			return re
		except mcb.Error,e:
			print "Error %d:%s" % (e.args[0],e.args[1])

	def insert_id(self):
		return self.conn.insert_id()
	
	def affected_rows(self):
		return self.cursor.rowcount

	def dealinsertdata(self,tablename,data):
		try:
			key=[]
			val=[]

			for i in range(len(data)):
				key.append("'" + data.keys()[i] + "'")
				k = data.keys()[i]
				val.append("'" + data[k] + "'")
			field=",".join(key)
			vals=",".join(val)
			sql="INSERT INTO " + tablename + "(" + field + ") VALUES (" + vals + ")"
			return sql
		except:
			print "array to string error"
	
	def dealupdatedata(self,tablename,data,condition):
		try:
			val=[]
			updatestr = ""
			for i in range(len(data)):
				k = data.keys()[i]
				val.append("'" + data.keys()[i] + "' = "+ "'" + data[k] + "'")

			vals=",".join(val)
			sql="UPDATE " + tablename + " SET " + vals + " where " + condition
			return sql
		except:
			print " array to string error"
	
	def mysql_close(self):
		self.conn.close()
		self.cursor.close()
	
	def __del__(self):
		self.mysql_close()		
