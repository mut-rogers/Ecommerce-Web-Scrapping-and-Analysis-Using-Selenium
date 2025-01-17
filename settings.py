
""" 
This module holds the project settings including 
- Constants 
- Common variables etc
"""


# URL for the website.
# product category and web page number will change on demand
BASE_URL = "https://www.kilimall.co.ke/category/{}?id={}&form=category&page={}"

# Contains product categories available on the page 
# and those which will be scrapped. 
# The product category has a unique id and category name as stored on the dict
PRODUCT_CATEGORIES = {
    "167": "clothes",
    "1": "bags"
}