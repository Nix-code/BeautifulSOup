import requests
from bs4 import BeautifulSoup
url='https://www.codewithharry.com/'
#step 1 get the html
r=requests.get(url)
htmlContent=r.content
#print(htmlContent)
#step 2 : Parse the html
#make the soup
soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup)  BeautifulSoup
#print beautifully
#print(soup.prettify)


#step 3 Tree traversal
title=soup.title #tag
#print(title)
#print(type(title))
#print(type(title.string)) #NavigableString

#commonly used types of objects
"""
1 Tag
2. NavigableString
3.BeautifulSoup
4. comment
"""

#get all the paragraphs from the page
paras=soup.find_all('p')
#print(paras)



#get all the anchor from the page

anchors=soup.find_all('a')
#print(anchors)


#find the 1st paragraphs
#print(soup.find('p'))
#print(soup.find('p')['class']) #get classes of any page
# can use id too
#find all the elements within the class lead
#print(soup.find_all('p',class_='lead'))

#print(soup.find('p').get_text())



#get all the links
#this may give repeated links
"""
for link in anchors:
    print(link.get('href'))


all_links=set()
for link in anchors:
    if(link.get('href')!="#"):
        linkText="https://codewithharry.com"+link.get('href')
        all_links.add(linkText)
        print(linkText)
"""
markup="<p><!-- this is a comment --></p>"
soup2=BeautifulSoup(markup)
print(soup2.p) #prints paragraph
print(soup2.p.string) # print string of comment

navbarSupportedContent=soup.find(id='navbarSupportedContent')
#for elem in navbarSupportedContent.contents:   #stored in memory
   # print(elem)
        
"""
for elem in navbarSupportedContent.children: #not stored in memory
    print(elem)"""
#for elem in navbarSupportedContent.strings:   #stored in memory
    #print(elem)

#for elem in navbarSupportedContent.stripped_strings:   #stored in memory
    #print(elem)
#for i in navbarSupportedContent.parents:   
    #print(i)


#print(navbarSupportedContent.next_sibling.next_sibling)
#print(navbarSupportedContent.previous_sibling.previous_sibling)

#elem=soup.select('#loginModal')
#print(elem)


elem=soup.select('.modal-footer')
print(elem)

