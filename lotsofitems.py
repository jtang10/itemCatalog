from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item

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
category1 = Category(name="Basketball")

session.add(category1)
session.commit()

item1 = Item(name="Sneakers", description="Shiny shoes you want to wear all the time.",
             category=category1)

session.add(item1)
session.commit()

item2 = Item(name="Jersey", description="Cavs jersey is for sure the best.",
             category=category1)

session.add(item2)
session.commit()

item3 = Item(name="wristband", description="No actual use, just looks cool",
             category=category1)

session.add(item3)
session.commit()

item4 = Item(name="headband", description="Cover your hairline",
             category=category1)

session.add(item4)
session.commit()

item5 = Item(name="goggle", description="This is baseketball goggle, not swimming goggle",
             category=category1)

session.add(item5)
session.commit()

print "Added basketball"

# Category for swimming
category2 = Category(name="Swimming")

session.add(category2)
session.commit()

item1 = Item(name="goggle", description="Most people have to wear goggle to swim",
             category=category2)

session.add(item1)
session.commit()

item2 = Item(name="shorts", description="I dare you not to wear that",
             category=category2)

session.add(item2)
session.commit()

item3 = Item(name="speedo", description="No idea what else will be used in swimming",
             category=category2)

session.add(item3)
session.commit()

item4 = Item(name="towels", description="Wipe yourself to prevent cold",
             category=category2)

session.add(item4)
session.commit()

print "Added swimming"

category3 = Category(name="Cycling")

session.add(category3)
session.commit()

item1 = Item(name="bicycle", description="I always want a good bicycle",
             category=category3)

session.add(item1)
session.commit()

item2 = Item(name="helmet", description="waterdrop-shaped helmet",
             category=category3)

session.add(item2)
session.commit()

item3 = Item(name="tight suit", description="tight suit description",
             category=category3)

session.add(item3)
session.commit()

print "Added cycling"

category4 = Category(name="soccer")

session.add(category4)
session.commit()

item1 = Item(name="soccer ball", description="You gotta get a soccer ball before playing the game",
             category=category4)

session.add(item1)
session.commit()

item2 = Item(name="long socks", description="Long socks for the soccer",
             category=category4)

session.add(item2)
session.commit()

print "Added Soccer"

category5 = Category(name="baseball")

session.add(category5)
session.commit()

item1 = Item(name="baseball bat", description="Lucieo",
             category=category5)

session.add(item1)
session.commit()

print "Added Hockey"

print "added all items successfully!"
