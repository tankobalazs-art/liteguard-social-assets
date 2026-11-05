import json

PLAY = ("https://play.google.com/store/apps/details?id=com.liteguard.android&referrer="
        "utm_source%3Dfacebook%26utm_medium%3Dsocial%26utm_campaign%3Dlatenight%26utm_content%3D{pid}")
RAW = "https://raw.githubusercontent.com/tankobalazs-art/liteguard-social-assets/main/{pid}/post.jpg"
TAGS = "#latenight #nightowl #privacy #vpn #android #nologs #yourbusiness"
PRODUCT = "LiteGuard encrypts your connection with one tap. No logs. Android · $3.99/month · 14-day money-back."

# (date, headline, scene, body, cta)
LATE = [
 ("2026-11-06", "Some tabs are just for you.",
  "a young man in a hoodie sitting on the edge of his bed in a dark bedroom, face lit by his phone, a knowing half-smile",
  "Late night. Door closed. Phone on.\n\nWhat you watch is your business — not your Wi-Fi's, not your provider's. Incognito only hides it from your phone; LiteGuard encrypts the connection itself.",
  "Night owls, where you at? 🦉👇"),
 ("2026-11-07", "Your 1 a.m. browsing is nobody's business.",
  "a woman wrapped in a blanket on a sofa in a dark living room at 1 a.m., phone glow on her face, amused expression",
  "1 a.m. thoughts deserve 1 a.m. privacy.\n\nYour internet provider can log every site you open. With a VPN, all they see is encrypted traffic.",
  "What time do you actually put your phone down? Be honest 👇"),
 ("2026-11-13", "Shared Wi-Fi? Your roommates don't need to know what you watch at night.",
  "a young man in a shared-apartment bedroom at night, door slightly ajar with hallway light, scrolling his phone with a grin",
  "Whoever manages the router can see which sites every device on it visits. Roommates, landlords, family — anyone with the admin login.\n\nEncrypt it and the router sees nothing useful.",
  "Who controls the Wi-Fi at your place? 👇"),
 ("2026-11-14", "Incognito hides it from your phone. Not from your Wi-Fi.",
  "a stylish woman curled up in a hotel room armchair at night, city lights through the window, looking at her phone with a mischievous smile",
  "Private mode = no history saved on your device.\nIt does NOT hide which sites you visit from the network or your provider.\n\nThat's what a VPN is for.",
  "Did you know this? 👀 Yes / No"),
 ("2026-11-20", "What happens on your screen stays on your screen.",
  "a man leaning on a city balcony railing late at night, skyline behind, phone glowing in his hand, relaxed smile",
  "Your screen, your choices, your business.\n\n" + PRODUCT,
  "Agree? 👇"),
 ("2026-11-21", "No one needs a list of what you watched last night.",
  "a woman in a dim kitchen late at night leaning on the counter with a glass of water, phone light on her face, playful smile",
  "Your provider keeps logs of the sites you visit. Advertisers would love that list.\n\nWe don't keep one. That's the point.",
  "What's your late-night guilty-pleasure scroll? Keep it PG 😅👇"),
 ("2026-11-27", "Late check-in. Private browsing, actually private.",
  "a man in a smart shirt relaxing on a hotel room sofa late at night, tie loosened, phone glow, knowing smile",
  "Hotel Wi-Fi is shared with every room in the building.\n\n" + PRODUCT,
  "Hotel or Airbnb? 👇"),
 ("2026-11-28", "Your search history: yours. Full stop.",
  "a woman sitting on a wide window seat at night with city lights outside, knees up, scrolling her phone with a sly smile",
  "Not your provider's. Not your Wi-Fi's. Not ours — we don't log it.\n\n" + PRODUCT,
  "What's the weirdest thing you've searched this week? (You don't have to answer 😏)"),
 ("2026-12-04", "Midnight. Lights off. Nobody's watching.",
  "a person lying on a sofa in a dark apartment at midnight, only the phone screen and a teal neon sign from the street lighting the room",
  "The best late-night rule: what you do online is your business.\n\n" + PRODUCT,
  "Who's still up? 🌙👇"),
 ("2026-12-05", "Door closed. Connection closed too.",
  "a young woman sitting on her bedroom floor against the bed at night, fairy lights, phone in hand, content smile",
  "Privacy isn't about hiding something. It's about choosing who gets to see.\n\n" + PRODUCT,
  "Weekend plans: going out or staying in? 👇"),
]

