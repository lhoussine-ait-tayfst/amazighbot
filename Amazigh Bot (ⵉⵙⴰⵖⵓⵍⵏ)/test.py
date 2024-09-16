import pywikibot

print("ⴰⵖⴰⵡⴰⵙ ⴰⵔ ⵉⵣⵣⵉⴳⵉⵣ")

site = pywikibot.Site()   #extraction of the site address
print("Amazigh Bot ⵢⵓⴼⴰ ⵡⵉⴽⵉⴱⵉⴷⵢⴰ ⵜⴰⵎⴰⵣⵉⵖⵜ : ",site)

#title = "Wikipidya"   #c'est un article


#ⵜⴰⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ 
pool = site.allpages(namespace=0,filterredir=False)   #extraction of all pages names

i=0
j=0

for page in pool:
    print("ⴰⵙⵏⴼⵍ ⵡⵉⵙⵙ : ",j)
    
    #ⵜⴰⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ  
    if "== ⵜⵉⵖⴱⵓⵍⴰ ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")  
        page.text = page.text.replace("== ⵜⵉⵖⴱⵓⵍⴰ ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "==ⵜⵉⵖⴱⵓⵍⴰ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")  
        page.text = page.text.replace("==ⵜⵉⵖⴱⵓⵍⴰ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        
    if "==ⵜⵉⵖⴱⵓⵍⴰ==" in page.text:
         if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
         page.text = page.text.replace("==ⵜⵉⵖⴱⵓⵍⴰ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
         page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "==ⵜⵉⵖⴱⵓⵍⴰ ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("==ⵜⵉⵖⴱⵓⵍⴰ ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "== ⵜⵉⵖⴱⵓⵍⴰ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("== ⵜⵉⵖⴱⵓⵍⴰ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "== ⵜⵉⵖⴱⵓⵍⴰ : ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("== ⵜⵉⵖⴱⵓⵍⴰ : ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "==ⵜⵉⵖⴱⵓⵍⴰ :==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("==ⵜⵉⵖⴱⵓⵍⴰ :==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "==ⵜⵉⵖⴱⵓⵍⴰ : ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("==ⵜⵉⵖⴱⵓⵍⴰ : ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "== ⵜⵉⵖⴱⵓⵍⴰ :==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("== ⵜⵉⵖⴱⵓⵍⴰ :==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "== ⵜⵉⵖⴱⵓⵍⴰ: ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("== ⵜⵉⵖⴱⵓⵍⴰ: ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "==ⵜⵉⵖⴱⵓⵍⴰ:==" in page.text:
        page.text = page.text.replace("==ⵜⵉⵖⴱⵓⵍⴰ:==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "== ⵜⴰⴱⵉⴱⵍⵢⵓⴳⵔⴰⴼⵉⵜt ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("== ⵜⴰⴱⵉⴱⵍⵢⵓⴳⵔⴰⴼⵉⵜt ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "== ⵉⵖⴱⵓⵍⴰ ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("== ⵉⵖⴱⵓⵍⴰ ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "==ⵉⵖⴱⵓⵍⴰ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("==ⵉⵖⴱⵓⵍⴰ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "== ⵉⵙⴰⵖⵓⵍⴻⵏ ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⴻⵏ ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "== ⵉⵙⴰⵖⵓⵍⴻⵏ: ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⴻⵏ: ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "== ⵉⵙⵓⴳⴰⵎ ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("== ⵉⵙⵓⴳⴰⵎ ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "== ⵉⵙⵓⴳⴰⵎ : ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("== ⵉⵙⵓⴳⴰⵎ : ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "==ⵉⵙⵓⴳⴰⵎ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("==ⵉⵙⵓⴳⴰⵎ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "== ⵜⵉⵎⵙⵍⵖⴰ ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ ==","")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("== ⵜⵉⵎⵙⵍⵖⴰ ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "==ⵉⵙⴰⵖⵓⵍⵏ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ =="," ")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("==ⵉⵙⴰⵖⵓⵍⵏ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "== ⵜⵉⵙⵓⵖⴰⵍⵉⵏ ==" in page.text:
        if "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
            page.text = page.text.replace("== ⵉⵙⴰⵖⵓⵍⵏ =="," ")
            page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")
        page.text = page.text.replace("== ⵜⵉⵙⵓⵖⴰⵍⵉⵏ ==","== ⵉⵙⴰⵖⵓⵍⵏ ==")
        page.save("ⵙⵙⵏⴼⵍⵖ ⵜⴰⴳⵓⵔⵉ ⵏⵏⴰ ⵉⵍⵍⴰⵏ ⴳ ⵓⴷⵖⴰⵔ ⵏ ⵜⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    if "=ⵉⵙⵓⵖⴰⵍ= " in page.text:
        page.text = page.text.replace("=ⵉⵙⵓⵖⴰⵍ= ","")
        page.save("ⴽⴽⵙⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵜⵉⵙⵙ ⵙⵏⴰⵜ ⵏ ⵉⵙⵓⵖⴰⵍ")
        
    if not "== ⵉⵙⴰⵖⵓⵍⵏ ==" in page.text:
        page.text += "\n== ⵉⵙⴰⵖⵓⵍⵏ =="
        page.save("ⵔⵏⵉⵖ ⵜⴰⴳⵟⵟⵓⵎⵜ ⵏ ⵉⵙⴰⵖⵓⵍⵏ")

    
    i+=1
    j+=1
    #ⵜⵉⴳⵉⵔⴰ ⵏ for


    





#ⵜⵉⴳⵉⵔⴰ ⵏ ⵓⵖⴰⵡⴰⵙ
print("ⴰⵖⴰⵡⴰⵙ ⵉⵙⵎⴷ ⵜⵡⵡⵓⵔⵉ ⵏⵙ !!")
