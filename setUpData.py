from database import init_db, db_session
from models import *

init_db()

r1 = Restaurant(name="Joe & the Juice", style="Coffee", address="240 Hamilton Ave, Palo Alto, CA 94301", city="Palo Alto", price="2", image_url="JoeJuice.jpg")
db_session.add(r1)

r2 = Restaurant(name="Kara’s Cupcakes", style="Dessert", address="855 El Camino Real #50, Palo Alto, CA 94301", city="Palo Alto", price="2", image_url="Karas.jpg")
db_session.add(r2)

r3 = Restaurant(name="Taro San", style="Restaurant", address="717 Stanford Shopping Center, Palo Alto, CA 94304", city="Palo Alto", price="2", image_url="TaroSan.jpg")
db_session.add(r3)

r4 = Restaurant(name="Subway", style="Fast Food", address="809 Santa Cruz Ave, Menlo Park, CA 94025", city="Menlo Park", price="1", image_url="Subway.jpg")
db_session.add(r4)

r5 = Restaurant(name="Scoop", style="Dessert", address="203 University Ave #1712, Palo Alto, CA 94301", city="Palo Alto", price="2", image_url="Scoop.jpg")
db_session.add(r5)

r6 = Restaurant(name="Happy Donuts", style="Dessert", address="1330 El Camino Real, Redwood City, CA 94063", city="Redwood City", price="1", image_url="HappyDonuts.jpg")
db_session.add(r6)

r7 = Restaurant(name="Sweetgreen", style="Restaurant", address="581 Ramona St Ste 120, Palo Alto, CA 94301", city="Palo Alto", price="2", image_url="Sweetgreen.jpg")
db_session.add(r7)

r8 = Restaurant(name="Pressed Juice", style="Restaurant", address="660 Stanford Shopping Center Ste 230, Palo Alto, CA 94304", city="Palo Alto", price="2", image_url="PressedJuice.jpg")
db_session.add(r8)

r9 = Restaurant(name="True Food Kitchen", style="Restaurant", address="180 El Camino Real Ste 1140, Palo Alto, CA 94304", city="Palo Alto", price="2", image_url="TrueFood.jpg")
db_session.add(r9)

r10 = Restaurant(name="Chick-fil-A", style="Fast Food", address="536 Whipple Ave, Redwood City, CA 94063", city="Redwood City", price="1", image_url="ChickFilA.jpg")
db_session.add(r10)

r11 = Restaurant(name="Tender Greens", style="Restaurant", address="180 El Camino Real Suite 1050, Palo Alto, CA 94304", city="Palo Alto", price="2", image_url="TenderGreens.jpg")
db_session.add(r11)

r12 = Restaurant(name="Left Bank", style="Restaurant", address="635 Santa Cruz Ave, Menlo Park, CA 94025", city="Menlo Park", price="3", image_url="LeftBank.jpg")
db_session.add(r12)

r13 = Restaurant(name="Lulu’s", style="Restaurant", address="3539 Alameda de las Pulgas, Menlo Park, CA 94025", city="Menlo Park", price="1", image_url="Lulus.jpg")
db_session.add(r13)

r14 = Restaurant(name="In-N-Out", style="Fast Food", address="949 Veterans Blvd, Redwood City, CA 94063", city="Redwood City", price="1", image_url="InNOut.jpg")
db_session.add(r14)

r15 = Restaurant(name="Stacks", style="Restaurant", address="314 El Camino Real, Redwood City, CA 94062", city="Redwood City ", price="2", image_url="Stacks.jpg")
db_session.add(r15)

r16 = Restaurant(name="McDonald’s", style="Fast Food", address="1100 El Camino Real, Menlo Park, CA 94025", city="Menlo Park", price="1", image_url="McDonalds.jpg")
db_session.add(r16)

r17 = Restaurant(name="Salt & Straw", style="Dessert", address="250 University Ave STE 110, Palo Alto, CA 94301", city="Palo Alto", price="2", image_url="SaltAndStraw.jpg")
db_session.add(r17)

r18 = Restaurant(name="SusieCakes", style="Dessert", address="642 Santa Cruz Ave, Menlo Park, CA 94025", city="Menlo Park", price="2", image_url="SusieCakes.jpg")
db_session.add(r18)

r19 = Restaurant(name="Mademoiselle Colette", style="Dessert", address="499 Lytton Ave, Palo Alto, CA 94301", city="Palo Alto", price="2", image_url="MademoiselleColette.jpg")
db_session.add(r19)

r20 = Restaurant(name="Reposado", style="Restaurant", address="236 Hamilton Ave, Palo Alto, CA 94301", city="Palo Alto", price="3", image_url="Reposado.jpg")
db_session.add(r20)

r21 = Restaurant(name="Osteria Toscana", style="Restaurant", address="247 Hamilton Ave, Palo Alto, CA 94301", city="Palo Alto", price="3", image_url="Osteria.jpg")
db_session.add(r21)

r22 = Restaurant(name="Gott’s Roadside", style="Restaurant", address="855 El Camino Real #65, Palo Alto, CA 94301", city="Palo Alto", price="2", image_url="Gotts.jpg")
db_session.add(r22)

