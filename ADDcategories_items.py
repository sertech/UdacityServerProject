#! /usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Category, Item, User

engine = create_engine('postgresql://catalog:password@localhost/catalog')

DBSession = sessionmaker(bind=engine)
session = DBSession()


# create a dummy user
userX = User(t_name="Test user31", t_email="project321User@testmail.com", t_picture="https://pbs.twimg2.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png")

session.add(userX)
session.commit()

# ----------------------create Device Accessories category-----------------------
cat1 = Category(t_catName = "Device Accessories", t_userId=1)
session.add(cat1)
session.commit()

# add a item1 to Device Accessories category
cat1Item1 = Item(t_userId=1, t_itemName="Echo Dot (2nd Generation) - Smart speaker with Alexa - Black", t_itemDescription="Sunt velit ad reprehenderit in. Incididunt adipisicing tempor commodo pariatur dolore qui minim nulla consectetur consequat esse ut consequat consectetur. Enim consequat magna officia fugiat elit non tempor aliquip.", t_relationC=cat1)
session.add(cat1Item1)
session.commit()

cat1Item2 = Item(t_userId=1, t_itemName="Fire TV Stick with Alexa Voice Remote | Streaming Media Player", t_itemDescription="Enim aliqua pariatur aliqua cillum enim quis anim dolor nulla esse nostrud.", t_relationC=cat1)
session.add(cat1Item2)
session.commit()

cat1Item3 = Item(t_userId=1, t_itemName="Fire TV with 4K Ultra HD and Alexa Voice Remote (Pendant Design) | Streaming Media Player", t_itemDescription="Dolore est aliqua et Lorem ex esse dolore proident. Et cupidatat officia voluptate labore ipsum proident aliquip ut ullamco. Occaecat qui labore ad deserunt excepteur laborum. Magna nostrud quis consequat exercitation eiusmod amet labore.", t_relationC=cat1)
session.add(cat1Item3)
session.commit()

cat1Item4 = Item(t_userId=1, t_itemName="Echo Spot - Black", t_itemDescription="Nostrud magna do quis elit eiusmod duis velit elit aliquip labore cillum eiusmod. Amet pariatur duis reprehenderit officia sint", t_relationC=cat1)
session.add(cat1Item4)
session.commit()

cat1Item5 = Item(t_userId=1, t_itemName="Amazon Cloud Cam Security Camera, Works with Alexa", t_itemDescription="Cillum adipisicing magna qui cupidatat anim velit esse duis nostrud dolor minim enim. Consequat dolore sint aliquip tempor ad mollit id.", t_relationC=cat1)
session.add(cat1Item5)
session.commit()

cat1Item6 = Item(t_userId=1, t_itemName="Verbatim CD-R 700MB 80 Minute 52x Recordable Disc - 100 Pack Spindle (FFP)", t_itemDescription="Esse incididunt id ullamco elit consectetur officia Lorem esse nostrud aliqua velit pariatur. Consequat adipisicing anim amet officia commodo nisi dolor velit cupidatat elit sit id commodo cillum.", t_relationC=cat1)
session.add(cat1Item6)
session.commit()

cat1Item7 = Item(t_userId=1, t_itemName="AWS DeepLens - Deep learning enabled video camera for developers", t_itemDescription="Reprehenderit voluptate qui non est quis aute officia eu amet esse. Consectetur nulla ea deserunt adipisicing non cillum dolore pariatur in proident minim dolor nulla veniam.", t_relationC=cat1)
session.add(cat1Item7)
session.commit()
#-------------------------end of category Device Accessories---------------------

# ----------------create Automotive & Powersports category-----------------------
cat2 = Category(t_catName = "Automotive & Powersports", t_userId=1)
session.add(cat2)
session.commit()

cat2Item1 = Item(t_userId=1, t_itemName="Kensun HID Kit Computer Warning Canceller & Anti Flicker (1 Pair)", t_itemDescription="Sunt velit ad reprehenderit in. Incididunt adipisicing tempor commodo pariatur dolore qui minim nulla consectetur consequat esse ut consequat consectetur. Enim consequat magna officia fugiat elit non tempor aliquip.", t_relationC=cat2)
session.add(cat1Item1)
session.commit()

cat2Item2 = Item(t_userId=1, t_itemName="ACDelco 214-1680 GM Original Equipment Vapor Canister Purge Valve", t_itemDescription="Nisi aliqua deserunt deserunt nisi magna nisi sunt aute commodo elit pariatur magna quis.", t_relationC=cat2)
session.add(cat2Item2)
session.commit()

