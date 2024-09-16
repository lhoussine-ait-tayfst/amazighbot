import pywikibot

print("Tawwri ar tzzigiz")

site = pywikibot.Site()   #extraction of the site address
print("Amazigh Bot iwfa Wikippidya taclḥit : ",site)


#Tagṭṭumt n Isaɣuln d Ẓṛ uggar //////////////////////////////////////////
pool = site.allpages(namespace=0,filterredir=False)   #extraction of all pages names

i=0
j=0

for page in pool:
    print("Asnfl n umnni wiss : ",j)
    
    #Tagṭṭumt n Ẓṛ uggar
    if "== ⵥⵕ ⴰⵡⴷ ==" in page.text:
        page.text = page.text.replace("== ⵥⵕ ⴰⵡⴷ ==","== ⵥⵕ ⵓⴳⴳⴰⵔ ==")
        page.save("ⵜⴰⵏⵟⵟⵓⴼⵜ ⵏ ⵜⵓⵟⵟⵓⵜ ⵏ ⵥⵕ ⵓⴳⴳⴰⵔ")

    if "==ⵥⵕ ⴰⵡⴷ==" in page.text:
        page.text = page.text.replace("==ⵥⵕ ⴰⵡⴷ==","== ⵥⵕ ⵓⴳⴳⴰⵔ ==")
        page.save("ⵜⴰⵏⵟⵟⵓⴼⵜ ⵏ ⵜⵓⵟⵟⵓⵜ ⵏ ⵥⵕ ⵓⴳⴳⴰⵔ")

    if "== ⵥⵕ ⵓⵍⵜⵓ ==" in page.text:
        page.text = page.text.replace("== ⵥⵕ ⵓⵍⵜⵓ ==","== ⵥⵕ ⵓⴳⴳⴰⵔ ==")
        page.save("ⵜⴰⵏⵟⵟⵓⴼⵜ ⵏ ⵜⵓⵟⵟⵓⵜ ⵏ ⵥⵕ ⵓⴳⴳⴰⵔ")

    if "== ⵥⵔ ⵓⵍⴰ ==" in page.text:
        page.text = page.text.replace("== ⵥⵔ ⵓⵍⴰ ==","== ⵥⵕ ⵓⴳⴳⴰⵔ ==")
        page.save("ⵜⴰⵏⵟⵟⵓⴼⵜ ⵏ ⵜⵓⵟⵟⵓⵜ ⵏ ⵥⵕ ⵓⴳⴳⴰⵔ")

    if "== ⵥⵕ ⵓⵍⴰ ==" in page.text:
        page.text = page.text.replace("== ⵥⵕ ⵓⵍⴰ ==","== ⵥⵕ ⵓⴳⴳⴰⵔ ==")
        page.save("ⵜⴰⵏⵟⵟⵓⴼⵜ ⵏ ⵜⵓⵟⵟⵓⵜ ⵏ ⵥⵕ ⵓⴳⴳⴰⵔ")


    
    
    i+=1
    j+=1
    #tigira n for


    





#Tigira n uɣawas
print("Tkmml twwuri !!")
