import MySQLdb
import fuzzy
from nltk.tokenize import TreebankWordTokenizer

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="ritesh", # your password
                      db="nlp") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
s="Get started by your reading our documentation awesome"
dmeta=fuzzy.DMetaphone();
words=TreebankWordTokenizer().tokenize(s)
cur = db.cursor();
for x in range(len(words)):
	
	word=words[x];		#taking the invidual word
	code=dmeta(word);	#generating code produce [code,None]
	code=code[0];			#obtain code from [code,None]
	try:
		rit="INSERT INTO dmetaphone(word,code) VALUES ('{0}','{1}');".format(word,code);  #mysql statement to insert data into dmetaphone table having word as primary key

		err=cur.execute(rit)
		print err;
		db.commit();
		print "{0} word enterred successfullly".format(word);
	except:
		print "{0} already exits".format(word);   #execute if primary key violaton haapen while inserting
	

