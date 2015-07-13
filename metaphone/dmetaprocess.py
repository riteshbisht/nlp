import MySQLdb;
import fuzzy;
inp=raw_input("enter the text");

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="ritesh", # your password
                      db="nlp") # name of the data base

dmeta=fuzzy.DMetaphone();	#initialized dmetaphone instance
code=dmeta(inp);			#produce [code,None]
code=code[0];			#fetch code from [code,None]

querystr="select word from dmetaphone where code='{0}' ".format(code)	#select word from dmetaphone where code='code';
cur=db.cursor();

p=cur.execute(querystr);

rows=cur.fetchall();	
row=rows[0]
print row[0];


