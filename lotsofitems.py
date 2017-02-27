from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, Users

engine = create_engine('postgresql:///itemcatalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Category for basketball
user1 = Users(name="Robo Barista", email="tinnyTim@udacity.com",
              picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')

session.add(user1)
session.commit()

user2 = Users(name="Jingning Tang", email="abc@def.com")

session.add(user2)
session.commit()

category1 = Category(user_id=1, name="Basketball")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Sneakers", description="Shiny shoes you want to wear all the time.",
             category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Jersey", description="Cavs jersey is for sure the best.",
             category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="wristband", description="No actual use, just looks cool",
             category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="headband", description="Cover your hairline",
             category=category1)

session.add(item4)
session.commit()

item5 = Item(user_id=1, name="goggle", description="This is baseketball goggle, not swimming goggle",
             category=category1)

session.add(item5)
session.commit()

print "Added basketball"

# Category for swimming
category2 = Category(user_id=1, name="Swimming")

session.add(category2)
session.commit()

item1 = Item(user_id=1, name="goggle", description="Most people have to wear goggle to swim",
             category=category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="shorts", description="I dare you not to wear that",
             category=category2)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="speedo", description="No idea what else will be used in swimming",
             category=category2)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="towels", description="Wipe yourself to prevent cold",
             category=category2)

session.add(item4)
session.commit()

print "Added swimming"

category3 = Category(user_id=1, name="Cycling")

session.add(category3)
session.commit()

item1 = Item(user_id=1, name="bicycle", description="I always want a good bicycle",
             category=category3)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="helmet", description="waterdrop-shaped helmet",
             category=category3)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="tight suit", description="tight suit description",
             category=category3)

session.add(item3)
session.commit()

print "Added cycling"

category4 = Category(user_id=1, name="soccer")

session.add(category4)
session.commit()

item1 = Item(user_id=1, name="soccer ball", description="You gotta get a soccer ball before playing the game",
             category=category4)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="long socks", description="Long socks for the soccer",
             category=category4)

session.add(item2)
session.commit()

print "Added Soccer"

category5 = Category(user_id=1, name="baseball")

session.add(category5)
session.commit()

item1 = Item(user_id=1, name="baseball bat", description="Lucieo",
             category=category5)

session.add(item1)
session.commit()

print "Added Hockey"

print "added all items successfully!"
