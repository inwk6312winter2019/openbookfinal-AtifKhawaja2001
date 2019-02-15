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

def unique_words(d1,d2,d3):
	for keys in d1:
		print(keys)


lower('Book1.txt','Book2.txt','Book3.txt')
