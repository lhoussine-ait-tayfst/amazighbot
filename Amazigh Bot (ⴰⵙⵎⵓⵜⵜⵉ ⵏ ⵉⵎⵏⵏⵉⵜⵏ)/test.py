#/////////////////////////////////////////////////////////////////////////////////////////////

#//////     Aɣawas ad ar ittkks imnnitn igigiln sg Wikipidya tamaziɣt    //////////////////////

#/////////////////////////////////////////////////////////////////////////////////////////////

import pywikibot


print("Tawwri ar tzzigiz")

site = pywikibot.Site()   #extraction of the site address
print("Amazigh Bot yufa Wikippidya tamazight : ",site)



target_str1 = "{{ⴰⵙⴱⵔⵔⴽ}}"
target_str2 = "\n== ⴰⵙⴱⵔⵔⴽ ==\n{{ⴰⵙⴱⵔⵔⴽ}} \n--[[User:Amazigh Bot|Amazigh Bot]]"




pool = site.allpages(namespace=0,filterredir=False)

i = 0
for page in pool:
    if not target_str1 in page.text: 
        print("Assnfl wiss :",i+1)
        page.text += target_str2
        page.save("ⵙⴱⵔⵔⴽⵖ ⵙ ⵓⵏⵙⵙⵎⵔⵙ")
        i+=1
    


print("Amazigh Bot iwfa g Wikipidya tamazight :",len(list(pool)),"n unssmrs")
#print("Tkmml twwuri !!")
        


#Tigira n uɣawas
print("Tkmml twwuri !!")
