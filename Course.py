

from bs4 import BeautifulSoup
import requests
import re
print('\nCybersecurity:')
response=requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Cybersecurity-Accelerated-Second-Degree-BS')

soup = BeautifulSoup(response.content, "html.parser")
s=soup.get_text()
#print(s)
t=soup.title
print(t)
#(?<=Please) (?!lazy) [^Sample]*    #(?<!Sample\sDegree\sPlan
#note that this

matches=re.findall('[ITMSCPH]{2,3}\s\d{3}[A-Za-z\s]{9,}\d{1}',s)


#matches=re.findall (r'[ITMSCPH]{2,3}\s\d{3}[A-Za-z\s]{9,}\d{1}',s) #(?=Samples Degree Plan)
id=re.findall (r'[ITMSCPH]{2,3}\s\d{3}(?=[A-Za-z\s]{9,}\d{1})',s)
course=re.findall(r'(?=[ITMSCPH]{2,3}\s\d{3})([A-Za-z\s]{9,})(?<=\d{1})',s)
credit=re.findall(r'(?=[ITMSCPH]{2,3}\s\d{3}[A-Za-z\s]{9,})\d{1} ',s)

#print(f'{id}, {course}, {credit}')

#matches=re.sub('[ITMSCPH]{2,3}\s\d{3}[A-Za-z\s]{9,}\d{1} ',',  , ',s)
#matches=re.findall(r'?! Major Requirements IT.*',t)
#print(matches)

"""
for m in matches:
    print(matches[index])
    if index==23:
        break
    index+=1
"""
filename = "Cybersecurity Accelerated Second Degree (B.S.).csv"
f = open(filename, "w")
index=0
for m in matches:
    print(matches[index])
    index += 1
    if index == 23:
        break
    f.write(m)

#SECOND SITE
print('\n\nInformation Technology')
response1=requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Information-Technology-B-S')

soup1 = BeautifulSoup(response1.content, "html.parser")
s1=soup1.get_text()
t1=soup1.title
print(t1)
matches1=re.findall('[ITMAMGTMSCPH]{2,3}\s\d{3}[A-Za-z\s]{9,}\d{1}',s1)
index1=0
filename1 = "Information Technology (B.S.).csv"
f1 = open(filename1, "w")
index1=1
for m in matches1:
    print(matches1[index1])
    if index1 == 28:
        break
    index1 += 1
    f1.write(m)


#THIRD SITE
print('\n\nB.S. AND M.S. Information Technology')

response2=requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Information-Technology-Combined-B-S-M-S-Program')

soup2 = BeautifulSoup(response2.content, "html.parser")
s2=soup2.get_text()
t2=soup2.title
print(t2)
matches2=re.findall('[IT]{2}\s\d{3}[A-Za-z\s]{1,}\n',s2)
index2=0
filename2 = "Information Technology Combined B.S. M.S. Program.csv"
f2 = open(filename2, "w")

index2=0
for m in matches2:
    print(matches2[index2])
    if index2 == 5:
        break
    index2 += 1
    f2.write(m)

#FOURTH SITE
print('\n\nB.S. AND M.S. Cybersecurity and Information Technology')

response3=requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Information-Technology-and-Cybersecurity-Combined-B-S-M-S-Program')

soup3 = BeautifulSoup(response3.content, "html.parser")
s3=soup3.get_text()
t3=soup3.title
print(t3)
matches3=re.findall('[ITMSC]{2,3}\s\d{3}[A-Za-z\s:,]{1,}\n',s3)
index3=0
filename3 = "Information Technology and Cybersecurity Combined B.S. M.S. Program.csv"
f3 = open(filename3, "w")

index3=0
for m in matches3:
    print(matches3[index3])
    if index3 == 5:
        break
    index3 += 1
    f3.write(m)

#FIFTH SITE
print('\n\nM.B.A.')
response4=requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Information-Technology-B-S-to-M-B-A-Program')

soup4 = BeautifulSoup(response4.content, "html.parser")
s4=soup4.get_text()
t4=soup4.title
print(t4)
matches4=re.findall('[MBA]{2,3}\s\d{3}[A-Za-z\s]{9,}\d{1}',s4)
index4=0
filename4 = "Information Technology (B.S.) to M.B.A Program.csv"
f4 = open(filename4, "w")
index4=0
for m in matches4:
    print(matches4[index4])
    if index4 == 28:
        break
    index4 += 1
    f4.write(m)

