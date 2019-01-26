import sys
import numpy
import math
chartext=list(input('Entr the text to be encrypted:')) #only capital letters
print('the text entered is:',chartext)
asciitext=[]

for d in range(len(chartext)):
	asciitext.append(ord(chartext[d]))
asciitext=numpy.asarray(asciitext)
asciitext=asciitext-65
print('the numeric form of text is:',asciitext)
length=len(chartext)
print('length of the text is:',length)

key=list(input('Enter key')) #only capital letters
for d in range(len(key)):
	key[d]=ord(key[d])
key=numpy.asarray(key)
key=key-65
print('the numeric of key is:',key)


keylen=int(input('enter matrix dimension'))
keymatrix=numpy.asarray(key[0:keylen*keylen+1])
keymatrix=numpy.reshape(keymatrix,(keylen,keylen))
print('keymatrix:')
print(keymatrix)




detkeymatrix=numpy.linalg.det(keymatrix)
detkeymatrix=math.ceil(detkeymatrix%26)
print('det of keymatrix is:',detkeymatrix)



cokeymatrix=numpy.linalg.inv(keymatrix).T*numpy.linalg.det(keymatrix)
adjkeymatrix=numpy.matrix.transpose(cokeymatrix)
adjkeymatrix=adjkeymatrix%26
print('adjoint of keymatrix is:')
print(adjkeymatrix)

detinverse=-1
for z in range(1,25):
	if (detkeymatrix*z)%26==1:
		detinverse=z
		break
if detinverse==-1:
	print('detinversen not initialized')
	exit()
	
print('det inverse is:',detinverse)

	
	


keyinverse=detinverse*adjkeymatrix
keyinverse=keyinverse%26
print('keyinverse is:')
print(keyinverse)



for x in range(0,length-keylen,keylen):
	tempmatrix=numpy.asarray(asciitext[x:x+keylen])
	tempmatrix=numpy.reshape(tempmatrix,(keylen,1))
	print('temp matrix is:')
	print(tempmatrix)
	enc=numpy.matmul(keymatrix,tempmatrix)
	enc=enc%26
	print('encrypted text is:')
	print(enc)
	dec=numpy.matmul(keyinverse,enc)
	dec=dec%26
	print('decrypted text is:')
	print(dec)
	