cat2Item3 = Item(t_userId=1, t_itemName="Mr. Gasket 918G Metric Header Bolt, (Set of 12)", t_itemDescription="Excepteur laboris irure eu do qui est. Dolor culpa et exercitation et non qui voluptate exercitation amet dolor tempor. ", t_relationC=cat2)
session.add(cat2Item3)
session.commit()

cat2Item4 = Item(t_userId=1, t_itemName="2005-2013 Corvette C6 Supercharger SLP Boost Gauge Pod Mount Housing", t_itemDescription="Eu enim excepteur commodo consequat. Et ea ipsum id sunt ipsum occaecat et ullamco nisi anim dolor.", t_relationC=cat2)
session.add(cat2Item4)
session.commit()

cat2Item5 = Item(t_userId=1, t_itemName="Flowmaster 817550 Force II 409S Stainless Steel Dual Rear Exit Cat-Back Exhaust System", t_itemDescription="Lorem magna aliquip eu eu est consectetur dolor aliqua ex qui ullamco laborum in culpa.", t_relationC=cat2)
session.add(cat2Item5)
session.commit()

cat2Item6 = Item(t_userId=1, t_itemName="Wells 847 Vapor Canister Purge Solenoid Connector", t_itemDescription="Ex occaecat sunt exercitation excepteur in aliqua qui. Reprehenderit cillum aliquip ullamco pariatur ut eu culpa consectetur ipsum qui. Commodo culpa est do eu laboris labore esse voluptate aute ad occaecat sint. Fugiat non excepteur ad magna. Duis pariatur anim eu aliqua veniam Lorem.", t_relationC=cat2)
session.add(cat2Item6)
session.commit()

cat2Item7 = Item(t_userId=1, t_itemName="2009-2013 C6 Corvette SLP PowerFlo Axle Back Exhaust System", t_itemDescription="Aute commodo dolore aliqua mollit irure ipsum. Fugiat veniam in dolore elit commodo minim dolore deserunt ea commodo sint consectetur.", t_relationC=cat2)
session.add(cat2Item7)
session.commit()
# ----------------end Automotive & Powersports category-----------------------



# ---------------------------create Beauty category----------------------------
cat3 = Category(t_userId=1, t_catName="Beauty")
session.add(cat3)
session.commit()

cat3item1 = Item(t_userId=1, t_itemName="Nautica Voyage Eau de Toilette Spray for Men, 3.4 oz", t_itemDescription="Dolor mollit do labore pariatur magna aliquip laboris ea excepteur deserunt eu id eiusmod duis. Laborum laborum tempor minim Lorem. Proident laborum nostrud in occaecat consequat.", t_relationC=cat3)
session.add(cat3item1)
session.commit()

cat3item2 = Item(t_userId=1, t_itemName="Acqua Di Gio By Giorgio Armani For Men", t_itemDescription="Qui qui incididunt amet consectetur qui exercitation exercitation excepteur pariatur amet eiusmod. Nisi occaecat id non duis ex ullamco nisi eiusmod voluptate sint.", t_relationC=cat3)
session.add(cat3item2)
session.commit()

cat3item3 = Item(t_userId=1, t_itemName="Davidoff Cool Water Edt Spray for Men, 6.7 oz", t_itemDescription="Nulla anim fugiat dolor exercitation enim. Magna sint aliquip ex enim sint ullamco ut eiusmod anim deserunt.", t_relationC=cat3)
session.add(cat3item3)
session.commit()

cat3item4 = Item(t_userId=1, t_itemName="David Beckham The Essence Eau de Toilette Spray", t_itemDescription="Officia velit consectetur pariatur reprehenderit aute duis ullamco et enim consequat velit ea magna incididunt. Adipisicing reprehenderit cupidatat aliquip fugiat Lorem velit incididunt dolore est cillum ut. Culpa dolor velit officia velit sunt magna cillum do.", t_relationC=cat3)
session.add(cat3item4)
session.commit()

cat3item5 = Item(t_userId=1, t_itemName="Aramis By Aramis for Men, Eau De Toilette Spray", t_itemDescription="Pariatur do reprehenderit occaecat amet ex velit ea consectetur ad sunt officia.", t_relationC=cat3)
session.add(cat3item5)
session.commit()