posts = json.load(open("schedule.json"))
posts = [p for p in posts if p.get("slot") != "d"]
for date, head, scene, body, cta in LATE:
    pid = "d" + date[5:7] + date[8:10] + "d"
    fb = body + "\n\n" + cta + "\n\nGet LiteGuard on Google Play (Android): " + PLAY.format(pid=pid) + "\n\n" + TAGS
    ig = body + "\n\n" + cta + "\n\nLiteGuard – no-logs VPN for Android. Link in bio.\n.\n" + TAGS
    posts.append(dict(id=pid, date=date, slot="d", time="23:07", image_url=RAW.format(pid=pid),
                      facebook_message=fb, instagram_caption=ig, headline=head, scene=scene))
# Launch evening 2026-11-05: one of each post type (slot "x", published by one-shot tasks by id)
TONIGHT = [
 ("n1105a", "21:15", "Meet LiteGuard. Your business stays yours.",
  "Hi 👋 We're LiteGuard — a no-logs VPN for Android.\n\nOne tap encrypts your connection on café, hotel, airport and home Wi-Fi. We don't log what you do. $3.99/month, cancel anytime, 14-day money-back.\n\nExpect privacy tips, honest questions and late-night chats here.",
  "What made you stop scrolling? 👇", True, "#liteguard #privacy #vpn #android #nologs #onlineprivacy"),
 ("n1105b", "21:45", "Public Wi-Fi? Turn the VPN on before you log in.",
  "The moment you join a public network, your apps start syncing — email, messages, logins.\n\nSwitch the VPN on first, then connect. Not the other way round.",
  "Which do you do first: Wi-Fi or VPN? 👇", True, "#privacytips #publicwifi #cybersecurity #vpn #android #techtips"),
 ("n1105c", "22:15", "Be honest: how many hours a day on your phone?",
  "A) Under 1 hour\nB) 1–3 hours\nC) 3–5 hours\nD) 5+ hours 😅\n\nCheck Settings → Digital Wellbeing if you dare.",
  "Drop your letter 👇", False, "#screentime #phone #android #privacy #question"),
 ("n1105d", "22:45", "Thursday night. Everyone's on the same Wi-Fi.",
  "Bars, cafés, hotels: one network, a room full of strangers.\n\n" + PRODUCT,
  "Out tonight or staying in? 👇", True, "#nightlife #thursdaynight #privacy #vpn #android #nologs"),
 ("n1105e", "23:15", "Late night. Your tabs. Your business.",
  "Some tabs are nobody else's business — not your Wi-Fi's, not your provider's.\n\nIncognito only hides them from your phone. LiteGuard encrypts the connection itself. No logs.",
  "Night owls, say hi 🦉👇", True, TAGS),
]
posts = [p for p in posts if p.get("slot") != "x"]
for pid, tm, head, body, cta, link, tags in TONIGHT:
    fb = body + "\n\n" + cta
    if link:
        fb += "\n\nGet LiteGuard on Google Play (Android): " + PLAY.replace("latenight", "launch").format(pid=pid)
    fb += "\n\n" + tags
    ig = body + "\n\n" + cta + "\n\nLiteGuard – no-logs VPN for Android. Link in bio.\n.\n" + tags
    posts.append(dict(id=pid, date="2026-11-05", slot="x", time=tm, image_url=RAW.format(pid=pid),
                      facebook_message=fb, instagram_caption=ig, headline=head))
json.dump(posts, open("schedule.json", "w"), ensure_ascii=False, indent=1)
print(len(posts))
