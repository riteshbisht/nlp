import MySQLdb
import fuzzy
from nltk.tokenize import TreebankWordTokenizer
import sys;

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="ritesh", # your password
                      db="nlp") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
file=open('/home/ritesh/Desktop/t.txt');
strdata=file.read();

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'","_","=",">","<","$","#","@","!","^","%","{","}","|","[","]","&","*","-","+","~","`","1","2","3","4","5","6","7","8","9","0"]


for i in punctuation:
	strdata=strdata.replace(i," ");
	
soundex=fuzzy.Soundex(6);
words=TreebankWordTokenizer().tokenize(strdata)
noofwords=len(words);
avg=noofwords/100;
print noofwords;
print avg;
cur = db.cursor();
count=0;
showper=0;
i=1;
print showper;
sys.stdout.write('.');
for x in range(len(words)):
	
	word=words[x];	
	if(word.isdigit() or len(word)==1):
		count=count+1;
		continue;	
	#taking the invidual word
	code=soundex(word);	#generating code produce [code,None]
	count=count+1;	
	#print count;
	try:
		rit="INSERT INTO dmetaphone(word,code) VALUES ('{0}','{1}');".format(word,code);  #mysql statement to insert data into dmetaphone table having word as primary key

		err=cur.execute(rit)
		#print err;
		db.commit();
		#print "{0} word enterred successfullly".format(word);
		if(count%avg==0):
			showper=showper+1;
			print showper;
			print count;
		if(count>(200*i)):
			sys.stdout.write('.');
			i=i+1;				
	except:
		
		#print "{0} already exits".format(word);   #execute if primary key violaton happen while inserting
		pass;
	
	