cat3item6 = Item(t_userId=1, t_itemName="Chrome Legend by Azzaro For Men", t_itemDescription="Cupidatat laboris amet non culpa sint sunt ipsum amet ad Lorem minim pariatur. Id do ullamco eiusmod magna ea duis deserunt deserunt. Adipisicing esse fugiat consequat ipsum mollit proident.", t_relationC=cat3)
session.add(cat3item6)
session.commit()

cat3item7 = Item(t_userId=1, t_itemName="Grey Flannel by Geoffrey Beene for Men", t_itemDescription="Cupidatat dolor in fugiat do consectetur magna anim velit est anim mollit tempor aute.", t_relationC=cat3)
session.add(cat3item7)
session.commit()
# ---------------------------end of Beauty category----------------------------

#---------------- create category Books-----------------------------------------
cat4 = Category(t_userId=1, t_catName="Books")
session.add(cat4)
session.commit()

cat4item1 = Item(t_userId=1, t_itemName="1984 (Signet Classics)", t_itemDescription="Cillum exercitation culpa ex cupidatat anim nostrud duis occaecat proident ex est. Adipisicing enim irure ullamco ea. Labore ut eu velit do. Anim cillum laborum proident nisi excepteur fugiat nostrud adipisicing sit amet consectetur.", t_relationC=cat4)
session.add(cat4item1)
session.commit()

cat4item2 = Item(t_userId=1, t_itemName="A Long Way Gone: Memoirs of a Boy Soldier", t_itemDescription="Qui qui excepteur incididunt in commodo pariatur. Ex ad sunt enim ut cillum Lorem nulla elit consectetur anim commodo.", t_relationC=cat4)
session.add(cat4item2)
session.commit()

cat4item3 = Item(t_userId=1, t_itemName="The Bad Beginning: Or, Orphans!", t_itemDescription="Officia labore elit labore ad. Ex aliquip dolore duis consequat sint enim ipsum pariatur cillum elit anim sit labore. Ut et magna esse occaecat minim duis. Sit ullamco aute quis do cupidatat adipisicing deserunt magna aliquip culpa. Laborum minim laborum labore in cupidatat nulla cupidatat eiusmod irure. Exercitation in ad aliqua magna ea aliquip.", t_relationC=cat4)
session.add(cat4item3)
session.commit()

cat4item4 = Item(t_userId=1, t_itemName="All the President's Men", t_itemDescription="In ea pariatur ex irure esse sunt laborum duis aliquip ipsum enim amet nulla. Ullamco occaecat veniam occaecat ex ut sit. Deserunt ad consectetur velit aliquip.", t_relationC=cat4)
session.add(cat4item4)
session.commit()

cat4item5 = Item(t_userId=1, t_itemName="The Giver", t_itemDescription="Enim ut ipsum exercitation ad tempor in. Eu fugiat incididunt et nostrud elit esse ut ex proident occaecat. Sunt commodo laborum exercitation ullamco excepteur ullamco reprehenderit tempor Lorem do culpa et. Sunt tempor dolor aute enim ex.", t_relationC=cat4)
session.add(cat4item5)
session.commit()

cat4item6 = Item(t_userId=1, t_itemName="The Golden Compass: His Dark Materials", t_itemDescription="Sunt est aliqua elit magna Lorem non quis ex laborum labore ad anim. Laboris nulla pariatur duis ut culpa. Id laborum officia minim exercitation Lorem. Ipsum aliquip magna cupidatat dolor anim minim amet nulla eiusmod nostrud eiusmod pariatur. Duis ex esse id exercitation laboris eu ipsum pariatur deserunt.", t_relationC=cat4)
session.add(cat4item6)
session.commit()

cat4item7 = Item(t_userId=1, t_itemName="The Long Goodbye", t_itemDescription="Aliqua adipisicing dolore exercitation adipisicing consectetur esse irure Lorem laborum qui laboris. Eiusmod tempor pariatur laborum amet elit ad in dolore esse. Ipsum eiusmod aute adipisicing quis Lorem duis duis ea non non aute. Reprehenderit cupidatat Lorem excepteur minim irure amet dolore. Labore esse proident aliquip do excepteur consectetur enim eiusmod ullamco elit. Et enim amet reprehenderit qui voluptate exercitation id.", t_relationC=cat4)
session.add(cat4item7)
session.commit()
#----------------------------- end category Books--------------------------------

#-------------------------add category PC Software----------------------------
cat5 = Category(t_userId=1, t_catName="PC Software")
session.add(cat5)
session.commit()