#SIXTH SITE

print('\n\nMINOR Networking and cyber')
response5=requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Computer-Networking-and-Cybersecurity-Minor')

soup5 = BeautifulSoup(response5.content, "html.parser")
s5=soup5.get_text()
t5=soup5.title
print(t5)
matches5=re.findall('[IT]{2,3}\s\d{3}[A-Za-z\s:]{1,}\d{1}',s5)
index5=0
filename5 = "Computer Networking and Cybersecurity (Minor).csv"
f5 = open(filename5, "w")
index5=0
for m in matches5:
    print(matches5[index5])
    if index5 == 6:
        break
    index5 += 1
    f5.write(m)

#SEVENTH SITE

print('\n\nCS MINOR')
response6=requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Computer-Science-Minor')

soup6 = BeautifulSoup(response6.content, "html.parser")
s6=soup6.get_text()
t6=soup6.title
print(t6)
matches6=re.findall('[ITMA]{2,3}\s\d{3}[A-Za-z\s:]{1,}\d{1}',s6)
index6=0
filename6 = "Computer Science (Minor).csv"
f6 = open(filename6, "w")
index6=0
for m in matches6:
    print(matches6[index6])
    if index6 == 6:
        break
    index6 += 1
    f6.write(m)

#EIGHT SITE

print('\n\nDataScience MINOR')
response7=requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Data-Science-Minor')

soup7 = BeautifulSoup(response7.content, "html.parser")
s7=soup7.get_text()
t7=soup7.title
print(t7)
matches7=re.findall('[ITMAMSC]{2,3}\s\d{3}[A-Za-z\s:]{1,}\d{1}',s7)
index7=0
filename7 = "Data Science (Minor).csv"
f7 = open(filename7, "w")
index7=0
for m in matches7:
    print(matches7[index7])
    if index7 == 9:
        break
    index7 += 1
    f7.write(m)


#NINTH SITE

print('\n\nForensic MINOR')
response8=requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Forensic-Computing-Minor')

soup8 = BeautifulSoup(response8.content, "html.parser")
s8=soup8.get_text()
t8=soup8.title
print(t8)
matches8=re.findall('[CJITMAMSC]{2,3}\s\d{3}[A-Za-z\s:]{1,}\d{1}',s8)
index8=0
filename8 = "Forensic Computing (Minor).csv"
f8 = open(filename8, "w")
index8=0
for m in matches8:
    print(matches8[index8])
    if index8 == 10:
        break
    index8 += 1
    f8.write(m)


#TENTH SITE

print('\n\nIT MINOR')
response9=requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Information-Technology-Minor')

soup9 = BeautifulSoup(response9.content, "html.parser")
s9=soup9.get_text()
t9=soup9.title
print(t9)
matches9=re.findall('[ITMSC]{2,3}\s\d{3}[A-Za-z\s:]{1,}\d{1}',s9)
index9=0
filename9 = "Information Technology (Minor).csv"
f9 = open(filename9, "w")
index9=0
for m in matches9:
    print(matches9[index9])
    if index9 == 10:
        break
    index9 += 1
    f9.write(m)


#ELEVENTH SITE
print('\n\n DATA SCIENCE CERTIFICATE')
response10=requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Data-Science-Post-Baccalaureate-Certificate')

soup10 = BeautifulSoup(response10.content, "html.parser")
s10=soup10.get_text()
t10=soup10.title
print(t10)
matches10=re.findall('[MAITMSC]{2,3}\s\d{3}[A-Za-z\s:]{1,}\d{1}',s10)
index10=0
filename10 = "Data Science (Post-Baccalaureate Certificate).csv"
f10= open(filename10, "w")
index10=0
for m in matches10:
    print(matches10[index10])
    if index10 == 10:
        break
    index10 += 1
    f10.write(m)



"""
text=response.text.replace('\n', ' ').replace('\r', '')response=requests.get('http://marymount.smartcatalogiq.com/2019-2020/Catalogs/Undergraduate-Catalog/School-of-Business-Administration/Information-Technology-and-Cybersecurity/Cybersecurity-Accelerated-Second-Degree-BS (Links to an external site.)')

    text=response.text.replace('\n', ' ').replace('\r', '') 
"""