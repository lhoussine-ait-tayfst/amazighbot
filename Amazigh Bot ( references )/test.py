#/////////////////////////////////////////////////////////////////////////////////////////////

#//////     Aɣawas ad ar ittawi taguri <references/> uḍɣaṛ ns g Wikipidya taclḥit    /////////

#/////////////////////////////////////////////////////////////////////////////////////////////

import pywikibot

print("Tawwri ar tzzigiz")

site = pywikibot.Site()   #extraction of the site address
print("Amazigh Bot yufa wiki tamazight : ",site)

#title = "Wikipidya"   #c'est un article


pool = site.allpages(namespace=0,filterredir=False)   #extraction of all pages names

i=0  
#Tagṭṭumt n <references/>
for page in pool:
    print("Assnfl wiss:",i)
    if "<references/>" in page.text:
        page.text = page.text.replace("<references/>","")
        page.save("Kksɣ <references/> tamzwarut")
    if "<references />" in page.text:
        page.text = page.text.replace("<references />","")
        page.save("Kksɣ <references /> tamzwarut")
    page.text = page.text.replace("== Isaɣuln ==","== Isaɣuln == \n {{Iɣbula}} \n <references/>")
    page.save("Rniɣ <references/> d {{Iɣbula}} i tagṭṭumt n Isaɣuln")
    i+=1
    #tigira n for


    




           




"""
#print(len(list(pool)))

#page = pywikibot.Page(site,title)

#page.text = page.text.replace(source_str,target_str)

#page.save("irim")


i = 0

for page in pool:
    if source_str in page.text:
        page.text = page.text.replace(source_str,target_str)
        page.save("irim")
        i+=1
        if i==10:
            break
        
"""


#Tigira n uɣawas
print("Tkmml twwuri !!")