cat5item1 = Item(t_userId=1, t_itemName="Adobe Acrobat Standard 2017", t_itemDescription="Fugiat in culpa aliquip nulla quis id ea ex. Laboris est velit amet anim labore id cillum nostrud consectetur id.", t_relationC=cat5)
session.add(cat5item1)
session.commit()

cat5item2 = Item(t_userId=1, t_itemName="Kaspersky Internet Security 3 Device/1 Year [Key Code] 2018 (3-Users)", t_itemDescription="Do cupidatat sunt et duis. Reprehenderit labore cillum eu commodo sunt Lorem ex. Exercitation ea officia tempor ea laboris nisi consectetur. Ut ex proident fugiat aliqua in est. Tempor labore dolor occaecat anim incididunt Lorem amet magna enim non.", t_relationC=cat5)
session.add(cat5item2)
session.commit()

cat5item3 = Item(t_userId=1, t_itemName="Acronis True Image 2018 Backup Software", t_itemDescription="Sint ullamco consequat commodo qui. Minim aliqua reprehenderit velit officia. Sunt commodo mollit eu magna esse irure ad ad dolore sit culpa. Qui mollit voluptate magna aliquip occaecat amet eiusmod amet deserunt minim. Voluptate duis officia nostrud laboris esse non exercitation amet incididunt officia.", t_relationC=cat5)
session.add(cat5item3)
session.commit()

cat5item4 = Item(t_userId=1, t_itemName="VEGAS Movie Studio 15 Suite - Create stunning movies [Download]", t_itemDescription="Excepteur aute ex dolor veniam ipsum ipsum excepteur est reprehenderit. Ut ex pariatur nisi qui ut ex est fugiat consequat sunt consectetur voluptate. Incididunt reprehenderit pariatur sunt culpa est eu excepteur id quis.", t_relationC=cat5)
session.add(cat5item4)
session.commit()

cat5item5 = Item(t_userId=1, t_itemName="Corel Painter 2018 Digital Art Suite for PC/Mac", t_itemDescription="Labore nulla deserunt nisi fugiat duis esse irure et enim anim eu non sint sit.", t_relationC=cat5)
session.add(cat5item5)
session.commit()

cat5item6 = Item(t_userId=1, t_itemName="Nero Standard 2018", t_itemDescription="Voluptate tempor do in labore incididunt do tempor ad eiusmod laboris exercitation minim tempor.", t_relationC=cat5)
session.add(cat5item6)
session.commit()

cat5item7 = Item(t_userId=1, t_itemName="Corel PaintShop Pro 2018 Ultimate Photo with Multi-cam Video Editing Software for PC - Amazon Exclusive", t_itemDescription="Consectetur consequat cupidatat labore tempor ut fugiat consectetur anim labore proident commodo incididunt. Cupidatat cillum quis irure Lorem est irure nulla ipsum dolor eu minim.", t_relationC=cat5)
session.add(cat5item7)
session.commit()
#----------------------------end category PC Software----------------------------


#------category  Musical Instruments : Band & Orchestra : Orchestral Strings-----
cat6 = Category(t_userId=1, t_catName=" Musical Instruments")
session.add(cat6)
session.commit()

cat6item1 = Item(t_userId=1, t_itemName="Cecilio CVN-300 Solidwood Ebony Fitted Violin with D'Addario Prelude Strings, Size 4/4 (Full Size)", t_itemDescription="Sint mollit ex excepteur ex pariatur ut magna magna. Velit proident sunt ex cillum sit sint officia exercitation adipisicing velit consequat minim.", t_relationC=cat6)
session.add(cat6item1)
session.commit()

cat6item2 = Item(t_userId=1, t_itemName="Bunnel Pupil Clearance Violin Outfit (4/4)", t_itemDescription="Incididunt sit aute deserunt labore dolor cillum. Incididunt consectetur anim cupidatat aliquip eiusmod proident tempor consequat tempor labore aliqua mollit laboris velit. Fugiat et in duis ea", t_relationC=cat6)
session.add(cat6item2)
session.commit()

cat6item3 = Item(t_userId=1, t_itemName="Brand New Erhu Instrument Chinese Violin Fiddle Huqin W/ Accessories", t_itemDescription="Deserunt veniam quis nulla veniam aliqua qui anim velit. Commodo dolore sit anim enim reprehenderit aliqua elit enim est exercitation ullamco. Enim exercitation culpa magna sunt excepteur est. Eiusmod ullamco veniam cupidatat consectetur. Eu nostrud elit ex duis proident excepteur ea proident.", t_relationC=cat6)
session.add(cat6item3)
session.commit()