r23 = Restaurant(name="Howie’s", style="Restaurant", address="855 El Camino Real #60, Palo Alto, CA 94301", city="Palo Alto", price="2", image_url="Howies.jpg")
db_session.add(r23)

r24 = Restaurant(name="Palo Alto Creamery", style="Restaurant", address="566 Emerson St, Palo Alto, CA 94301", city="Palo Alto", price="2", image_url="PaloAltoCreamery.jpg")
db_session.add(r24)

r25 = Restaurant(name="Chipotle ", style="Fast Food", address="180 El Camino Real Ste 15A, Palo Alto, CA 94304", city="Palo Alto", price="1", image_url="Chipotle.jpg")
db_session.add(r25)

r26 = Restaurant(name="Onigilly", style="Restaurant", address="164 University Ave, Palo Alto, CA 94301", city="Palo Alto", price="1", image_url="Onigilly.jpg")
db_session.add(r26)

r27 = Restaurant(name="Bare Bowls", style="Restaurant", address="530 Emerson St, Palo Alto, CA 94301", city="Palo Alto", price="2", image_url="BareBowls.jpg")
db_session.add(r27)

r28 = Restaurant(name="P.F. Chang’s", style="Restaurant", address="900 Stanford Shopping Center Bldg. W, Palo Alto, CA 94304", city="Palo Alto", price="2", image_url="PFChangs.jpg")
db_session.add(r28)

r29 = Restaurant(name="Panda Express", style="Fast Food", address="2310 El Camino Real, Palo Alto, CA 94306", city="Palo Alto", price="1", image_url="PandaExpress.jpg")
db_session.add(r29)

r30 = Restaurant(name="Peet’s Coffee", style="Coffee", address=" 899 Santa Cruz Ave, Menlo Park, CA 94025", city="Menlo Park", price="1", image_url="PeetsCoffee.jpg")
db_session.add(r30)

r31 = Restaurant(name="Coffee Bar", style="Coffee", address="1149 Chestnut St, Menlo Park, CA 94025", city="Menlo Park", price="2", image_url="CoffeeBar.jpg")
db_session.add(r31)

r32 = Restaurant(name="Blue Bottle Coffee", style="Coffee", address="456 University Ave, Palo Alto, CA 94301", city="Palo Alto", price="2", image_url="BlueBottle.jpg")
db_session.add(r32)

r33 = Restaurant(name="Baskin Robbins", style="Dessert", address="863 Santa Cruz Ave, Menlo Park, CA 94025", city="Menlo Park", price="1", image_url="BaskinRobbins.jpg")
db_session.add(r33)

r34 = Restaurant(name="Amici’s", style="Restaurant", address="880 Santa Cruz Ave, Menlo Park, CA 94025", city="Menlo Park", price="2", image_url="Amicis.jpg")
db_session.add(r34)

r35 = Restaurant(name="The Refuge", style="Restaurant", address="1143 Crane St, Menlo Park, CA 94025", city="Menlo Park", price="2", image_url="Refuge.jpg")
db_session.add(r35)

r36 = Restaurant(name="Cafe Borrone", style="Coffee", address="1010 El Camino Real, Menlo Park, CA 94025", city="Menlo Park", price="2", image_url="CafeBorrone.jpg")
db_session.add(r36)

r37 = Restaurant(name="Chuck’s Donuts", style="Dessert", address="801 Woodside Rd, Redwood City, CA 94061", city="Redwood City", price="1", image_url="Chucks.jpg")
db_session.add(r37)

r38 = Restaurant(name="Milk Bar", style="Dessert", address="1531 Main St Unit #1, Redwood City, CA 94063", city="Redwood City", price="2", image_url="MilkBar.jpg")
db_session.add(r38)

r39 = Restaurant(name="Starbucks", style="Coffee", address="1045 El Camino Real, Redwood City, CA 94063", city="Redwood City", price="2", image_url="Starbucks.jpg")
db_session.add(r39)

r40 = Restaurant(name="Brew", style="Coffee", address="3176 Middlefield Rd, Redwood City, CA 94063", city="Redwood City", price="2", image_url="Brew.jpg")
db_session.add(r40)

r41 = Restaurant(name="The Counter", style="Restaurant", address="426 MacArthur Ave, Redwood City, CA 94063", city="Redwood City", price="2", image_url="Counter.jpg")
db_session.add(r41)

r42 = Restaurant(name="Milagros", style="Restaurant", address="1099 Middlefield Rd, Redwood City, CA 94063", city="Redwood City", price="2", image_url="Milagros.jpg")
db_session.add(r42)

r43 = Restaurant(name="Donato Enoteca", style="Restaurant", address="1041 Middlefield Rd, Redwood City, CA 94063", city="Redwood City", price="3", image_url="Donato.jpg")
db_session.add(r43)

r44 = Restaurant(name="Pinkberry", style="Dessert", address=" 680 Stanford Shopping Center Suite 14, Palo Alto, CA 94304", city="Palo Alto", price="1", image_url="Pinkberry.jpg")
db_session.add(r44)

u1 = User(username="emma", password="123")
db_session.add(u1)

db_session.commit()


