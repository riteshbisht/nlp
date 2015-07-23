import MySQLdb
from nltk.tokenize import TreebankWordTokenizer

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="ritesh", # your password
                      db="test") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need


file=open('/home/ritesh/Desktop/t.txt');
strdata=file.read();

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'","_","=",">","<","$","#","@","!","^","%","{","}","|","[","]","&","*","-","+","~","`","1","2","3","4","5","6","7","8","9","0"]


for i in punctuation:
	strdata=strdata.replace(i," ");
	

words=TreebankWordTokenizer().tokenize(strdata)
cur = db.cursor();
for x in range(len(words)):
	
	
	setofalpha=set(words[x]);
	currentword=words[x];
	if(currentword.isdigit() or len(currentword)==1):
		
		continue;	
	k=list(setofalpha);
	length=len(k);
	strq="";
	strq=k[0];
	strvalue="'"+currentword+"'"+',true';
	for i in range(1,length):
		#print k;
		strq=strq+","+k[i];
		strvalue=strvalue+',true'
	try:
		rit="INSERT INTO alphabets (words,{0}) VALUES ({1});".format(strq,strvalue);
		err=cur.execute(rit)
		#print err;
		db.commit();
		#print "{0} word enterred successfullly".format(currentword);
	except:
		pass;
		#print "word already exits"; 
	print x;