cat6item4 = Item(t_userId=1, t_itemName="Bunnel Shredder Clearance Electric Violin (Jet Black)", t_itemDescription="Laboris consequat nisi excepteur tempor laboris tempor dolor reprehenderit officia aliquip cupidatat. Et et veniam consectetur ex elit magna culpa. Pariatur ut irure ad mollit irure elit duis consequat aute quis.", t_relationC=cat6)
session.add(cat6item4)
session.commit()

cat6item5 = Item(t_userId=1, t_itemName="Lyre Harp, 16 String", t_itemDescription="Ipsum officia adipisicing adipisicing sint laboris cillum commodo culpa veniam sunt labore cillum nisi. Id pariatur anim dolor et officia deserunt. Enim est anim aute nulla veniam.", t_relationC=cat6)
session.add(cat6item5)
session.commit()

cat6item6 = Item(t_userId=1, t_itemName="Merano 3/4 Size Blue Student Cello with Bag and Bow+2 Sets of Strings+Cello Stand+Black Music Stand+Metro Tuner+Rosin+Rubber Round Mute", t_itemDescription="Voluptate ut in laboris minim ipsum laborum incididunt dolore duis voluptate labore sint. Nulla officia commodo do in deserunt voluptate sint fugiat.", t_relationC=cat6)
session.add(cat6item6)
session.commit()

cat6item7 = Item(t_userId=1, t_itemName="Orient Light Entry Level Traditional Erhu Chinese 2-string Violin Fiddle Sinitic Musical Instrument Handicraft Yellow Tracery with Bag", t_itemDescription="Ea mollit incididunt magna eiusmod laboris est magna exercitation id anim fugiat tempor commodo. Culpa nisi pariatur anim incididunt ea nostrud amet dolor enim amet ex cillum.", t_relationC=cat6)
session.add(cat6item7)
session.commit()

#---end category  Musical Instruments : Band & Orchestra : Orchestral Strings---


#------------------------category videogames------------------------------------
cat7 = Category(t_userId=1, t_catName="video games")
session.add(cat7)
session.commit()

cat7item1 = Item(t_userId=1, t_itemName="Shenmue I & II", t_itemDescription="Elit ullamco dolor consequat esse cillum officia do occaecat laborum qui. Deserunt minim veniam id Lorem elit consectetur culpa et excepteur veniam officia ex ut veniam. Amet ea dolore dolore id laboris irure labore ad. Veniam qui voluptate duis esse minim ullamco incididunt dolor.", t_relationC=cat7)
session.add(cat7item1)
session.commit()

cat7item2 = Item(t_userId=1, t_itemName="Kingdom Hearts III", t_itemDescription="Consectetur proident sint laborum adipisicing fugiat sunt pariatur sunt minim. Sint magna incididunt irure id. Et qui exercitation aliqua duis irure eiusmod consequat cupidatat quis magna quis eiusmod adipisicing sunt.", t_relationC=cat7)
session.add(cat7item2)
session.commit()

cat7item3 = Item(t_userId=1, t_itemName="Mega Man X Legacy Collection 1+2", t_itemDescription="Cillum cillum irure et quis voluptate ad proident ex aute enim commodo. Magna reprehenderit fugiat occaecat quis nisi. Esse et occaecat anim sint ullamco id tempor nulla do anim consectetur nulla veniam Lorem. Nostrud sit ullamco exercitation incididunt.", t_relationC=cat7)
session.add(cat7item3)
session.commit()

cat7item4 = Item(t_userId=1, t_itemName="Street Fighter 30th Anniversary Collection", t_itemDescription="Sint magna tempor culpa anim ex exercitation excepteur reprehenderit. Velit mollit in irure fugiat irure. Ex aute magna non id dolor Lorem deserunt qui reprehenderit.", t_relationC=cat7)
session.add(cat7item4)
session.commit()

cat7item5 = Item(t_userId=1, t_itemName="Nioh", t_itemDescription="Labore laboris commodo eu qui. Nostrud eiusmod ut deserunt deserunt velit est voluptate consequat officia incididunt id do consequat. Incididunt voluptate ad amet do anim laborum deserunt officia excepteur mollit nulla aliqua", t_relationC=cat7)
session.add(cat7item5)
session.commit()

