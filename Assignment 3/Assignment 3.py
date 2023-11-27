# 1.
StringA = "GGGCCGTTGGT"
StringB = "GGACCGTTGAC"


###Assigning hamming_distance as the function to identify the position of the elements
def hamming_distance(StringA, StringB):
    ### count refers to the number of times the string is looped over
    count = 0
    ###i is reffered to each element in the string
    for i in range(len(StringA)):
        if StringA[i] == StringB[i]:
            print("Nucleotides matched")
        else:
            print("Neucleotides mismatched")
            count += 1
    print(count)


hamming_distance(StringA, StringB)

###The hamming distance is 3.


# 2.
# import the file
F = open('contigs.fasta', 'r')
# The output file is designated
output_file = open('answer2.fasta', 'w')
# n is the length of the sequence
n = 80
# using while loop, we are considering two lines, 'header' and 'sequence'
while True:
    header = F.readline()
    # Mentioning the break statement so that it does not run into an infinite loop and stops when there is no line
    if not header:
        break
    # print(header)
    output_file.write(header)
    # Applying logic to the sequence line
    sequence = F.readline()
    for i in range(0, len(sequence), n):
        startP = i
        endP = i + n
        print(sequence[startP:endP]+'\n')
        output_file.write(sequence[startP:endP] + '\n')
F.close()
output_file.close()



#3.
3.
#import the file in fastq format
X =open(r"C:\Users\chari\binf690_charitha\FASTQ",'r')
#to write the header and sequence into a new file, open a new file Y
Y = open('new.fasta', 'w')


# using while loop, we are assigning variables to the first four lines.
#Since the fastq format have a pattern of 4 lines in repetition.
#Assigning header line, sequence line, info line and qual line to the first, four lines of the fastq file.

for line in X:
    header = line
    sequence= X.readline()
    info = X.readline()
    qual = X.readline()
    print(header.replace('@',''))    #the fasta file is devoid of the @ symbol hence must be removed from the fastq file.
    Y.write('>'+header.replace('@','')) #the fasta file starts with '>' and hence the fastq file is modified and written to file Y
    Y.write(sequence)   #the second line if the fasta is always the sequence and is hence copied into the new file Y.
#Close file X and Y to push the changes made.
X.close()
Y.close()


4.
#import the file in fastq format
X =open(r"C:\Users\chari\binf690_charitha\FASTQ",'r')
#Make an output file A
A = open('trimmed.fasta', 'w')


qual=20
n=50
# Create a dictionary of the phred scores using the chr function
phred_score={}
for x in range(0,94):
    phred_score.update({(chr(x+33)):x})

#Read the fastq file by assigning a variable to each line HI, SI, I1 AND Q1
for line in X:
    H1 = line
    S1 = X.readline().strip()
    I1 = X.readline()
    Q1 = X.readline().strip()

#To trim from the left and right end, assign a variable left that starts from 0 and right end that starts at the end
#of the sequence
    left_I = 0
    right_I = len(S1)

    # trimming from the left end of the sequence
    for i in range(0, len(S1)):

        if phred_score[Q1[i]] < qual:
            continue
        else:
            left_I = i
            break
            # S1=S1[i:]
            # Q1=Q1[i:]

    # trimming from right end of the sequence
    for i in range((len(S1) - 1), 0, -1):
        if phred_score[Q1[i]] < qual:
            continue
        else:
            right_index = i + 1
            break

    t_seq = S1[left_I:right_I ]
    if len(t_seq) >= n:
        A.write(H1)
        A.write(t_seq + '\n')
        A.write(I1)
        A.write(Q1[left_I:right_I ] + '\n')

X.close()
A.close()

###Q5. FASTQ file and threshold

IF = open('file.fastq','r')
OF = open('quality-above-threshold.fastq','w')
OF1 = open('quality-below-threshold.fastq', 'w')


for line in IF:
    # creating a list so that avg quality can be measured in integers
    L = []
    H2 = line
    S2 = IF.readline()
    I2 = IF.readline()
    Q2 = IF.readline()
#To measure the quality in terms of integers

    for i in range(0, len(Q2)):     #Q2 is read to append the scores of the characters
        L.append((ord(Q2[i])-33)) #convert each score to its value and - 33 (phred score)

    average_quality=(sum(L)/len(Q2))  #the average quality is the sum of the length of the sequence divided by the length of Q2


    #Since the threshold is taken as 20
    Threshold = 20

    if average_quality >= Threshold:
        OF.write(H2)
        OF.write(S2)
        OF.write(I2)
        OF.write(Q2)
    else:
        OF1.write(H2)
        OF1.write(S2)
        OF1.write(I2)
        OF1.write(Q2)

#Close the file to push the contents
IF.close()
OF.close()
OF1.close()

