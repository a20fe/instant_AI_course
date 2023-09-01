import re 
with open("instant_task_8.txt" , 'r') as file :
    text=file.read()
    print(text)
    
names =[]
numbers =[]
mails =[]

pattern1=re.compile(r"\b[a-zA-Z]+ [a-zA-Z]+\b ([a-zA-Z][a-z]+)?\b")
matches=pattern1.finditer(text)
for match in matches :
    names.append(match.group())
print (f"names in file 1 :{names}")

pattern2=re.compile(r"\b[A-Za-z_0-9]+@\b[A-Za-z]{2,15}\.[a-z]{2,10}")
matches=pattern2.finditer(text)
for match in matches :
    mails.append(match.group())
print (f"mails in file 1 :{mails}")

pattern3 =re.compile(r"\b01[1205]\d{8}")
matches=pattern3.finditer(text)
for match in matches :
    numbers.append(match.group())
print (f"numbers in file 1 :{numbers}")