cat7item6 = Item(t_userId=1, t_itemName="Tekken 7", t_itemDescription="Sint laborum minim ut dolore magna commodo excepteur. Culpa incididunt amet qui cillum cillum nulla in et qui ea in magna Lorem aliquip. Dolor non nulla proident reprehenderit et consectetur consequat laborum labore laborum excepteur", t_relationC=cat7)
session.add(cat7item6)
session.commit()

cat7item7 = Item(t_userId=1, t_itemName="My Hero One's Justice", t_itemDescription="Eu ullamco irure aliquip in pariatur duis. Consequat ad reprehenderit minim tempor dolor eiusmod. Qui aliquip exercitation consequat ex eiusmod veniam culpa pariatur. Lorem sunt id consequat laboris adipisicing aliquip fugiat duis.", t_relationC=cat7)
session.add(cat7item7)
session.commit()
#----------------------end category videogames---------------------------------

#--------------- random adds---------------------------------------------------


cat1Item8 = Item(t_userId=1, t_itemName="Panda Wireless PAU09 N600 Dual Band (2.4GHz and 5GHz) Wireless N USB Adapter W/ Dual 5dBi Antennas", t_itemDescription="Elit sint anim reprehenderit irure adipisicing labore mollit. Enim ex eu veniam fugiat velit duis consequat do id laborum veniam enim velit pariatur.", t_relationC=cat1)
session.add(cat1Item8)
session.commit()

cat2Item8 = Item(t_userId=1, t_itemName="Timken 510050 Wheel Bearing", t_itemDescription="Qui in laboris exercitation Lorem est ipsum id deserunt qui laboris tempor. Deserunt veniam ipsum ullamco aliquip anim amet exercitation in ullamco sint labore magna et. Consectetur ex ipsum cillum adipisicing reprehenderit adipisicing voluptate.", t_relationC=cat2)
session.add(cat2Item8)
session.commit()

cat3item8 = Item(t_userId=1, t_itemName="Seoul Ceuticals Korean Skin Care Snail Repair Cream Moisturizer - 97.5% Snail Mucin Extract ", t_itemDescription="Anim commodo cupidatat irure esse consectetur irure magna. Proident ad est aliqua exercitation. Adipisicing amet sit id elit exercitation ad laborum ipsum id elit consequat eu eiusmod. Elit exercitation esse velit in consequat commodo nostrud. Ex et pariatur cupidatat anim consectetur consequat exercitation consequat tempor nisi qui. Non aliqua ex ex mollit.", t_relationC=cat3)
session.add(cat3item8)
session.commit()

cat4item8 = Item(t_userId=1, t_itemName="The Art of Deception: Controlling the Human Element of Security", t_itemDescription="Nisi dolore veniam deserunt deserunt commodo adipisicing dolor non aute duis. Eiusmod nostrud irure sint culpa anim reprehenderit sunt nostrud excepteur non.", t_relationC=cat4)
session.add(cat4item8)
session.commit()

cat5item8 = Item(t_userId=1, t_itemName="Visual Studio Professional 2017", t_itemDescription="Lorem dolore ex in excepteur sint Lorem. Nisi minim dolore Lorem fugiat dolore nisi eu est ex. Commodo mollit exercitation consequat excepteur amet reprehenderit dolore adipisicing labore eu nulla. Laboris laborum id est tempor fugiat. Aute ex enim in aliqua eiusmod proident duis aute aliquip magna tempor minim. Et enim sint pariatur quis velit.", t_relationC=cat5)
session.add(cat5item8)
session.commit()

cat6item8 = Item(t_userId=1, t_itemName="Ohuhu Legend of Zelda Ocarina 12 Hole Alto C with Textbook Display Stand Protective Bag", t_itemDescription="Eu aliqua veniam id excepteur tempor deserunt commodo. Aliquip mollit adipisicing id cupidatat ex voluptate voluptate occaecat id excepteur do. ", t_relationC=cat6)
session.add(cat6item8)
session.commit()

cat7item8 = Item(t_userId=1, t_itemName="Mega Man 11 - PlayStation 4", t_itemDescription="Mega man returns! the newest entry in this iconic series blends classic, challenging 2D platforming action with a fresh new visual style. The new double Gear system boosts Mega Man's speed and power for a new twist to the satisfying gameplay the series is known for.", t_relationC=cat7)
session.add(cat7item8)
session.commit()