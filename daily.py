import json, datetime

PLAY = ("https://play.google.com/store/apps/details?id=com.liteguard.android&referrer="
        "utm_source%3D{src}%26utm_medium%3Dsocial%26utm_campaign%3Ddaily%26utm_content%3D{pid}")
RAW = "https://raw.githubusercontent.com/tankobalazs-art/liteguard-social-assets/main/{pid}/post.jpg"
FOOT = "LiteGuard · No-logs VPN for Android"
SAFE = ("Portrait 2:3. Keep ALL text inside the central area (at least 12% margin from top and bottom edges, "
        "8% from the sides) because the image will be cropped to 4:5. Spell every word exactly as given. "
        "At the bottom, small and subtle: \"" + FOOT + "\". No real brand logos, no real people, no celebrities.")

STYLE = {
 "a": ("Clean premium editorial social-media card. Deep navy (#0b1630) background with a soft teal (#3ddbc9) glow. "
       "In the upper-middle, a simple, elegant flat-3D illustration of: {scene}. Below it a small teal label "
       "\"PRIVACY TIP #{n}\" and a bold white modern sans-serif headline: \"{headline}\". Minimal, lots of breathing room, "
       "Apple-keynote-like polish."),
 "b": ("Playful, bright social-media engagement graphic. Soft gradient background from mint teal to light lavender. "
       "Glossy 3D clay-style illustration of: {scene}. Large bold dark-navy rounded sans-serif headline: \"{headline}\". "
       "Fun, friendly, high contrast, scroll-stopping."),
 "c": ("Photorealistic cinematic night photograph: {scene}. Stylish, fully clothed adults, natural poses, "
       "teal and warm neon tones, shallow depth of field, phone screen glow, 35mm film look. "
       "Bold clean white headline in the upper third: \"{headline}\"."),
}

TAGS = {
 "a": "#privacytips #cybersecurity #onlineprivacy #android #vpn #publicwifi #techtips",
 "b": "#privacy #publicwifi #android #techlife #vpn #question",
 "c": "#nightlife #travel #privacy #vpn #android #nologs #liteguard",
}
PRODUCT = "LiteGuard encrypts your connection with one tap. No logs. Android · $3.99/month · 14-day money-back."

