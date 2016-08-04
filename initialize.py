from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import *
engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# You can add some starter data for your database here.
fact1=Fact(tribe="Israel",statement="Einstein was offered the presidency of Israel which he politely declined.",correct_answer="True")
fact2=Fact(tribe="Israel",statement="Israel is so small, you can run through it from west to east in 2 hours and from top to bottom in 9 days.",correct_answer="True")
fact3=Fact(tribe="Israel",statement="Every year, 1,000 letters arrive in Jerusalem, Israel, addressed to God.",correct_answer="True")
fact4=Fact(tribe="Israel",statement="2,000-year-old seeds were discovered in 1963 inside an ancient jar in Israel. They were planted in 2005 and a tree that had been extinct for over 1800 years sprouted.",correct_answer="True")
fact5=Fact(tribe="Israel",statement="Jerusalem, Israel, has been destroyed twice , besieged 23 times, attacked 52 times, captured and recaptured 44 times and it's one of the world's oldest cities.",correct_answer="True")
fact6=Fact(tribe="Us",statement="An average person in the U.S. eats 35 tons of food in a lifetime.",correct_answer="True")
fact7=Fact(tribe="Us",statement="49% of U.S. Adults eat one sandwich a day.",correct_answer="True")
fact8=Fact(tribe="Us",statement="Since 2015, throwing away food is illegal in Seattle.",correct_answer="True")
fact9=Fact(tribe="Us",statement="California is the world's 1st (5th) largest supplier of food.",correct_answer="True")
fact10=Fact(tribe="Us",statement="In the U.S., as much as 40% of produce grown is never sold or eaten because it is too big(ugly).",correct_answer="True")
fact11=Fact(tribe="Japan",statement="Late-night dancing was illegal in Japan until 2015.",correct_answer="True")
fact12=Fact(tribe="Japan",statement="Japan suffers 1,500 earthquakes every year.",correct_answer="True")
fact13=Fact(tribe="Japan",statement="Japan has more than 50,000 people who are under(over) 100 years old.",correct_answer="True")
fact14=Fact(tribe="Japan",statement="Japan consists of over 6,800 islands.",correct_answer="True")
fact15=Fact(tribe="Japan",statement="In Japan there are more pets than vegetabsles(children).",correct_answer="True")
fact16=Fact(tribe="India",statement="According to Indian food theory, there are six different tastes: sweet, sour, salty, spicy, bitter, and astringent.",correct_answer="True")
fact17=Fact(tribe="India",statement="India consumes 50% of the world’s whiskey",correct_answer="True")
fact18=Fact(tribe="India",statement="India has the world’s lowest meat consumption per person.",correct_answer="True")
fact19=Fact(tribe="India",statement="the entire western hemisphere of earth(india) has more population than india. (the entire western hemisphere of earth)",correct_answer="True")
fact20=Fact(tribe="India",statement="in indian it is uncommon (common) to consume marijuana in milkshake form.",correct_answer="True")
fact21=Fact(tribe="Left-handed",statement="10% of the world's population is right-handed(left-handed).",correct_answer="True")
fact22=Fact(tribe="Left-handed",statement="Every August 13th is celebrated "Left-Handers Day" since 1996.",correct_answer="True")
fact23=Fact(tribe="Left-handed",statement="More than 2,500 left-handed people are killed every year by using equipment meant for right-handed people.",correct_answer="True")
fact24=Fact(tribe="Left-handed",statement="Left-handers peopled die 3 years longer(earlier)than right handed people.",correct_answer="True")
fact25=Fact(tribe="Left-handed",statement="Homosexuals are  39%  more likely to be left-handed.",correct_answer="True")
fact26=Fact(tribe="Poverty",statement="20,000 children die worldwide every day due to poverty.",correct_answer="True")
fact27=Fact(tribe="Poverty",statement="Nearly 1 billion people will go to bed hungry tonight.",correct_answer="True")
fact28=Fact(tribe="Poverty",statement="80% of humanity lives on less than US$10 per day.",correct_answer="True")
fact29=Fact(tribe="Poverty",statement="If you earn more than US$21,000 a year, you are part of the richest 4% of the planet.",correct_answer="True")
fact30=Fact(tribe="Poverty",statement="The poorest place in the U.S. is Allen, South Dakota, where 96% are Native American.",correct_answer="True")
fact31=Fact(tribe="Men",statement="Men spend almost a year of their lives staring at women, a survey found.",correct_answer="True")
fact32=Fact(tribe="Men",statement="In his lifetime, a man spends almost six months shaving. ",correct_answer="True")
fact33=Fact(tribe="Men",statement="A man walks about 7% slower when with wives or girlfriends, and speeds up when with other men.",correct_answer="True")
fact34=Fact(tribe="Men",statement="Breast Cancer  kills 450 men  in the U.S. every year.",correct_answer="True")
fact35=Fact(tribe="Men",statement="women(men) are more likely to say "I love you" first than men(women) are, a study found.",correct_answer="True")
fact36=Fact(tribe="Women",statement="they arecccc here",correct_answer="True")
fact37=Fact(tribe="Women",statement="they arecccc here",correct_answer="True")
fact38=Fact(tribe="Women",statement="they arecccc here",correct_answer="True")
fact39=Fact(tribe="Women",statement="they arecccc here",correct_answer="True")
fact40=Fact(tribe="Women",statement="they arecccc here",correct_answer="True")


session.add(fact1)
session.add(fact2)
session.add(fact3)
session.commit()

WOMEN:
39. A pregnant Iroquois woman would stop eating turtles so that her baby would not grow up clumsy on land, like a turtle.
40. MEN SWEAT UP TO  TWICE AS MUCH AS A WOMAN
41. men speak more than woman(women speak about 20,000 words a day)
42. in russia there are 9 million more women than men.
43. 40% of births in the U.S come from unmarried women



