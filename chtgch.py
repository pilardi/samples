#! /usr/bin/python
# eg: cat /usr/share/dict/words | python chtgch.py
from re import compile as _r

validChars=_r('^[ybtnslowreghc]{6}$') # a 6 char word with valid chars
doubleChars=_r(r'(.)\1+') # at least 2 consecutive equal chars
graph={'b':_r('[blrtyo]'),'c':_r('[ceghro]'),'e':_r('[ecglro]'),'g':_r('[gcehwo]'),'h':_r('[hcgswo]'),'l':_r('[lberto]'),'n':_r('[nbstyo]'),'o':_r('.'),'r':_r('[rbcelo]'),'s':_r('[shnwyo]'),'t':_r('[tblnyo]'),'w':_r('[wghnso]'),'y':_r('[ybnsto]')}

def inGraph(word):
	def _inGraph(i=0):
		return graph[word[i]].match(word[i+1]) and (i == 4 or (i < 4 and _inGraph(i+1)))  
	return validChars.match(word) and doubleChars.search(word) and _inGraph()

if __name__ == "__main__":
	import sys
	for word in sys.stdin: 
		if inGraph(word): sys.stdout.write(word)
