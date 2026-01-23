

# Read in the freq
lines = []
for _ in range(10):
	lines.append(input())

words = []
for i,line in enumerate(lines):
	t = line.split()
	f = float(t[-1]) / 100 # convert to decimal representation
	r = i+1
	word = t[1]
	words.append((f,r, word))
# Question (a)
# formula = (f = A / r)
# A= f*r
est = [f * r for f , r,w in words]
estimated_average = sum(est) / len(est)
#Question (b)
# formula = (f = A / r)
estimated_freq = [ (f, estimated_average / r) for f,r,_ in words]
# Question (c)
from nltk.stem import PorterStemmer
ps = PorterStemmer()
stem_words = ["space" , "rocket" , "illustration" , "engine"]

for word in stem_words:
	print(ps.stem(word))