6.
# initializing string
S="TGTCAGCTACCTTGATGGATTGAGTTTGTTTCGGTCGATGCTCCATCGGGAGAGAGTCTGCGTCCTGGTCCGAGCAAGTCCCACCAAGTGGCACTTGGCGGCGCCATGTCCTATCTAGTGCCACCATGTCCGAGGACTTTGATGGCACATGGTGGCACTTGATTTGCCCAAGTCCCACCTGCTCCGACGTGGACCGACTTCGTGGCACATCGCTATCACCCACTCTACCGTTGAAAAGCCGAAGTCAAGCGCCGAAAGCTGATCGATTTGCGGTGTGATACGTTGCCAGTGATTCGTTCCGTGGTTTATGCTTGGCGCACCTACCGCGTCCCCGACGCATCGACTCCGCCGCCATTGCGCGGCACAAAACGGCCTTCGATCCTTCCGTACGGAGGGGTACTGCAGGGCTCACTGTTCATGCCGGAAATTGCACCGGCTTTTTTTTCAATCAAATCAAGTGGACCGTGTCGGATAGTGAGGACACCGGACACCGCGATACCAAGCCGATTGGCGGTCTGTTTGTGAAAATAGACCGTAGTGCGGACAATTCCGAAGCCGGACACCGGACAGGTGCTCTGTGGAAATTCCGCGTATGCCCGACACCCTTACAGCCGCGTGGCTGGGTGCGGATCACGAAGCCCAAAACACTGCGGCGGGGATGATCTGACTTTGGGGTGGGGAGCTGCTTTGCGTGCCGAATGACGGCGAACGCAGGCTTCTGAGCAAATATCGATCCGGGGGGCGCCACCGGTACCAGAACGGCGCAACAGGTAATCACCCATCACGGCAAGGGCCGCAGGCGTGTGGACGCAATCCACGCGAAGGCAGGCTCGCATCCAGAGATGCACCGGATAGGGTGGCCGCGCAAGCGGTGCGTGAGGCGAGAGCCTTGCATGTTCGCGAAGCGGACGGTCACGACGCATTGCTTCCATGCTCAGGGCCGATCGGTTTGGCATCGCTAAAGGACCGGAAGAGTGGTTGTAGGACCGGCAGGGTGGGCCGGCAAGCTGGGGGTGGTACCCCGGTGCACCAAGCGGGCAGGGCCAATTCGGGGTTGGCGCCGCCGAGAATTGGGTTGCGCAGATTTGCGCGGCCGGCGGGATGCGCTTAGCGCGAATAGGAATCCGTC"

#The longest repeat can only be less than or equal to half length of the sequence
#HS is half of the sequence
HS = int(len(S)/2)
#assign a variable for half the sequence
n= HS
#To find the longest repeat (LR) we can use the function set
LR = set()
#Using a while loop where when n>2, also use a for loop
while n>=2:
    for i in range(0,HS-n+1):
        sub_seq = S[i:i+n]
        if S.count(sub_seq) > 1:
            LR.add(sub_seq)
    if len(LR) > 0:
        break
    n = n-1

print(LR)


#7.
#Ask the user for a string and print out whether this string is a palindrome or not.
#(A palindrome is a string that reads the same forwards and backwards.)

n=input("Enter sequence:")
P=n
O=n [::-1]

if P==O:
    print("It is a Palindrome sequence")
elif P !=O:
    print("It is not a palindrome sequence")

#8.
###Guessing game, generate a random number between 1 and 9 (including 1 and 9).
##Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

g="Guess a number between 1-9"
print(g)

#Create a list of numbers between 1 to 9
L=[1,2,3,4,5,6,7,8,9]

#let x be an element in list L
for x in L:
    a=input("Enter number:")    #variable 'a' is any random number entered
    b=int(a)  # variable 'b' is an integer of 'a'

#In a condition where b is equal to 5
    if b == 5:
        print("Exactly right!!")
#In a condition when b is less than 5
    elif b<5:
        print("Too low")
#In a condition when b is greater than 5
    else:
        print ("Too High")
    break

# 9.
# import the file rna.fasta and extract only the rna sequence from the file
R= open (r"C:\Users\chari\pythonProject\rna.fasta",'r')
# To assign a variable for each line in the file to only extract the sequences from the file
for line in R:
    header=line
    sequence=R.readline()
new_sequence=sequence.replace("\n","")   #extract the sequences only from the file
print(new_sequence)

#Let DictA be the dictionary
D= {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
         "UCU": "S", "UCC": "s", "UCA": "S", "UCG": "S",
         "UAU": "Y", "UAC": "Y", "UAA": "---", "UAG": "---",
         "UGU": "C", "UGC": "C", "UGA": "---", "UGG": "W",
         "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
         "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
         "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
         "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
         "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
         "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
         "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
         "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
         "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
         "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
         "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
         "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }

protein = "" #Generate another empty string where the translated proteins can be added

# To generate protein string

for i in range(0, len(new_sequence)-(len(new_sequence)%3), 3): #range(start=0, stop, How many jumps the make)
    if D[new_sequence[i:i+3]] == "STOP" :
        break                               # Apply break to when the stop codon is mentioned
    protein += D[new_sequence[i:i+3]]    #To the new string called protein, keep adding the amino acid values
                                          # corresponding from the Dictionary.

# Print the protein string
print ("Protein string : ", protein)



