import string

def lower(book1,book2,book3):

	res1 = []
	res2 = []
	res3 = []
	d1 = dict()
	d2 = dict()
	d3 = dict()

#Book1
	myfile1 = open(book1)
	for line in myfile1:
		line1 = line.split()
		for word in line1:
			word1 = word.strip(string.whitespace + string.punctuation)
			res1.append(word1)

	for word in res1:
		d1[word] = d1.get(word,0) + 1
		val = d1[word]
		d1.setdefault(word,val)


#Book2
	myfile2 = open(book1)
	for line in myfile2:
		line1 = line.split()
		for word in line1:
			word1 = word.strip(string.whitespace + string.punctuation)
			res2.append(word1)
	for word in res2:
		d2[word] = d2.get(word,0) + 1
		val = d2[word]
		d2.setdefault(word,val)


#Book3
	myfile3 = open(book1)
	for line in myfile3:
		line1 = line.split()
		for word in line1:
			word1 = word.strip(string.whitespace + string.punctuation)
			res3.append(word1)
	for word in res3:
		d3[word] = d3.get(word,0) + 1
		val = d3[word]
		d3.setdefault(word,val)


	unique_words(d1,d2,d3)

	count_the_article(res1,res2,res3)

	sorted_list(res1,res2,res3,d1,d2,d3)

	common_words(d1,d2,d3)

def unique_words(d1,d2,d3):
	for keys in d1:
		print(keys)


def count_the_article(res1,res2,res3):
	c1 = 0
	for i in res1:
		c1 = c1+1
	print("The total number of words in Book1 = ",c1)

	c2 = 0
	for i in res2:
		c2 = c2+1
	print("The total number of words in Book2 = ",c2)

	c3 = 0
	for i in res3:
		c3 = c3+1
	print("The total number of words in Book3 = ",c3)

def sorted_list(res1,res2,res3,d1,d2,d3):

	lt1 = []
	sub1 = []
	t1 = d1.items()
	for key,value in t1:
		lt1.append(key)
		lt1.append(value)	

	for i in range(0,len(lt1),2):
		sub1.append(lt1[i:i+2])
	sub1.sort(key = lambda s:s[1],reverse = True)

	print(sub1)

	lt2 = []
	sub2 = []
	t2 = d2.items()
	for key,value in t2:
		lt2.append(key)
		lt2.append(value)        

	for i in range(0,len(lt2),2):
		sub2.append(lt2[i:i+2])
	sub2.sort(key = lambda s:s[1],reverse = True)

	print(sub2)

	lt3 = []
	sub3 = []
	t3 = d3.items()
	for key,value in t3:
		lt3.append(key)
		lt3.append(value)        

	for i in range(0,len(lt3),2):
		sub3.append(lt3[i:i+2])
	sub3.sort(key = lambda s:s[1],reverse = True)

	print(sub3)

def character_word_count(res1,res2,res3):

	d1 =  {}
	for word in res1:
                d1[word] = d1.get(word,0) + 1
                val = d1[word]
                d1.setdefault(word,val)
	print(d1)

	d2 = {}
	for word in res2:
                d2[word] = d2.get(word,0) + 1
                val = d2[word]
                d2.setdefault(word,val)
	print(d2)

	d3 = {}
	for word in res3:
                d3[word] = d3.get(word,0) + 1
                val = d3[word]
                d3.setdefault(word,val)
	print(d3)

def common_words(d1,d2,d3):
	s1 = set(d1).intersection(set(d2))
	s2 = s1.intersection(set(d3))

	l = []
	for keys in s2:
		l.append(keys)

	for i in range(20):
		print("The 20 most common words = ",l[i])

lower('Book1.txt','Book2.txt','Book3.txt')
