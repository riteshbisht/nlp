import MySQLdb;
import fuzzy;
import Levenshtein as leves;

def dmeta(inp):
	db = MySQLdb.connect(host="localhost", # your host, usually localhost
                    	 user="root", # your username
                     	 passwd="ritesh", # your password
                      	db="nlp") # name of the data base

	soundex=fuzzy.Soundex(6);	#initialized dmetaphone instance
	code=soundex(inp);			#produce [code,None]

	print code;
	querystr="select word from dmetaphone where code='{0}' ".format(code)	#select word from dmetaphone where code='code';
	cur=db.cursor();

	p=cur.execute(querystr);

	rows=cur.fetchall();
	options=[];
	for i in range(len(rows)):
		k=rows[i];
		options.append(k[0]);	

	dis=[];
	for i in range(len(options)):
		s=leves.distance(inp,options[i]);
		#print inp+"-"+options[i]+"="+"{0}".format(s);
		dis.append(s);
	#print dis;
	#print options;
	minindex=dis.index(min(dis));

	#print options[minindex];
	s="";	
	for l in range(len(options)):
		s=s+options[l]+", ";	
	
	return options;

