import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'project.settings')
import django
django.setup()
from the_pantry.models import Category, Recipe

def populate():
    mains_recipes = [{"title": "Potatoes with things",
                     "author": "Rebecaitlyn Jenkins",
                     "content": "A lot of potatoes and some things",
                     "views":0, "likes": 0, "created_on": datetime.datetime.now() },
                     ]

    sides_recipes = [{"title": "Green salad",
                     "author": "John Doe",
                     "content": "Grean things only",
                     "views":0, "likes": 0, "created_on": datetime.datetime.now() },
                     ]

    desserts_recipes = [{"title": "Cheesecake",
                     "author": "Jane Doe",
                     "content": "Sweet sweet sugar",
                     "views":0, "likes": 0, "created_on": datetime.datetime.now() },
                     ]

    quick_recipes = [{"title": "Sandwich",
                     "author": "Kate Jones",
                     "content": "Bread and some darn good veggies",
                     "views":0, "likes": 0, "created_on": datetime.datetime.now() },
                     ]

    cats = {"Mains": {"recipes": mains_recipes},
            "Sides": {"recipes": sides_recipes},
            "Desserts": {"recipes": desserts_recipes},
            "Quick Recipes": {"recipes": quick_recipes}}

    # Add each category to the cats dictionary
    # and then each recipe to the associated category
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for r in cat_data["recipes"]:
            add_recipe(c, r["title"], r["author"], r["content"], r["views"], r["likes"], r["created_on"])

    # Print out added categories:
    for c in Category.objects.all():
        for r in Recipe.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(r)))

def add_recipe(cat, title, author, content, created_on, views=0, likes=0,):
    r = Recipe.objects.get_or_create(category=cat, title=title)[0]
    r.author=author
    r.content=content
    r.views=views
    r.likes=likes
    r.created_on=created_on
    r.save()
    return r

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

# Start execution:
if __name__ == '__main__':
    print("Starting population script...")
    populate()
