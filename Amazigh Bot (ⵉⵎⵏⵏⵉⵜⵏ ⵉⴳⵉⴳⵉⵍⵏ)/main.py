#/////////////////////////////////////////////////////////////////////////////////////////////

#//////     Aɣawas ad ar ittkks imnnitn igigiln sg Wikipidya tamaziɣt    //////////////////////

#/////////////////////////////////////////////////////////////////////////////////////////////

import pywikibot


print("Tawwri ar tzzigiz")

site = pywikibot.Site()   #extraction of the site address
print("Amazigh Bot yufa Wikippidya tamazight : ",site)

#title = "Wikipidya"   #c'est un article


target_str1 = "== ⵉⵙⴰⵖⵓⵍⵏ =="
target_str2 = "\n== ⵉⵙⴰⵖⵓⵍⵏ == \n*'''ⴰⵙⴳⵣⴰⵡⴰⵍ ⵏ [[ⴰⵙⵉⵏⴰⴳ ⴰⴳⵍⴷⴰⵏ ⵏ ⵜⵓⵙⵙⵏⴰ ⵜⴰⵎⴰⵣⵉⵖⵜ]](ⵙ.ⴳ.ⵙ.ⵎ) :''' [[ⵎⵙⵎⵓⵏ ⴰⵡⴰⵍ ⴰⵎⴰⵜⴰⵢ ⴰⵙⵏⵎⴰⵍⴰⵢ ⵏ ⵜⵎⴰⵣⵉⵖⵜ]] (ⵎ.ⵎ.ⵙ.ⵎ)"
target_str3 = "\n*'''ⴰⵙⴳⵣⴰⵡⴰⵍ ⵏ [[ⴰⵙⵉⵏⴰⴳ ⴰⴳⵍⴷⴰⵏ ⵏ ⵜⵓⵙⵙⵏⴰ ⵜⴰⵎⴰⵣⵉⵖⵜ]](ⵙ.ⴳ.ⵙ.ⵎ) :''' [[ⵎⵙⵎⵓⵏ ⴰⵡⴰⵍ ⴰⵎⴰⵜⴰⵢ ⴰⵙⵏⵎⴰⵍⴰⵢ ⵏ ⵜⵎⴰⵣⵉⵖⵜ]] (ⵎ.ⵎ.ⵙ.ⵎ)"




pool = site.deadendpages()

i = 0
for page in pool:
    if target_str1 in page.text: 
        print("Assnfl wiss :",i+1)
        page.text += target_str3
        page.save("ⵔⵏⵉⵖ ⴰⵙⴰⵖⵓⵍ ⵙ ⵎⵙⵎⵓⵏ ⴰⵡⴰⵍ ⵏ ⵓⵙⵉⵏⴰⴳ ⴰⴳⵍⴷⴰⵏ ⵏ ⵜⵓⵙⵙⵏⴰ ⵜⴰⵎⴰⵣⵉⵖⵜ")
        i+=1

    if not target_str1 in page.text: 
        print("Assnfl wiss :",i+1)
        page.text += target_str2
        page.save("ⵔⵏⵉⵖ ⴰⵙⴰⵖⵓⵍ ⵙ ⵎⵙⵎⵓⵏ ⴰⵡⴰⵍ ⵏ ⵓⵙⵉⵏⴰⴳ ⴰⴳⵍⴷⴰⵏ ⵏ ⵜⵓⵙⵙⵏⴰ ⵜⴰⵎⴰⵣⵉⵖⵜ")
        i+=1
    


print("Amazigh Bot iwfa g Wikipidya tamazight :",len(list(pool)),"n umnni igan igigil")
#print("Tkmml twwuri !!")
        


#Tigira n uɣawas
print("Tkmml twwuri !!")
