import MySQLdb
from nltk.tokenize import TreebankWordTokenizer

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="ritesh", # your password
                      db="test") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
s="The Treebank tokenizer uses regular expressions to tokenize text as in Penn Treebank"
words=TreebankWordTokenizer().tokenize(s)
cur = db.cursor();
for x in range(len(words)):
	
	setofalpha=set(words[x]);
	currentword=words[x];
	k=list(setofalpha);
	length=len(k);
	strq="";
	strq=k[0];
	strvalue="'"+currentword+"'"+',true';
	for i in range(1,length):
		print k;
		strq=strq+","+k[i];
		strvalue=strvalue+',true'
	try:
		rit="INSERT INTO alphabets (words,{0}) VALUES ({1});".format(strq,strvalue);
		err=cur.execute(rit)
		#print err;
		db.commit();
		print "{0} word enterred successfullly".format(currentword);
	except:
		print "word already exits"; 
	

