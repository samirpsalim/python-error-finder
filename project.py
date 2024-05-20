"""
Program to accept a python file in the same directory as this file as input and analyse small errors
1.Quotes not closed
2.Open multiline comments
3.Brackets closed where they are not expected
4.Brackets left open
5.':' missing at the end of lines containg if,else,elif,for,while,def
6.more than one of if,else,elif,for,while,def present in a single line
7.An expected indented block at the end of a file is missing
8.Improper indentation after usage of if,else,elif,for,while,def

input format:
Enter filename when "Enter filename: " is prompted
eg:
Enter filename: file1.py

Mini project
Done by:
Anandu AP -2019csb1069
Samir P Salim -2019csb1117
"""
def splitline(s,ch):#this function splits the given string into different substrings at the special character'ch'
    #ch is not found in the output
    """
    eg:splitline("7 8 6"," ")
    returns ["7","8","6"]
    """
    ans=[]#returns this list
    start=0#notes the character from which each branch starts ie,each time ch is encountered the next character
    for i in range(len(s)):
        if(s[i]==ch):
            ans.append(s[start:i])#adds each branch to ans .Each branch ends just before ch.The character at position i is
            #ch and is not added
            start=i+1#each time ch is encountered the position of the next character is assigned 
    if(s[len(s)-1]!=ch):#if the last character is not ch it does not get added to the list in the loop.So it is added here  
        ans.append(s[start:len(s)])
    return ans#returns the list

def readfile(a):#This function reads the contents of the file and returns it as a string
    """
    eg:readfile("k.txt")
    where contents of k is (the part between the lines containing '***')
    ***
    This is a sample to demonstrate
    the function
    
    ***
    returns "This is a sample to demonstrate\nthis function\n\n"
    where \n represents end of line
    """
    f=open(a,"r")#Opens the given file
    k=f.read()#Reads it and assigns contents to k
    f.close()#Closes the file
    return k#returns the list

sp=['"',"'","(",")","{","}","[","]","for","else","while","if","def","elif","#"]#this list stores all the strings which are 
#noted in the program
k1=""#This is to append "'''" to sp
k2=""#This is to append '"""' to sp
sp2=["(","[","{"," ","Multiline comment","if"]#This is to track the positions of open brackets and multiline comment and 
#if stattements and number of spaces required for proper indentation
sp3=[]#This is to track the positions of open brackets and multiline comment and number of spaces required for proper
#indentation 
for i in range(6):#This loop appends 6 lists containing [0],thus initialising sp3
    sp3.append([0])
for i in range(3):#makes k1 as"'''" and k2 as'"""'
    k1=k1+"'"
    k2+='"'
sp.append(k1)#appends k1
sp.append(k2)#appends k2
a=input("Enter filename: ")#Accepts the filename of the file in the same directory as input
k=readfile(a)#assigns file contents as a string to k
k=splitline(k,"\n")#splits k into a list where the file contains "\n" between two consecutive elements of k
sp1=[0]*17#This list is to check if there is an open bracket or string literal or a multline comment or if an if statement have 
#appeared in the file
ans=[]#This list contains the errors and is used to sort them according to their line number

def bracket():#returns the bracket that closes the last bracket opened
    if(sp1[2]==1 and sp1[4]==0 and sp1[6]==0):#if '(' is open returns ')' 
        return sp[3]
    elif(sp1[2]==0 and sp1[4]==1 and sp1[6]==0):#if '{' is open returns '}'
        return sp[5]
    elif(sp1[2]==0 and sp1[4]==0 and sp1[6]==1):#if '[' is open returns ']'
        return sp[7]
    elif(sp1[2]==1 and sp1[4]==1 and sp1[6]==0):#if both '(' and '{' have appeared returns the one that closes the last 
        #bracket opened 
        if(sp3[0][len(sp3[0])-1]>sp3[2][len(sp3[2])-1]):#compares the last appearances of '(' and "{' and returns the one
            #that closes the last bracket opened 
            return sp[3]
        elif(sp3[0][len(sp3[0])-1]<sp3[2][len(sp3[2])-1]):#compares the last appearances of '(' and "{' and returns the one
            #that closes the last bracket opened 
            return sp[5]
    elif(sp1[2]==1 and sp1[4]==0 and sp1[6]==1):#if both '(' and '[' have appeared returns the one that closes the last 
        #bracket opened 
        if(sp3[0][len(sp3[0])-1]>sp3[1][len(sp3[1])-1]):#compares the last appearances of '(' and "[' and returns the one
            #that closes the last bracket opened 
            return sp[3]
        elif(sp3[0][len(sp3[0])-1]<sp3[1][len(sp3[1])-1]):#compares the last appearances of '(' and "[' and returns the one
            #that closes the last bracket opened 
            return sp[7]
    elif(sp1[2]==0 and sp1[4]==1 and sp1[6]==1):#if both '{' and '[' have appeared returns the one that closes the last 
        #bracket opened 
        if(sp3[1][len(sp3[1])-1]>sp3[2][len(sp3[2])-1]):#compares the last appearances of '{' and "[' and returns the one
            #that closes the last bracket opened 
            return sp[7]
        elif(sp3[1][len(sp3[1])-1]<sp3[2][len(sp3[2])-1]):#compares the last appearances of '{' and "[' and returns the one
            #that closes the last bracket opened 
            return sp[5]
    else:
        if(sp3[0][len(sp3[0])-1]<sp3[1][len(sp3[1])-1] and sp3[1][len(sp3[1])-1]>sp3[2][len(sp3[2])-1]):#if '[' have 
            #appeared last returns ']'
            return sp[7]
        elif(sp3[0][len(sp3[0])-1]<sp3[2][len(sp3[2])-1] and sp3[1][len(sp3[1])-1]<sp3[2][len(sp3[2])-1]):#if '{' have 
            #appeared last returns '}'
            return sp[5]
        elif(sp3[0][len(sp3[0])-1]>sp3[1][len(sp3[1])-1] and sp3[0][len(sp3[0])-1]>sp3[2][len(sp3[2])-1]):#if '(' have 
            #appeared last returns ')'
            return sp[3]
        
