import MySQLdb;

inp=raw_input("enter the text");

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="ritesh", # your password
                      db="test") # name of the data base


setofalphabets=set(inp);
k=list(setofalphabets);
strval=" ";
for i in range(len(k)-1):
	strval=strval+k[i]+"=true and ";
strval=strval+k[len(k)-1]+"=true"
querystr="select words from alphabets where {0} ".format(strval)
cur=db.cursor();
print querystr
p=cur.execute(querystr);

rows=cur.fetchall();
print rows;
