import pywikibot
from pywikibot import pagegenerators


print("Tawwri ar tzzigiz")

# Set the site for Wikimedia Incubator and Moroccan Tamazight Wikipedia
incubator_site = pywikibot.Site('incubator', 'incubator')
tamazight_site = pywikibot.Site('zgh', 'wikipedia')

# Set the source and target languages
source_lang = 'wikipedia:incubator:tzm'  # Replace 'xyz' with the source language code
target_lang = 'zgh'  # Moroccan Tamazight Wikipedia language code

# Set the category of articles to move
category_name = 'Category:Wp/tzm'  # Replace 'XYZ' with the category name

# Get the category page
category_page = pywikibot.Category(incubator_site, category_name)

# Get all pages in the category
pages = pagegenerators.CategorizedPageGenerator(category_page)

# Move each page
for page in pages:
    # Construct the new title on the target wiki
    new_title = page.title(withNamespace=False).replace(source_lang + '/', '')
    
    # Check if the page exists on the target wiki
    if pywikibot.Page(tamazight_site, new_title).exists():
        pywikibot.warning("Page '{}' already exists on the target wiki. Skipping.".format(new_title))
        continue
    
    # Move the page
    try:
        page.move(new_title, reason="Moving from Wikimedia Incubator to standard Moroccan Tamazight Wikipedia")
        pywikibot.output("Page '{}' successfully moved to '{}'.".format(page.title(), new_title))
    except Exception as e:
        pywikibot.error("Failed to move page '{}': {}".format(page.title(), e))



#Tigira n uɣawas
print("Tkmml twwuri !!")