def num(i,k):
    """ 
    accepts i,k and returns a number such that last 3 digits indicate k and the ones before it i as long as k<1000
    eg:num(23,15)
    returns 23015
    """
    return i*1000+k
    
def exist(s,l):
    """
    returns the number of elements in the list l that appears in s
    """
    ans=0#Returns this number
    for k in l:#traversing through the list
        if(s.find(k)!=-1):#if k is found in s
            ans+=1#increment answer
    return ans

def blanklength(t):
    """
    Returns the number of spaces in the beginning of the string t
    """
    ans=0#returns this number
    if(len(t)!=0):#if t is not ""
        while(t[ans]==" " and ans<len(t)-1):#as long as spaces keep on repeating and ans<index of last element
            ans=ans+1
        if(t[len(t)-1]==" "):#if last element is  a space
            ans+=1
    return ans

def lastline(l):
    """
    Returns the last line which contain anything other than a space if there exist such a line
    ie, it's content and line number
    """
    i=0#keeps the loop running till the required line is found
    s=l[len(l)-1]#s is the string that will be returned assigning the last line
    k=1#k is used to go to the previous line
    while(i==0 and k<=len(l)):#as long as the required line is not found and the first line is not reached 
        if(blanklength(s)==len(s)):#if the line is full of blanks
            k=k+1
            s=l[len(l)-k]#going to the previous line
        else:#if the required line is reached
            i=1#breaking the loop
    if(k!=len(l)+1):#if a line was found
        return [s,len(l)-k]

def lastchar(f):
    """
    this function returns the position of the last character in f which is not a space
    """
    ans=-1#this variable is returned
    for i in range(len(f)):#till the end of f
        if(f[i]!=" "):#if the current character is not a space
            ans=i
    return ans

