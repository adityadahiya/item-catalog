from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

# Clear database
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

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

# Create dummy user
user1 = User(name="Aditya", email="abc@xyz.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(user1)
session.commit()

# Items for Category 1
category1 = Category(name="Movies", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Logan", user_id=1, description="A mutant on his last journey to save a girl.", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Wonder Woman", user_id=1,  description="A powerful princess comes to the man's world frst time in order to end all wars.", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Bahubali 2", user_id=1, description="Son takes his revenge on a tryant ruler responsible for his father's death.", category=category1)

session.add(item3)
session.commit()

# Items for Category 2
category2 = Category(name="Games", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Watch Dogs", user_id=1, description="Watch Dogs is an action-adventure video game developed by Ubisoft Montreal and published by Ubisoft.", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Sleeping Dogs", user_id=1,  description="Sleeping Dogs is a 2012 open world action-adventure video game by United Front Games and Square Enix London originally released for PlayStation 3, Windows, and Xbox 360 platforms", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Batman Arkham Orgins", user_id=1, description="Batman Arkham Origins is a 2013 action-adventure video game developed by WB Games Montreal and published by Warner Bros. Interactive Entertainment for Microsoft Windows and the PlayStation 3, Wii U and Xbox 360 video game consoles.", category=category2)

session.add(item3)
session.commit()

# Items for Category 3
category3 = Category(name="TV Series", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Game of Thrones", user_id=1, description="Several royal families desire the Iron Throne to gain control of Westeros. Whilst kingdoms fight each other for power, a sinister force lurks beyond the Wall in the north.", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Sherlock", user_id=1, description="Dr. Watson, a former army doctor, finds himself sharing a flat with Sherlock Holmes, an eccentric individual with a knack for solving crimes. Together, they take on the most unusual cases.", category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Da Vinci's Demons", user_id=1, description="Leonardo da Vinci, an eccentric genius in his mid-20s, begins seeing and inventing things far beyond his time.", category=category3)
session.add(item3)
session.commit()

# Items for Category 4
category4 = Category(name="Songs", user_id=1)

session.add(category4)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name