# (headline, scene, body, cta, link_on_fb)
D = [
# day 1 – Fri Nov 6
[("Public Wi-Fi names can be faked.", "a phone Wi-Fi list showing two identical networks named Cafe_Free_WiFi, one with a tiny hidden devil-tail",
  "Anyone can name a hotspot \"Cafe_Free_WiFi\" or \"Airport_Guest\". Join the wrong one and whoever runs it can watch your traffic.\n\nAsk staff for the exact network name, and switch on a VPN before you log in to anything.",
  "Have you ever joined a Wi-Fi you weren't 100% sure about? Be honest 👇", True),
 ("Café Wi-Fi or mobile data?", "split screen: left a 3D coffee cup with an open padlock and Wi-Fi symbol, right a 3D phone with signal bars",
  "Quick one. When you sit down at a café, what do you actually do?\n\n☕ = connect to the café Wi-Fi\n📶 = stay on mobile data",
  "Comment ☕ or 📶 — let's see who wins.", False),
 ("Friday night. Phone at 12%. Hotel Wi-Fi.", "a woman in a smart blazer in an elegant hotel lobby at night, low battery icon on her phone, warm lamps",
  "Friday night, new city, battery dying, and the only network is \"Hotel_Guest\".\n\nEvery guest in the building is on that same network. " + PRODUCT,
  "Where are you spending this Friday night? 👇", True)],
# day 2 – Sat Nov 7
[("Incognito mode doesn't hide you from the Wi-Fi.", "a browser window with an incognito hat and glasses, while a router behind it still sees through a magnifying glass",
  "Incognito only stops your phone from saving history. The Wi-Fi owner and your internet provider can still see which sites you visit.\n\nA VPN encrypts the connection itself, so the network sees only scrambled traffic.",
  "Did you know this one? Yes / No 👇", True),
 ("The sketchiest Wi-Fi I ever used was at ____", "3D icons floating: an airplane, a hotel bell, a coffee cup, a train, a beach umbrella, each with a Wi-Fi symbol",
  "Fill in the blank. Airport? Hostel? A beach bar with a password written on a napkin?",
  "Tell us your sketchiest Wi-Fi story 👇 Best one gets pinned.", False),
 ("Saturday plans: yours. Your browsing: also yours.", "two friends laughing on a rooftop bar terrace at night with city lights behind, one glancing at her phone",
  "Out tonight? Enjoy it. Your phone keeps working in the background on whatever network it finds.\n\n" + PRODUCT,
  "Rooftop, club, or couch tonight? 👇", True)],
# day 3 – Sun Nov 8
[("3 signs a Wi-Fi network isn't safe.", "a Wi-Fi symbol with three small warning badges around it: an open lock, a duplicated sign, a form asking for too much information",
  "1. No password at all.\n2. Two networks with almost the same name.\n3. A login page that asks for your email password or card details.\n\nSee one of these? Stay on mobile data or turn on a VPN first.",
  "Which of these have you seen? 1, 2 or 3? 👇", True),
 ("How many Wi-Fi networks has your phone saved?", "a 3D phone with a long curling receipt of Wi-Fi network names spilling out of the screen",
  "Go to Settings → Wi-Fi → Saved networks and count.\n\nA) Under 10\nB) 10–50\nC) 50+\nD) I'm scared to check",
  "Drop your letter (or the actual number 👀)", False),
 ("Even at home, your provider sees every site you visit.", "a man relaxing on a sofa in a dim cozy apartment at night, phone glow on his face, city window behind",
  "Home Wi-Fi feels private. But your internet provider can still log every site you open.\n\n" + PRODUCT,
  "Did you know your provider can see this? 👇", True)],
# day 4 – Mon Nov 9
[("Forget networks you don't use.", "a phone settings screen with old Wi-Fi networks being swept away by a small 3D broom",
  "Your phone auto-joins any saved network name it sees again. Someone can create a hotspot with that same name.\n\nSettings → Wi-Fi → Saved networks → delete the ones you don't need. Takes 30 seconds.",
  "Done it? Comment ✅ when you've cleaned your list.", True),
 ("Rate your privacy habits: 1–10", "a big glossy 3D slider from 1 to 10 with a tiny phone character standing on number 5 looking unsure",
  "No judgement. Same password everywhere? Joins every free Wi-Fi? Never updates apps?\n\nGive yourself a score.",
  "What's your number? 1–10 👇", False),
 ("Monday commute. Same train, same Wi-Fi, 200 strangers.", "commuters on a modern city train at night, a woman in a wool coat scrolling her phone by the window",
  "Train Wi-Fi is one big shared network. Everyone on board is on it with you.\n\n" + PRODUCT,
  "Do you use train Wi-Fi? Yes / No / Only when desperate 👇", True)],
# day 5 – Tue Nov 10
[("HTTPS is good. It isn't everything.", "a padlock in a browser bar, with the website name still visible on a glowing label floating above it",
  "The padlock means the page content is encrypted. But the network can still see which sites you visit.\n\nA VPN hides that list too.",
  "Did you think the padlock covered everything? 👇", True),
 ("Describe public Wi-Fi in 3 emojis.", "three giant 3D emoji bubbles with question marks inside, floating next to a Wi-Fi symbol",
  "Ours: 🐢🔓🙃\n\nYour turn.",
  "Three emojis, go 👇", False),
 ("Working late? Shared office = shared network.", "a man working late in a modern coworking space at night, laptop and phone on the desk, city lights outside",
  "Coworking spaces are great. Their Wi-Fi is shared with everyone in the building.\n\n" + PRODUCT,
  "Office, home, or coworking — where do you work best? 👇", True)],
# day 6 – Wed Nov 11
[("Turn off auto-join for public networks.", "a phone with a toggle switch labeled Auto-join being flipped off by a small hand",
  "When auto-join is on, your phone connects to networks without asking you.\n\nOn Android: tap a saved public network → turn off \"Auto-reconnect\".",
  "Is auto-join on or off on your phone right now? 👇", True),
 ("Myth or fact: a VPN makes you 100% anonymous.", "a big 3D question mark split in two halves, one teal labeled MYTH and one lavender labeled FACT",
  "Vote first, then read on.\n\nAnswer: MYTH. A VPN encrypts your connection and hides your IP from websites. It doesn't make you invisible — if you log in to an account, that site still knows it's you. Anyone promising \"100% anonymous\" is overselling.",
  "Did you get it right? 👇", False),
 ("Late walk home. Notifications off. Connection encrypted.", "a woman in a long coat walking down a rain-wet city street at night, neon reflections, phone in hand",
  "Small habits, quiet mind.\n\n" + PRODUCT,
  "Night owl or early bird? 👇", True)],
# day 7 – Thu Nov 12
[("Update your apps. Seriously.", "a phone with a glowing update arrow, a small shield appearing over it",
  "Most updates quietly fix security holes. Old apps are the easiest way in.\n\nTurn on auto-update in the Play Store and stop thinking about it.",
  "Auto-update: on or off? 👇", True),
 ("Airport lounge or gate floor + power outlet?", "split screen: left a comfy 3D lounge armchair, right a 3D phone charging from a floor socket next to a backpack",
  "Be honest about your airport style.\n\n🛋️ = lounge\n🔌 = floor next to the only working outlet",
  "🛋️ or 🔌? 👇", False),
 ("New city. New hotel. Same question: who runs this Wi-Fi?", "a man in a hotel room at night looking out a floor-to-ceiling window over a glittering city, phone in hand",
  "You don't know who set up the hotel network, or who else is on it.\n\n" + PRODUCT,
  "Last city you stayed in? 👇", True)],
# day 8 – Fri Nov 13
[("Your IP address tells sites roughly where you are.", "a 3D map pin hovering over a phone, with a dotted line connecting to a world map",
  "Every site you visit sees your IP address — usually enough to guess your city and provider.\n\nWith a VPN, sites see the VPN server's address instead of yours.",
  "Did you know this? 👇", True),
 ("Caption this.", "a cute nervous 3D phone character with big eyes staring at a glowing FREE WIFI sign in a dark street",
  "We have no idea what's going through his mind.",
  "Best caption gets pinned 👇", False),
 ("Dinner booked. Restaurant Wi-Fi password on the menu.", "a couple at a candle-lit modern restaurant at night, a small card with a Wi-Fi password on the table, phone glow",
  "Same network as every table in the room.\n\n" + PRODUCT,
  "What's your Friday dinner tonight? 👇", True)],
# day 9 – Sat Nov 14
[("Protect your email first.", "a 3D envelope with a key and a shield, other app icons connected to it by thin lines",
  "Your email resets every other password you have. If someone gets it, they get everything.\n\nTurn on two-step verification for your email today. It's the single best 5-minute privacy upgrade.",
  "Is 2-step verification on for your email? Yes / No / What's that? 👇", True),
 ("Where do you use public Wi-Fi most?", "four 3D icons in a grid: a coffee cup, an airplane, a hotel bell, a train, each with a Wi-Fi symbol",
  "☕ Cafés\n✈️ Airports\n🏨 Hotels\n🚆 Trains",
  "Vote with an emoji 👇", False),
 ("Weekend trip. Station Wi-Fi. Think before you log in.", "a young woman with a weekend bag on a grand train station platform at night, warm lights, phone in hand",
  "Stations are full of open networks — and of people setting up fake ones.\n\n" + PRODUCT,
  "Where's your next weekend trip? 👇", True)],
# day 10 – Sun Nov 15
[("Check which apps know your location.", "a 3D location pin with several small app icons lined up in front of it, some fading out",
  "Settings → Location → App location permissions.\n\nSwitch anything that doesn't need it to \"Don't allow\" or \"Only while using\".",
  "How many apps had location access? 👇", True),
 ("Unpopular opinion: free VPNs aren't free.", "a 3D price tag reading FREE with a tiny hidden fishing hook on its string",
  "Running servers costs money. If you're not paying, the money has to come from somewhere — often ads or your data.\n\nAgree or disagree?",
  "Agree 👍 or disagree 👎? 👇", False),
 ("Sunday reset: clean your saved Wi-Fi list.", "a calm woman at a kitchen table on Sunday evening with tea and a phone, soft lamp light",
  "30 seconds, once a week. Delete networks you won't use again.\n\n" + PRODUCT,
  "What's your Sunday-night ritual? 👇", True)],
# day 11 – Mon Nov 16
[("Banking on open Wi-Fi? Encrypt first.", "a 3D bank card and phone under a teal glass dome shield",
  "Banking apps use their own encryption, but the rest of your phone keeps talking on the same network.\n\nWith LiteGuard your banking app can stay on its normal connection while everything else is encrypted.",
  "Do you ever do banking on public Wi-Fi? 👇", True),
 ("Quiz: who can see the sites you visit?", "three 3D answer cards labeled A, B and C floating over a soft gradient",
  "A) The Wi-Fi owner\nB) Your internet provider\nC) Both\n\nAnswer in the comments — we'll reply to every right one.",
  "A, B or C? 👇", False),
 ("Late office. Empty floor. Still connected.", "a woman working late in an empty modern office at night, city skyline through windows, phone glowing",
  "Office networks are managed by people you don't know.\n\n" + PRODUCT,
  "What time did you finish work today? 👇", True)],
# day 12 – Tue Nov 17
[("Set file sharing to contacts only.", "a phone sending a file icon, with a small shield limiting it to a few contact bubbles",
  "Nearby file sharing set to \"Everyone\" lets strangers send you files in public places.\n\nAndroid: Settings → Connected devices → Quick Share → Contacts only.",
  "What's yours set to right now? 👇", True),
 ("Would you rather…", "two 3D doors: one with a phone in a locked box labeled 1 WEEK, one with a browser history scroll labeled BOSS",
  "A) Lose your phone for a week\nB) Your boss reads your browser history\n\nYou have to pick one.",
  "A or B? 👇", False),
 ("Hostel night. 40 backpackers. One password.", "backpackers in a stylish hostel common room at night, string lights, one young man checking his phone",
  "Shared rooms, shared kitchen, shared Wi-Fi.\n\n" + PRODUCT,
  "Hostel or hotel? 👇", True)],
# day 13 – Wed Nov 18
[("On a shared computer? Always log out.", "a public library computer screen with a big glowing LOG OUT button",
  "Closing the tab isn't logging out. The next person may land straight in your account.\n\nLog out, and never tick \"Remember me\" on a device that isn't yours.",
  "Ever found someone else logged in? 👇", True),
 ("Tag someone who joins every free Wi-Fi 😅", "a 3D phone character with a fishing rod catching Wi-Fi symbols like fish",
  "We all have that friend.",
  "Tag them 👇 (they know who they are)", False),
 ("Late study session. Campus Wi-Fi.", "students studying late in a modern university library at night, warm desk lamps, phone and notes",
  "Thousands of students, one network.\n\n" + PRODUCT,
  "What are you studying (or wish you'd studied)? 👇", True)],
# day 14 – Thu Nov 19
[("What a VPN actually does, in 20 seconds.", "a simple diagram: phone → glowing teal tunnel → server → internet, with a blurred router outside the tunnel",
  "Your phone → encrypted tunnel → VPN server → the website.\n\nThe Wi-Fi and your provider see only scrambled data going to the VPN. Websites see the VPN's address, not yours. That's it.",
  "Questions about VPNs? Ask below, we answer all of them 👇", True),
 ("True or false: hotel Wi-Fi with a password is private.", "a 3D hotel key card with a Wi-Fi password printed on it, a big TRUE / FALSE toggle next to it",
  "Think about it…\n\nFALSE. Every guest gets the same password. A password keeps strangers out of the building's network — not out of your traffic.",
  "Did you get it? 👇", False),
 ("Business trip. Hotel desk. Client files open.", "a man in a dress shirt working at a hotel room desk at night, laptop and phone, city lights in the window",
  "Client work on a hotel network. Worth one tap.\n\n" + PRODUCT,
  "How many work trips have you done this year? 👇", True)],
# day 15 – Fri Nov 20
[("QR codes can point anywhere.", "a 3D QR code on a café table with a small magnifying glass revealing a suspicious link",
  "A sticker over a real QR code can send you to a fake payment or login page.\n\nBefore opening, check the link preview. If it looks odd, type the address yourself.",
  "Do you check where a QR code goes? 👇", True),
 ("How do you feel about apps tracking you?", "four giant 3D emoji faces in a row: angry, grimacing, shrugging, relaxed",
  "😡 Furious\n😬 Uncomfortable\n🤷 I've given up\n😌 Don't care",
  "Pick one 👇", False),
 ("Friday. Cocktail bar. Free Wi-Fi.", "two friends at a dim stylish cocktail bar at night, teal neon behind the bottles, one holding a phone",
  "Enjoy the drinks. Let the encryption do its job.\n\n" + PRODUCT,
  "What are you drinking tonight? 🍸 🍷 🍺 🧃 👇", True)],
# day 16 – Sat Nov 21
[("Block third-party cookies.", "a browser window with small 3D cookies being stopped by a teal shield at the edge",
  "Third-party cookies follow you from site to site to build an ad profile.\n\nIn your browser settings, block third-party cookies. Most sites work just fine.",
  "Have you changed this setting? 👇", True),
 ("I'd never log into ____ on public Wi-Fi.", "a 3D login form with a blinking cursor, floating next to a Wi-Fi symbol with a question mark",
  "Finish the sentence.",
  "👇 What's yours?", False),
 ("Mountain weekend. Lodge Wi-Fi.", "friends in sweaters around a fireplace in a wooden mountain lodge at night, snow outside the window, one checking a phone",
  "Cozy lodge, shared network.\n\n" + PRODUCT,
  "Mountains or beach? 👇", True)],
# day 17 – Sun Nov 22
[("Use a password manager.", "a 3D vault with many small keys neatly organized inside",
  "Reusing one password means one leak opens everything.\n\nA password manager creates and remembers a different strong password for every site.",
  "Do you use one? Yes / No / Thinking about it 👇", True),
 ("How many passwords do you reuse?", "a single giant 3D key unlocking a stack of many doors",
  "0 — every one is unique\n1–2\n3+\nDon't ask",
  "Be honest 👇", False),
 ("Sunday night. Couch. Phone. Nothing to prove.", "a woman wrapped in a blanket on a sofa at night, soft TV glow, scrolling her phone",
  "Even lazy Sundays deserve privacy.\n\n" + PRODUCT,
  "What are you watching tonight? 👇", True)],
# day 18 – Mon Nov 23
[("Before you fly: update, download, encrypt.", "a 3D checklist next to a passport and boarding pass, three ticked boxes",
  "✅ Update your phone and apps\n✅ Download maps and tickets for offline use\n✅ Turn on a VPN before using airport Wi-Fi",
  "Flying anywhere this month? 👇", True),
 ("Window or aisle?", "a 3D airplane seat row with one window seat and one aisle seat glowing",
  "And bonus question: do you pay for in-flight Wi-Fi?",
  "Window 🪟 or aisle 🚶? 👇", False),
 ("Gate 42. Delayed. Airport Wi-Fi.", "a stylish woman sitting at an airport gate at night, departure board showing DELAYED, phone in hand",
  "Delays mean scrolling. Scrolling means airport Wi-Fi.\n\n" + PRODUCT,
  "Longest delay you've ever had? 👇", True)],
# day 19 – Tue Nov 24
[("Fake login pages: never enter your email password.", "a 3D Wi-Fi login page asking for EMAIL PASSWORD with a warning sign",
  "A real Wi-Fi login page might ask for a room number or a code. It never needs your email password.\n\nIf it asks, close it.",
  "Ever seen one of these? 👇", True),
 ("Rate the last hotel Wi-Fi you used.", "five big glossy 3D stars, only one and a half lit up, next to a slow loading spinner",
  "⭐ to ⭐⭐⭐⭐⭐\n\nSpeed, reliability, how many times it asked you to log in again…",
  "Your rating + the city 👇", False),
 ("Christmas market. Hot wine. Open network.", "friends at a festive Christmas market at night with lights and wooden stalls, holding warm drinks and a phone",
  "Festive season, crowded networks.\n\n" + PRODUCT,
  "Best Christmas market you've been to? 👇", True)],
# day 20 – Wed Nov 25
[("Mobile data isn't invisible either.", "a cell tower with a small eye icon, and a phone with signal bars",
  "Mobile data is safer than open Wi-Fi, but your carrier can still see which sites you visit.\n\nA VPN works on mobile data too.",
  "Mostly Wi-Fi or mostly mobile data? 👇", True),
 ("Myth or fact: \"Nobody cares about my data.\"", "a 3D shrugging phone character next to a pile of small data cubes",
  "MYTH. Your data is worth money to advertisers and data brokers — that's why so many apps collect it.",
  "Did you think nobody cared? 👇", False),
 ("11 p.m. Ordering food. Saved card on file.", "a man in a dim apartment kitchen at night ordering food on his phone, warm under-cabinet light",
  "Late-night orders, saved payment details, whatever network you're on.\n\n" + PRODUCT,
  "Late-night order of choice? 🍕 🍜 🍔 🥗 👇", True)],
# day 21 – Thu Nov 26
[("Shopping scam check: look at the URL, not the logo.", "a browser address bar with a misspelled shop address highlighted, and a perfect-looking logo beside it",
  "Fake shops copy logos perfectly. The web address is harder to fake.\n\nCheck the spelling of the address before you pay.",
  "Have you ever nearly bought from a fake shop? 👇", True),
 ("What's on your Black Friday list?", "a 3D shopping bag overflowing with small gift boxes and a long list",
  "Headphones? Shoes? Nothing at all?",
  "Tell us 👇", False),
 ("Black Friday week. Shopping street. Mall Wi-Fi.", "shoppers with bags on a festive lit-up shopping street at night, a woman checking prices on her phone",
  "Comparing prices on whatever network the mall gives you?\n\n" + PRODUCT,
  "Shopping in store or online this year? 👇", True)],
# day 22 – Fri Nov 27
[("Shopping on public Wi-Fi: 3 rules.", "three numbered 3D cards: a padlock, a shop address bar, a credit card with a shield",
  "1. Turn on a VPN first.\n2. Type the shop address yourself, don't click ads.\n3. Use a card, not a bank transfer, for new shops.",
  "Which rule do you already follow? 👇", True),
 ("Black Friday deal or Black Friday trick?", "a 3D price tag being flipped, showing a bigger price on the back",
  "Comment the most suspicious \"discount\" you've seen this week.",
  "👇 Worst fake deal wins", False),
 ("No fake discounts. $3.99. Every day.", "a woman in a stylish coat on a city sidewalk at night, holding shopping bags and looking at her phone, neon lights",
  "No countdown timer. No \"was $14.99\". LiteGuard is $3.99/month, cancel anytime, 14-day money-back.\n\nEncrypted connection with one tap. No logs. Android.",
  "Did you buy anything today? 👇", True)],
# day 23 – Sat Nov 28
[("\"Your parcel is waiting\" texts are usually scams.", "a phone with a fake delivery SMS and a 3D parcel with a fishing hook",
  "Delivery scams spike in November. They link to fake pages that ask for a small fee and your card details.\n\nTrack parcels only in the shop's own app or site.",
  "Got one of these this week? 👇", True),
 ("Have you ever received a fake parcel text?", "a 3D phone buzzing with many parcel notification bubbles",
  "Yes / No / Every single day",
  "👇", False),
 ("Cabin weekend. Weak signal. Strong privacy.", "friends in a modern wooden cabin at night with warm lights, forest outside, one looking at a phone",
  "Even off the grid, your phone finds a network.\n\n" + PRODUCT,
  "Your dream weekend escape? 👇", True)],
# day 24 – Sun Nov 29
[("Hide notification content on your lock screen.", "a phone lock screen with blurred notification bubbles and a small shield",
  "Messages and codes on your lock screen can be read by anyone next to you.\n\nSettings → Notifications → Lock screen → hide sensitive content.",
  "Did you change it? ✅ 👇", True),
 ("What % is your battery right now?", "a giant 3D battery icon with a question mark in it",
  "No editing. Look at your phone and comment the number.",
  "👇", False),
 ("Arrivals hall. Sunday night. First thing you do?", "a traveler with a suitcase walking through a modern airport arrivals hall at night, checking her phone",
  "Text home, find a ride, join the airport Wi-Fi.\n\n" + PRODUCT,
  "First thing you do after landing? 👇", True)],
# day 25 – Mon Nov 30
[("Cyber Monday: pay new shops by card.", "a 3D credit card with a shield next to a shopping cart",
  "Cards usually make it easier to dispute a charge than a bank transfer does.\n\nAnd skip shops that only accept transfers or gift cards.",
  "What did you buy this weekend? 👇", True),
 ("Cyber Monday confession:", "a 3D shopping cart overflowing with boxes and a little phone character hiding behind it",
  "What did you buy that you definitely didn't need?",
  "Confess below 👇", False),
 ("Home office. 8 p.m. Still going.", "a man at a stylish home office desk at night, warm lamp, city view, phone and coffee",
  "Your home network deserves the same care as the office one.\n\n" + PRODUCT,
  "What time do you usually stop working? 👇", True)],
# day 26 – Tue Dec 1
[("December travel? Do this before you go.", "a 3D suitcase with a phone, a padlock and a small checklist",
  "Update your phone, back it up, turn on Find My Device, and set up a VPN before the trip — not at the gate.",
  "Travelling in December? Where to? 👇", True),
 ("Where are you spending the holidays?", "a 3D house and a 3D airplane facing each other with a question mark between them",
  "🏠 At home\n✈️ Travelling\n🤔 Still deciding",
  "👇", False),
 ("December. Snow. City lights.", "a couple walking down a snowy old-town street at night with festive lights, one holding a phone",
  "Season of travel, cafés and borrowed Wi-Fi.\n\n" + PRODUCT,
  "Snow: love it or hate it? ❄️ 👇", True)],
# day 27 – Wed Dec 2
[("5-minute app permissions check.", "a 3D phone with app icons and small toggles beside each, a stopwatch showing 5 minutes",
  "Settings → Privacy → Permission manager. Check camera, microphone and location.\n\nRemove access for anything that doesn't need it.",
  "Find any surprises? 👇", True),
 ("Dark mode or light mode?", "a 3D phone split in half diagonally, one half dark with a moon, the other light with a sun",
  "This is a serious question.",
  "🌙 or ☀️? 👇", False),
 ("Night train. Sleeper cabin. Rolling Wi-Fi.", "a woman reading her phone in a cozy night train sleeper cabin, landscape lights passing in the window",
  "Hundreds of kilometres, one shared on-board network.\n\n" + PRODUCT,
  "Ever taken a night train? 👇", True)],
# day 28 – Thu Dec 3
[("Give guests their own Wi-Fi.", "a 3D home router with two separate glowing networks, one labeled GUEST",
  "Most home routers can create a separate guest network. Visitors get internet, but not access to your own devices.",
  "Do you have a guest network at home? 👇", True),
 ("Tag the friend who always asks for your Wi-Fi password 😅", "a 3D phone character holding up a sign reading WI-FI PASSWORD?",
  "Every group has one.",
  "Tag them 👇", False),
 ("Holiday party. 30 guests. One Wi-Fi.", "friends at a stylish apartment holiday party at night, string lights, one person checking a phone by the window",
  "Fun party, crowded network.\n\n" + PRODUCT,
  "First holiday party of the season yet? 👇", True)],
# day 29 – Fri Dec 4
[("Turn on Find My Device before you travel.", "a 3D phone with a location pin and a radar circle",
  "Settings → Security → Find My Device → on. If your phone goes missing, you can locate, lock or wipe it.",
  "Ever lost your phone abroad? 👇", True),
 ("Your best travel hack in one sentence.", "a 3D backpack with a lightbulb popping out of it",
  "Ours: download everything offline before you leave, and turn on the VPN before the first Wi-Fi.",
  "Yours 👇", False),
 ("Friday night by the harbour.", "friends on a harbour promenade at night, boats and city lights reflected on the water, one holding a phone",
  "End the week somewhere nice.\n\n" + PRODUCT,
  "Where are you this Friday? 👇", True)],
# day 30 – Sat Dec 5
[("This month's 5 privacy habits.", "five small 3D icons in a row: a broom, an update arrow, a key vault, a padlock, a location pin",
  "1. Clean saved Wi-Fi networks\n2. Keep apps updated\n3. Use a password manager\n4. Encrypt public Wi-Fi\n5. Check app permissions",
  "Which one will you start with? 👇", True),
 ("Which tip helped you most?", "a 3D trophy with a phone character holding it up",
  "Wi-Fi names, incognito, saved networks, QR codes, password managers… which one changed something for you?",
  "Tell us 👇", False),
 ("Thanks for being here. Your business stays yours.", "a group of stylish friends laughing on a city rooftop at night, skyline and soft teal neon behind them",
  "A month of tips, questions and late-night chats. Thanks for following along.\n\n" + PRODUCT,
  "What should we talk about next month? 👇", True)],
]

