"Let a=3, b=5, c=7 and d=9"

"1. Let the value of Base 'a' be 3units and Height 'b' be 5units"
a = 3
b = 5
Hypotenuse = (a ** 2 + b ** 2) ** 0.5
print(Hypotenuse)
print('The Hypotenuse value is %0.5f units' % (Hypotenuse))

"2.1. Let the value of the length of the rectangle(c) be 7units, and the width(d) be 9units"
"The area of the rectangle be 'A'"
c = 7
d = 9
A = c * d
print(A)
print('The area of the rectangle value is %0.5f units' % (A))

"2.2. Let the value of the length of the rectangle(c) be 7units, and the width(d) be 9units"
"The perimeter of the rectangle be 'P'"
c = 7
d = 9
P = 2 * (c + d)
print(P)
print('The perimeter of the rectangle value is %0.5f units' % (P))

"3.1. Let the radius of the circle 'a' be 3 units and the value of pi be 3.14 "
"Let the area of the circle be 'A'"
a = 3
pi = 3.14
A = pi * a ** 2
print(A)
print('The area of the circle value is %0.5f units' % (A))

"3.2. Let the radius of the circle 'a' be  3 units and the value of pi be 3.14 "
"Let the circumference of the circle be 'C'"
a = 3
pi = 3.14
C = 2 * pi * a
print(C)
print('The circumference of the circle value is %0.5f units' % (C))

"4.1. Let the string= ATCTATGGTCATGCTATCTTATGGTAGATC"
"Let a=3, b=5, c=7 and d=9"

"Let the Slice the string S from indices a through b and c through d (with space in between), inclusively"
S= ('CGCAGTTGTATTGCTTCCCACATTTATTAGACCACCTATTAAAAATGGATTTCTTCCCATTTCAAGCTGCCCACAAATCTCGCTCCTGATACGTTCTTCACTTCAAGCCGTAGCATCCCAATATCAGAAGCGGCGCCGGACTTGTTTTCAAAATATCCACGTATCCCTTCTTTCTCTTTCAATAGAAAACACCCATTGGTTCCGAAATAACGCATCTTATACTGTGGCTTATTGGCGTTACCC')

print(len(S))
A = S[3:6]
B = S[7:10]

print("The slice will be:")
print(A, B)

print('4.2. The reverse of the string will be:')
S = 'CGCAGTTGTATTGCTTCCCACATTTATTAGACCACCTATTAAAAATGGATTTCTTCCCATTTCAAGCTGCCCACAAATCTCGCTCCTGATACGTTCTTCACTTCAAGCCGTAGCATCCCAATATCAGAAGCGGCGCCGGACTTGTTTTCAAAATATCCACGTATCCCTTCTTTCTCTTTCAATAGAAAACACCCATTGGTTCCGAAATAACGCATCTTATACTGTGGCTTATTGGCGTTACCC'
print(''.join(reversed(S)))

"5.1. To find the first and last position of stop codon "
S='CGCAGTTGTATTGCTTCCCACATTTATTAGACCACCTATTAAAAATGGATTTCTTCCCATTTCAAGCTGCCCACAAATCTCGCTCCTGATACGTTCTTCACTTCAAGCCGTAGCATCCCAATATCAGAAGCGGCGCCGGACTTGTTTTCAAAATATCCACGTATCCCTTCTTTCTCTTTCAATAGAAAACACCCATTGGTTCCGAAATAACGCATCTTATACTGTGGCTTATTGGCGTTACCC'
p='TAG'
print(S.index(p))
print(S.rfind(p))
print("The first position of the stop codon 'TAG' is 27 and the last location is 182")

"5.2. To Split the DNA string by stop codon TAG and report each fragment and their respective length"
print(S.split(p))
'Let P, Q, R and S be the substring of string S'
P='CGCAGTTGTATTGCTTCCCACATTTAT'
Q='ACCACCTATTAAAAATGGATTTCTTCCCATTTCAAGCTGCCCACAAATCTCGCTCCTGATACGTTCTTCACTTCAAGCCG'
R='CATCCCAATATCAGAAGCGGCGCCGGACTTGTTTTCAAAATATCCACGTATCCCTTCTTTCTCTTTCAA'
S='AAAACACCCATTGGTTCCGAAATAACGCATCTTATACTGTGGCTTATTGGCGTTACCC'
print(len(P))
print(len(Q))
print(len(R))
print(len(S))
print("The length of substring P=27, Q=80, R=69 and S=58")

'5.3. To find the Percent GC of original DNA string S'
S='CGCAGTTGTATTGCTTCCCACATTTATTAGACCACCTATTAAAAATGGATTTCTTCCCATTTCAAGCTGCCCACAAATCTCGCTCCTGATACGTTCTTCACTTCAAGCCGTAGCATCCCAATATCAGAAGCGGCGCCGGACTTGTTTTCAAAATATCCACGTATCCCTTCTTTCTCTTTCAATAGAAAACACCCATTGGTTCCGAAATAACGCATCTTATACTGTGGCTTATTGGCGTTACCC'
print(S.count('GC'))
PercentageofGC=(S.count('G')+(S.count('C')/len(S))*100)
print(PercentageofGC)


'5.4. The report of number of A, C, T and G in string S'
S='CGCAGTTGTATTGCTTCCCACATTTATTAGACCACCTATTAAAAATGGATTTCTTCCCATTTCAAGCTGCCCACAAATCTCGCTCCTGATACGTTCTTCACTTCAAGCCGTAGCATCCCAATATCAGAAGCGGCGCCGGACTTGTTTTCAAAATATCCACGTATCCCTTCTTTCTCTTTCAATAGAAAACACCCATTGGTTCCGAAATAACGCATCTTATACTGTGGCTTATTGGCGTTACCC'
print(len(S))
a=print(S.count('A'))
print(S.count('T'))
print(S.count('G'))
print(S.count('C'))

print('The number of A is 62, B is 77, C is 35 and D is 69')

"6.1 To find the list of all unique elements"
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

uniquenumbers1 = list(set(a))
print(uniquenumbers1)
uniquenumbers2 = list(set(b))
print(uniquenumbers2)

"6.2 To find the list of all common elements"
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(a))
L1=list(a)
L2=list(b)

L1=set(a)
L2=set(b)

z=L1.intersection(L2)
print(z)

"6.2 To find the list of all elements"
k=a+b
print(list(k))