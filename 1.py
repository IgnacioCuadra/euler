from time import time

#logica de programación simple
def method_a(a,b,c):
	output = 0
	for x in range(1,c):
		if x%a == 0 or x%b == 0: output+=x
	return output

#logica matematica: progresión aritmetica
# s = (a1+an)/2*n
# a1 = primer termino, an = ultimo termino, n = numero de terminos
# para obtener el n numero de una sucesión aritmetica:
# an = a1 + (n - 1)d
#an = numero que quiero, a1 = primer termino, n = el numero que queremos encontrar, d = la diferencia entre cada numero
def method_b(a,b,c):
	ab = a*b
	an = (a+(int(c/a)-1)*a)
	bn = (b+(int(c/b)-1)*b)
	abn = (ab+(int(c/ab)-1)*ab)
	aout = (a+an)/2*int(c/a)
	bout = (b+bn)/2*int(c/b)
	about = (ab+abn)/2*int(c/ab)
	return int(aout+bout-about)


a = 3
b = 5
c = 1000

stime = time()
for x in range(0,10000):
	output = method_a(a,b,c)
etime = time()

print("a) ",output, "[", (etime - stime) ,"]")


stime = time()
for x in range(0,10000):
	output = method_b(a,b,c)
etime = time()
print("b) ",output, "[", (etime - stime) ,"]")