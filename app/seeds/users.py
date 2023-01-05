from app.models import db, User, environment, SCHEMA, Product, ProductImage, Review, ReviewImage, OrderProduct, Order


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password')
    mike = User(
        username="Mike's Pet Emporium", email='mike@aa.io', password='password123')
    johnny = User(
        username="Johnny's cash exchange", email='johnny@aa.io', password='password')
    kat = User(
        username="Kat's cat stuff", email='kat@aa.io', password='password')
    jumbo = User(
        username='Mumbo Jumbo Pet Supplies', email='jumbo@aa.io', password='password')
    bo = User(
        username='Bo Knows Dogs', email='bo@aa.io', password='password')
    tarot = User(
        username="Tarot's for Parrots", email='tarot@aa.io', password='password')
    sanford = User(
        username='Sanford and Sons Pet Supplies', email='sanford@aa.io', password='password')
    miller = User(
        username='Miller Pets', email='miller@aa.io', password='password')
    cozey = User(
        username='Cozey Critters', email='cozey@aa.io', password='password')
    joe = User(
        username="Joe Exotic's Pet Supplies", email='joe@aa.io', password='password')
    pitbull = User(
        username="Mr Worldwide's Pitbull Store", email='pitbull@aa.io', password='password')
    chris = User(
        username="Chris' Cattery", email='chris@aa.io', password='password')

    users = [demo, mike, johnny, kat, jumbo, bo, tarot, sanford, miller, cozey, joe, pitbull, chris]

    for user in users:
        db.session.add(user)
        db.session.commit()

    seed_data = [
        {
            "user_id": 2,
            "name": "Personalized Dog Bed",
            "price": 53.99,
            "description": "The comfiest dog bed money can buy",
            "product_images": ["https://i.etsystatic.com/21637299/r/il/54efa6/2109724800/il_794xN.2109724800_sdo1.jpg", "https://i.etsystatic.com/21637299/r/il/4fb10b/2100965646/il_794xN.2100965646_r2b8.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "Our dog loves her new bed! It’s such great quality and so soft! Our pitt mix pup is 50 lbs, and we got the large! It’s a perfect size so she still has room to snuggle and move around.",
                "review_images": ["https://i.etsystatic.com/iap/dc1fdc/4291261405/iap_640x640.4291261405_5p9t9mcu.jpg?version=0"]
                },
                {
                "rating": 5,
                "text": "We received this yesterday and it exceeds our expectations! This dog bed is so well made and complements our decor. We couldn’t be happier and Lucy, our puppy loves it. Thank you!",
                "review_images": ["https://i.etsystatic.com/iap/b4e5dc/3396813168/iap_640x640.3396813168_mhxcqlct.jpg?version=0"]
                }
            ]
        },
        {
            "user_id": 1,
            "name": "Personalized Dog Robe",
            "price": 28,
            "description": "Pamper your pup in true spa-like style with this cuddly soft robe featuring a cozy hood and an absorbent quick-drying design",
            "product_images": ["https://i.etsystatic.com/11219945/r/il/b296a5/3198246561/il_1140xN.3198246561_hk7l.jpg", "https://i.etsystatic.com/11219945/r/il/f5da74/3404674236/il_1140xN.3404674236_gww9.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "Oh my gosh! Amazing! My little baby loves it! The weather is getting colder and she needed this for bath time!",
                "review_images": ["https://i.etsystatic.com/iap/3e090e/3460717491/iap_640x640.3460717491_rzkp5pk0.jpg?version=0"]
                },
                {
                "rating": 5,
                "text": "Got each of my girls a robe - Pink for Izzie and Aqua for Emmie. Robes are well made and so cute on each girl. Hoods are a plus. Their names are each embroidered very nicely as are the doggie paws. I would definitely order from this vendor again.",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 2,
            "name": "Personalized Dog Treats",
            "price": 15,
            "description": "Jake's is getting personal! Due to the high number of customer request for personalizing dog treats, we are offering this fun service. These treats make great gifts for a new pup, parties, weddings, or advertising your business. The maximum number we can stamp on our 2 inch bone is 9 letters.",
            "product_images": ["https://i.etsystatic.com/10516948/r/il/be81be/1699380446/il_1140xN.1699380446_7s04.jpg", "https://i.etsystatic.com/10516948/r/il/69e6b4/1746731087/il_1140xN.1746731087_rzjn.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "These were perfect! I work at a doggy daycare and we had a dog who was such a treat phein and we got her treats with her name on it as a going away gift when they moved. SOOOO happy with this purchase!",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "An awesome Birthday gift for a sweet pup! These personalized treats were extra special and paired perfectly with one special Happy Birthday treat! Akela thought they tasted pretty great too!! SUPER fast shipping and delivery! Thank you!!",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 2,
            "name": "Cat Toys -- Organic Wool!",
            "price": 10.97,
            "description": "100 percent biodegradable, renewable, sustainable and certified cruelty-free kiwi wool. Each cat Mouse is hand-felted with love from 100% natural organic wool to ensure a happy and healthy kitty.",
            "product_images": ["https://i.etsystatic.com/32942464/r/il/871835/4245716966/il_1140xN.4245716966_b6cx.jpg", "https://i.etsystatic.com/32942464/r/il/c86551/4245626188/il_1140xN.4245626188_9993.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "Marley is already loving his mice just nice simple mice, i really like the size for him. But he’s loving his mice. Thank you so very much. I will definitely be back soon. I’m Wanting to try out the dryer balls sometime . Thank you.",
                "review_images": ["https://i.etsystatic.com/iap/5b6ee3/4316884328/iap_640x640.4316884328_pee705a3.jpg?version=0"]
                },
                {
                "rating": 5,
                "text": "These little mice are beautiful and a perfect Christmas gift for a cat lover friend of mine!",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 2,
            "name": "Plush Squeaky Toy For Puppies",
            "price": 13.99,
            "description":  "There are 7 design squeaky dogs , Polyester Fiber Fill Dog Toy perfect gift for small, medium breeds",
            "product_images": ["https://i.etsystatic.com/17360662/r/il/0d5f32/4243920725/il_1140xN.4243920725_a49y.jpg", "https://i.etsystatic.com/17360662/r/il/c098ea/4196250530/il_1140xN.4196250530_qatv.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "Very cute. My pup loved it immediately. It was a gift for her birthday. She’s hard on toys and did rip it almost immediately. It’s ok, I’m used to sewing her toys.",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "The cute little stuffed dog was lovely. Well crafters, arrived on time, and with a hand written gift card to my friend and her new fur baby!",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "So cute! Looks just as pictured!",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "Loved them!",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 3,
            "name": "Cash Dog Tag",
            "price": 19,
            "description":  "Please note, that each tag is made to order. Let's embrace imperfections as they do happen on handmade items!",
            "product_images": ["https://i.etsystatic.com/32995477/r/il/0453a3/4259870907/il_1140xN.4259870907_8z2z.jpg", "https://i.etsystatic.com/32995477/r/il/05418f/4259874189/il_1140xN.4259874189_4p7j.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "The tag turned out perfect! Everyone comments how cool it is. I requested a custom tag with mini chocolate chips and Audra happily completed it and quickly at that. I want to order more tags for my other pets now!",
                "review_images": ["https://i.etsystatic.com/iap/97c118/4257881012/iap_640x640.4257881012_qf1zn0gy.jpg?version=0"]
                },
                {
                "rating": 5,
                "text": "I absolutely LOVE how this tag turned out! I couldn’t make a decision on a font, so I chose to be surprised and I am NOT disappointed! Thank you so much, it matches Keller’s new collar perfectly!",
                "review_images": ["https://i.etsystatic.com/iap/90a261/4098147602/iap_640x640.4098147602_j4nusfwm.jpg?version=0"]
                }
            ]
        },
        {
            "user_id": 3,
            "name": "Pet Bling",
            "price": 19.99,
            "description": "Pet Bling Dog Dollar Sign Pendant (free gold necklace - one size)",
            "product_images": ["https://i.etsystatic.com/8286341/r/il/6b9514/3149209015/il_1140xN.3149209015_tfk4.jpg", "https://i.etsystatic.com/8286341/r/il/a89138/3149196617/il_1140xN.3149196617_2dj9.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "I got the 22” chain for my blue pitty. She looks so cute haha. It also still looks good with a normal color. Seems well made and has a good quality latch!",
                "review_images": ["https://i.etsystatic.com/iap/b4e79a/3742961320/iap_640x640.3742961320_gbzs5744.jpg?version=0"]
                },
                {
                "rating": 5,
                "text": "Thank you!!! My dog is so styling now!!!",
                "review_images": ["https://i.etsystatic.com/iap/b4e79a/3742961320/iap_640x640.3742961320_gbzs5744.jpg?version=0"]
                }
            ]
        },
        {
            "user_id": 3,
            "name": "Money Dog or Cat Collar",
            "price": 10.99,
            "description": "Fun money pattern for this Dog collar or Cat Collar. This material really looks like money. :-)",
            "product_images": ["https://i.etsystatic.com/5520396/r/il/f1e105/481667435/il_1140xN.481667435_djsl.jpg", "https://i.etsystatic.com/5520396/r/il/1fb34a/481632844/il_794xN.481632844_ftcj.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "Love it! My boy has cost me a small fortune in the 2 months I've owned him so this collar is absolutely appropriate for around his neck.",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "Love this money collar! My boy, Cash hasn’t tried to fight this one off~the collar sits comfortably and is well-made. Great communication from the seller, absolutely recommend!",
                "review_images": ["https://i.etsystatic.com/iap/e054f5/2296664261/iap_640x640.2296664261_m2xt6wid.jpg?version=0"]
                }
            ]
        },
        {
            "user_id": 3,
            "name": "Bark of America dog toy",
            "price": 39.51,
            "description": "Brighten up your furry friends bed with this Funny Bark of America dog toy. It also squeaks when squeezed!",
            "product_images": ["https://i.etsystatic.com/25062291/r/il/a15231/3531469401/il_1140xN.3531469401_98y2.jpg", "https://i.etsystatic.com/25062291/r/il/65d433/3683266068/il_794xN.3683266068_63er.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "Super Fantastic, pricey though, even though my little diva takes pretty good care of her toys, especially purses because I paid so much for this, over two times what I would for any other Faux Designer Doggie hand bag.  LOVE IT THOUGH VERY MUCH.",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "Great seller, beautiful products! Very responsive and caring to my questions/concerns. Her products are beautiful and made very well. My only advice is to look at the dimensions of the product to make sure the size of the products is right",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "Everything right down to the lovely packaging is five stars, highly recommend this shop to everyone!",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "Such fabulous and fun designs! My pup loves her new toys!",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 3,
            "name": "Your Pet on a Dollar",
            "price": 10.99,
            "description": '''~ Now, it is time for you to have your pet's picture on REAL, Spendable Money! ~

            Your pet will be forever remembered and celebrated on this real dollar bill!''',
            "product_images": ["https://i.etsystatic.com/10703188/r/il/d6db62/1490374685/il_1140xN.1490374685_qp2o.jpg", "https://i.etsystatic.com/iap/c04359/3547180662/iap_640x640.3547180662_7i3ymeeo.jpg?version=0"],
            "reviews": [
                {
                "rating": 5,
                "text": "Great quality! Gifts for friends, they loved them!",
                "review_images": []
                },
                {
                "rating": 1,
                "text": "Never received my order !",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "Fine dollar bill and neatly packaged. Reliable and recommendable. Image is 100% which corresponds to the order. Valuable banknotes with the never-to-be-forgotten twin towers",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "Beautiful Snoopy ,lovely centre design ,good clean crisp note I wouldn't expect anything less from this quality top rated seller ,she'll love it and will be asking for Tom Hanks soon I guarantee 12 stars.",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 4,
            "name": "Refillable Catnip Mat with Organic Catnip",
            "price": 12.28,
            "description": "This pretty 15x15 inch catnip mat is the purrfect place to sleep away the afternoon. A small velcro opening in the side allows you to add more catnip as needed, and the flannel fabric and layer of cotton batting makes it just that much better to snooze on.",
            "product_images": ["https://i.etsystatic.com/5837345/r/il/592d4e/2833825036/il_1588xN.2833825036_dfbq.jpg", "https://i.etsystatic.com/5837345/r/il/784226/2708060839/il_1588xN.2708060839_25gb.jpg", "https://i.etsystatic.com/5837345/r/il/bb9550/2707812245/il_1588xN.2707812245_qzdq.jpg", "https://i.etsystatic.com/5837345/r/il/65d633/2881492231/il_1588xN.2881492231_k00p.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "I was in love with these from the moment I came across Sarah’s shop! Funny, adorable, high quality, and fast arrival... I suppose the most important is that Leo loves them too!",
                "review_images": ["https://i.etsystatic.com/iap/cca1ed/4130465473/iap_640x640.4130465473_e5x2gfxs.jpg?version=0"]
                },
                {
                "rating": 5,
                "text": "My cat loves her new toy, she goes absolutely nuts for it!! Plus it’s fun to show my co workers the pictures I have of her playing with it :)",
                "review_images": ["https://i.etsystatic.com/iap/c0e1d8/4130467897/iap_640x640.4130467897_orvs4qz3.jpg?version=0"]
                }
            ]
        },
        {
            "user_id": 4,
            "name": "Emerald Cat Collar",
            "price": 30.87,
            "description": "Stunning large Sparkling Emeralds & Diamond Crystals set on a faux leather collar",
            "product_images": ["https://i.etsystatic.com/6402885/r/il/6e0f2a/1856906838/il_1140xN.1856906838_dflj.jpg", "https://i.etsystatic.com/iap/27d15e/3771050581/iap_640x640.3771050581_nlzcgtdo.jpg?version=0"],
            "reviews": [
                {
                "rating": 5,
                "text": "Oh this is so SO darling on my handsome baby I couldn’t get hedwig to sit perfectly still but he really does seem to adore his new collar",
                "review_images": ["https://i.etsystatic.com/iap/5af4c2/2459291218/iap_640x640.2459291218_il6rp3w9.jpg?version=0"]
                },
                {
                "rating": 5,
                "text": "Beautiful collar, very well made, excellent service- Nala and I couldn’t be happier! Will be ordering more in the future!",
                "review_images": ["https://i.etsystatic.com/iap/ec0cde/2165188032/iap_640x640.2165188032_i9hjbza8.jpg?version=0=0"]
                }
            ]
        },
        {
            "user_id": 4,
            "name": "Interactive Cat Toy",
            "price": 11.90,
            "description": "Hands Free Cat Wand, Stand Up Cat Toy, Suction Cup Cat Wand (6.8x4.5x17cm). This cat toy is designed for those busy cat owners who have a lot on there plate day-to-day, but also want to give attention to their pet. Simply suction to you desired spot and let your pet do the rest.",
            "product_images": ["https://i.etsystatic.com/38243747/r/il/b72026/4315418703/il_1140xN.4315418703_edaw.jpg", "https://i.etsystatic.com/38243747/r/il/eb03b6/4268021086/il_794xN.4268021086_h543.jpg"],
            "reviews": []
        },
        {
            "user_id": 4,
            "name": "Catnip Infused Felt Balls",
            "price": 8.50,
            "description": "Catnip infused Felted Balls have all the power of catnip without the mess of loose catnip. Fair Trade felted balls come fully charged with B Happy (Our custom catnip blend) and ready for play. When kitty seems to lose interest in the balls, return them to the tin to recharge. The Catnip pod in the bottom of the tin will magically recharge the balls. Please allow 24-48 hours for balls to fully recharge.",
            "product_images": ["https://i.etsystatic.com/8678713/r/il/a50e72/2579419192/il_1140xN.2579419192_dix2.jpg", "https://i.etsystatic.com/8678713/r/il/519fb3/2627081377/il_1140xN.2627081377_2fea.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "These are so cute! The packaging is smart -- they can be 'recharged' with an enclosed catnip tea bag -- and they're the right size and weight even for my furry little goober. I love the combination of colors, too!",
                "review_images": ["https://i.etsystatic.com/iap/6be6dc/4293217550/iap_640x640.4293217550_42j81ogy.jpg?version=0"]
                },
                {
                "rating": 5,
                "text": "My kitties love their new toys! They are always playing with them & I am thrilled with my purchase!",
                "review_images": ["https://i.etsystatic.com/iap/c884ca/4285305588/iap_640x640.4285305588_9a4z6kr8.jpg?version=0"]
                }
            ]
        },
        {
            "user_id": 4,
            "name": "Scratch Post",
            "price": 116.93,
            "description": "Lovely modern scratching post",
            "product_images": ["https://i.etsystatic.com/26068660/r/il/c65709/3286818439/il_1140xN.3286818439_8xdv.jpg", "https://i.etsystatic.com/26068660/r/il/bf88bc/3474025549/il_1140xN.3474025549_29jw.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "This post exceeded my expectations. It is so sturdy and well made. The materials are phenomenal. To top it all off, it isn’t ugly. Looks amazing in my living room.",
                "review_images": ["https://i.etsystatic.com/iap/54dd2d/4268414418/iap_640x640.4268414418_5kxhlqx0.jpg?version=0"]
                },
                {
                "rating": 5,
                "text": "Excellent quality and really beautiful. Does not take up a lot of space, but tall enough for my cats to stretch. Base is thick and heavy, keeping the post stable. Highly recommend!",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "Just got mine a few days after making the purchase. I’m shocked how fast I got it considering where it was shipping from. It’s gorgeous and very high quality.",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "Not yet cat tested, but looks fantastic in the room. We think it will be a hit with our six-month old kitten. Thanks for making something both functional and beautiful.",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 5,
            "name": "Plush Dragon Dog Toy",
            "price": 16.74,
            "description": "Lovely plush dragon toy that both you and your furbaby will love. Super durable and made of sustainable materials",
            "product_images": ["https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/1349074-center-5", "https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/1349074-center-4"],
            "reviews": [
                {
                "demo" : True,
                "rating": 1 ,
                "text": "My frenchie puppy had the squeaker punctured in about 2 minutes and the whole thing ripped open in the first hour.",
                "review_images": ["https://photos-us.bazaarvoice.com/photo/2/cGhvdG86cGV0Y28/05b1f7fa-fd2a-52d8-a6df-e48e24a8bd80"]
                },
                {
                "rating":5 ,
                "text": "I was really surprised to read the poor reviews on this toy. These toys are the only soft toys that have held up for my cocker spaniel. He loves soft toys but destroys them within a day or two, but not these soft toys!",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 5,
            "name": "Plush Sloth Mermaid Dog Toy",
            "price": 5.14,
            "description": "This plush sloth mermaid is a funky treat your pup will love. Soft plush is cuddly and squeaker and crackle make delightfun sounds",
            "product_images": ["https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/3486456-center-1", "https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/3486456-center-3"],
            "reviews": [
                {
                "rating": 5,
                "text": "My puppy is four months old and absolutely loves the crinkle! We’ve had it for two weeks and she did puncture it going for the squeaker so I remove the squeaker and stitched our precious sushi back up and she’s good for couple more weeks of play.",
                "review_images": ["https://photos-us.bazaarvoice.com/photo/2/cGhvdG86cGV0Y28/5bbef906-3518-57fe-894c-a7e6945a4823"]
                },
                {
                "rating": 4,
                "text": "I purchased this a few weeks ago as a car toy for my pet on long rides. He loves it!",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 5,
            "name": "Window Teaser Assorted Cat Toy",
            "price": 9.89,
            "description": "The KONG window Teaser affixes to smooth surfaces, creating an active challenge for cats, even when you're not available to play. Each toy contains KONG Premium North American Catnip, bright feathers and a crinkle sound for added stimulation.",
            "product_images": ["https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/2402046-center-1", "https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/2402046-center-2"],
            "reviews": [
                {
                "rating": 5,
                "text": "Both of our cats love this toy!! Stays where we put it real well!! Our cats have already chewed the toy off the first one & we have already replaced it!!",
                "review_images": []
                },
                {
                "rating": 2,
                "text": "Would have given this product 5 stars because my cat LOVES this toy, but it broke very very quickly. Wish they made the attachments stronger, but I guess things are bound to break when they get used every day!",
                "review_images": []
                },
                {
                "rating": 3,
                "text": "Only lasted overnight. They bit the elastic. Cats 3. Birds 0. Would buy again on sale, but $9 per catnip bird is a little steep in my opinion. Haha",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 5,
            "name": "EveryYay Essentials Pink Snooze Fest Dog Bed Bundle, 22 inch L X 18 inch W",
            "price": 35.67,
            "description": "Make your fur babies dreams come true with the EveryYay Essentials Pink Snooze Fest Dog Bed Bundle. This 3-piece set includes a nester bed with the coziest sleep surface, a cuddly plush throw and a bone-shaped squeak toy so they can head right into playtime after naptime.",
            "product_images": ["https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/l_sale-badge,fl_relative,w_0.12,g_north_west,e_sharpen/l_bypetco-badge,fl_relative,w_0.20,g_south_east,e_sharpen/3323825-center-1", "https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/3323825-center-4"],
            "reviews": [
                {
                "demo" : True,
                "rating": 5,
                "text": "My dog loves this bed and the bone pillow that comes with it. Its the cutest pink. The pillow and blanket are an added bonus.",
                "review_images": []
                },
                {
                "rating":3,
                "text": "It took a long time to get here, and it was pretty small, even though my Min-Pin is small. She likes to stretch out, and this is more cat sized that small dog size. So far, the cats have not even used it! I have hope tho!",
                "review_images": []
                },
                {
                "rating":3,
                "text": "This is the 2nd bed I purchased for my puppy. I wanted her to hzve her choice where she wanted to nap or sleep and be warm and cozy. I had this bed for 13 years with my previous dog Luna and she loved it.",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 5,
            "name": "Multipet Medium Yellow Pineapple House",
            "price": 12.99,
            "description": "A cozy place to relax for your small animal companion. Made of soft fleece. Includes convenient hang tabs and clips to allow the flexibility to hang or sit on the floor.",
            "product_images": ["https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/2160147-left-1", "https://photos-us.bazaarvoice.com/photo/2/cGhvdG86cGV0Y28/7b1e3da3-18be-5249-a198-59ebe31aea2d"],
            "reviews": [
                {
                "rating": 4,
                "text": "My rats love it but its a pain to clean. Well, you're not suppose to submerge it, but that sure would be easier. Looking for something similar but washable now.",
                "review_images": ["https://photos-us.bazaarvoice.com/photo/2/cGhvdG86cGV0Y28/70bc3f60-5f44-5049-8ea1-2962ca601da4"]
                },
                {
                "rating": 3,
                "text": "Bought it for our guinea pigs. They were 2 months old and they could fit then. We had it about a month and the rope pieces are barely hanging on and a spot in the seam is coming undone.",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 6,
            "name": "Sherpa Reversible Dog Jacket",
            "price": 50.89,
            "description": "The Sherpa Reversible Jacket from Reddy features a cute camo design on one side and a cozy sherpa lining on the other. Light polyfill with sonic weld detailing keeps your pup especially cozy on windy mornings and cooler afternoons.",
            "product_images": ["https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/l_sale-badge,fl_relative,w_0.12,g_north_west,e_sharpen/3537954-center-11", "https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/3537954-center-10"],
            "reviews": [
                {
                "rating": 4,
                "text": "I bought this two days ago before I went on a 14 mile hike with my pup. It kept him warmed",
                "review_images": ["https://photos-us.bazaarvoice.com/photo/2/cGhvdG86cGV0Y28/c80f39d7-7f0a-542c-ab91-8870aad3a587"]
                },
                {
                "rating": 5,
                "text": "I purchased a small for my Maltipoo and it fits perfectly. The back zipper makes it so convenient to put on and take off.",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 6,
            "name": "Bootique Dog & Cat Taco Costume",
            "price": 18.99,
            "description": "Your pet will be taco the town in this Taco Costume from Bootique. A hook and loop closure that makes it easy peasy to secure this costume for your pet during trick or treating, photoshoots, or greeting little goblins.",
            "product_images": ["https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/l_bypetco-badge,fl_relative,w_0.20,g_south_east,e_sharpen/3568144-center-1", "https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/3568144-center-10"],
            "reviews": [
                {
                "rating": 5,
                "text": "I got a 3XL for my golden retriever mix and it fit he perfectly. He doesn’t like anything on his head so this costume was perfect and now he’s ready for Halloween!",
                "review_images": ["https://photos-us.bazaarvoice.com/photo/2/cGhvdG86cGV0Y28/1f6b98e4-e085-59ea-bd3f-628ab6e09e17"]
                },
                {
                "rating": 4,
                "text": "Cute costume. Seems to be a little bit higher quality than some of the costumes on the market right now. Easy to get on/off as dog doesn’t have to put paws through any holes to get in.",
                "review_images": ["https://photos-us.bazaarvoice.com/photo/2/cGhvdG86cGV0Y28/869be58b-ce43-51ae-abba-4d99e82087b5"]
                }
            ]
        },
        {
            "user_id": 6,
            "name": "The Green Rain Dog Jacket",
            "price": 80.99,
            "description": "The Green Dog Rain Jacket helps keep rainy days from getting in the way of enjoying the outdoors. The shielded leash portal provides additional protection from the rain so you can enjoy an un-furgettable adventure.",
            "product_images": ["https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/3478641-center-6", "https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/3478641-center-4"],
            "reviews": [
                {
                "rating": 4,
                "text": "The raincoat we ordered for my American Staffordshire Terrier is great except for one thing. The zipper. It's so hard to zip it up. Velcro would be better. I might add vecro straps to it.",
                "review_images": ["https://photos-us.bazaarvoice.com/photo/2/cGhvdG86cGV0Y28/93a406fb-047a-5e71-99ee-921b05b3fa0c"]
                },
                {
                "rating": 5,
                "text": "Love this raincoat! Fit my dog perfectly ! He loves it.",
                "review_images": ["https://photos-us.bazaarvoice.com/photo/2/cGhvdG86cGV0Y28/120b4519-3920-55dd-a571-61bf77c35158"]
                }
            ]
        },
        {
            "user_id": 6,
            "name": "Bootique Dog & Cat Pumpkin Hoodie",
            "price": 10.99,
            "description": "This Pumpkin Hoodie from Bootique is pick of the patch this Halloween! Your pet will love its coziness and you'll love that it's machine washable!",
            "product_images": ["https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/3568013-center-2", "https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/3568013-center-10"],
            "reviews": [
                {
                "demo" : True,
                "rating": 5,
                "text": "I just bought this a few days ago. It’s soft and doesn’t seem to bug my dog to wear it, but it does run small. ",
                "review_images": ["https://photos-us.bazaarvoice.com/photo/2/cGhvdG86cGV0Y28/39b30263-1b21-54e6-a822-0c7cde85d0ee"]
                },
                {
                "rating": 3,
                "text": "They're cute! The only issue I have is I just wish the hoods fit better...",
                "review_images": ["https://photos-us.bazaarvoice.com/photo/2/cGhvdG86cGV0Y28/08331b1e-fcc9-566d-99cd-ff9f11e5db5e"]
                }
            ]
        },
        {
            "user_id": 6,
            "name": "Prehistoric Fun Dinosaur Plush Dog Toy",
            "price": 5.89,
            "description": "Prehistoric Fun Dinosaur Plush Dog Toy delights your doggo in a great deal of fun. From thrilling textures to squeaky surprises, our Petco toys treat them to twice as much entertainment with the perfect duo of playtime pals.",
            "product_images": ["https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/1501666-center-1", "https://assets.petco.com/petco/image/upload/c_pad,dpr_1.0,f_auto,q_auto,h_468,w_500/c_pad,h_468,w_500/1501666-center-3"],
            "reviews": [
                {
                "rating": 5,
                "text": "My 16 year chihuahua never in her life has played with toys (she is a rescue) and as soon as she saw this Dino she went crazy for it! Highly recommend this!",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "I just bought this less than a week ago and my smaller dog is only about 25 lb so this was the perfect squeaky toy size for her-she loves it!",
                "review_images": ["https://photos-us.bazaarvoice.com/photo/2/cGhvdG86cGV0Y28/cfb63535-81aa-5d65-ad07-3ddc0c2e60c3"]
                }
            ]
        },
        {
            "user_id": 1,
            "name": "LARGE parrot TOY ** FIRECRACKER ** perfect for pluckers and foragers",
            "price": 27.00,
            "description": "This large toy includes lots of birdie bagels, crinkle paper, finger traps, marbella beads and a roll of paper on an extra large birdie bagel base. A must have for parrots that pluck!! Comes with a pear hook for hanging.",
            "product_images": ["https://i.etsystatic.com/6911893/r/il/07e788/1077917957/il_1588xN.1077917957_8ymq.jpg", "https://i.etsystatic.com/6911893/r/il/4750df/1159290852/il_1588xN.1159290852_ii7m.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "This ring is BIG! Or in my African Greys words meh. Its a tiny bit small!",
                "review_images": []
                },
                {
                "rating": 5,
                "text": "I chose this for our B&G Macaw rescue, Max. When we got him his chest was bare, now its finally starting to fill in. This toy is apparently another favorite.",
                "review_images": ["https://i.etsystatic.com/iap/e03900/1094898254/iap_300x300.1094898254_4az9xfql.jpg?version=0"]
                }
            ]
        },
        {
            "user_id": 7,
            "name": "Hanging Bird Toy for Parrots",
            "price": 13.71,
            "description": "The hanging toy is made of birch blocks, jute rope, cardboard sheets, acriylic mirrors and small bells. Easily and quickly hung in a cage or elsewhere with a small carabiner (included).",
            "product_images": ["https://i.etsystatic.com/37950554/r/il/df9d32/4342180663/il_1588xN.4342180663_akl3.jpg", "https://i.etsystatic.com/37950554/r/il/b2734a/4294683220/il_1588xN.4294683220_26bd.jpg"],
            "reviews": []
        },
        {
            "user_id": 7,
            "name": "Mega Parrot Stand",
            "price": 2250.00,
            "description": "The Strongest Organic parrot wood available in the entire United States is used to create all Mega Parrot Stand. Each Mega Parrot Stand is completely unique and strategically designed to fit the birds.",
            "product_images": ["https://i.etsystatic.com/25796398/r/il/893901/2758276236/il_1588xN.2758276236_i8rr.jpg", "https://i.etsystatic.com/25796398/r/il/0fc5dc/2758276266/il_1588xN.2758276266_sr9d.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "I’m really happy with the way the bird stand turned out. It arrived sooner than I expected and the seller was very kind and helpful as well!",
                "review_images": ["https://i.etsystatic.com/iap/979e19/2805942635/iap_300x300.2805942635_464gdqdk.jpg?version=0"]
                },
                {
                "rating": 5,
                "text": "Order a mega for the indoor, bulk wood for outdoor and a table top for office. ",
                "review_images": ["https://i.etsystatic.com/iap/6ad3a5/3810531706/iap_300x300.3810531706_6qq53lxu.jpg?version=0"]
                }
            ]
        },
        {
            "user_id": 7,
            "name": "UP AND OVER botllebrush toy",
            "price": 31.99,
            "description": "This bird toy is a great addition to any setup. Full of wood to chew and rip apart, this toy will keep any wood loving parrot busy for hours at a time.",
            "product_images": ["https://i.etsystatic.com/23144235/r/il/d75b42/3950341158/il_1588xN.3950341158_60mv.jpg", "https://i.etsystatic.com/23144235/r/il/65a421/3774771638/il_1588xN.3774771638_kb4s.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "My geriatric Rosey Bourke (20 years oldwith gout (being treated with meds) is loving her new bottle brush perch!",
                "review_images": ["https://i.etsystatic.com/iap/2f799b/4241015177/iap_300x300.4241015177_wn1tqefi.jpg?version=0"]
                },
                {
                "rating": 4,
                "text": "My bird just loved this toy. Her favorite parts are the mahogany pieces. It didn’t last real long but it made her happy!!",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 7,
            "name": "Can-o-Nuts Indestructible",
            "price": 12.99,
            "description": "Bonka Bird Toys 60002 Small Can-o-Nuts Birds is an interactive toy for your small to medium-sized cherished feathered friends",
            "product_images": ["https://i.etsystatic.com/7045787/r/il/f2da2c/4146973094/il_1588xN.4146973094_tth9.jpg", "https://i.etsystatic.com/7045787/r/il/7399ca/4194635027/il_1588xN.4194635027_c7py.jpg"],
            "reviews": [
                {
                "rating": 5,
                "text": "Its so much larger than I thought! I hope my Lucy bird loves it as much as I do!!",
                "review_images": ["https://i.etsystatic.com/iap/7ba83f/4313527508/iap_300x300.4313527508_9wgue2ax.jpg?version=0"]
                },
                {
                "rating": 1,
                "text": "I thought I ordered from the small section. This thing is big enough for a macaw. I have it in my conures cage and he isn't afraid of it so that's good",
                "review_images": []
                }
            ]
        },
        {
            "user_id": 8,
            "name": "Applé Naturalé ",
            "price": 19.95,
            "description": "The delicious dog food of Applé Naturalé that has an exciting mix of natural ingredients. With the Goodness of 100% Natural Ingredients",
            "product_images": ["https://placedog.net/142", "https://placedog.net/143"],
            "reviews": [
                {
                  "rating": 5,
                  "text": "Applé Naturalé is the most advanced dog food with technology that increases muscle oxygenation, stabilizes active muscles, and makes your dog look great",
                  "review_images": ["https://placedog.net/144"]
                },
                {
                  "rating": 1,
                  "text": "My dog doesn't think Applé Naturalé tastes like apples, would not recommend.",
                  "review_images": ["https://placedog.net/145"]
                },
                {
                  "rating": 5,
                  "text": "Applé Naturalé is great tasting and my dog loves it!",
                  "review_images": ["https://placedog.net/146"]
                }
            ]
        },
        {
            "user_id": 8,
            "name": "Orangé Naturalé",
            "price": 19.95,
            "description": "The delicious dog food Orangé Naturalé that has an exciting mix of natural ingredients. With the Goodness of 100% Natural Ingredients",
            "product_images": ["https://placedog.net/152", "https://placedog.net/153"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "My dog loves the natural orange flavor of Orangé Naturalé!",
                    "review_images": ["https://placedog.net/154"]
                },
                {
                    "rating": 5,
                    "text": "It really tastes like oranges.",
                    "review_images": ["https://placedog.net/155"]
                },
                {
                    "rating": 1,
                    "text": "My dog says it tastes like oranges but the texture is off.",
                    "review_images": ["https://placedog.net/156"]
                }
            ]
        },
        {
            "user_id": 8,
            "name": "Grapé Naturalé",
            "price": 19.95,
            "description": "The delicious dog food Grapé Naturalé that has an exciting mix of natural ingredients. With the Goodness of 100% Natural Ingredients",
            "product_images": ["https://placedog.net/162", "https://placedog.net/163"],
            "reviews": [
                {
                    "rating": 1,
                    "text": "Does not make good wine.",
                    "review_images": ["https://placedog.net/164"]
                },
                {
                    "rating": 5,
                    "text": "Yummy!",
                    "review_images": ["https://placedog.net/165"]
                },
                {
                    "rating": 1,
                    "text": "If it is natural grape flavor, why isn't it purple?",
                    "review_images": ["https://placedog.net/166"]
                }
              ]
        },
        {
            "user_id": 8,
            "name": "Limé Naturalé",
            "price": 19.95,
            "description": "The delicious dog food Limé Naturalé that has an exciting mix of natural ingredients. With the Goodness of 100% Natural Ingredients",
            "product_images": ["https://placedog.net/172", "https://placedog.net/173"],
            "reviews": [
                {
                    "rating": 1,
                    "text": "Too sour for my puppy.  Maybe an older dog would like it better.",
                    "review_images": ["https://placedog.net/174"]
                },
                {
                    "rating": 5,
                    "text": "Perfect for dogs who bark too much!",
                    "review_images": ["https://placedog.net/175"]
                },
                {
                    "rating": 5,
                    "text": "I wish there was a coconut flavor so I put my lime in the coconut and drink them both!",
                    "review_images": ["https://placedog.net/176"]
                }
            ]
        },
        {
            "user_id": 8,
            "name": "Pomegranaté Naturalé",
            "price": 19.95,
            "description": "The delicious dog food of Pomegranaté Naturalé that has an exciting mix of natural ingredients. With the Goodness of 100% Natural Ingredients",
            "product_images": ["https://placedog.net/182", "https://placedog.net/183"],
                "reviews": [
                    {
                        "rating": 1,
                        "text": "If it is 100% natural, why didn't pomegranates grow when I planted Pomegranaté Naturalé dog food?  Think about that before buying.",
                        "review_images": ["https://placedog.net/184"]
                    },
                    {
                        "rating": 1,
                        "text": "My dog thinks there are too many seeds. Buyer beware.",
                        "review_images": ["https://placedog.net/185"]
                    },
                    {
                        "rating": 5,
                        "text": "I love that it is full of antioxidants!",
                        "review_images":  ["https://placedog.net/186"]
                    }
                ]
        },
        {
            "user_id": 9,
            "name": "Miller Bite for Cats",
            "price": 19.95,
            "description": "The best diet non-alcoholic beer for cats in the world. Taste's great, less filling!  Miller Pets is not responsible for misuse of this product.",
            "product_images": ["https://cataas.com/cat/says/hello", "https://cataas.com/cat/cute/says/I%20love%20Miller%20Bite"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "My cat went crazy for Miller Bite!",
                    "review_images": ["https://cataas.com/cat/cute/says/I%20love%20Miller%20Bite"]
                },
                {
                  "rating": 1,
                  "text": "My cat didn't like it, she thought it was too hoppy.",
                  "review_images": ["https://cataas.com/cat/cute/says/Me%20no%20likey"]
                },
                {
                    "rating": 5,
                    "text": "Wonderful, I love it is low calorie and my cat does too!",
                    "review_images":  ["https://cataas.com/cat/cute/says/gotta%20stay%20in%20shape"]
                }
            ]
        },
        {
            "user_id": 9,
            "name": "Miller Bite for Foxes",
            "price": 19.95,
            "description": "The best diet non-alcoholic beer for foxes in the world. Taste's great, less filling!  Miller Pets is not responsible for misuse of this product.",
            "product_images": ["https://randomfox.ca/images/32.jpg", "https://randomfox.ca/images/1.jpg"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "What does the fox say?  That he loves Miller Bite!!!",
                    "review_images": ["https://randomfox.ca/images/2.jpg"]
                },
                {
                    "rating": 5,
                    "text": "My fox loves this stuff.",
                    "review_images": ["https://randomfox.ca/images/3.jpg"]
                },
                {
                    "rating": 4,
                    "text": "Store keeps running out of stock, but foxes love it so I'm giving it a four out of five!",
                    "review_images":  ["https://randomfox.ca/images/4.jpg"]
                }
            ]
        },
        {
            "user_id": 9,
            "name": "Miller Bite for Dogs",
            "price": 9.95,
            "description": "The best diet non-alcoholic beer for dogs in the world. Taste's great, less filling!  Miller Pets is not responsible for misuse of this product.",
            "product_images": ["https://placedog.net/282", "https://placedog.net/283"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "My dog can't get enough of Miller Bite!",
                    "review_images": ["https://placedog.net/284"]
                },
                {
                    "rating": 5,
                    "text": "I would love to meet the brewer, Miller Bite is the best!  I love their commercial, 'Who ate the homework, woof, woof!'",
                    "review_images": ["https://placedog.net/285"]
                 },
                {
                    "rating": 5,
                    "text": "My dog loves to settle in with a Miller Bite after a long day of chasing cars and barking at delivery drivers!",
                    "review_images":  ["https://placedog.net/286"]
                }
            ]
        },
        {
            "user_id": 9,
            "name": "Miller Genuine Draft for Dogs",
            "price": 9.95,
            "description": "The best full flavor and full calorie non-alcoholic beer for dogs in the world!  Miller Pets is not responsible for misuse of this product.",
            "product_images": ["https://placedog.net/382", "https://placedog.net/383"],
            "reviews": [
                {
                    "rating": 1,
                    "text": "My dog didn't like it compared to other brands",
                    "review_images": ["https://placedog.net/384"]
                },
                {
                    "rating": 2,
                    "text": "Never in stock.",
                    "review_images": ["https://placedog.net/385"]
                },
                {
                    "rating": 5,
                    "text": "I love it is so much cheaper on Petsy than the grocery store!",
                    "review_images":  ["https://placedog.net/386"]
                }
            ]
        },
        {
            "user_id": 9,
            "name": "Miller Genuine Draft for Cats",
            "price": 9.95,
            "description": "The best full flavor and full calorie non-alcoholic beer for cats in the world!  Miller Pets is not responsible for misuse of this product.",
            "product_images": ["https://cataas.com/cat/cute/says/MGDC%20is%20great", "https://cataas.com/cat/cute/says/MGDC%20is%20yummy%20in%20my%20tummy"],
            "reviews": [
                {
                    "rating": 1,
                    "text": "Why is MGD for Dogs cheaper?  No stars if I could!",
                    "review_images": ["https://cataas.com/cat/cute/says/don't%20buy"]
                },
                {
                    "rating": 3,
                    "text": "My order came with one empty bottle, the delivery cat looked guilty too!",
                    "review_images": ["https://cataas.com/cat/cute/says/missing%20a%20tasty%20bottle"]
                },
                {
                    "rating": 5,
                    "text": "My cat loves this stuff!",
                    "review_images":  ["https://cataas.com/cat/cute/says/loving%20it"]
                }
            ]
        },
        {
            "user_id": 10,
            "name": "Electric Cozey for Dogs",
            "price": 199.95,
            "description": "The warmest cozey for dogs, now with electricity!",
            "product_images": ["https://placedog.net/582", "https://placedog.net/583"],
            "reviews": [
                {
                    "rating": 1,
                    "text": "It is too electric for my dog",
                    "review_images": ["https://placedog.net/584"]
                },
                {
                    "rating": 1,
                    "text": "It shocked my dog!  ",
                    "review_images": ["https://placedog.net/585"]
                },
                {
                    "rating": 1,
                    "text": "What is this exactly and why is it for dogs?",
                    "review_images":  ["https://placedog.net/586"]
                }
            ]
        },
        {
            "user_id": 10,
            "name": "Electric Cozey for Cats",
            "price": 199.95,
            "description": "The warmest cozey for cats, now with electricity!",
            "product_images": ["https://cataas.com/cat/cute/says/Cozey%20Cat", "https://cataas.com/cat/cute/says/It's%20GRRReat"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "Just right!",
                    "review_images": ["https://cataas.com/cat/cute/says/Just%20Right"]
                },
                {
                    "rating": 1,
                    "text": "Too cold.",
                    "review_images": ["https://cataas.com/cat/cute/says/Too%20Cold"]
                },
                {
                    "rating": 1,
                    "text": "Too hot",
                    "review_images":  ["https://cataas.com/cat/cute/says/Too%20Hot"]
                }
            ]
        },
        {
            "user_id": 10,
            "name": "Small Cozey for Pets",
            "price": 299.95,
            "description": "The best cozey for small pets!",
            "product_images": ["https://placedog.net/682", "https://cataas.com/cat/cute/says/Cozey%20Cat"],
            "reviews": [
                {
                    "rating": 1,
                    "text": "It's too small for my dog.",
                    "review_images": ["https://placedog.net/784"]
                },
                {
                    "rating": 1,
                    "text": "It's too big for my cat.",
                    "review_images": ["https://cataas.com/cat/cute/says/Too%20big"]
                },
                {
                    "rating": 5,
                    "text": "I love this, it is so warm!",
                    "review_images":  ["https://cataas.com/cat/cute/says/Loves%20it"]
                }
            ]
        },
        {
            "user_id": 10,
            "name": "Medium Cozey for Pets",
            "price": 399.95,
            "description": "The best cozey for medium pets!",
            "product_images": ["https://placedog.net/412", "https://placedog.net/413"],
            "reviews": [
                {
                  "rating": 5,
                  "text": "My dog loves it!",
                  "review_images": ["https://placedog.net/414"]
                },
                {
                    "rating": 5,
                    "text": "It's the best cozey ever!",
                    "review_images": ["https://placedog.net/415"]
                },
                {
                    "rating": 5,
                    "text": "It's is cozy!  Wow!",
                    "review_images":  ["https://placedog.net/416"]
                }
            ]
        },
        {
            "user_id": 10,
            "name": "Large Cozey for Pets",
            "price": 499.95,
            "description": "The large cozey for large pets!",
            "product_images": ["https://randomfox.ca/images/5.jpg", "https://randomfox.ca/images/6.jpg"],
            "reviews": [
                {
                    "rating": 1,
                    "text": "Too large for my fox.",
                    "review_images": ["https://randomfox.ca/images/7.jpg"]
                },
                {
                    "rating": 1,
                    "text": "My fox got lost in this cozey!  Do not recommend for foxes.",
                    "review_images": ["https://randomfox.ca/images/8.jpg"]
                },
                {
                    "rating": 1,
                    "text": "Why do they advertise for foxes when it clearly isn't for foxes? No star for you!",
                    "review_images":  ["https://randomfox.ca/images/9.jpg"]
                }
            ]
        },
        {
            'user_id': 11,
            'name': 'Personalized Collars',
            'price': 10.00,
            'description': 'Classy, secure and soft leather pet collar - we are trying to make luxury affordable to everyone. :)',
            'product_images': ["https://i.etsystatic.com/24214074/r/il/ab7ed6/3763184462/il_1588xN.3763184462_a362.jpg", "https://i.etsystatic.com/24214074/r/il/e54cc7/3639250820/il_1588xN.3639250820_q7ob.jpg", "https://i.etsystatic.com/24214074/r/il/c2ddb4/3686856275/il_1588xN.3686856275_gn4l.jpg"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "Beautiful Collar withexecellent material. Customer service is excellent. 5 stars!!",
                    "review_images": ["https://i.etsystatic.com/iap/88237a/4383637589/iap_640x640.4383637589_4au3clfi.jpg?version=0"]
                },
                {
                    "rating": 5,
                    "text": "This was my second purchase and I love the collar. I’ve had the first one a few weeks now and it has held up perfectly and still looks brand new. Great quality collars and ships quickly.",
                    "review_images": ["https://i.etsystatic.com/iap/95051a/4192588926/iap_640x640.4192588926_86l5cqq4.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 11,
            'name': 'Custom Handmade Socks of your Pet',
            'price': 5.50,
            'description': 'Get custom socks with your very own fur babies face on them! They make the perfect gift for pet lovers! Every pair is made to order.',
            'product_images': ["https://i.etsystatic.com/7532280/r/il/566a7a/2110216053/il_1588xN.2110216053_55gr.jpg", "https://i.etsystatic.com/7532280/r/il/9106b2/2686830627/il_1588xN.2686830627_1nzq.jpg", "https://i.etsystatic.com/7532280/r/il/80acd5/2639170168/il_1588xN.2639170168_fimv.jpg"],
            "reviews": [
                {
                    "rating": 4,
                    "text": "Quick turnaround. The image on the socks wasn't perfect but they shipped me another pair. Quality socks!",
                    "review_images": ["https://i.etsystatic.com/iap/01e94d/1598346764/iap_640x640.1598346764_mti1c8qp.jpg?version=0"]
                },
                {
                    "rating": 5,
                    "text": "I purchased these socks in November as a Christmas gift for a friend. They were supposed to show up well before Christmas but with the virus and the ongoing issues with USPS they unfortunately got lost in the mail.",
                    "review_images": ["https://i.etsystatic.com/iap/8cca17/3973205797/iap_640x640.3973205797_a94vprdd.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 11,
            'name': 'Luxurious Dog Bed - Modern and Cute with Removable Cover',
            'price': 450.99,
            'description': 'Introducing the Modern Luxury Dog Bed – the perfect bed for your fur-baby! Made with high-quality 26D orthopedic foam, this bed is both durable and comfy, making it the perfect place for your pup to snuggle up and sleep. Plus, the removable and washable cover makes it easy to clean, so you can keep your pet bed clean and fresh with just a little bit of effort. This pet bed can be used as a cute cat bed as well.',
            'product_images': ["https://i.etsystatic.com/13496394/r/il/7f7bef/2262617506/il_1588xN.2262617506_hspl.jpg", "https://i.etsystatic.com/13496394/r/il/5d64a4/2262618328/il_1588xN.2262618328_3vux.jpg", "https://i.etsystatic.com/13496394/r/il/94b5ba/2262619122/il_1588xN.2262619122_4flt.jpg", "https://i.etsystatic.com/13496394/r/il/2cc140/2262618110/il_1588xN.2262618110_qrxr.jpg"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "Absolutely love it!! It took two months for me to receive my order which is a little too long. But considering that it was coming from Europe and been made by hands, I’m more than happy is exactly what I wanted for my fur baby.",
                    "review_images": ["https://i.etsystatic.com/iap/233150/3017276300/iap_640x640.3017276300_590tchqo.jpg?version=0"]
                },
                {
                    "rating": 5,
                    "text": "It’s perfect study well made well worth the money matched description exactly what I expected I could not be happier best quality purchase I have made I am so happy ! Came very quickly it’s is awesome thank you so much !",
                    "review_images": ["https://i.etsystatic.com/iap/357fd2/4265110810/iap_640x640.4265110810_4v65xam3.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 11,
            'name': 'Le Catnip',
            'price': 13.95,
            'description': "Le Catnip Premium and Organically Grown Catnip. The highest quality organically grown catnip, hand-harvested at the peak of the season for freshness, and a brilliant design you and your cats will love! Our catnip is non-GMO, pesticide-free, and all-natural. We make sure we only harvest the best quality catnip possible because we believe your pets are our family and only sell our catnip within a year of harvest for maximum potency and donate the previous year's supply to animal non-profits cat shelters.",
            'product_images': ["https://img.estadao.com.br/thumbs/640/resources/jpg/3/4/1529591672143.jpg"],
            "reviews": [
                {
                    "rating": 2,
                    "text": "Product is not bad but customer service is lacking",
                    "review_images": ["https://i.etsystatic.com/iap/4fce49/3957937718/iap_640x640.3957937718_5vyonsel.jpg?version=0"]
                },
                {
                    "rating": 3,
                    "text": "Shipping was prompt. May cat loved the cat nip, but customer service was bad.",
                    "review_images": ["https://i.etsystatic.com/iap/c960b7/4108007328/iap_640x640.4108007328_f1zaury9.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 11,
            'name': 'Personalised Pet Mug',
            'price': 12.99,
            'description': "Check out this beautifully printed pet face coffee mug. Personalized pet mug for pet mom & pet Dad. Custom pet photo mug perfect for your coffee, tea and hot chocolate. This classic shape white, durable ceramic coffee mug also comes in black, red, pink, and blue color rim/handles, Sizes 11oz & 15oz respectively.",
            'product_images': ["https://i.etsystatic.com/25392586/r/il/cb208c/3321600491/il_1588xN.3321600491_4iee.jpg", "https://i.etsystatic.com/25392586/r/il/862ec1/3583776062/il_1588xN.3583776062_nijl.jpg"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "So in love with this cup!! Everything I had hoped for and more",
                    "review_images": ["https://i.etsystatic.com/iap/6440f6/3868968124/iap_640x640.3868968124_fp4q3vts.jpg?version=0"]
                },
                {
                    "rating": 4,
                    "text": "I love buying custom mugs for my roommate and this one is her new favorite! The art style is beautiful, and it looks exactly like my roommate’s cat. Such a wonderful mug!",
                    "review_images": ["https://i.etsystatic.com/iap/1926a1/3785666175/iap_640x640.3785666175_rxvrbvl8.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 12,
            'name': 'Gourmet Dog Treats',
            'price': 12.99,
            'description': "Check out this beautifully printed pet face coffee mug. Personalized pet mug for pet mom & pet Dad. Custom pet photo mug perfect for your coffee, tea and hot chocolate. This classic shape white, durable ceramic coffee mug also comes in black, red, pink, and blue color rim/handles, Sizes 11oz & 15oz respectively.",
            'product_images': ["https://i.etsystatic.com/15234848/r/il/c000e0/3090858494/il_1588xN.3090858494_kupm.jpg", "https://i.etsystatic.com/15234848/r/il/29a235/3090858608/il_1588xN.3090858608_nkqh.jpg"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "My Yogi boy loves them! And they even smell nice, unlike regular dog treats",
                    "review_images": ["https://i.etsystatic.com/iap/14731d/3128521034/iap_640x640.3128521034_ne5das3s.jpg?version=0"]
                },
                {
                    "rating": 5,
                    "text": "My doggo took it away to her bed and a few seconds later it was gone! I’d say she liked them, thank you again!",
                    "review_images": ["https://i.etsystatic.com/iap/1926a1/3785666175/iap_640x640.3785666175_rxvrbvl8.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 12,
            'name': 'Funny Custom Pet Portrait',
            'price': 15.50,
            'description': "This is the best way to show off your love for your pet to just about everyone who enters your home! These portraits are a life long product that will last forever when framed! Express your love for your best friend on our premium highest-quality matte poster or a premium framed portrait!",
            'product_images': ["https://i.etsystatic.com/26335741/r/il/caca72/3015003196/il_1588xN.3015003196_e6c4.jpg", "https://i.etsystatic.com/26335741/r/il/dcb624/2819101821/il_1588xN.2819101821_hvac.jpg", "https://i.etsystatic.com/26335741/r/il/b25128/3739554770/il_1588xN.3739554770_24rf.jpg"],
            "reviews": [
                {
                    "rating": 4,
                    "text": "Quality is amazing, matched the description perfectly & we beyond LOVE our portrait of our special boy ❤️",
                    "review_images": ["https://i.etsystatic.com/iap/b46798/3896649307/iap_640x640.3896649307_4sd1jzj8.jpg?version=0"]
                },
                {
                    "rating": 4,
                    "text": "I'm absolutely in love with this fun little portrait of Crouton!! It came in super quickly and I think it's so cute.",
                    "review_images": ["https://i.etsystatic.com/iap/05d5cc/3148299282/iap_640x640.3148299282_hz3rgtwy.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 12,
            'name': 'Organic Pet Shampoo',
            'price': 9.99,
            'description': "Keep your dog clean with this incredible shampoo. Mild, gentle, and certified organic. Hints of oak, lemon and rosemary.",
            'product_images': ["https://i.etsystatic.com/19456819/r/il/229195/2394384756/il_1588xN.2394384756_8i53.jpg", "https://i.etsystatic.com/19456819/r/il/22a02a/2356069697/il_1588xN.2356069697_hltb.jpg"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "I will be ordering this again! Aprill was prompt, friendly, and clearly cares about what she does. This shampoo is gentle on my little Pomeranian, whose fur picks up a lot of dirt.",
                    "review_images": ["https://i.etsystatic.com/iap/8e8861/2511640056/iap_640x640.2511640056_lzayttyi.jpg?version=0"]
                },
                {
                    "rating": 2,
                    "text": "I love the fact that this is all-natural, but I hate that it's messy. It left so much residue on my carpet, making me feel like it's more trouble than it's worth. My dogs smell nice, though.",
                    "review_images": ["https://i.etsystatic.com/iap/db6557/3382464356/iap_300x300.3382464356_dsnd6csw.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 1,
            'name': 'Indestructible Chew Toy for Dogs',
            'price': 4.75,
            'description': "This Chew toy is one of a kind! It is made of natural rubber and is highly indestructible. It is able to withstand the force of a 220-pound steel brick.",
            'product_images': ["https://i.etsystatic.com/28085568/r/il/0fa399/4086018953/il_1588xN.4086018953_5a6j.jpg", "https://i.etsystatic.com/28085568/r/il/51c539/4038308008/il_1588xN.4038308008_nw7l.jpg"],
            "reviews": [
                {
                    "rating": 4,
                    "text": "My grand dog loves these bones. I got one for all three of my grand dogs but she likes them so much that she won’t let the other dogs have one.",
                    "review_images": ["https://i.etsystatic.com/iap/643b44/4045813019/iap_640x640.4045813019_3diun98m.jpg?version=0"]
                },
                {
                    "rating": 3,
                    "text": "Quality is ok, My dog likes it.",
                    "review_images": ["https://i.etsystatic.com/iap/9c7599/4180848465/iap_640x640.4180848465_7ly9btpu.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 12,
            'name': 'Custom Made Flea and Tick Collar',
            'price': 12.99,
            'description': "Protect your pet with this made to order flea and tick collar. Come in multiple colors and patterns",
            'product_images': ["https://i.etsystatic.com/30582641/r/il/36c2d7/3728723437/il_1588xN.3728723437_82fu.jpg", "https://i.etsystatic.com/30582641/r/il/5d20fe/3217355003/il_1588xN.3217355003_f7f5.jpg"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "A very nice and reliable saleswoman! She also responded to my color request. Everything was great!",
                    "review_images": ["https://i.etsystatic.com/iap/ff0107/4047435528/iap_640x640.4047435528_b4jr263x.jpg?version=0"]
                },
                {
                    "rating": 3,
                    "text": "I am very very excited about the top quality of this leash :-D It is very robust and stable, so that it would be quite quick to undress in case ! I am happy about this beautiful part, thank you for being there ;-) I will order from you again!",
                    "review_images": ["https://i.etsystatic.com/iap/66cb6f/4251018328/iap_640x640.4251018328_ofuert8b.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 13,
            'name': 'Scratching Post',
            'price': 30.00,
            'description': 'Handcrafted scratching post for healthy and happy cats! 36” tall with a 16" x 16" base. Post is handmade in the USA',
            'product_images': ["https://i.etsystatic.com/29797583/r/il/d0a209/3090466748/il_1588xN.3090466748_kmki.jpg", "https://i.etsystatic.com/29797583/r/il/db3ada/3138196537/il_1588xN.3138196537_ovmk.jpg"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "The scratching post is well-constructed, sturdy, and nice-looking. I appreciated being able to choose the appropriate height, as well as the wood grain color of the base. It looks well in my home.",
                    "review_images": ["https://i.etsystatic.com/iap/239098/3152257902/iap_640x640.3152257902_c8zgz8nr.jpg?version=0"]
                },
                {
                    "rating": 1,
                    "text": "Poor packaging, it was broken when it arrived",
                    "review_images": ["https://i.etsystatic.com/iap/b3fd45/4386424657/iap_640x640.4386424657_kc17ki91.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 13,
            'name': 'Modern Cat Tree',
            'price': 120.99,
            'description': "Cat furniture with a solid base to ensure stability;This piece of art contains real natural wood that is hand-made and professionally crafted to fit a cat tree. Each piece is unique, 1 of 1 and makes great furniture for cats. Looking for a wood cat condo, modern cat tree, a new cat gift, or some awesome cat accessories? You've found the right shop!",
            'product_images': ["https://i.etsystatic.com/21169689/r/il/be435b/3961816702/il_1588xN.3961816702_lqok.jpg", "https://i.etsystatic.com/21169689/r/il/3d3b8d/4312050609/il_1588xN.4312050609_az94.jpg"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "Easily one of the best purchases I have EVER made. We run a rescue out of our home and have 25 cats flying around wrecking everything all the time, but they cannot wreck this! It is STURDY, and they absolutely love it!",
                    "review_images": ["https://i.etsystatic.com/iap/552b89/4280364872/iap_640x640.4280364872_oqmfceta.jpg?version=0"]
                },
                {
                    "rating": 5,
                    "text": "If you are hesitating bc of the wait time - do not! Worth the wait and every single penny! Not only is this tree very beautiful it is also functional. It it steady and extremely well made.",
                    "review_images": ["https://i.etsystatic.com/iap/0690d3/4085425063/iap_640x640.4085425063_d3bk1am7.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 13,
            'name': 'Cat Ornament',
            'price': 3.99,
            'description': "This handmade ceramic cat ornament is hand-cut ornament is cut from earthenware clay, hand-painted with under-glaze, gloss glazed and kiln fired producing a lasting keepsake. Satin ribbon for hanging. This ornament is an ideal cat lover's gift! You can easily personalize with a marker or craft pen or I can do it for you.",
            'product_images': ["https://i.etsystatic.com/32636655/r/il/6049e6/4157978054/il_1588xN.4157978054_swbr.jpg", "https://i.etsystatic.com/32636655/r/il/4746b8/4205631895/il_1588xN.4205631895_az3q.jpg"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "Very nicely done. The creativity is excellent - it's not just a photo. It's a memory - and a good one.",
                    "review_images": ["https://i.etsystatic.com/iap/32bca0/4257848470/iap_640x640.4257848470_bs68o0mu.jpg?version=0"]
                },
                {
                    "rating": 3,
                    "text": "It was much smaller than I expected. The background is more cream color than the white background on the website picture. The owner of the company was very nice and kept me up to date on everything.",
                    "review_images": ["https://i.etsystatic.com/iap/e4be70/4363909191/iap_640x640.4363909191_hdxp6d9j.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 13,
            'name': 'Cat Party Decorations',
            'price': 10.99,
            'description': "Take the stress out of party planning with our Kitty Cat Party decorations we have everything you need for a totally puuuuuuurfect party! Cat Balloon Model Set contains: balloons (34 pcs), foil balloon (1 piece), modeling balloons (2 pcs), paper straw (1 piece), foam tape (24 pcs) and 2.5 m of balloon garland tape. Size approx. 83 x 140 cm.",
            'product_images': ["https://i.etsystatic.com/15338498/r/il/e93faa/3269862153/il_1588xN.3269862153_r3ss.jpg", "https://i.etsystatic.com/15338498/r/il/6bc9b5/3177869830/il_1588xN.3177869830_b1uh.jpg"],
            "reviews": [
                {
                    "rating": 5,
                    "text": "Adorable decor for my cat's 13th birthday. Made it a festive event.",
                    "review_images": ["https://i.etsystatic.com/iap/ce25dc/4179311782/iap_640x640.4179311782_ltbf6r9l.jpg?version=0"]
                },
                {
                    "rating": 3,
                    "text": "Amazing seller and product",
                    "review_images": ["https://i.etsystatic.com/iap/db79d5/3342081749/iap_640x640.3342081749_kk1wnoi6.jpg?version=0"]
                }
            ]
        },
        {
            'user_id': 13,
            'name': 'Neon Cat Sign',
            'price': 103.45,
            'description': "Flex LED neon sign is made of flexible silicon tubes with LED lights inside tubes look like vintage glass neon sign. The size of the neon presented in the photo is 14.1x8.2in(36x21cm)",
            'product_images': ["https://i.etsystatic.com/33072429/r/il/04049e/3793477357/il_1588xN.3793477357_kaxx.jpg", "https://i.etsystatic.com/33072429/r/il/511214/3793465513/il_1588xN.3793465513_anzw.jpg"],
            "reviews": [
                {
                    "rating": 1,
                    "text": "very flimsy and low quality unfortunately :( thought it could stand up on its own based on the pictures but it needs to be mounted. Reached out the seller but they refused a refund.",
                    "review_images": ["https://i.etsystatic.com/iap/7c996e/4353667507/iap_640x640.4353667507_9smdfx92.jpg?version=0"]
                },
                {
                    "rating": 3,
                    "text": "Great color buyt average quality",
                    "review_images": ["https://i.etsystatic.com/33072429/r/il/b74bf9/3793465583/il_1588xN.3793465583_rl4r.jpg"]
                }
            ]
        }
    ]

    for seed in seed_data:
        new_product = Product(
            user_id=seed["user_id"],
            name=seed["name"],
            price=seed["price"],
            description=seed["description"],
        )
        db.session.add(new_product)
        db.session.commit()


        for i, url in enumerate(seed["product_images"]):
            preview_image = False
            if i == 0:
                preview_image = True
            new_product_image = ProductImage(
                product_id=new_product.id,
                url=url,
                preview_image=preview_image
            )

            db.session.add(new_product_image)

        db.session.commit()

        new_id = new_product.user_id + 1
        if new_id > 13:
            new_id = 12


        for review in seed["reviews"]:
            new_id = new_product.user_id + 1
            if new_id > 13:
                new_id = 12
            if review.get('demo'):
                new_id = 1

            new_review = Review(
                user_id = new_id,
                product_id=new_product.id,
                text=review["text"],
                rating=review["rating"]
            )
            db.session.add(new_review)
            db.session.commit()

            if review["review_images"]:
                new_review_image = ReviewImage(
                    review_id=new_review.id,
                    url=review["review_images"][0]
                )
                db.session.add(new_review_image)
                db.session.commit()

    # Seed data for an order
    new_order = Order(
        user_id = 1,
        total_price = 44.47
    )
    order_product1 = OrderProduct(
        product_id = 16,
        item_price = 16.74,
        quantity = 2,
        order_id = 1
    )
    order_product2 = OrderProduct(
        product_id = 24,
        item_price = 10.99,
        quantity = 1,
        order_id = 1
    )
    new_order2 = Order(
        user_id = 1,
        total_price = 35.67
    )
    order_product3 = OrderProduct(
        product_id = 19,
        item_price = 35.67,
        quantity = 1,
        order_id = 2
    )

    db.session.add(new_order)
    db.session.add(new_order2)
    db.session.add(order_product1)
    db.session.add(order_product2)
    db.session.add(order_product3)
    db.session.commit()



# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")
        db.session.execute("DELETE FROM orders")
        db.session.execute("DELETE FROM products")
        db.session.execute("DELETE FROM reviews")
        db.session.execute("DELETE FROM order_products")
        db.session.execute("DELETE FROM product_images")
        db.session.execute("DELETE FROM review_images")

    db.session.commit()
