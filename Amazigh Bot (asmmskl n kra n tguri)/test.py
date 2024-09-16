import pywikibot

print("Tawwri ar tzzigiz")

site = pywikibot.Site()   #extraction of the site address
print("Amazigh Bot iwfa Wikippidya taclḥit : ",site)

#title = "Wikipidya"   #c'est un article


#Tagṭṭumt n Isaɣuln d Ẓṛ uggar //////////////////////////////////////////
pool = site.allpages(namespace=0,filterredir=False)   #extraction of all pages names

i=0
j=0

for page in pool:
    print("Asnfl n umnni wiss : ",j)
    
      
    # Ar smmskalɣ "-nes" s " ns"
    if "-nes" in page.text:
        page.text = page.text.replace("-nes"," ns")
        page.save("Smmsklɣ -nes s ns")
        
    # Ar smmskalɣ "-is " s "is "
    if "-is " in page.text:
        page.text = page.text.replace("-is ","is ")
        page.save("Smmsklɣ -is s is")
        
    # Ar smmskalɣ "as-d-" s "as d "
    if "as-d-" in page.text:
        page.text = page.text.replace("as-d-","as d ")
        page.save("Smmsklɣ as-d- s as d ")
        
    # Ar smmskalɣ "-s " s "s "
    if "-s " in page.text:
        page.text = page.text.replace("-s ","s ")
        page.save("Smmsklɣ -s s s")
        
    # Ar smmskalɣ "-t-inn" s "tinn"
    if "-t-inn" in page.text:
        page.text = page.text.replace("-t-inn","tinn")
        page.save("Smmsklɣ -t-inn s tinn")
        
    # Ar smmskalɣ "-nnes" s " nns"
    if "-nnes" in page.text:
        page.text = page.text.replace("-nnes"," nns")
        page.save("Smmsklɣ -nnes s nns")
        
    # Ar smmskalɣ "-nnɣ" s " nnɣ"
    if "-nnɣ" in page.text:
        page.text = page.text.replace("-nnɣ"," nnɣ")
        page.save("Smmsklɣ -nnɣ s  nnɣ")
        
    # Ar smmskalɣ "-t-id" s "tid"
    if "-t-id" in page.text:
        page.text = page.text.replace("-t-id","tid")
        page.save("Smmsklɣ -t-id s tid")

    # Ar smmskalɣ " ɣakud" s " ɣ akud"
    if " ɣakud" in page.text:
        page.text = page.text.replace(" ɣakud"," ɣ akud")
        page.save("Smmsklɣ ɣakud s ɣ akud")
        
        
    i+=1
    j+=1
    #tigira n for


#Tigira n uɣawas
print("Tkmml twwuri !!")