def check():
    """
    The function where all the error finding takes place
    """
    for j in range(len(k)):#till the end of file
        i=k[j]#i is the j+1 th line
        for t in range(len(i)):#till the end of line
            if(sp1[15]==1):#if in a multiline comment starting as '''
                if(t>=2):#from the third element of the line
                    if(i[t-2:t+1]==sp[15]):#if the t+2 to t are '''
                        sp1[15]=0
            elif(sp1[16]==1):#if in a multiline comment starting as """
                if(t>=2):#from the third element of the line
                    if(i[t-2:t+1]==sp[16]):#if the t+2 to t are """
                        sp1[16]=0
            elif(sp1[0]+sp1[1]==1):#if a quote is open    
                if(sp1[0]==1):#if the quote starts with "
                    if(i[t]==sp[0]):#if the current character is a "
                        sp1[0]=0
                else:#if the quote starts with '
                    if(i[t]==sp[1]):#if the current character is a "
                        sp1[1]=0
            elif(i[t]==sp[14]):#if the character is a # ie,beginning of a singleline comment
                break #skip to next line
            elif((sp1[2]==1 or sp1[4]==1 or sp1[6]==1) and bracket()==i[t]):#if a bracket is open and the current character
                #is the closing bracket
                if(i[t]==sp[3]):#if it is a ')'
                    sp3[0].remove(sp3[0][len(sp3[0])-1])#remove the last opened '(' from the list of open '('
                    if(len(sp3[0])==1):#if there are no more '(' left to be closed
                        sp1[2]=0
                elif(i[t]==sp[5]):#if it is a '}'
                    sp3[2].remove(sp3[2][len(sp3[2])-1])#remove the last opened '{' from the list of open '{'
                    if(len(sp3[2])==1):#if there are no more '{' left to be closed
                        sp1[4]=0
                elif(i[t]==sp[7]):
                    sp3[1].remove(sp3[1][len(sp3[1])-1])#remove the last opened '[' from the list of open '['
                    if(len(sp3[1])==1):#if there are no more '[' left to be closed
                        sp1[6]=0
            elif(i[t]==sp[3] or i[t]==sp[5] or i[t]==sp[7]):#if the current character is a closing bracket but that is not 
                #the bracket that closes the last open bracket or if there is no open bracket
                ans.append([j,"line "+str(j+1)+"\n"+i+"\nWrong bracket closed"])#adding the error to the answer
            elif(i[t]==sp[2]):#if it is a'('
                sp1[2]=1
                sp3[0].append(num(j+1,t))#noting the open bracket
            elif(i[t]==sp[4]):#if it is a'{'
                sp1[4]=1
                sp3[2].append(num(j+1,t))#noting the open bracket
            elif(i[t]==sp[6]):#if it is a'['
                sp1[6]=1
                sp3[1].append(num(j+1,t))#noting the open bracket
            elif(i[t]==sp[0]):#if it is a "
                if(t>=2):#if this is after the second element
                    if(i[t-2:t+1]==sp[16]):#if the last three elements is """
                        sp1[16]=1
                        sp3[4][0]=num(j+1,t)#noting the start of a multiline comment
                    else:#if it is an ordinary string that starts with "
                        sp1[0]=1
                else:#if it is one of the first two elements it is taken as an ordinary string if it is not so sp1[0] becomes 
                    #zero at the second " and comes back here 
                    sp1[0]=1
            elif(i[t]==sp[1]):#if it is a '
                if(t>=2):#if this is after the second element
                    if(i[t-2:t+1]==sp[15]):#if the last three elements is '''
                        sp1[15]=1
                        sp3[4][0]=num(j+1,t)#noting the start of a multiline comment
                    else:#if it is an ordinary string that starts with "
                        sp1[1]=1
                else:#if it is one of the first two elements it is taken as an ordinary string if it is not so sp1[0] becomes 
                    #zero at the second " and comes back here 
                    sp1[1]=1
        #the following errors are checked after each line
        if(sp1[15]==0 and sp1[16]==0):#if it is not in a multiline comment
            if(blanklength(i)<sp3[3][0] and blanklength(i)!=len(i)):#if it is not a blankline without insufficient spaces
                #in the beginning
                ans.append([j,"line "+str(j+1)+"\n"+i+"\nIndentation error"])           
            if(exist(i,sp[8:14])>1):#if there are more than one of if,else,elif def,for,while
                ans.append([j,"line "+str(j+1)+"\n"+i+"\nMultiple conditional or iterational statements in a single line"])
            elif(exist(i,sp[8:14])==1):#if there is exactly one of them
                if(i.find("if")!=-1):#if that is an if
                    sp1[11]=1
                    sp3[5].append(blanklength(i))#noting the position of that if
                if(i[lastchar(i)]!=":"):#if the last character
                    ans.append([j,"line "+str(j+1)+"\n"+i+"\n':' missing"])
                sp3[3][0]=blanklength(i)+1#noting the number of spaces required in the next line for proper indentation
            elif(blanklength(i)!=len(i)):#if all elements are not spaces
                sp3[3][0]=0
            if(sp1[1]==1 or sp1[0]==1):#if any of the quotes are open
                ans.append([j,"line "+str(j+1)+"\n"+i+"\nquotes not closed"])
                sp1[0]=0
                sp1[1]=0
    #the following is noted at the end of a file
    if(sp1[15]==0 and sp1[16]==0):#if no multiline comment is open
        if(sp1[2]==1 or sp1[4]==1 or sp1[6]==1):#if any bracket is open
            for i in range(3):#all these open brackets are added as errors in the answer
                for j in range(1,len(sp3[i])):
                    ans.append([sp3[i][j]//1000-1,"line "+str(sp3[i][j]//1000)+"\n"+k[sp3[i][j]//1000-1]+"\nBracket not closed"])
        if(exist(lastline(k)[0],sp[8:14])):#if the last line that is not a blankline contains any of 
            #if,else,def,elif,for,while
            ans.append([lastline(k)[1],"line "+str(lastline(k)[1]+1)+"\n"+k[lastline(k)]+"\nExpected an indented block"]) 
    if(sp1[15]==1 or sp1[16]==1):#if a multiline comment is open
        ans.append([sp3[4][0]//1000-1,"line"+str(sp3[4][0]//1000)+"\n"+k[sp3[4][0]//1000-1]+"\nOpen multiline comment"])

check()#calling the check function
if(len(ans)!=0):#if there is some error
    print("\n\n")
    ans.sort()#sort the errors according to line number
    for i in range(len(ans)):#for all errors noted
        print(ans[i][1])#print each error
else:#if no error is found
    print("\nNo error detected in the given file")