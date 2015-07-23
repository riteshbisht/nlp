import MySQLdb;
import Levenshtein as leves;


def proc(inp):

	db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     	user="root", # your username
                      	passwd="ritesh", # your password
                      	db="test") # name of the data base


	setofalphabets=set(inp);
	k=list(setofalphabets);
	#print k;
	strval=" ";
	#print len(k)
	for i in range(len(k)-1):
		strval=strval+k[i]+"=true and ";
	strval=strval+k[len(k)-1]+"=true;"
	querystr="select words from alphabets where {0} ".format(strval)
	cur=db.cursor();
	#print querystr
	p=cur.execute(querystr);

	rows=cur.fetchall();
	alp=[];
	for d in range(len(rows)):
		k=rows[d]
		#print rows[d];
		alp.append(k[0]);
	#print alp;

	dis=[];
	for i in range(len(alp)):
		s=leves.distance(inp,alp[i]);
		dis.append(s);
	#print dis;
	#print alp;
	minindex=dis.index(min(dis));

	#print alp[minindex];

	s="";	
	for l in range(len(alp)):
		s=s+alp[l]+", ";	
	return alp[minindex];
	