start = datetime.date(2026, 11, 6)
SLOTS = {"a": "08:37", "b": "12:37", "c": "20:37"}
posts, prompts = [], []
tipn = 0
for i, day in enumerate(D):
    date = start + datetime.timedelta(days=i)
    for slot, (head, scene, body, cta, link) in zip("abc", day):
        pid = "d%s%s" % (date.strftime("%m%d"), slot)
        if slot == "a":
            tipn += 1
        prompt = STYLE[slot].format(scene=scene, headline=head, n=tipn) + " " + SAFE
        fb = body + "\n\n" + cta
        if link:
            fb += "\n\nGet LiteGuard on Google Play (Android): " + PLAY.format(src="facebook", pid=pid)
        fb += "\n\n" + TAGS[slot]
        ig = body + "\n\n" + cta + "\n\nLiteGuard – no-logs VPN for Android. Link in bio.\n.\n" + TAGS[slot]
        posts.append(dict(id=pid, date=date.isoformat(), slot=slot, time=SLOTS[slot],
                          image_url=RAW.format(pid=pid), facebook_message=fb, instagram_caption=ig))
        prompts.append(dict(id=pid, headline=head, prompt=prompt))

assert len(posts) == 90 and all(len(d) == 3 for d in D)
json.dump(posts, open("schedule.json", "w"), ensure_ascii=False, indent=1)
json.dump(prompts, open("prompts.json", "w"), ensure_ascii=False, indent=1)
print(len(posts), max(len(p["instagram_caption"]) for p in posts))
