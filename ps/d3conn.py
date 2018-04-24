import ibm_db

def connect_to_db2():
	max_try = 5
	attempts = 0
	dsn="""DRIVER={IBM DB2 ODBC DRIVER};DATABASE=EUC3DB2A;HOSTNAME=meuc3.vipa.uk.ibm.com;PORT=446;PROTOCOL=TCPIP;UID=in14267;PWD=may16may;CURRRENTSCHEMA=CEDSR;AUTHENTICATION=SERVER;"""
	while attempts < max_try:
		try:
			conn = ibm_db.pconnect(dsn,'','')
		except:
			attempts += 1
			print "Connection failed:", ibm_db.conn_errormsg()
		else:
			print "Connection was successfully established"	
			return conn

conn = connect_to_db2()
# print conn
sql = """SELECT * FROM RCBV0500_PARM WHERE PARAMETER_NUMBER = 'RCB000'
			fetch first 5 rows only"""
print sql
stmt = ibm_db.exec_immediate(conn, sql)
dictionary = ibm_db.fetch_assoc(stmt)
while dictionary != False:
	print dictionary
	dictionary = ibm_db.fetch_assoc(stmt)