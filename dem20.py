import math
import random
import csv
import textwrap
import time
import subprocess
import sys
import json

try:
    from wcwidth import wcswidth
except ImportError:
    print("📦 Installing required package: wcwidth...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "wcwidth"])
    from wcwidth import wcswidth
try:
    import emoji
except ImportError:
    import subprocess
    import sys

    print("📦 Installing 'emoji' module...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "emoji"])

    import emoji
import os

def filepath(filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
def pad(text, width):
    return text + " " * max(0, width - wcswidth(text))
def removeemoji(text):
    return emoji.replace_emoji(str(text), replace="").strip()

def align_left(text, width):
    text = str(text)
    return text + " " * max(0, width - wcswidth(text))


def align_right(text, width):
    text = str(text)
    return " " * max(0, width - wcswidth(text)) + text


def align_center(text, width):
    text = str(text)
    total = max(0, width - wcswidth(text))
    left = total // 2
    right = total - left
    return " " * left + text + " " * right
class movie:
    def __init__(self, system=None, name="Chutiyapa",house="Chudi", genre="", hype=0, castcrew=0, budget=0, city="Unknown", Leadactress=""):
        self.name = name
        self.system = system
        self.house = house
        self.city = city
        self.hype = hype
        self.budget = budget
        self.castcrew = castcrew
        self.genre = genre
        self.origincity = "la"
        self.lead=Leadactress

        self.releasedla = "False"
        self.releasedmm = "False"
        self.releasedlv = "False"

        self.audience = 0
        self.critics = 0

        self.revenue = 0
        self.profit = 0

        self.awards = 0
        self.status = "Not Released"
        if self.system is None:
            pass
        elif self.system.city=="la":
            self.distributioncost=math.floor(self.budget*0.15)
        elif self.system.city=="mm":
            self.distributioncost=math.floor(self.budget*0.12)
        elif self.system.city=="lv":
            self.distributioncost=math.floor(self.budget*0.2)
            import csv

    def movupdate(self):

        movies = []

        # ─────────────────────────────
        # READ ALL MOVIES
        # ─────────────────────────────
        try:
            with open(filepath("movies.csv"), "r", newline="", encoding="utf-8") as file:

                reader = csv.DictReader(file)
                fields = reader.fieldnames
                found = False
                for row in reader:

                    if row["Name"] == self.name:
                        found = True

                        row["Genre"] = self.genre
                        row["Hype"] = str(self.hype)
                        row["Budget"] = str(self.budget)
                        row["MovieHouse"] = self.house
                        row["LeadActress"] = self.lead
                        row["OriginCity"] = self.origincity

                        row["ReleasedLA"] = self.releasedla
                        row["ReleasedMM"] = self.releasedmm
                        row["ReleasedLV"] = self.releasedlv

                        row["AudienceScore"] = str(self.audience)
                        row["CriticScore"] = str(self.critics)

                        row["TotalRevenue"] = str(self.revenue)
                        row["NetProfit"] = str(self.profit)

                        row["AwardWins"] = str(self.awards)
                        row["Status"] = self.status

                    movies.append(row)
                if not found:
                    movies.append({
                        "MovieID": len(movies) + 1,
                        "Name": self.name,
                        "Genre": self.genre,
                        "Hype": self.hype,
                        "Budget": self.budget,
                        "MovieHouse": self.house,
                        "LeadActress": self.lead,
                        "OriginCity": self.origincity,
                        "ReleasedLA": (self.releasedla),
                        "ReleasedMM": (self.releasedmm),
                        "ReleasedLV": (self.releasedlv),
                        "AudienceScore": self.audience,
                        "CriticScore": self.critics,
                        "TotalRevenue": self.revenue,
                        "NetProfit": self.profit,
                        "AwardWins": self.awards,
                        "Status": self.status
                    })
            # ─────────────────────────────
            # REWRITE CSV
            # ─────────────────────────────

            with open(filepath("movies.csv"), "w", newline="", encoding="utf-8") as file:

                writer = csv.DictWriter(file, fieldnames=fields)

                writer.writeheader()

                for movie in movies:
                    writer.writerow(movie)

            # ─────────────────────────────
            # RELOAD THIS MOVIE
            # ─────────────────────────────

            with open(filepath("movies.csv"), "r", newline="", encoding="utf-8") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    if row["Name"] == self.name:

                        self.genre = row["Genre"]
                        self.hype = int(row["Hype"])
                        self.budget = int(math.floor(float(row["Budget"])))

                        self.house = row["MovieHouse"]
                        self.lead=row["LeadActress"]
                        self.origincity = row["OriginCity"]

                        self.releasedla = (row["ReleasedLA"]) 
                        self.releasedmm = (row["ReleasedMM"]) 
                        self.releasedlv = (row["ReleasedLV"])

                        self.audience = int(math.floor(float(row["AudienceScore"])))
                        self.critics = int(math.floor(float(row["CriticScore"])))

                        self.revenue = int(math.floor(float(row["TotalRevenue"])))
                        self.profit = int(math.floor(float(row["NetProfit"])))

                        self.awards = int(math.floor(float(row["AwardWins"])))
                        self.status = row["Status"]

                        break
        except FileNotFoundError:
            with open(filepath("movies.csv"), "w", newline="", encoding="utf-8") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "MovieID",
                    "Name",
                    "Genre",
                    "Hype",
                    "Budget",
                    "MovieHouse",
                    "LeadActress",
                    "OriginCity",
                    "ReleasedLA",
                    "ReleasedMM",
                    "ReleasedLV",
                    "AudienceScore",
                    "CriticScore",
                    "TotalRevenue",
                    "NetProfit",
                    "AwardWins",
                    "Status"
                ])

                writer.writerow([
                    1,
                    self.name,
                    self.genre,
                    self.hype,
                    self.budget,
                    self.house,
                    self.lead,
                    self.origincity,
                    (self.releasedla),
                    (self.releasedmm),
                    (self.releasedlv),
                    self.audience,
                    self.critics,
                    self.revenue,
                    self.profit,
                    self.awards,
                    self.status
                ])
    def setgenre(self, genre):
        genre = genre.strip().lower().capitalize()

        genres = {
            "Action": "💥",
            "Romance": "💖",
            "Drama": "🎭",
            "Comedy": "😂",
            "Thriller": "🔪",
            "Horror": "👻",
            "Sci-fi": "🚀",
            "Fantasy": "🐉",
            "Porn": "🍑",
            "Rom-com": "💘"

        }

        if genre not in genres:
            raise ValueError(
                f"Invalid genre '{genre}'. "
                f"Valid genres are: {', '.join(genres.keys())}"
            )

        self.genre = genre
        self.genreemoji = genres[genre]

    def output(self, enumeration=0):
        genres = {
            "Action": "💥",
            "Romance": "💖",
            "Drama": "🎭",
            "Comedy": "😂",
            "Thriller": "🔪",
            "Horror": "👻",
            "Sci-fi": "🚀",
            "Fantasy": "🐉",
            "Porn": "🍑",
            "Rom-com": "💘"

        }
        emoji = genres.get(self.genre)

        INSIDE = 74          # Width between the two ║'s
        DIVIDER = ""

        # ---------------- Line 1 ----------------

        line1 = f"[{enumeration}] 🎬 {self.name}    by    {self.house}"

        # ---------------- Line 2 ----------------

        left2 = f"{emoji} {self.genre}        🔥 Hype: {self.hype}/100"
        right2 = "Starting From"

        # ---------------- Line 3 ----------------

        left3 = f"🫦  Actresses Required: {self.castcrew}"
        right3 = f"💰 ${self.budget:,}"

        # Widths of both columns
        LEFT_WIDTH = 47
        RIGHT_WIDTH = INSIDE - LEFT_WIDTH - 1      # -1 for │

        print(
            "╔" + "═"*INSIDE + "╗"
        )

        print(
            f"║ {pad(line1, INSIDE-2)} ║"
        )

        print(
            f"║ {pad(left2, LEFT_WIDTH)}{DIVIDER}{pad(right2, RIGHT_WIDTH)}║"
        )

        print(
            f"║ {pad(left3, LEFT_WIDTH)}{DIVIDER}{pad(right3, RIGHT_WIDTH)} ║"
        )

        print(
            "╚" + "═"*INSIDE + "╝"
        )
    def market(self,tier):
        moviehouses = {
    1: [
        "Hollywood House of Graphics",
        "Starlight Boulevard"
    ],

    2: [
        "Vixen Velour",
        "Northstar Hall of Glamour",
        "South Beach Bikini Studios",
        "Flamecrest Productions"
    ],

    3: [
        "Sin City Pictures",
        "Diamond of Cards",
        "Sampson, Sons & Co.",
        "Sunset Avenue",
        "Neon Mirage",
        "Golden Palms"
    ]
}
        if tier not in (1, 2, 3):
            raise ValueError("Movie tier must be 1, 2 or 3.")

        with open("D:\\py things\\python  dem\\flirt.json", "r", encoding="utf-8") as f:
            data = json.load(f)

            genres = [
                "Action",
                "Romance",
                "Drama",
                "Comedy",
                "Thriller",
                "Horror",
                "Sci-fi",
                "Fantasy",
                "Porn",
                "Rom-com"

            ]

            self.setgenre(random.choice(genres))

            self.name = random.choice(data["moviename"][self.genre])

            self.house = random.choice(moviehouses[tier])

            if tier == 1:
                self.hype = random.randint(82, 100)
                self.castcrew = random.randint(4, 5)
                self.budget = random.randint(220000, 350000)//1000*1000

            elif tier == 2:
                self.hype = random.randint(58, 84)
                self.castcrew = random.randint(3, 4)
                self.budget = random.randint(120000, 220000)//1000*1000

            else:
                self.hype = random.randint(30, 60)
                self.castcrew = random.randint(2, 3)
                self.budget = random.randint(50000, 120000)//1000*1000
        if self.system.city=="la":
            self.distributioncost=math.floor(self.budget*0.15)
        elif self.system.city=="mm":
            self.distributioncost=math.floor(self.budget*0.12)
        elif self.system.city=="lv":
            self.distributioncost=math.floor(self.budget*0.2)
    def proceed(self,system=None):
        allgirls=system.girls
        actresslist=system.checkgirl(intent="actress")
        selectedactresses=system.listgirlsmult(actresslist,"cast",limit=self.castcrew)
        print(selectedactresses==None)
        if selectedactresses==None:
            return
        k=self.separate(selectedactresses)
        self.finalcontract(k[0],k[1])
    def separate(self, girls):
        girls.sort(key=lambda girl: girl.effectivelevel, reverse=True)
        index=-1
        for girl in girls:
            if girl.level >=30:
                continue
            if index==-1:
                index=girls.index(girl)
            elif girl.level==girls[index].level:
                if girl.cup>girls[index].cup:
                    index=girls.index(girl)
        lead=girls[index]
        girls.remove(lead)
        return [lead, girls]



            

    def finalcontract(self, lead, support):

        WIDTH = 74
        self.lead=lead.name
        print("╔" + "═"*WIDTH + "╗")
        print(f"║{align_left('🎬 FINAL PRODUCTION APPROVAL 🎬'.center(WIDTH-2), WIDTH-2)}║")
        print("╠" + "═"*WIDTH + "╣")
        if self.system.city=="la":
            city="Los Angeles"
        elif self.system.city=="mm":
            city="Miami"
        elif self.system.city=="lv":
            city="Las Vegas"

        print(f"║ {pad(f'🎬 {self.name} by {self.house}', WIDTH-2)} ║")
        print(f"║ {pad(f'{self.genreemoji} {self.genre}',20)}"
            f"{pad(f'🔥 Hype: {self.hype}/100',22)}"
            f"{pad(f'🌴 Premieres In: {city.upper()}',30)} ║")

        print("╠" + "═"*WIDTH + "╣")

        # ---------------- LEAD ----------------

        print(f"║ {pad('⭐ LEAD ACTRESS', WIDTH-2)} ║")

        leadcost = lead.defaultrate * 10
        
        print(
            f"║    {pad(lead.flag + ' ' + lead.name,45)}"
            f"{align_right(f'💰 ${leadcost:,}',25)}║"
        )

        print("╠" + "═"*WIDTH + "╣")

        # ---------------- SUPPORT ----------------

        print(f"║ {pad('🎭 SUPPORTING ACTRESSES', WIDTH-2)} ║")

        for girl in support:

            cost = girl.defaultrate * 3

            print(
                f"║    {pad(girl.flag + ' ' + girl.name,45)}"
                f"{align_right(f'💰 ${cost:,}',25)}║"
            )

        print("╠" + "═"*WIDTH + "╣")

        salary = leadcost + sum(g.defaultrate * 3 for g in support)

        total = self.budget + salary + self.distributioncost

        print(
            f"║ {pad('💰 Opening Bid',22)}│"
            f"{align_right(f'${self.budget:,}',50)}║"
        )

        print(
            f"║ {pad('👠 Actress Salaries',22)}│"
            f"{align_right(f'${salary:,}',50)}║"
        )

        print(
            f"║ {pad('📦 Distribution Fee',22)}│"
            f"{align_right(f'${self.distributioncost:,}',50)}║"
        )

        print(
            f"║ {'─'*22}┼{'─'*50}║"
        )

        print(
            f"║ {pad('💵 TOTAL INVESTMENT',22)}│"
            f"{align_right(f'${total:,}',50)}║"
        )

        print("╠" + "═"*WIDTH + "╣")

        footer = (
            "[1] ✅ Sign Contract"
            "    │    "
            "[2] 🔄 Recast"
            "    │    "
            "[3] ❌ Withdraw"
        )

        print(f"║ {pad(footer, WIDTH-2)} ║")

        print("╚" + "═"*WIDTH + "╝")
        while True:

            try:
                choice = int(input("\nChoose ► "))
            except:
                print("❌ That's not a valid option.")
                continue

            # ───────────────────────────────────────────────
            # SIGN CONTRACT
            # ───────────────────────────────────────────────

            if choice == 1:

                total = (
                    self.budget
                    + self.distributioncost
                    + lead.defaultrate * 10
                    + sum(g.defaultrate * 3 for g in support)
                )

                if self.system.coin < total:

                    print(f"""
══════════════════════════════════════════════════════════════════════════════

💸 Oops... Hollywood isn't accepting Monopoly money.

💰 Needed : ${total:,}
🪙 You Have : ${self.system.coin:,}

❌ Earn some cash and come back, boss.

══════════════════════════════════════════════════════════════════════════════
""")
                    return False

                self.system.coin -= total
                # self.system.update()

                print(f"""
══════════════════════════════════════════════════════════════════════════════

🎬 ✅ CONTRACT LOCKED IN!

💸 ${total:,} invested.
🍿 Cameras are rolling...
🌟 Cast confirmed.
🔥 Time to make Hollywood proud!

══════════════════════════════════════════════════════════════════════════════
        """)

                time.sleep(2)
                                # ──────────────────────────────────────────────────────────────
                # 🎬 PREMIERE IN HOME CITY
                # ──────────────────────────────────────────────────────────────

                print(f"""
══════════════════════════════════════════════════════════════════════════════
                🍿✨ PREMIERE NIGHT ✨🍿
══════════════════════════════════════════════════════════════════════════════

🎬 {self.name} is now premiering in {self.system.city.upper()}!

🍿 The audience has filled every seat...
📰 Critics are publishing their first reviews...
💰 Box office numbers are coming in...

══════════════════════════════════════════════════════════════════════════════
""")

                time.sleep(3)

                hit = random.choices(
                    [True, False],
                    weights=[self.hype * 2, 200 - self.hype],
                    k=1
                )[0]

                if hit:

                    percent = random.randint(self.hype, self.hype * 2)

                    revenue = total + total * percent // 100

                    self.revenue += revenue
                    self.profit += revenue - total
                    if lead.level < 27:
                        lead.level += 3
                    else:
                        lead.level = 30

                    if self.system.city == "la":
                        self.releasedla = "True"
                    elif self.system.city == "mm":
                        self.releasedmm = "True"
                    else:
                        self.releasedlv = "True"

                    self.status = "Released"
                    self.system.coin += revenue
                    

                    print(f"""
══════════════════════════════════════════════════════════════════════════════
                    🌟 BOX OFFICE HIT! 🌟
══════════════════════════════════════════════════════════════════════════════

🎬 {self.name} has become a massive success!

📈 Return on Investment : +{percent}%
💵 Box Office Revenue   : ${revenue:,}
💰 Net Profit           : ${self.profit:,}

🌟 {self.lead} is becoming a household name!

══════════════════════════════════════════════════════════════════════════════
""")
                    self.budget=total
                    time.sleep(2)
                    self.movupdate()
                    return True

                else:

                    percent = random.randint(0, 100 - self.hype)

                    revenue = total - total * percent // 100

                    self.revenue += revenue
                    self.profit += revenue - total
                    self.system.coin += revenue

                    if self.system.city == "la":
                        self.releasedla = "True"
                    elif self.system.city == "mm":
                        self.releasedmm = "True"
                    else:
                        self.releasedlv = "True"

                    self.status = "Released"

                    print(f"""
══════════════════════════════════════════════════════════════════════════════
                    💀 BOX OFFICE FLOP 💀
══════════════════════════════════════════════════════════════════════════════

🎬 {self.name} failed to impress audiences...

📉 Loss : -{percent}%
💵 Box Office Revenue : ${revenue:,}
💸 Net Profit         : ${self.profit:,}

😬 Better luck with your next production.

══════════════════════════════════════════════════════════════════════════════
""")
                   

                time.sleep(2)
                

                # self.production(lead, support)
                self.budget=total
                self.movupdate()
                return True

            # ───────────────────────────────────────────────
            # RECAST
            # ───────────────────────────────────────────────

            elif choice == 2:

                print("""
══════════════════════════════════════════════════════════════════════════════

🎭 "Nah... we can do better."

🔄 Reopening auditions...
🌟 Hunting for a stronger cast.

══════════════════════════════════════════════════════════════════════════════
        """)

                time.sleep(1)

                self.proceed(self.system)
                return False

            # ───────────────────────────────────────────────
            # WITHDRAW
            # ───────────────────────────────────────────────

            elif choice == 3:

                print("""
══════════════════════════════════════════════════════════════════════════════

🚪 Production cancelled.

📄 Contracts shredded.
🍿 Crew dismissed.
🎬 Maybe the next script will be the blockbuster.

══════════════════════════════════════════════════════════════════════════════
        """)

                time.sleep(1)

                return False

            else:
                print("❌ Choose 1, 2 or 3.")
    def rerelease(self,system,city):
        self.system=system
        if city=="la":
            cityx = "ReleasedLA"
            cityname = "Los Angeles"
            
            percent = 15
        elif city=="mm":
            cityx = "ReleasedMM"
            cityname = "Miami"
            
            percent = 12
        elif city=="lv":
            self.releasedlv="False"
            cityx = "ReleasedLV"
            cityname = "Las Vegas"
            
            percent = 20
        else:
            print("invalid city")
            return
        
        cost = self.budget * percent // 100

        if self.system.coin < cost:

            print(f"""══════════════════════════════════════════════════════════════════════════════

❌ You don't have enough cash to distribute this movie.

💵 Distribution Cost : ${cost:,}
🪙 Available Cash    : ${self.system.coin:,}

══════════════════════════════════════════════════════════════════════════════""")

            return

        self.system.coin -= cost

        origin = self.origincity

        base = {
            "la":15,
            "mm":12,
            "lv":20
        }

        effectivehype = round(
            int(self.hype) /
            base[origin]
            * percent
        )

        effectivehype = max(1, min(100, effectivehype))
        hit = random.choices(
        [True, False],
        weights=[
            effectivehype * 2,
            200 - effectivehype
        ],
        k=1
        )[0]
        budget = self.budget
        print(f"""
══════════════════════════════════════════════════════════════════════════════
                        🍿✨ PREMIERE NIGHT ✨🍿
══════════════════════════════════════════════════════════════════════════════

🎬 {self.name} is now premiering in {cityname}!

🍿 The audience has filled every seat...
📰 Critics are publishing their first reviews...
💰 Box office numbers are coming in...

══════════════════════════════════════════════════════════════════════════════
""")
        time.sleep(2)

        if hit:

            roi = random.randint(
                effectivehype*2,
                effectivehype*3
            )

            revenue = budget + budget*roi//100
            self.system.coin += revenue


            print(f"""
══════════════════════════════════════════════════════════════════════════════
                    🌟 MASSIVE BOX OFFICE HIT! 🌟
══════════════════════════════════════════════════════════════════════════════

🎬 {self.name} has become a massive success!

📈 Return on Investment : +{percent}%
💵 Box Office Revenue   : ${revenue:,}
💰 Net Profit           : ${self.profit:,}

🌟 {self.lead} is becoming a household name!

══════════════════════════════════════════════════════════════════════════════
""")

        else:

            loss = random.randint(
                100-effectivehype,
                min(200,(100-effectivehype)*2)
            )

            revenue = max(
                0,
                budget-budget*loss//100
            )
            self.system.coin += revenue

            print(f"""
══════════════════════════════════════════════════════════════════════════════
                    💀 MASSIVE BOX OFFICE FLOP 💀
══════════════════════════════════════════════════════════════════════════════

🎬 {self.name} failed to impress audiences...

📉 Loss : -{percent}%
💵 Box Office Revenue : ${revenue:,}
💸 Net Profit         : ${self.profit:,}

😬 Better luck with your next production.

══════════════════════════════════════════════════════════════════════════════
""")
            self.revenue = self.revenue + revenue
        

        self.profit= self.profit + revenue - cost
        

        self.status = "Released"

        if city == "la":
            self.releasedla = "True"

        elif city == "mm":
            self.releasedmm = "True"

        else:
            self.releasedlv = "True"
        self.movupdate()
        print("Press Enter to continue...")
        input()
        time.sleep(1)
        return

class girl:
    def __init__(self,name,level=6,defaultrate=1000,boost=None,preg=False,jail=False,city="la",cup="A",guard=None,bodycount=0,past="clean",trust=0,mood="neutral",persona1="normal",persona2="normal",nation="white",age=18): 
        self.name=name
        self.level=level
        self.boost = None if boost in ("", "None", None) else boost
        self.preg=preg
        self.jail=jail
        self.defaultrate=defaultrate
        self.rate=self.getrate()
        self.city=city
        self.cup=cup
        self.guard = None if guard in ("", "None", None) else guard
        self.past=past
        self.trust=trust
        self.mood=mood
        self.persona1=persona1
        self.persona2=persona2
        self.nation=nation
        self.age=age
        self.bodycount=bodycount
        self.flag="error"
        self.setflag()
        self.getboost()
       
    def classify(self):
        m=[self.name,self.level,self.boost,self.preg,self.jail,self.city,self.cup,self.guard,self.bodycount,self.past,self.trust,self.mood,self.persona1,self.persona2,self.nation,self.age]
        return m
    

    def setflag(self):

        flags = {
            "White": [
                "🇺🇸",
                "🇬🇧",
                "🇷🇺",
                "🇮🇹"
            ],

            "Asian": [
                "🇨🇳",
                "🇯🇵",
                "🇰🇷",
                "🇹🇭"
            ],

            "Latina": [
                "🇧🇷",
                "🇪🇸",
                "🇨🇺",
                "🇲🇽"
            ]
        }

        if self.nation not in flags:
            raise ValueError(f"Invalid nation '{self.nation}'")

        self.flag = random.choice(flags[self.nation])
    def setdefaultrate(self,defaultrate):
        self.defaultrate=defaultrate
    def upgradecupsize(self):
        cup_sizes = ["A", "B", "C", "D", "DD","DDD", "E", "F", "G"]
        current_index = cup_sizes.index(self.cup)
        if current_index < len(cup_sizes) - 1:
            self.cup = cup_sizes[current_index + 1]
            print(f"{self.name}'s cup size has been upgraded to {self.cup}.")
            return True
        else:
            print(f"{self.name} already has the maximum cup size.")
            return False 
    def getcupsize(self):
        return self.cup
    def transfer(self,city):
        if city in ["la","mm","lv"]:
            self.city=city
        else:
            print("invalid city")
    def getrate(self,level=None):
        if level==None:
            level=self.level

        return math.floor(self.defaultrate*level/6)
    def getboost(self):
        #here we enter data according to the data input inside the method def getrux and accordingly fill the levels
        if self.boost=="laitem1":
            self.effectivelevel=self.level+2
        elif self.boost=="laitem2" and self.city=="la":
            self.effectivelevel=self.level+5
        elif self.boost=="laitem3":
            if self.city=="la":
                self.effectivelevel=self.level+7
            else:
                self.effectivelevel=self.level+5
        elif self.boost=="laitem4" and self.city=="la":
            self.effectivelevel=self.level+4
        elif self.boost=="laitem5":
            if self.city=="la":
                self.effectivelevel=self.level+20
            else:
                self.effectivelevel=self.level+15
        elif self.boost=="mmitem1" and self.city=="mm":
            self.effectivelevel=self.level+5
        elif self.boost=="mmitem2":
            if self.city=="mm":
                self.effectivelevel=self.level+8
            else:
                self.effectivelevel=self.level+5
        elif self.boost=="mmitem3" and self.city=="mm":
            self.effectivelevel=self.level+3
        elif self.boost=="mmitem4" and self.city=="mm":
            self.effectivelevel=self.level+5
        elif self.boost=="mmitem5":
            if self.city=="mm":
                self.effectivelevel=self.level+20
            else:
                self.effectivelevel=self.level+15
        elif self.boost=="lvitem1":
            if self.city=="lv":
                self.effectivelevel=self.level+8
            else:
                self.effectivelevel=self.level+5
        elif self.boost=="lvitem2" and self.city=="lv":
            self.effectivelevel=self.level+10
        elif self.boost=="lvitem3":
            if self.city=="lv":
                self.effectivelevel=self.level+12
            else:
                self.effectivelevel=self.level+7
        elif self.boost=="lvitem4" and self.city=="lv":
            self.effectivelevel=self.level+6
        elif self.boost=="lvitem5":
            if self.city=="lv":
                self.effectivelevel=self.level+25
            else:
                self.effectivelevel=self.level+18
        else:
            self.effectivelevel=self.level
            


    def setboost(self,boost=None):
        
        
            
        if boost=="laitem1":
            self.boost="laitem1"
        elif boost=="laitem2":
            self.boost="laitem2"
        elif boost=="laitem3":
            self.boost="laitem3"
        elif boost=="laitem4":
            self.boost="laitem4"
        elif boost=="laitem5":
            self.boost="laitem5"
        elif boost=="mmitem1":
            self.boost="mmitem1"
        elif boost=="mmitem2":
            self.boost="mmitem2"
        elif boost=="mmitem3":
            self.boost="mmitem3"
        elif boost=="mmitem4":
            self.boost="mmitem4"
        elif boost=="mmitem5":
            self.boost="mmitem5"
        elif boost=="lvitem1":
            self.boost="lvitem1"
        elif boost=="lvitem2":
            self.boost="lvitem2"
        elif boost=="lvitem3":
            self.boost="lvitem3"
        elif boost=="lvitem4":
            self.boost="lvitem4"
        elif boost=="lvitem5":
            self.boost="lvitem5"
        self.getboost()
    def setguard(self,guard):
        if guard=="ess1":
            self.guard="ess1"
        elif guard=="ess2":
            self.guard="ess2"
        elif guard=="ess3":
            self.guard="ess3"
        elif guard=="ess4":
            self.guard="ess4"
        elif guard=="ess5":
            if self.preg==True:
                self.preg=False
                self.guard=None
            else:
                print(f"{self.name} is not pregnant, cannot use this item")
                return False
    def glowup(self,glowup):
        if self.guard=="ess4":
            print(f"{self.name} is a mother now and cannot be glowuped anymore")
            return False
        elif glowup=="labeauty1" or glowup=="mmbeauty1" or glowup=="lvbeauty1":
            x=self.upgradecupsize()
            return x
        elif glowup=="labeauty2" or glowup=="mmbeauty2" or glowup=="lvbeauty2":
            if self.level<27:
                self.level+=4
                self.getboost()
                return True
            elif 27<=self.level<30:
                self.level=30
                self.getboost()
                return True
            return False
            
            
        elif glowup=="labeauty3" or glowup=="mmbeauty3" or glowup=="lvbeauty3":
            y=False
            if self.level<27:
                self.level+=4
                self.getboost()
                y=True
            elif 27<=self.level<30:
                self.level=30
                self.getboost()
                y=True
            x=self.upgradecupsize()
            return x or y
    def abort(self):
        if self.preg==True:
            self.preg=False
            print(f"🖤 Congratulations, {self.name}! The streets called... and you answered. 🎀") 
        else:
            print(f"{self.name} is not pregnant, cannot abort")
            return False
    def deliver(self):
        if self.preg==True:
            self.preg=False
            self.guard="ess4"
            print(f"🩷 New beginnings, tiny footsteps, endless memories. Congratulations, {self.name}! 👶🎀")
        else:
            print(f"{self.name} is not pregnant, cannot deliver")
            return False  

    

            
    def concent(self,cut,action=None):

        if cut> 80 :
            return False
        elif 80>=cut>20:
            if action==None:
                b=random.choices([True,False],weights=[max(self.trust-(cut-20)//2,5),max(self.effectivelevel+(cut-20)//2,5)],k=1)[0]
                return b
            elif action=="photo":
                b=random.choices([True,False],weights=[max(self.trust+self.effectivelevel,5),max((cut-20)*3//2,5)],k=1)[0]
                return b
        else:
            return True


    def getorgasm(self,client=None):
        a=client.getstandard()
        b=self.effectivelevel
        c={"A":4,"B":5,"C":6,"D":7,"DD":9,"DDD":10,"E":12,"F":13,"G":15}
        d=c.get(self.cup)
        jump=random.choices([True,False],weights=[b+2*d,math.floor(a*4.5)],k=1)[0]
        finallyrating=random.choices([1,2,3,4,5],weights=[a*4,a*2+d*2,a*2+b+d,a+b+3*d,max(b+2*d-a*2,5)],k=1)[0]
        return [jump,finallyrating]
    def getfun(self,avgstand):
        if avgstand<6:
            return random.choices([True,False],weights=[self.effectivelevel,avgstand],k=1)[0]
        else:
            return random.choices([True,False],weights=[self.effectivelevel,avgstand*3],k=1)[0]
    def photo(self,cut=20,system=None):
        if not self.concent(cut,"photo"):
                rejection_statements = [
                "No way… you’re asking for way too much cut. My trust in you is gone 💔🖤😠",
                "I’m done with this. That cut is too greedy… I can’t trust you anymore 💔🖤😤",
                "Absolutely not. You’re taking too big a share. Trust broken between us 💔🖤😠",
                "I trusted you but this cut is ridiculous. I’m walking away 💔🖤😡",
                "Hell no. You want too much… my faith in you just shattered 💔🖤😠"]
                print(f"🎀 {self.name} : {random.choice(rejection_statements)}")
                self.trust=max(0,self.trust-5)
                system.update()
                return
        rate=(self.defaultrate//6*self.effectivelevel)*cut//100
        additionalbonus=""
        if self.boost=="laitem2" and self.city=="la":
            additionalbonus="💖 +50% Shoot earnings from Starlight Gown 💖"
            rate=math.floor(rate*1.5)
        elif self.boost=="mmitem1" and self.city=="mm":
            additionalbonus="💖 +50% Shoot earnings from South Beach Bikini 💖"
            rate=math.floor(rate*1.5)
        elif self.boost=="lvitem2" and self.city=="lv":
            additionalbonus="💖 +50% Shoot earnings from Diamond Diva Dress 💖"
            rate=math.floor(rate*1.5)
        elif self.boost=="laitem1" and self.city=="la":
            additionalbonus="💖 +20% Shoot earnings from Scarlet Kiss Lipstick 💖"
            rate=math.floor(rate*1.2)
        elif self.boost=="mmitem3" and self.city=="mm":
            additionalbonus="💖 +40% Shoot earnings from Ocean Temptress Shades 💖"
            rate=math.floor(rate*1.4)

        print(f"💖 {self.name} took some amazing photos for you! 💖")
        with open("D:\\py things\\python  dem\\flirt.json", "r", encoding="utf-8") as file:
            dial = json.load(file)
            dialogue = dial.get("shoottext")
            for rev in dialogue:
                if self.cup in rev["cup_group"] and self.effectivelevel < int(rev["beauty_level"]) and self.nation==rev["nation"]:
                    reviewtext=rev["replies"]
        for review in reviewtext:
            print(f"🎀 {self.name} : {review}")
            time.sleep(0.2)
            print("📷",end="")
            time.sleep(2.5)
            print("📸✨",end="\n")
           
            
            
        print(f"""
══════════════════════════════════════════════════════════════════════════════

🌟 The campaign was a complete success.
{additionalbonus}
📸 {self.name} stole the spotlight, earning widespread praise
and bringing greater recognition to your agency.

══════════════════════════════════════════════════════════════════════════════
""")   
        print("✅ you recieved your cut of $",rate)
        system.coin+=rate
        if self.city=="la":
            system.clients[1].updatetrust(5)
        elif self.city=="mm":
            system.clients[6].updatetrust(5)
        # elif self.city=="lv":
        #     system.clients[11].updatetrust(5)
        system.update()
        time.sleep(0.55)
        return
    def strip(self,clients=None,number=100,cut=20,system=None): 
        girltext=""
        reviewtext=""
        rate=(self.defaultrate//6*self.effectivelevel)*number*cut//100
        if not self.concent(cut):
                rejection_statements = [
                "No way… you’re asking for way too much cut. My trust in you is gone 💔🖤😠",
                "I’m done with this. That cut is too greedy… I can’t trust you anymore 💔🖤😤",
                "Absolutely not. You’re taking too big a share. Trust broken between us 💔🖤😠",
                "I trusted you but this cut is ridiculous. I’m walking away 💔🖤😡",
                "Hell no. You want too much… my faith in you just shattered 💔🖤😠"]
                print(f"🎀 {self.name} : {random.choice(rejection_statements)}")
                self.trust=max(0,self.trust-5)
                system.update()
                return
        with open("D:\\py things\\python  dem\\flirt.json", "r", encoding="utf-8") as file:
            dial = json.load(file)
            dialogue = dial.get("striptext")
            for scriptlist in dialogue:
                if scriptlist["nation"] == self.nation and scriptlist["persona1"] == self.persona1:
                    girltext = scriptlist["replies"]
                    break
        titles = [
            "🖤 Velvet Nights ✨ | The Spotlight Awaits ✨ 🧡",
            "🖤 Lights Down, Hearts Racing ✨ | Show Time Begins ✨ 🧡",
            "🖤 Welcome to Tonight's Main Attraction ✨ | Let the Stage Ignite ✨ 🧡",
            "🖤 Neon Dreams ✨ | The Crowd Is Ready ✨ 🧡",
            "🖤 Center Stage ✨ | An Unforgettable Performance Begins ✨ 🧡"
                    ]
        with open("D:\\py things\\python  dem\\flirt.json", "r", encoding="utf-8") as file:
            dial = json.load(file)
            dialogue = dial.get("stripreview")
            for rev in dialogue:
                if self.cup in rev["cup_group"] and self.effectivelevel < int(rev["beauty_level"]) and self.nation==rev["nation"]:
                    reviewtext=rev["reviews"]

        finaltitle = random.choice(titles)

        print("══════════════════════════════════════════════════════════════════════════════")
        print(f"{finaltitle:^78}")
        print("══════════════════════════════════════════════════════════════════════════════")
        print(f"💖 {self.name} is ready to perform for you 💖")
        time.sleep(2)
        print(f"🎀 {self.name} : {random.choice(girltext)}")
        time.sleep(2.5)
        avgstand=0
        gglist=random.sample(reviewtext, len(clients))
        i=0
        for client in clients:
            print(f"👤 {client.name} : {gglist[i].replace('{self.name}', self.name)}")
            avgstand+=client.getstandard()
            i+=1
            time.sleep(0.7)
        avgstand//=len(clients)
        print("══════════════════════════════════════════════════════════════════════════════")

        if self.getfun(avgstand):
            print(f"💖 {self.name} had an amazing time performing for you all! 💖 Her trust on you has increased from the excitement~")
            self.trust=self.trust+3 if self.trust<97 else 100
        else:
            print(f"💔 {self.name} didn't enjoy the performance as much as she hoped... 💔 Her trust on you has decreased from the disappointment 🖤")
            
            self.trust=max(0,self.trust-3)
        system.coin+=rate
        print("✅ you recieved your cut of $",rate)
        system.update()
        time.sleep(0.55)
        return

    def sex(self,client=None,cut=20,system=None,force=False):
        luckytext=[]
        reviews=[]
        
        with open("D:\\py things\\python  dem\\flirt.json", "r", encoding="utf-8") as file:
            dial = json.load(file)
            dialogue = dial.get("girlsex")
            for scriptlist in dialogue:
                if scriptlist["persona1"] == self.persona1 and scriptlist["persona2"] == self.persona2 and scriptlist["nation"] == self.nation:
                    scripts = scriptlist["replies"]
                    break
            luckytext =random.sample(scripts["greeting"],3)
            title=["Unwrapping Desire 🎀 | Passionate Night Begins 🖤",
                    "Silk & Sin 🎀 | Starting Our Heated Night 🖤",
                    "Ribbon of Temptation 🎀 | Let the Passion Ignite 🖤",
                    "Bound in Heat 🎀 | Our Steamy Night Awaits 🖤",
                    "Midnight Cravings 🎀 | Ready for Intense Pleasure 🖤"]
            finaltitle=random.choice(title)
            print("══════════════════════════════════════════════════════════════════════════════")
            print(f"{finaltitle:^78}")
            print("══════════════════════════════════════════════════════════════════════════════")
            if self.effectivelevel>6*client.getstandard() and not force:
                print(f"💔 {self.name} is not in the mood for this, {client.name}. 💔")
                print(f"🎀 {self.name} : My trust dropped for you 💔 . New Trust {self.trust}")
                self.trust=max(0,self.trust-5)
                system.update()
                return
            elif self.concent(cut) or force:
                print(f"💖 {self.name} is ready to please you, {client.name}! 💖")
                time.sleep(2)
                print(f"🎀 {self.name} : {luckytext[0].replace('{client.name}', client.name)}")
                time.sleep(2.5)
                print(f"🎀 {self.name} : {luckytext[1].replace('{client.name}', client.name)}")
                time.sleep(2.5)
                print(f"🎀 {self.name} : {luckytext[2].replace('{client.name}', client.name)}")
                time.sleep(2.5)
                for i in range(8):
                    
                    print("Ah!~💖 ", end="", flush=True)
                    if i<4:
                        time.sleep(0.7)
                    else:
                        time.sleep(0.4)
                print("\n")
                xxx=self.getorgasm(client)
                rating=xxx[1]
            
            else:
                rejection_statements = [
                "No way… you’re asking for way too much cut. My trust in you is gone 💔🖤😠",
                "I’m done with this. That cut is too greedy… I can’t trust you anymore 💔🖤😤",
                "Absolutely not. You’re taking too big a share. Trust broken between us 💔🖤😠",
                "I trusted you but this cut is ridiculous. I’m walking away 💔🖤😡",
                "Hell no. You want too much… my faith in you just shattered 💔🖤😠"]
                print(f"🎀 {self.name} : {random.choice(rejection_statements)}")
                self.trust=max(0,self.trust-5)
                system.update()
                return
        with open("D:\\py things\\python  dem\\flirt.json", "r", encoding="utf-8") as file:
            dialx = json.load(file)
            dialogue = dialx.get("sexreview")

            for rev in dialogue:
                if self.cup in rev["cup_group"] and self.effectivelevel < int(rev["beauty_level"]) and self.nation==rev["nation"] and rev["review_quality"] == int(rating):
                    reviews=rev["reviews"]
        heart="💔"
        if rating==5 and xxx[0]==True:
            heart="💖"
            self.level=self.level+2 if self.level<29 else 30
            self.trust=self.trust+8 if self.trust<93 else 100
        elif rating==4 and xxx[0]==True:
            heart="💗" 
            self.level=self.level+1 if self.level<30 else 30
            self.trust=self.trust+5 if self.trust<95 else 100
        elif rating==3 and xxx[0]==True:
            heart="💓"
            self.level=self.level+1 if self.level<30 else 30
            self.trust=self.trust+3 if self.trust<97 else 100
        elif rating==2 and xxx[0]==True:
            heart="💔"
            self.level=self.level+1 if self.level<30 else 30
            self.trust=self.trust+1 if self.trust<99 else 100
        elif rating==1 and xxx[0]==True:
            heart="💔"
            self.level=self.level+1 if self.level<30 else 0
            self.trust=self.trust+1 if self.trust<99 else 100
        else:
            heart="💔"
            self.level=max(1,self.level-1)
            self.trust=max(0,self.trust-3)
        
        print("══════════════════════════════════════════════════════════════════════════════")
        review = random.choice(reviews).replace("{self.name}", self.name)
        review = review.replace("{client.name}", client.name)
        print(f"{heart} {client.name}'s Rating:  {"★"*rating}{ "☆"*(5-rating) }")
        print(f"👤 {client.name} : {review}")
        print("══════════════════════════════════════════════════════════════════════════════")
        time.sleep(0.55)
        if xxx[0]==True:
            print(random.choice([
                f"💖 {self.name} had an orgasm! 💖 Her body glowing even more beautiful now~",
                f"💖 {self.name} moaned in ecstasy as she came hard! 💖 That orgasm made her beauty bloom brighter!",
                f"💖 {self.name} shuddered with a powerful orgasm! 💖 Her beauty flourished even more from the pleasure~",
                f"💖 {self.name} reached an intense orgasm! 💖 Waves of pleasure made her look even more stunning!",
                f"💖 {self.name} exploded in a mind-blowing orgasm! 💖 Her beauty shining brighter than ever~"
            ]))
            mycut=(self.defaultrate*self.effectivelevel//6)*cut//100
            print("✅ you recieved your cut of $",mycut)
            print("💖 her trust increased for you 💖 . New Trust ",self.trust)
            system.coin+=mycut
        else:
            negative_orgasm_lines = [
                f"🥀 {self.name} couldn't cum no matter how hard {client.name} tried... 🥀 Her beauty wilted and decreased from the frustration 🖤",
                f"🥀 {self.name} faked her orgasm again... 🥀 The disappointment made her beauty visibly fade and shrink 🖤",
                f"🥀 No real climax for {self.name} tonight... 🥀 Her beauty dulled and decreased, leaving her less attractive 💔",
                f"🥀 {self.name} never reached orgasm... 🥀 The lack of pleasure caused her beauty to wither noticeably 🥀",
                f"🥀 {self.name} stayed dry and unsatisfied... 🥀 Her beauty faded and looked less appealing after the failed night 🖤"
            ]
            print(random.choice(negative_orgasm_lines))
            mycut=(self.defaultrate*self.effectivelevel//6)*cut//100
            print("✅ you recieved your cut of $",mycut)
            print("💔 her trust dropped for you 💔 . New Trust ",self.trust)
            system.coin+=mycut
        self.getboost()
        self.bodycount+=1
        if self.past=="clean":
            self.past="used"
        system.update()
        time.sleep(0.55)
        return
        

    def getcat(self):
        if 1 <= self.level <= 4:
            return "Cutie"
        elif 5 <= self.level <= 8:
            return "Baddie"
        elif 9 <= self.level <= 12:
            return "Mommy"
        elif 13 <= self.level <= 16:
            return "Goddess"
        elif 17 <= self.level <= 20:
            return "Waifu Queen"
class client:
    def __init__(self,name,gender,age,passport,city,netw,bio,standard,occupation,quote,trust=0):
        self.name=name
        self.gender=gender
        self.age=age    
        self.passport=passport
        self.city=city
        self.netw=netw
        self.bio=bio
        self.standard=standard
        self.occupation=occupation
        self.quote=quote
        self.trust=trust
    def getstandard(self):
        
        
        return self.standard
    def incity(self,searchedcity):
        if self.city==searchedcity:
            return True
        else:
            return False
    def trusttitle(self):
        if self.trust < 20:
            return "⚪ Stranger"
        elif self.trust < 40:
            return "🟢 Acquaintance"
        elif self.trust < 60:
            return "🔵 Trusted Contact"
        elif self.trust < 80:
            return "🟣 Business Partner"
        elif self.trust < 95:
            return "🟡 Elite Associate"
        return "👑 Inner Circle"      

    def intro(self):

        passport = {
            "A": "American",
            "I": "Italian",
            "B": "British",
            "F": "French",
            "S": "Spanish",
            "C": "Canadian",
            "J": "Japanese"
        }

        city = {
            "la": "Los Angeles",
            "mm": "Miami",
            "lv": "Las Vegas"
        }

        gender = {
            "M": "Male",
            "F": "Female"
        }

        icons = {
            "la": ["🎬","🌴","📸","🎥","⭐","🎭","🏆","🍷","🚘","🌇"],
            "mm": ["🌊","🛥","🏖","🍹","🌴","🌺","🐬","🦩","💎","☀"],
            "lv": ["🎰","🎲","🍾","🥂","💎","♠","♥","♦","♣","🎭"]
        }

        icon = random.choice(icons[self.city])

        bio = textwrap.fill(self.bio, width=62)

        print(f"""
══════════════════════════════════════════════════════════════════════
                            {icon} {self.name.upper()}
══════════════════════════════════════════════════════════════════════

    Age             : {self.age}
    Gender          : {gender[self.gender]}
    Nationality     : {passport[self.passport]}
    Residence       : {city[self.city]}
    Net Worth       : ${self.netw} Billion
    Occupation      : {self.occupation}
    Trust Level     : {self.trust}/100

──────────────────────────────────────────────────────────────────────

    {bio}

──────────────────────────────────────────────────────────────────────

    "{self.quote}"

══════════════════════════════════════════════════════════════════════
    """)
    def updatetrust(self, amount):
        self.trust += amount
        if self.trust < 0:
            self.trust = 0
        elif self.trust > 100:
            self.trust = 100
    def classify(self):
        return [self.name, self.gender, self.age, self.passport, self.city, self.netw, self.bio, self.standard, self.occupation, self.quote, self.trust]   
class system:
    def __init__(self):
        self.girls=[]
        self.defaultrate=1000
        self.coin=3000
        self.loan=0
        self.count=1
        self.clients=[]
        self.inventory={}
        self.city="la"
        filename = filepath("girls.csv")
        secret=filepath("secrets.csv")
        directory=filepath("clients.csv")
        clashlist=filepath("inventory.csv")
        try:
            g=open(secret,"r", newline="")
            self.defaultrate=int(math.ceil(float(g.readline().strip())))
            self.coin=int(math.ceil(float(g.readline().strip())))
            self.loan=int(math.ceil(float(g.readline().strip())))
            self.count=int(math.ceil(float(g.readline().strip())))
            self.city=g.readline().strip()
            g.close()
        except FileNotFoundError:
            with open(filepath("secrets.csv"),"x") as filex:
                filex.write("3000\n5000\n0\n1\nla") 

        try:
            f = open(filename, "r")
            reader=csv.reader(f)
            k=True
            for row in reader:
                if k:
                    k=False
                    continue
                self.girls.append(girl(row[0],int(row[1]),self.defaultrate,row[2],row[3]=="True",row[4]=="True",row[5],row[6],row[7],int(row[8]),row[9],int(row[10]),row[11],row[12],row[13],row[14],int(row[15])))
            f.close()    
        except FileNotFoundError:
            with open(filepath("girls.csv"),"x", newline="") as file:
                writer=csv.writer(file)
                writer.writerow(["name","level","boost","preg","jail","city","cup","guard","bodycount","past","trust","mood","persona1","persona2","nation","age"])
                writer.writerow(["kurumi",8,None,"False","False","la","C",None,0,"clean",0,"neutral","Tsundere","Princess","Asian",18])
        
        try:
            h=open(directory,"r", newline="")
            reader=csv.reader(h)
            k=True
            for row in reader:
                if k:
                    k=False
                    continue
                self.clients.append(client(row[0],row[1],int(row[2]),row[3],row[4],float(row[5]),row[6],int(row[7]),row[8],row[9],int(row[10])))
            h.close()
        except FileNotFoundError:

            with open(filepath("clients.csv"),"x", newline="") as file:
                writer=csv.writer(file)
                writer.writerow(["name","gender","age","passport","city","netw","bio","standard","occupation","quote","trust"])   
                writer.writerow(["Vincent Blackwood","M",54,"A","la",4.2,"Vincent Blackwood owns the legendary Sunset Strip Club in the heart of Los Angeles.\nHis club has hosted celebrities, athletes and politicians for decades.\n\nBehind the glamorous lights lies a sophisticated financial network.\nAuthorities suspect millions disappear through shell companies every year.\n\nVincent respects only disciplined partners who deliver results.\nOne successful deal with him can elevate an agency's reputation.",8,"Sunset Strip Club Owner","Luxury isn't purchased. It's remembered.",50])

                writer.writerow(["Ethan Sterling","M",46,"A","la",1.7,"Ethan runs Hollywood's largest private photoshoot studio for celebrities.\nHis photographers are considered among the finest in California.\n\nFashion agencies constantly compete for exclusive contracts with him.\nHis recommendations can launch unknown faces into stardom.\n\nProfessionalism matters more than beauty in Ethan's eyes.\nHe rewards consistency above everything else.",6,"Hollywood Photoshoot Studio Owner","Every picture tells a story. Make yours unforgettable.",0])

                writer.writerow(["Sonnet Laurent","M",34,"F","la",1.1,"Sonnet directs one of Hollywood's most prestigious casting agencies.\nHe discovers talent long before the entertainment industry notices.\n\nMajor film studios frequently seek his recommendations.\nOnly agencies with impeccable reputations earn his trust.\n\nHe believes every opportunity should be earned.\nSuccess follows preparation, never luck.",7,"Casting Agency Director","Fame begins with one perfect audition.",0])

                writer.writerow(["Carl Brooks","M",31,"B","la",0.9,"Carl owns Beverly Hills' most luxurious fashion boutique.\nExclusive brands from around the world compete for shelf space.\n\nHe influence shapes seasonal fashion trends across California.\nCelebrities often visit after business hours for private fittings.\n\nHe admires elegance and professionalism above extravagance.\nA polished image always opens new doors.",5,"Fashion Boutique Owner","Style speaks before you do.",0])

                writer.writerow(["Isabella Rossi","F",39,"I","mm",1.4,"Isabella operates Miami's famous South Beach Strip Club.\nHer establishment is known for luxury service and absolute discretion.\n\nVIP guests often arrive aboard private yachts before sunset.\nRumors suggest she quietly arranges exclusive entertainment offshore.\n\nShe values confidence and loyalty in business partners.\nBreaking her trust is almost impossible to repair.",9,"South Beach Strip Club Owner","The ocean rewards those who think bigger.",0])

                writer.writerow(["Diego Alvarez","M",45,"S","mm",2.6,"Diego owns the largest luxury yacht fleet in Miami.\nHis parties attract billionaires from every continent.\n\nEvery weekend another private celebration leaves the marina.\nSecurity and privacy are his greatest selling points.\n\nReliable agencies receive invitations others never see.\nOne successful voyage can transform an entire career.",10,"Luxury Yacht Fleet Owner","Business tastes better at sea.",0])

                writer.writerow(["Olivia Carter","F",29,"A","mm",0.8,"Olivia built Miami's leading beach photoshoot company.\nHer campaigns frequently appear in international magazines.\n\nTourism brands compete for her seasonal collaborations.\nCreative ideas earn far more than expensive equipment.\n\nShe enjoys ambitious agencies willing to innovate.\nFresh faces always have a chance with her.",6,"Beach Photoshoot Studio Owner","Every sunset deserves an audience.",0])

                writer.writerow(["Amelia Hart","F",32,"B","mm",1.5,"Amelia owns Oceanfront Boutique, famous for rare luxury jewelry.\nCollectors from across the world travel to Miami for private auctions.\n\nAuthorities occasionally investigate missing gemstones without success.\nNothing has ever been traced back to Amelia.\n\nShe values silence as much as wealth.\nLoose lips never receive a second opportunity.",8,"Oceanfront Boutique Owner","True luxury is never loud.",0])

                writer.writerow(["Marco Bellini","M",51,"I","lv",3.3,"Marco oversees the legendary Platinum Strip Club in Las Vegas.\nHis VIP lounge hosts the city's wealthiest visitors every night.\n\nCasino executives, celebrities and investors gather under his roof.\nEvery successful introduction creates another profitable connection.\n\nMarco expects perfection from every partnership.\nFailure is remembered longer than success.",9,"Platinum Strip Club Owner","The house always wins. Unless you're working with me.",0])
  
                writer.writerow(["Ava Sinclair","F",28,"A","lv",1.2,"Ava manages the exclusive VIP Casino Lounge on the Strip.\nOnly invited guests are welcomed through its private entrance.\n\nWhispers speak of underground poker tables hidden beneath the casino.\nNo investigation has ever uncovered convincing evidence.\n\nShe appreciates confidence backed by results.\nFortune favors those willing to take calculated risks.",10,"VIP Casino Lounge Manager","Luck is temporary. Influence is forever.",0])
            
                writer.writerow(["Elena Moretti","F",30,"I","lv",1.8,"Elena owns the renowned High Roller Escort Service on the Las Vegas Strip.\nHer agency is trusted by celebrities, diplomats and billionaire guests.\n\nEvery client is carefully selected through private recommendations.\nDiscretion has made her one of the city's most respected entrepreneurs.\n\nShe values professionalism above everything else.\nOne mistake is enough to lose her confidence.",8,"High Roller Escort Service Owner","Luxury begins where anonymity is guaranteed.",0])

                writer.writerow(["Scarlett Monroe","F",27,"A","lv",1.0,"Scarlett transformed Neon Night Club into one of Vegas' hottest destinations.\nFamous DJs and performers headline her venue every weekend.\n\nHer club is the first stop for young millionaires and influencers.\nThe nightlife scene changes quickly, but Scarlett always stays ahead.\n\nShe admires ambition backed by confidence.\nThe spotlight belongs to those willing to earn it.",7,"Neon Night Club Owner","Tonight's memories become tomorrow's legends.",0])
        try:
            n=open(clashlist,"r", newline="",encoding="utf-8")
            reader=csv.reader(n)
            k=True
            for row in reader:
                if k:
                    k=False
                    continue
                self.inventory.update({row[0]:[row[1],row[2],int(row[3]),int(row[4])]})
            n.close()

        except FileNotFoundError:
            with open(filepath("inventory.csv"),"x",newline="",encoding="utf-8") as filex:
                rux=self.getrux()
                writer=csv.writer(filex)
                writer.writerow(["item id","name","bio","price","owned"])
                for key in list(rux.keys()):
                    writer.writerow([key,rux[key][0],rux[key][1],rux[key][2],rux[key][3]])
                    self.inventory.update({key:rux[key]})
        




            self.__init__()
    def update(self):
        
        self.count+=1
        if self.count%3==0:
            self.bank()
            self.loan+=self.loan*5//100
        try:
            with open(filepath("girls.csv"),"w",newline="") as file:
                writer=csv.writer(file)
                writer.writerow(["name","level","boost","preg","jail","city","cup","guard","bodycount","past","trust","mood","persona1","persona2","nation","age"])
                for girl in self.girls: 
                    writer.writerow(girl.classify())
            with open(filepath("secrets.csv"),"w") as filex:
                filex.write(f"{self.defaultrate}\n{self.coin}\n{self.loan}\n{self.count}\n{self.city}")
            with open(filepath("clients.csv"),"w",newline="") as file:
                writer=csv.writer(file)
                writer.writerow(["name","gender","age","passport","city","netw","bio","standard","occupation","quote","trust"])
                for client in self.clients:
                    writer.writerow(client.classify())
            with open(filepath("inventory.csv"),"w",newline="",encoding="utf-8") as filex:
                writer=csv.writer(filex)
                writer.writerow(["item id","name","bio","price","owned"])
                for key in list(self.inventory.keys()):
                    writer.writerow([key,self.inventory[key][0],self.inventory[key][1],self.inventory[key][2],self.inventory[key][3]])
        except FileNotFoundError:
            print("failed to update")
    def extract(self):
        with open(filepath("girls.csv"),"r",newline="") as file:
            reader=csv.reader(file)
            k=True
            for row in reader:
                if k:
                    k=False
                    continue
                self.girls.append(girl(row[0],int(row[1]),self.city,row[2],row[3]=="True",row[4]=="True",row[5],row[6],row[7],int(row[8]),row[9],int(row[10]),row[11],row[12],row[13],row[14],int(row[15])))
        with open(filepath("clients.csv"),"r",newline="") as file:
            reader=csv.reader(file)
            k=True
            for row in reader:
                if k:
                    k=False
                    continue
                self.clients.append(client(row[0],row[1],int(row[2]),row[3],row[4],float(row[5]),row[6],int(row[7]),row[8],row[9],int(row[10])))
        with open(filepath("inventory.csv"),"r",newline="",encoding="utf-8") as file:
            reader=csv.reader(file)
            k=True
            for row in reader:
                if k:
                    k=False
                    continue
                self.inventory.update({row[0]:[row[1],row[2],int(row[3]),int(row[4])]})
        
    def view(self):
        i=0
        for girl in self.girls:
            print(f"{i+1}. {girl.name}'s reputation : {girl.level} & is a {girl.getcat()} , Rate: $ {girl.getrate()}")
            i+=1
    def addgirl(self):
            
        while True:
            if(self.coin<self.defaultrate):
                print("oops bro you dont have enough money for new bitches :/")
                break
            egirl=self.match(input(f"\nEnter name of yo babe ,hiring price ${self.defaultrate}\nEnter exit to stop adding more\n"))
            if egirl=="Exit":
                break
            elif self.searchgirl(egirl)!="0":
               print("hey that bitch is present in yo team dude ,she loyal to u :)") 
               continue
            yii=random.choices([6,8,10],weights=[6,3,1],k=1)[0]
            newgirl=girl(egirl,yii,self.defaultrate)
            self.girls.append(newgirl)
            if yii==6:
                print("uff thats a common hoe dawg :(")
            elif yii==8:
                print("oh thats a classic one +_-")
            else:
                print("bro thats a baddie! a perfect 10! :)")
            self.coin-=self.defaultrate
            
    def match(self,string):
         return string.strip().lower().capitalize()     
    def searchgirl(self,string,mock=False):
        for girl in self.girls:
            if self.match(string)==self.match(girl.name):
                return girl
        if mock:
            print("sorry dude that girl aint yours :/")
        return "0"
    def globalpimp(self):
        print("choose a girl from the list given below :3\n")
        self.view()
        g=input()
        x=self.searchgirl(g,True)
        if x=="0":
            return
        print("Ask ur girl for percentage cut ;)\n")
        try:
            cut=int(input())
            sample=x.pimp(cut)
            self.coin+=sample
            
        except IOError:
            return
    
    def bank(self):
        if self.loan > 0:

            net = self.coin - self.loan

            if net > 0:

                if net >= 5 * self.loan:
                    repayment = self.loan

                elif net < self.loan:
                    ratio = net / self.loan
                    bank_rate = 0.20 + 0.40 * ratio
                    repayment = math.floor(net * bank_rate)

                else:
                    ratio = (net - self.loan) / (4 * self.loan)
                    bank_rate = 0.60 + 0.60 * (ratio ** 2)
                    repayment = min(math.floor(net * bank_rate), self.loan)
                print(f"💰 Bank Repayment: ${repayment} has been deducted from your account.")
                time.sleep(1.5)
                self.coin -= repayment
                self.loan -= repayment
    def viewfinancialreport(self):
        print(f'''
══════════════════════════════════════════════════════════════════════════════
                    🏦 FINANCIAL REPORT 🏦
══════════════════════════════════════════════════════════════════════════════

💰 Current Cash          : ${self.coin:,}
🏦 Outstanding Loan      : ${self.loan:,}
📈 Loan Interest Rate    : 5% per collection cycle
📅 Current Day           : {self.count}
👯 Total Girls           : {len(self.girls)}
🌴 Current City          : {self.city.upper()}

══════════════════════════════════════════════════════════════════════════════
ASSET SUMMARY
══════════════════════════════════════════════════════════════════════════════
''')

        la_girls = len([g for g in self.girls if g.city == "la"])
        mm_girls = len([g for g in self.girls if g.city == "mm"])
        lv_girls = len([g for g in self.girls if g.city == "lv"])

        print(f"🌴 Los Angeles Girls    : {la_girls}")
        print(f"🌊 Miami Girls          : {mm_girls}")
        print(f"🎰 Las Vegas Girls     : {lv_girls}")

        total_level = sum(g.level for g in self.girls)
        avg_level = round(total_level / len(self.girls), 1) if self.girls else 0

        print(f"📊 Average Girl Level   : {avg_level}")
        print(f"💎 Total Agency Value   : ${self.coin + (total_level * 5000):,}")

        print('''
══════════════════════════════════════════════════════════════════════════════
💡 TIP: Repay loans quickly to avoid interest accumulation.
══════════════════════════════════════════════════════════════════════════════
''')
        input("Press Enter to return...")
        if self.city=="la":
            self.labank
        elif self.city=="mm":
            self.mmbank
        elif self.city=="lv":
            self.lvbank
    def addloan(self):#updation done
        net=self.coin-self.loan
        limit=max((net)*5,20000)
        limit=max(0,20000-self.loan) if net<20000 else limit
        
        try:
            ask=int(input(f"enter amount u need for loan , sanctioned loan {limit}\nChoose amount :►"))
            if(0<ask<=limit):
                print(f"Loan fund transfered to {math.floor(ask/limit*100)}% of the sanctioned funds")
                self.coin+=ask
                self.loan+=ask
                self.update()
                time.sleep(1)
            else:
                print("You are not eligible for such a loan")
        except:
            print("bruh that aint a number -_-")
    def inflate(self,amount):
        
        self.loan=self.loan*amount//self.defaultrate
        self.defaultrate=amount
        for girl in self.girls:
            girl.setdefaultrate(self.defaultrate)
    def la(self):
        print(f'''\n\n\n\n\n\n
══════════════════════════════════════════════════════════════════════
                    🌴 LOS ANGELES 🌴
══════════════════════════════════════════════════════════════════════

          ☀ Hollywood • Beverly Hills • Venice

            🌴      🏖      🌴       🌇      🌴

        ╭──────────────────────────────────────────╮
        │          LOS ANGELES DISTRICT            │
        ╰──────────────────────────────────────────╯

        🏠 Businesses
        ├── [1] 💃 Sunset Strip Club
        ├── [2] 📸 Hollywood Photoshoot Studio
        ├── [3] 🌆 Skyline Social Club
        ├── [4] ✨ Hollywood House of Glam
        ├── [5] 🏦 City Bank
        ├── [6] ✈ Airport
        ├── [7] 🌐 VIP Network
        └── [8] 🚘 Return to Headquarters
              
═══════════════════════════════════════════════════════
    Current Girls : {len(self.girls)}
    Available Cash: {self.coin}
    Outstanding Loan: {self.loan}
    Police Heat: LOW
═══════════════════════════════════════════════════════

Choose a destination ►''',end="")    
        try:
            num=int(input())
            if num==8:
                return
            elif num==5:
                self.labank()
            elif num==6:
                self.airway("la")
            elif num==7:
                self.network()
            elif num==4:
                self.lashop()
            elif num==1:
                self.lastripclub()
            elif num==2:
                self.laphoto()
            elif num==3:
                self.lasky()
        except Exception as e:
            print(e)
            
            print("bruh that aint a number -_-")
            return


    def lastripclub(self):
        vincentblackwood = self.clients[0]  # Assuming Vincent Blackwood is the first client in the list

        # Prestige based on Vincent Blackwood's Trust
        if vincentblackwood.trust >= 95:
            prestige = 5
            prestigetext = "★★★★★ Hollywood Elite"

        elif vincentblackwood.trust >= 75:
            prestige = 4
            prestigetext = "★★★★☆ Premier Destination"

        elif vincentblackwood.trust >= 55:
            prestige = 3
            prestigetext = "★★★☆☆ Popular Hotspot"

        elif vincentblackwood.trust >= 35:
            prestige = 2
            prestigetext = "★★☆☆☆ Rising Venue"

        elif vincentblackwood.trust >= 15:
            prestige = 1
            prestigetext = "★☆☆☆☆ Local Attraction"

        else:
            prestige = 0
            prestigetext = "☆☆☆☆☆ Unknown Venue"

        # Crowd Calculation
        crowd = random.randint(1, 5) * 20 * prestige

        if crowd == 0:
            crowdtext = "Deserted"
        elif crowd <= 40:
            crowdtext = "Quiet"
        elif crowd <= 80:
            crowdtext = "Moderate"
        elif crowd <= 200:
            crowdtext = "Busy"
        elif crowd <= 400:
            crowdtext = "Packed"
        else:
            crowdtext = "Overflowing"

        

        print(f"""
══════════════════════════════════════════════════════════════════════════════
                        💃 SUNSET STRIP CLUB 💃
                    "Hollywood's Crown Jewel Since 1986"
══════════════════════════════════════════════════════════════════════════════

📍 Location            • Sunset Boulevard, Los Angeles
👑 Proprietor          • Vincent Blackwood
👥 Crowd Tonight       • {crowdtext} ({crowd} Guests)
⭐ Tonight's Prestige  • {prestigetext}

──────────────────────────────────────────────────────────────────────────────
                            BUILDING DIRECTORY
──────────────────────────────────────────────────────────────────────────────

[1] 💃 Main Stage                     • Ground Floor
    ◆ Live Performances ◆ Packed Audience ◆ Steady Revenue

[2] 🌙 Velvet Eclipse                 • First Floor
    ◆ Exclusive Lounge ◆ Private Bookings ◆ Agency Operations

[3] 💎 Crimson Room                   • Second Floor
    ◆ VIP Clients ◆ High Society ◆ Luxury Contracts

[4] 🎬 Neon Mirage                    • Third Floor
    ◆ Celebrity Circle ◆ Talent Scouting ◆ Industry Influence

[0] 🚪 Return

══════════════════════════════════════════════════════════════════════════════
""")

        while True:
                try:
                    choice = int(input(" Select Destination :► "))

                    if choice == 1:
                        girls=self.checkgirl("lastrip")
                        girl=self.listgirls(girls,"strip")
                        if girl==None:
                            self.lastripclub()
                            return
                        girl.setdefaultrate(70)
                        clientlist=[]
                        t=0
                        if crowd == 0:
                            crowdtext = "Deserted"
                        elif crowd <= 40:
                            crowdtext = "Quiet"
                            t=1
                        elif crowd <= 80:
                            crowdtext = "Moderate"
                            t=2
                        elif crowd <= 200:
                            crowdtext = "Busy"
                            t=3
                        elif crowd <= 400:
                            crowdtext = "Packed"
                            t=4
                        else:
                            crowdtext = "Overflowing"
                            t=5
                        for i in range(t):
                            clientlist.append(self.randomclient())
                        print(f"💵 Enter the percentage cut you want to take from crowd's payment:► ", end="")
                        while True:
                            try:
                                cut = int(input())
                                if 0 <= cut <= 100:
                                    break
                                else:
                                    print("❌ Invalid percentage. Please enter a value between 0 and 100.")
                            except ValueError:
                                print("❌ Invalid input. Please enter a valid integer percentage.")
                        
                        girl.strip(clientlist,crowd,cut,self)
                        girl.setdefaultrate(self.defaultrate)
                        time.sleep(2)
                        self.lastripclub()
                        
                        
                        

                    elif choice == 2:
                        girls=self.checkgirl("la")
                        girl=self.listgirls(girls,"pimp")
                        if girl==None:
                            self.lastripclub()
                            return
                        girl.setdefaultrate(5000)
                        sampleclient=self.randomclient()
                        print(f"💼 {sampleclient.name} has requested a private session with {girl.name}")
                        print(f"👤 The standard of {sampleclient.name} is {sampleclient.getstandard()}")
                        print(f"💵 Enter the percentage cut you want to take from {sampleclient.name}'s payment:► ", end="")
                        while True:
                            try:
                                cut = int(input())
                                if 0 <= cut <= 100:
                                    break
                                else:
                                    print("❌ Invalid percentage. Please enter a value between 0 and 100.")
                            except ValueError:
                                print("❌ Invalid input. Please enter a valid integer percentage.")
                        
                        girl.sex(sampleclient, cut, self)
                        vincentblackwood.updatetrust(5)
                        girl.setdefaultrate(self.defaultrate)
                        time.sleep(2)
                        self.lastripclub()
                        
                        
                        
                        pass

                    elif choice == 3:
                        
                        print("\n══════════════════════════════════════════════════════════════════════════════")
                        print(f"{'💎 Crimson Room Reservation 💎':^78}")
                        print("══════════════════════════════════════════════════════════════════════════════")
                        print("🏛 Reservation Fee : $5000")
                        print("🤝 VIP Commission  : Fixed 30%")
                        print()
                        print("⚠ IMPORTANT")
                        print("• Booking does NOT guarantee meeting a VIP.")
                        print("• Staff will attempt to invite elite guests.")
                        print("• Maximum Attempts : 5")
                        print("• Reservation fee is NON-REFUNDABLE.")
                        print("══════════════════════════════════════════════════════════════════════════════")
                        print("[1] 💎 Reserve Crimson Room")
                        print("[0] 🔙 Return")
                        print("══════════════════════════════════════════════════════════════════════════════")
                        
                        try:
                            book = int(input("Choose ► "))
                        except:
                            continue

                        if book == 0:
                            self.lastripclub()
                            continue

                        if self.coin < 5000:
                            print("\n❌ You don't have enough money to reserve the Crimson Room.")
                            time.sleep(2)
                            continue

                        self.coin -= 5000

                        girls = self.checkgirl("la")
                        girl = self.listgirls(girls, "vipsex")

                        if girl is None:
                            self.coin += 5000
                            self
                            continue

                        girl.setdefaultrate(30000)

                        print("\n💎 Reserving Crimson Room...")
                        vincentblackwood.updatetrust(5)
                        time.sleep(1.5)

                        print("📨 Sending invitations to Hollywood VIPs...")
                        time.sleep(2)

                        success = False
                        vip = None

                        for attempt in range(1, 6):

                            print(f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                            print(f"Attempt {attempt}/5")
                            print("Searching", end="", flush=True)

                            for _ in range(6):
                                time.sleep(0.4)
                                print(".", end="", flush=True)

                            print()

                            vip = random.choices(
                                [
                                    self.clients[0],
                                    self.clients[1],
                                    self.clients[2],
                                    self.clients[3],
                                    None
                                ],
                                weights=[
                                    max(self.clients[0].trust, 5),
                                    max(self.clients[1].trust, 5),
                                    max(self.clients[2].trust, 5),
                                    max(self.clients[3].trust, 5),
                                    100
                                ],
                                k=1
                            )[0]

                            if vip is None:
                                print("❌ No VIP accepted the invitation.")
                                time.sleep(1.5)
                                continue

                            success = True
                            break

                        if success:

                            print("\n═══════════════════════════════════════════════")
                            print("🎉 VIP FOUND!")
                            print("═══════════════════════════════════════════════\n")

                            print(f"👑 {vip.name} has arrived.")
                            print(f"💼 {vip.occupation}")
                            print(f"⭐ Standard : {vip.getstandard()}")
                            print(f"🤝 Trust : {vip.trust}/100\n")

                            print("Agency Cut has been fixed at 30%.")
                            

                            girl.sex(vip, 30, self,True)
                            # Store whether this VIP was previously undiscovered
                            newvip = (vip.trust == 0)

                            

                            # Unlock animation if first encounter
                            if newvip:

                                print("""
══════════════════════════════════════════════════════════════════════════════
                        🌟 NEW VIP DISCOVERED 🌟
══════════════════════════════════════════════════════════════════════════════
                            """)

                                time.sleep(1.5)

                                print("🔍 Updating Network Database", end="", flush=True)

                                for _ in range(6):
                                    time.sleep(0.4)
                                    print(".", end="", flush=True)

                                print()

                                time.sleep(1)

                                print(f"""
🎉 Congratulations!

👑 {vip.name}
💼 {vip.occupation}

has been added to your exclusive Los Angeles VIP Network.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✔ Future encounters unlocked
✔ VIP profile unlocked
✔ Trust progression unlocked

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

                                

                            # Increase trust after the first meeting
                            vip.updatetrust(5)

                            self.update()

                            

                        else:

                            print("""
══════════════════════════════════════════════════════════════

💔 Unfortunately none of the invited VIPs accepted tonight.

The Crimson Room reservation has expired.

Unfortunately the booking fee is non-refundable.

Better luck next time.

══════════════════════════════════════════════════════════════
""")

                        girl.setdefaultrate(self.defaultrate)

                        self.update()

                        time.sleep(2)

                        self.lastripclub()
                        return
                        
                        

                        

                    elif choice == 4:

                        

                        # ──────────────────────────────────────────────────────────────
                        # Trust Requirement
                        # ──────────────────────────────────────────────────────────────
                        if vincentblackwood.trust < 70:

                            print(f"""
══════════════════════════════════════════════════════════════════════════════
                        🎬 NEON MIRAGE
                Hollywood Celebrity Circle
══════════════════════════════════════════════════════════════════════════════

🔒 ACCESS DENIED

Vincent Blackwood doesn't trust your agency enough
to introduce you to Hollywood's celebrity network.

Only agencies with exceptional reputation and loyalty
are granted access to this confidential service. (gain trust in crimson room )

──────────────────────────────────────────────────────────────────────────────

Required Trust : 70
Current Trust  : {vincentblackwood.trust}

──────────────────────────────────────────────────────────────────────────────

💬 Vincent Blackwood

"Earn my trust first.
Hollywood's biggest names don't gamble with amateurs."

══════════════════════════════════════════════════════════════════════════════
""")

                            input("Press Enter to Return...")
                            self.lastripclub()
                            return

                        # ──────────────────────────────────────────────────────────────
                        # Menu
                        # ──────────────────────────────────────────────────────────────

                        print("""
══════════════════════════════════════════════════════════════════════════════
                        🎬 NEON MIRAGE
                Hollywood Celebrity Circle
══════════════════════════════════════════════════════════════════════════════

Reservation Fee : $60000

Vincent Blackwood will privately contact his elite
Hollywood network in search of celebrities interested
in joining your agency.

⚠ Reservation fee is NON-REFUNDABLE.

[1] Begin Celebrity Search
[0] Return

══════════════════════════════════════════════════════════════════════════════
""")
                        while True:
                            try:
                                choice = int(input("Choose ► "))
                                break
                            except:
                                print("❌ Invalid input. Please enter a valid number.")
                                continue

                        if choice == 0:
                            self.lastripclub()
                            return

                        if self.coin < 60000:
                            print("\n❌ You don't have enough money.")
                            time.sleep(2)
                            return

                        self.coin -= 60000
                        vincentblackwood.updatetrust(5)

                        print("\nVincent Blackwood has activated his Hollywood connections.\n")

                        print("Please wait", end="", flush=True)

                        for i in range(6):
                            time.sleep(0.5)
                            print(".", end="", flush=True)

                        print("\n")

                        # ──────────────────────────────────────────────────────────────
                        # Hidden Search
                        # ──────────────────────────────────────────────────────────────

                        found = []

                        for i in range(10):
                            print(len(found))

                            # 1 in 3 chance
                            if not random.randint(1, 3) == 1:
                                continue

                            celeb = self.randomgirl(1,True)

                            duplicate = False

                            # Already recruited?
                            for girl in self.girls:
                                if girl.name == celeb.name:
                                    duplicate = True
                                    break

                            # Already found during THIS search?
                            if not duplicate:
                                for girl in found:
                                    if girl.name == celeb.name:
                                        duplicate = True
                                        break

                            if duplicate:
                                continue

                            found.append(celeb)
                            

                            if len(found) == 4 and not found == []:
                                break

                                

                        # ──────────────────────────────────────────────────────────────
                        # Nobody Found
                        # ──────────────────────────────────────────────────────────────

                        if len(found) == 0:

                            print("""
══════════════════════════════════════════════════════════════════════════════

Unfortunately none of the contacted celebrities
accepted Vincent's invitation.

The scouting fee has been consumed.

Vincent Blackwood:
"Hollywood never guarantees success."

══════════════════════════════════════════════════════════════════════════════
                    """)

                            self.update()
                            time.sleep(2)
                            self.lastripclub()
                            return

                        # ──────────────────────────────────────────────────────────────
                        # Celebrity Selection
                        # ──────────────────────────────────────────────────────────────

                        print("""
══════════════════════════════════════════════════════════════════════════════

Several celebrities have expressed interest
in joining your agency.

Choose one to negotiate with.

══════════════════════════════════════════════════════════════════════════════
                    """)

                        girl = self.listgirls(found, "celebrity")

                        if girl is None:
                            return

                        self.girls.append(girl)

                        print(f"""
══════════════════════════════════════════════════════════════════════════════

🎉 Congratulations!

⭐ {girl.name} has officially joined your agency.

Hollywood's elite have begun recognizing your influence.

══════════════════════════════════════════════════════════════════════════════
                    """)

                        self.update()

                        time.sleep(2)
                        self.lastripclub()
                    
                        pass

                    elif choice == 0:
                        self.la()
                        return

                    else:
                        print("❌ Invalid Choice!")
                

                except Exception as e:
                     print (e)
                     print("❌ Please enter a valid number!")
    def laphoto(self,redirect=0,skipper=True):
        signedcelebs = 0

        for girl in self.girls:
            if girl.effectivelevel >= 40:
                signedcelebs += 1

        owner = self.clients[1]
        if skipper:
            print(r"""
██╗  ██╗ ██████╗ ██╗     ██╗     ██╗   ██╗██╗    ██╗ ██████╗  ██████╗ ██████╗
██║  ██║██╔═══██╗██║     ██║     ╚██╗ ██╔╝██║    ██║██╔═══██╗██╔═══██╗██╔══██╗
███████║██║   ██║██║     ██║      ╚████╔╝ ██║ █╗ ██║██║   ██║██║   ██║██║  ██║
██╔══██║██║   ██║██║     ██║       ╚██╔╝  ██║███╗██║██║   ██║██║   ██║██║  ██║
██║  ██║╚██████╔╝███████╗███████╗   ██║   ╚███╔███╔╝╚██████╔╝╚██████╔╝██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝  ╚═════╝ ╚═════╝

══════════════════════════════════════════════════════════════════════════════
                    ★  LIGHTS • CAMERA • ACTION  ★
══════════════════════════════════════════════════════════════════════════════""")
            for i in range(39):
                x=["🎬", "🎥", "📸", "🌟", "✨"]
                print(x[i%5], end="", flush=True)
                time.sleep(1.7 / 39)   # Total animation ≈ 1.7 seconds

            print()
        if redirect==0:
            print(fr"""
══════════════════════════════════════════════════════════════════════════════
                          🎬 HOLLYWOOD STUDIOS
══════════════════════════════════════════════════════════════════════════════

        ★ Welcome to the World's Greatest Entertainment Hub ★

Studio Owner      : {owner.name}
Reputation        : {owner.trust}/100
Signed Celebrities: {signedcelebs}

──────────────────────────────────────────────────────────────────────────────

[1] 🌟 Talent Recruitment
    Fresh Faces • Agency Contracts • Rising Stars

[2] 📸 Premium Photoshoots
    Designer Brands • Cover Shoots • Prestige

[3] 🎥 Movie Auditions
    Blockbusters • Casting Calls • Stardom

[4] 🚪 Return

──────────────────────────────────────────────────────────────────────────────

      "Every superstar was once an unknown face."

══════════════════════════════════════════════════════════════════════════════
""")
        while True:
                # try:
                    choice = int(input(" Select Destination :► ")) if redirect==0 else redirect
                    if choice == 1:
                        print(r"""
══════════════════════════════════════════════════════════════════════════════
                    🎬✨ TALENT RECRUITMENT ✨🎬
══════════════════════════════════════════════════════════════════════════════

           🌟 Discover the next generation of Hollywood talent. 🌟

[1] 👑 VIP Society
    Heiresses • Celebrity Circle • Elite Beauties            💰 $60,000

[2] 📱 Creator Space
    Influencers • Lifestyle Creators • Internet Stars        💰 $30,000

[3] 🎬 Studio Talent
    Models • Dancers • Aspiring Actresses                    💰 $15,000

[4] 🎓 College Circuit
    College Girls • Campus Leaders • Exchange Students       💰 $7,500

[5] ☕ Everyday Life
    Professionals • Baristas • Hidden Gems                   💰 $3,000

[6] 🚪 Return

══════════════════════════════════════════════════════════════════════════════
""")
                        while True:
                            try:
                                sub_choice = int(input("Choose a recruitment tier :► "))
                                if sub_choice in [1, 2, 3, 4, 5, 6]:
                                    break
                                else:
                                    print("❌ Invalid choice. Please select a valid option.")
                            except ValueError:
                                print("❌ Invalid input. Please enter a valid number.")
                        if sub_choice == 6:
                            self.laphoto(0,False)
                            return
                        if self.coin < [60000, 30000, 15000, 7500, 3000][sub_choice - 1]:
                            print("❌ Insufficient funds for this recruitment tier.")
                            continue
                        self.coin -= [60000, 30000, 15000, 7500, 3000][sub_choice - 1]
                        if sub_choice == 6:
                            self.laphoto(0,False)
                        elif sub_choice in [1, 2, 3, 4, 5]:
                            females=self.recruitgirls(4,sub_choice)
                            girl=self.recruitlist(females)
                            if girl == None:
                                self.laphoto(1,False)
                                return
                            print(f"\n🎬 {girl.name} has officially signed with your agency!")
                            print("👏 Welcome to the Hollywood family!")    
                            self.girls.append(girl)
                            self.update()
                            time.sleep(2)
                            self.laphoto(1,False)
                    elif choice == 2:
                        girls=self.checkgirl("la")
                        girl=self.listgirls(girls,"photo")
                        if girl==None:
                            self.laphoto(0,False)
                            return
                        girl.setdefaultrate(7000)
                        print(f"💵 Enter the percentage cut you want to take from shoot:► ", end="")
                        while True:
                            try:
                                cut = int(input())
                                if 0 <= cut <= 100:
                                    break
                                else:
                                    print("❌ Invalid percentage. Please enter a value between 0 and 100.")
                            except ValueError:
                                print("❌ Invalid input. Please enter a valid integer percentage.")
                        girl.photo(cut,self)
                        time.sleep(2)
                        self.laphoto(2,False)
                    elif choice == 3:
                        print(r"""
══════════════════════════════════════════════════════════════════════════════
                      🎥✨ HOLLYWOOD CINEMA ✨🎥
══════════════════════════════════════════════════════════════════════════════

          ★ Where Blockbusters And Superstars Are Born ★

[1] 🎬 Studio Productions
    Create Movies • Hire Cast • Begin Filming

[2] 🍿 Premiere Night
    Release Films • Box Office • Audience Reviews

[3] 👑 Celebrity Partnerships
    Luxury Brands • Commercials • Sponsorships

[4] 🚪 Return

══════════════════════════════════════════════════════════════════════════════
""")
                        while True:
                            try:
                                sub_choice = int(input("Choose an option :► "))
                                if sub_choice in [1, 2, 3, 4]:
                                    break
                                else:
                                    print("❌ Invalid choice. Please select a valid option.")
                            except ValueError:
                                print("❌ Invalid input. Please enter a valid number.")
                        if sub_choice == 4:
                            self.laphoto(0,False)
                            return
                        elif sub_choice == 2:
                            

                            print(r"""
══════════════════════════════════════════════════════════════════════════════
                    🌍 GLOBAL DISTRIBUTION NETWORK 🌍
══════════════════════════════════════════════════════════════════════════════

Choose a city for your next theatrical release.

[1] 🌴 Los Angeles      📦 Distribution Fee : 15% of Budget
[2] 🌊 Miami            📦 Distribution Fee : 12% of Budget
[3] 🎰 Las Vegas        📦 Distribution Fee : 20% of Budget

[0] 🚪 Return

══════════════════════════════════════════════════════════════════════════════
                            """)

                            choice = int(input("Choose ► "))

                            if choice == 0:
                                return

                            elif choice == 1:
                                city = "ReleasedLA"
                                cityname = "Los Angeles"
                                citycode="la"
                                percent = 15

                            elif choice == 2:
                                city = "ReleasedMM"
                                cityname = "Miami"
                                citycode="mm"
                                percent = 12

                            elif choice == 3:
                                city = "ReleasedLV"
                                cityname = "Las Vegas"
                                citycode="lv"
                                percent = 20

                            else:
                                print("❌ Invalid choice.")
                                return


                            print(f"""
══════════════════════════════════════════════════════════════════════════════
                🎬 AVAILABLE FOR {cityname.upper()} 🎬
══════════════════════════════════════════════════════════════════════════════
                            """)

                            allmovies = []
                            

                            with open(filepath("movies.csv"), "r", newline="", encoding="utf-8") as file:

                                reader = csv.DictReader(file)
                                for row in reader:
                                    newmovie=movie(self,row["Name"],row["MovieHouse"],row["Genre"],int(row["Hype"]),0,int(row["Budget"]),row["OriginCity"],row["LeadActress"])
                                    newmovie.releasedla = row["ReleasedLA"]
                                    newmovie.releasedmm = row["ReleasedMM"]
                                    newmovie.releasedlv = row["ReleasedLV"]
                                    newmovie.totalrevenue = int(math.floor(float(row["TotalRevenue"])))
                                    newmovie.netprofit = int(math.floor(float(row["NetProfit"])))
                                    newmovie.status = row["Status"]
                                    newmovie.audiencescore = int(math.floor(float(row["AudienceScore"])))
                                    newmovie.criticscore = int(math.floor(float(row["CriticScore"])))
                                    allmovies.append(newmovie)
                            available=[]
                            num=1
                            for moviex in allmovies:
                                if city == "ReleasedLA" and not moviex.releasedla == "True":
                                    available.append(moviex)
                                    
                                    
                                elif city == "ReleasedMM" and not  moviex.releasedmm == "True":
                                    available.append(moviex)
                                    
                                elif city == "ReleasedLV" and not moviex.releasedlv == "True":
                                    available.append(moviex)

                                else:
                                    continue
                                cost = moviex.budget * percent / 100
                                print(f"""[{num}] 🎬 {moviex.name}    by   {moviex.house} 
    🎭 {moviex.genre}            🔥 Hype: {moviex.hype}/100
    🌟 Starring : {moviex.lead}
    📦 Distribution Fee: ${cost:,}
──────────────────────────────────────────────────────────────────────────────""")
                                num+=1

                            print("[0] 🚪 Return")
                            print("══════════════════════════════════════════════════════════════════════════════")
                            while True:
                                try:
                                    choice = int(input("\nChoose Movie ► "))
                                    if choice == 0:
                                        self.laphoto(3,False)
                                        return
                                    if 1 <= choice <= len(available):
                                        break
                                    else:
                                        print("❌ Invalid choice. Please select a valid option.")
                                except ValueError:
                                    print("❌ Invalid input. Please enter a valid number.")

                            selected = available[choice-1]
                            selected.rerelease(self,citycode)
                            self.update()
                            time.sleep(0.5)
                            self.laphoto(3,False)

                            


                        elif sub_choice==1:
                            print(r"""
══════════════════════════════════════════════════════════════════════════════
                      🔥 NOW TRENDING IN HOLLYWOOD 🔥
══════════════════════════════════════════════════════════════════════════════

      🎬 The hottest scripts are making waves across Hollywood.
          Choose a project before another studio steals it.

──────────────────────────────────────────────────────────────────────────────
""")
                            movielist=[]
                            for i in range(4):
                                a=movie(self)
                                a.market(random.randint(1,3))
                                movielist.append(a)
                                a.output(i+1)
                                
                            while True:
                                try:
                                    choice = int(input("Choose a movie to produce :► "))
                                    if choice in [1, 2, 3, 4]:
                                        break
                                    else:
                                        print("❌ Invalid choice. Please select a valid option.")
                                except ValueError:
                                    print("❌ Invalid input. Please enter a valid number.")
                            movielist[choice-1].proceed(self)
                            self.update()
                            self.laphoto(3,False)
                        elif sub_choice==3:
                            self.actressagency()
                            self.update()
                            self.laphoto(3,False)
                            

                            
                    elif choice == 4:
                        self.la()
                        return
                    else:
                        print("❌ Invalid choice. Please select a valid option.")


                #except:
                    # print("❌ Invalid input. Please enter a valid number.")
                    # continue
                    
        pass
    def actressagency(self):
        

        

        career = {}

        # ───────────────────────────────────────────────
        # READ MOVIES DATABASE
        # ───────────────────────────────────────────────

        with open(filepath("movies.csv"), "r", newline="", encoding="utf-8") as file:
            if self.city=="la":
                show="HOLLYWOOD"
            elif self.city=="mm":
                show="VICE"

            reader = csv.DictReader(file)

            for row in reader:

                lead = row["LeadActress"].strip()

                if lead == "":
                    continue

                if lead not in career:

                    career[lead] = {
                        "leads": 0,
                        "hits": 0,
                        "flops": 0,
                        "movies": []
                    }

                career[lead]["leads"] += 1

                career[lead]["movies"].append(
                    f'{row["Name"]} ({row["Genre"]})'
                )

                if float(row["NetProfit"]) >= 0:
                    career[lead]["hits"] += 1
                else:
                    career[lead]["flops"] += 1

        actresses = []

        for girl in self.girls:

            if girl.name in career:

                actresses.append((girl, career[girl.name]))
        if len(actresses) == 0:
            

        

            print(f"""
══════════════════════════════════════════════════════════════════════════════

🎬 {show} CASTING AGENCY

No established actresses are currently available.

══════════════════════════════════════════════════════════════════════════════
    """)
            input("Press Enter...")
            return None

        WIDTH = 118
        

        print("╔" + "═"*WIDTH + "╗")
        print(f"║{align_center(f'🎬 {show}   CASTING AGENCY',WIDTH)}║")
        print(f"║{align_center('Hire proven lead actresses for your next blockbuster',WIDTH)}║")
        print("╠" + "═"*WIDTH + "╣")

        print(
            f"║ {'ID':<3}"
            f"│ {'ACTRESS':<24}"
            f"│ {'LEADS':^7}"
            f"│ {'HITS':^6}"
            f"│ {'FLOPS':^7}"
            f"│ {'HIRE FEE':^12}"
            f"│ PREVIOUS MOVIES"
            + " "*(31)
            + "║"
        )

        print("╠" + "═"*WIDTH + "╣")

        for i, (girl, info) in enumerate(actresses, 1):

            fee = girl.defaultrate * info["leads"]

            movies = ", ".join(info["movies"])

            if len(movies) > 41:
                movies = movies[:41] + "..."

            print(
                f"║ {i:<3}"
                f"│ {pad(girl.flag+' '+girl.name,24)}"
                f"│ {info['leads']:^7}"
                f"│ {info['hits']:^6}"
                f"│ {info['flops']:^7}"
                f"│ ${fee:>11,}"
                f"│ {pad(movies,44)}  ║"
            )

        print("╠" + "═"*WIDTH + "╣")
        print(f"║ {'[0] 🚪 Return':<{WIDTH-2}}║")
        print("╚" + "═"*WIDTH + "╝")

        while True:

            try:
                choice = int(input("\nChoose Actress ► "))
            except:
                print("❌ Invalid Choice.")
                continue

            if choice == 0:
                return None

            if 1 <= choice <= len(actresses):

                girl, info = actresses[choice-1]

                fee = girl.defaultrate * info["leads"]

                print("\n" + "═"*78)
                print(f"🎬 {girl.flag} {girl.name}")
                print("═"*78)

                print(f"⭐ Lead Roles : {info['leads']}")
                print(f"🌟 Box Office Hits : {info['hits']}")
                print(f"💀 Box Office Flops : {info['flops']}")
                print(f"💰 Hiring Fee : ${fee:,}")

                print("\n🎥 Filmography\n")

                for n, movie in enumerate(info["movies"],1):

                    print(f"   {n}. {movie}")

                print("\n══════════════════════════════════════════════════════════════")

                if self.coin < fee:

                    print(f"""
❌ Not enough money.

Required : ${fee:,}
Available: ${self.coin:,}
""")
                    input("Press Enter...")
                    return None
                while True:
                    try:
                        ask = input("\nHire this actress? (y/n) ► ").lower()
                        break
                    except:
                        print("❌ Invalid Choice.")
                        continue

                if ask == "y":
                    with open("D:\\py things\\python  dem\\flirt.json", "r", encoding="utf-8") as f:
                        data = json.load(f)
                        company=data["company"]


                    print("""
══════════════════════════════════════════════════════════════════════════════
                        💼 BRAND ENDORSEMENT OFFERS
══════════════════════════════════════════════════════════════════════════════

Top luxury companies have shown interest in your actress.
Choose a campaign to negotiate.

""")

                    offers = random.sample(company, 4)
                    brandlogo = (["👑","💎","✨","🌹","💄","🧴","🫧","🧼","🌸","💖","💝","🕯️","🛁","🌺","🪷","🍷","🎀","👠","👜","💋","🥂","🌟","🏆","🎖️","🌙","☀️","🌴","🌊","🎬","🎰"])
                    logos=random.sample(brandlogo,4)

                    for i, deal in enumerate(offers, 1):

                        payout = girl.defaultrate * random.randint(8, 15)

                        deal["offer"] = payout
                        
                        print(f"""[{i}] {logos[i-1]} {deal["name"]}
    💰 Campaign Value : ${payout:,}
──────────────────────────────────────────────────────────────────────────────""")

                    print("[0] 🚪 Return")
                    print("══════════════════════════════════════════════════════════════════════════════")

                    choice = int(input("\nChoose Campaign ► "))

                    if choice == 0:
                        return

                    selected = offers[choice-1]

                    print("\n" + "═"*78)
                    print(random.choice(selected["brandambassador"]).replace("{self.name}", girl.name).replace("**",""))
                    print("═"*78)

                    print(f"""
💰 Brand Offer : ${selected["offer"]:,}
How much percentage should {girl.name} receive?
""")

                    while True:

                        try:
                            cut = int(input("🎭 Actress Cut (%) ► "))
                        except:
                            print("❌ Enter a valid percentage.")
                            continue

                        if 0 <= cut <= 100:
                            break

                        print("❌ Percentage must be between 0 and 100.")

                    accept = random.randint(35,95)

                    print("\nNegotiating with executives... 📞")

                    time.sleep(2)

                    if cut <= accept:

                        actresspay = selected["offer"] * cut // 100
                        studiopay = selected["offer"] - actresspay

                        print(f"""
══════════════════════════════════════════════════════════════════════════════

                    🤝 CONTRACT SIGNED!

🏢 Company         : {selected["name"]}

💵 Campaign Value  : ${selected["offer"]:,}

👠 {girl.name}'s Cut : {cut}%
💰 Actress Earned  : ${actresspay:,}
🏦 Studio Earned   : ${studiopay:,}

══════════════════════════════════════════════════════════════════════════════
""")

                        self.coin += studiopay
                        return

                    else:

                        print(f"""
══════════════════════════════════════════════════════════════════════════════

                    ❌ NEGOTIATION FAILED

🏢 {selected["name"]} rejected the demand.

The executives felt the requested share was unrealistic.

══════════════════════════════════════════════════════════════════════════════
""")

            else:
                print("❌ Invalid Choice.")
    def laclub(self):
        pass
        
    def lashop(self,redirect=0):
        avg = 0
        count = 0

        for client in self.clients:
            if client.city == "la":
                avg += client.trust
                count += 1

        avg //= count

        if avg < 20:
            status = "Unknown Face"
        elif avg < 40:
            status = "Rising Prospect"
        elif avg < 60:
            status = "Hollywood Insider"
        elif avg < 80:
            status = "Celebrity Favorite"
        elif avg < 95:
            status = "Hollywood Elite"
        else:
            status = "Living Legend"
        
        if redirect ==0:
            print(f'''
═══════════════════════════════════════════════════════════════
                    ✦ HOLLYWOOD HOUSE OF GLAM ✦
                   ✨ Where Icons Are Created ✨
═══════════════════════════════════════════════════════════════

    ┌───────────────────────────────────────────────────────┐
    │ ⭐ 1. Signature Collection                            │
    │    Hollywood-exclusive luxury outfits & accessories.  │
    ├───────────────────────────────────────────────────────┤
    │ 💋 2. Beauty Atelier                                  │
    │    Premium cosmetic enhancements & transformations.   │
    ├───────────────────────────────────────────────────────┤
    │ 👜 3. Essentials Collection                           │
    │    Protection, accessories & everyday necessities.    │
    ├───────────────────────────────────────────────────────┤
    │ 🪞  4. Vanity Suite                                    │
    │    Dress your stars for the spotlight.                │
    ├───────────────────────────────────────────────────────┤
    │ 🌴 5. Return                                          │
    └───────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════

      💰 Cash             : ${self.coin}
      🌟 Hollywood Status : {status}

═══════════════════════════════════════════════════════════════
''', end="\n")
        try:
            while True:
                num=int(input("Choose a service ►")) if redirect==0 else redirect
                if num not in [1, 2, 3, 4, 5]:
                    print("❌ Invalid service selected. Please choose a valid option.")
                    continue
                break           
            if num==5:
                self.la()
                return
            elif num==1:
                print(f'''
══════════════════════════════════════════════════════════════════════════════
                         ✦ HOUSE OF GLAM COUTURE ✦
                      Hollywood Signature Collection
══════════════════════════════════════════════════════════════════════════════
''')
                self.shopbox("laitem")
            elif num==2:
                print(f'''
══════════════════════════════════════════════════════════════════════════════
                         ✦ HOUSE OF GLAM COUTURE ✦
                         Hollywood Beauty Atelier
══════════════════════════════════════════════════════════════════════════════
''')
                self.shopbox("labeauty")
            elif num==3:
                print(f'''
══════════════════════════════════════════════════════════════════════════════
                         ✦ HOUSE OF GLAM COUTURE ✦
                           Hollywood Essentials 
══════════════════════════════════════════════════════════════════════════════
''')
                self.shopbox("ess")
            elif num==4:
                print(f'''
══════════════════════════════════════════════════════════════════════════════
                         ✦ HOUSE OF GLAM COUTURE ✦
                           Hollywood Vanity Suite
══════════════════════════════════════════════════════════════════════════════
''')
                girl=self.listgirls(self.checkgirl("la"))
                if girl==None:
                    self.lashop()
                    return
                self.rejuvenate(girl)
            else:
                print("❌ Invalid service selected.")
                return

            

            while True:
                try:     
                   
                    choice = int(input("Choose an item :► "))
                    if (choice == 6 and num in [1, 3]) or (choice == 4 and num == 2):
                        break

                        
                    elif num==1 and 1<=choice <=5:
                        self.purchase("laitem",choice)
                        
                    elif num==2 and 1<=choice <=3:
                        self.purchase("labeauty",choice)
                        
                        time.sleep(1.5)
                        self.lashop(2)
                        
                    elif num==3 and 1<=choice <=5:
                        
                        self.purchase("ess",choice)
                    else :
                        print("❌ Invalid choice. Please select a valid item number.")
                    
                except Exception as e:
                    print(e)
                      
                    print("bruh that aint a number -_- flag here")
                
            self.lashop()
        except:
            print("bruh that aint a number -_- flag")
    def labank(self):
        print(f'''
══════════════════════════════════════════════════════════════════════════════

                 🏦 PACIFIC CROWN PRIVATE BANK 🏦

══════════════════════════════════════════════════════════════════════════════

              "Where Hollywood Builds Empires"

          🌴 Beverly Hills • Los Angeles • Since 1982

                 ╭──────────────────────────────╮
                 │   Welcome, Esteemed Client.  │
                 │  Prestige Begins with Wealth │
                 ╰──────────────────────────────╯

💰 Available Balance : ${self.coin}
🏦 Outstanding Loan  : ${self.loan}
📈 Interest Rate     : 5% / Collection
⭐ Client Status      : Platinum
══════════════════════════════════════════════════════════════════════

        📈 Interest Rate     : 5% / Collection
        ⭐ Client Status      : Platinum

═══════════════════════════════════════════════════════════════

    [1] 💵 Apply for a Loan
    [2] 💳 Repay Outstanding Debt
    [3] 📊 View Financial Report
    [4] 🚪 Return

═══════════════════════════════════════════════════════════════''')
        
        try:
            num=int(input())
            if num==1:
                self.addloan()
            elif num==2:
                self.volrepay()
            elif num==3:
                self.viewfinancialreport()
            elif num==4:
                pass
            self.la()
        except Exception as e:
            print(e)
            
            print("bruh that aint a number -_-")
            return
    def lasky(self):
        print(f'''
══════════════════════════════════════════════════════════════════════════════
                    🌇 SKYLINE SOCIAL CLUB 🌇
               "Where Hollywood's Future Begins."
══════════════════════════════════════════════════════════════════════════════

[1] ☕ Skyline Café          $8,000
[2] 🌅 Skyline Terrace       $25,000
[3] 🌃 Skyline Rooftop       $40,000
[4] 🚪 Return
══════════════════════════════════════════════════════════════════════════════
''')
        #try:
        if True:
            choice = int(input("Choose Floor ► "))
            if choice == 4:
                self.la()
                return
            elif choice == 1:
                self.skylinecafe()
            elif choice == 2:
                self.skylineterrace()
            elif choice == 3:
                self.skylinerooftop()
            else:
                print("❌ Invalid floor.")
        #except:
            #print("❌ Invalid input.")
        #self.lasky()

    def skylinecafe(self):
        girlreview=0
        print(f'''
══════════════════════════════════════════════════════════════════════════════
                    ☕ SKYLINE CAFÉ ☕
          "Hollywood Rumors Shape Tomorrow's Stars"
══════════════════════════════════════════════════════════════════════════════

Entry Fee : $8,000
''')
        if self.coin < 8000:
            print("❌ Insufficient funds for entry.")
            input("Press Enter...")
            return
        self.coin -= 8000
        available = [g for g in self.girls if g.city == "la" and not g.jail]
        if available==[]:
            print("❌ No girls available in Los Angeles.")
            input("Press Enter...")
            self.update()
            return
        girl = self.listgirls(available)
        if girl is None:
            self.coin += 8000
            return
        with open("D:\\py things\\python  dem\\flirt.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            rumorcafe = data.get("rumorcafe")
            for reviews in rumorcafe:
                if girl.persona2==reviews["persona2"]:
                    rumors=reviews
            
        print("\nSettling in for deep Hollywood gossip...\n")
        for _ in range(30):
            if random.random() < 0.5:
                rumor = random.choice(rumors.get("positive"))
                print(f"📰 Positive Rumor: {rumor}")
                girlreview += 1
            else:
                rumor = random.choice(rumors.get("negative", ["Some concerns about her attitude."]))
                print(f"📰 Negative Rumor: {rumor}")
                girlreview -= 1
            if girlreview >= 2:
                boost = min(1, girlreview // 2)
                old = girl.level
                girl.level = min(30, girl.level + boost)
                girlreview = 0
                print(f"🌟 Confidence surged! Level {old} → {girl.level}")
            elif girlreview <= -2:
                drop = min(1, abs(girlreview) // 2)
                old = girl.level
                girl.level = max(1, girl.level - drop)
                girlreview = 0
                print(f"💔 Confidence shaken... Level {old} → {girl.level}")
            time.sleep(2)
        print(f"\n📊 Final Rumor Score: {girlreview}")
        girl.getboost()
        self.update()
        input("\nPress Enter to continue...")
        self.la()

    def skylineterrace(self):
        print(f'''
══════════════════════════════════════════════════════════════════════════════
                    🌅 SKYLINE TERRACE 🌅
          "Sunset Outings for Personal Growth"
══════════════════════════════════════════════════════════════════════════════

Entry Fee : $25,000
''')
        if self.coin < 25000:
            print("❌ Insufficient funds for entry.")
            input("Press Enter...")
            return
        self.coin -= 25000
        available = [g for g in self.girls if g.city == "la" and not g.jail and not g.preg and g.level < 30]
        if not available:
            print("❌ No girls need relaxation right now.")
            input("Press Enter...")
            self.update()
            return
        selected = self.listgirlsmult(available, "party", limit=min(5, len(available)))
        if selected is None:
            self.coin += 25000
            return
        print("\nThe girls enjoy a beautiful sunset outing...\n")
        for girl in selected:
            if girl.level < 30:
                boost = random.randint(1, 3)
                old = girl.level
                girl.level = min(30, girl.level + boost)
                print(f"💖 {girl.name} feels refreshed! Level {old} → {girl.level}")
        self.update()
        input("\nPress Enter to continue...")
        self.la()

    def skylinerooftop(self):
        print(f'''
══════════════════════════════════════════════════════════════════════════════
                    🌃 SKYLINE ROOFTOP 🌃
          "Live Hollywood Interview Spotlight"
══════════════════════════════════════════════════════════════════════════════

Entry Fee : $40,000
''')
        if self.coin < 40000:
            print("❌ Insufficient funds for entry.")
            input("Press Enter...")
            return
        self.coin -= 40000
        available = [g for g in self.girls if g.city == "la" and not g.jail]
        if not available:
            print("❌ No girls available.")
            input("Press Enter...")
            self.update()
            return
        girl = self.listgirls(available)
        if girl is None:
            self.coin += 40000
            return
        with open("D:\\py things\\python  dem\\flirt.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            focusgroup = data.get("focusgroup", [])
        entry = next((e for e in focusgroup if e.get("persona1") == girl.persona1), None)
        if not entry or not entry.get("questions"):
            print("❌ Interview data unavailable.")
            self.coin += 40000
            return
        total_score = 0
        print(f"\n🎤 {girl.name} steps into the spotlight for a live interview...\n")
        time.sleep(1)
        for q in entry["questions"]:
            print(f"Q: {q['question']}")
            for i, ans in enumerate(q["answers"], 1):
                print(f"[{i}] {ans['reply']}")
            while True:
                try:
                    ch = int(input("Choose answer ► "))
                    if 1 <= ch <= 4:
                        total_score += q["answers"][ch-1]["effect"]
                        break
                except:
                    pass
            time.sleep(0.8)
        print(f"\n📊 Final Interview Score: {total_score}")
        if total_score >= 10:
            gain = 10
            rating = "Legendary"
        elif total_score >= 8:
            gain = 5
            rating = "Excellent"
        elif total_score >= 6:
            gain = 2
            rating = "Great"
        elif total_score >= 4:
            gain = 1
            rating = "Good"
        elif total_score >= 2:
            gain = 0
            rating = "Average"
        else:
            gain = -1 if total_score < 0 else 0
            rating = "Terrible" if total_score < 0 else "Poor"
        old = girl.level
        girl.level = min(30, max(1, girl.level + gain))
        print(f"🌟 {rating} Interview! Level {old} → {girl.level}")
        girl.getboost()
        self.update()
        input("\nPress Enter to continue...")  
        self.la()      
            
    def mm(self):
            print(f'''\n\n\n\n\n\n
══════════════════════════════════════════════════════════════════════
                       🌊 MIAMI BEACH 🌊
══════════════════════════════════════════════════════════════════════

          ☀ Ocean Drive • South Beach • Little Havana

           🌴      🌊      🛥      🌴      🌅

        ╭──────────────────────────────────────────╮
        │             MIAMI DISTRICT               │
        ╰──────────────────────────────────────────╯

        🏠 Businesses
        ├── [1] 🍸 South Beach Strip Club
        ├── [2] 🛥 Luxury Yacht Parties
        ├── [3] 🏖 Beach Photoshoot Studio
        ├── [4] 💎 Oceanfront Boutique
        ├── [5] 🏦 Miami National Bank
        ├── [6] ✈ Airport
        ├── [7] 🌐 VIP Network
        └── [8] 🚘 Return to Headquarters

═══════════════════════════════════════════════════════
    Current Girls : {len(self.girls)}
    Available Cash: {self.coin}
    Outstanding Loan: {self.loan}
    Police Heat: MEDIUM
═══════════════════════════════════════════════════════

Choose a destination ►''',end="")  
            try:
                num=int(input())
                if num==8:
                    return
                elif num==2:
                    self.mmyacht()
                    self.update()
                elif num==3:
                    self.mmphoto()
                    self.update()
                elif num==1:
                    self.mmstripclub()
                    self.update()
                elif num==5:
                    self.mmbank()
                    self.update()
                elif num==6:
                    self.airway("mm")
                    self.update()
                elif num==7:
                    self.network()
                
                    
                elif num==4:
                    self.mmshop()
                    self.update()
            except Exception as e:
                print(e)
                
                print("bruh that aint a number -_-")
                return
    def mmstripclub(self):
        isabella = self.clients[4]  # Assuming Isabella Rossi is the fifth client in the list

        # Prestige based on Isabella Rossi's Trust
        if isabella.trust >= 95:
            prestige = 5
            prestigetext = "★★★★★ Star Island Elite"

        elif isabella.trust >= 75:
            prestige = 4
            prestigetext = "★★★★☆ Premier Destination"

        elif isabella.trust >= 55:
            prestige = 3
            prestigetext = "★★★☆☆ Popular Hotspot"

        elif isabella.trust >= 35:
            prestige = 2
            prestigetext = "★★☆☆☆ Rising Venue"

        elif isabella.trust >= 15:
            prestige = 1
            prestigetext = "★☆☆☆☆ Local Attraction"

        else:
            prestige = 0
            prestigetext = "☆☆☆☆☆ Unknown Venue"

        # Crowd Calculation
        crowd = random.randint(1, 5) * 20 * prestige

        if crowd == 0:
            crowdtext = "Deserted"
        elif crowd <= 40:
            crowdtext = "Quiet"
        elif crowd <= 80:
            crowdtext = "Moderate"
        elif crowd <= 200:
            crowdtext = "Busy"
        elif crowd <= 400:
            crowdtext = "Packed"
        else:
            crowdtext = "Overflowing"

        

        print(f"""
══════════════════════════════════════════════════════════════════════════════
                     🍹 SOUTH BEACH STRIP CLUB 🍹
                    "Where Beauty Meets the Beach."
══════════════════════════════════════════════════════════════════════════════

📍 Location            • Ocean Drive • South Beach, Miami
👑 Proprietor          • Isabella Rossi
👥 Crowd Tonight       • {crowdtext} ({crowd} Guests)
⭐ Tonight's Prestige  • {prestigetext}

══════════════════════════════════════════════════════════════════════════════

                           BUILDING DIRECTORY

══════════════════════════════════════════════════════════════════════════════

[1] 🌴 Palm Paradise             • Ground Floor
    ◆ Live Performances ◆ Beach Crowd ◆ Tropical Vibes

[2] 🍹 Ocean Lounge              • First Floor
    ◆ Private Suites ◆ Luxury Guests ◆ Premium Bookings

[3] 🛥 Yacht Club                • Second Floor
    ◆ Millionaire Clients ◆ VIP Parties ◆ Ocean Contracts

[4] 🌊 Skyline Terrace           • Third Floor
    ◆ Café Dating ◆ Elite Matchmaking ◆ Sunset Lounge

[0] 🚪 Return

══════════════════════════════════════════════════════════════════════════════
""")

        while True:
                try:
                    choice = int(input(" Select Destination :► "))

                    if choice == 1:
                        girls=self.checkgirl("mmstrip")
                        girl=self.listgirls(girls,"strip")
                        if girl==None:
                            self.mmstripclub()
                            return
                        girl.setdefaultrate(70)
                        clientlist=[]
                        t=0
                        if crowd == 0:
                            crowdtext = "Deserted"
                        elif crowd <= 40:
                            crowdtext = "Quiet"
                            t=1
                        elif crowd <= 80:
                            crowdtext = "Moderate"
                            t=2
                        elif crowd <= 200:
                            crowdtext = "Busy"
                            t=3
                        elif crowd <= 400:
                            crowdtext = "Packed"
                            t=4
                        else:
                            crowdtext = "Overflowing"
                            t=5
                        for i in range(t):
                            clientlist.append(self.randomclient())
                        print(f"💵 Enter the percentage cut you want to take from crowd's payment:► ", end="")
                        while True:
                            try:
                                cut = int(input())
                                if 0 <= cut <= 100:
                                    break
                                else:
                                    print("❌ Invalid percentage. Please enter a value between 0 and 100.")
                            except ValueError:
                                print("❌ Invalid input. Please enter a valid integer percentage.")
                        
                        girl.strip(clientlist,crowd,cut,self)
                        girl.setdefaultrate(self.defaultrate)
                        time.sleep(2)
                        self.mmstripclub()
                        
                        
                        

                    elif choice == 2:
                        girls=self.checkgirl("mm")
                        girl=self.listgirls(girls,"pimp")
                        if girl==None:
                            self.mmstripclub()
                            return
                        girl.setdefaultrate(5000)
                        sampleclient=self.randomclient()
                        print(f"💼 {sampleclient.name} has requested a private session with {girl.name}")
                        print(f"👤 The standard of {sampleclient.name} is {sampleclient.getstandard()}")
                        print(f"💵 Enter the percentage cut you want to take from {sampleclient.name}'s payment:► ", end="")
                        while True:
                            try:
                                cut = int(input())
                                if 0 <= cut <= 100:
                                    break
                                else:
                                    print("❌ Invalid percentage. Please enter a value between 0 and 100.")
                            except ValueError:
                                print("❌ Invalid input. Please enter a valid integer percentage.")
                        
                        girl.sex(sampleclient, cut, self)
                        isabella.updatetrust(5)
                        girl.setdefaultrate(self.defaultrate)
                        time.sleep(2)
                        self.mmstripclub()
                        
                        
                        
                        pass

                    elif choice == 3:
                        
                        print("\n══════════════════════════════════════════════════════════════════════════════")
                        print(f"{'🛥 Yacht Club Reservation 🛥':^78}")
                        print("══════════════════════════════════════════════════════════════════════════════")
                        print("⚓ Reservation Fee : $5000")
                        print("🤝 VIP Commission  : Fixed 30%")

                        print()

                        print("⚠ IMPORTANT")
                        print("• Booking does NOT guarantee meeting a VIP.")
                        print("• Staff will attempt to invite yacht guests.")
                        print("• Maximum Attempts : 5")
                        print("• Reservation fee is NON-REFUNDABLE.")
                        print("══════════════════════════════════════════════════════════════════════════════")
                        print("[1] 🛥 Reserve Yacht Club")
                        print("[0] ↩ Return")
                        print("══════════════════════════════════════════════════════════════════════════════")
                        try:
                            book = int(input("Choose ► "))
                        except:
                            continue

                        if book == 0:
                            self.mmstripclub()
                            continue

                        if self.coin < 5000:
                            print("\n❌ You don't have enough money to reserve the Yacht Club.")
                            time.sleep(2)
                            continue

                        self.coin -= 5000

                        girls = self.checkgirl("mm")
                        girl = self.listgirls(girls, "vipsex")

                        if girl is None:
                            self.coin += 5000
                            self.mmstripclub()
                            continue

                        girl.setdefaultrate(30000)

                        print("\n💎 Reserving Yacht Club...")
                        isabella.updatetrust(5)
                        time.sleep(1.5)

                        print("📨 Sending invitations to Hollywood VIPs...")
                        time.sleep(2)

                        success = False
                        vip = None

                        for attempt in range(1, 6):

                            print(f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                            print(f"Attempt {attempt}/5")
                            print("Searching", end="", flush=True)

                            for _ in range(6):
                                time.sleep(0.4)
                                print(".", end="", flush=True)

                            print()

                            vip = random.choices(
                                [
                                    self.clients[4],
                                    self.clients[5],
                                    self.clients[6],
                                    self.clients[7],
                                    None
                                ],
                                weights=[
                                    max(self.clients[4].trust, 5),
                                    max(self.clients[5].trust, 5),
                                    max(self.clients[6].trust, 5),
                                    max(self.clients[7].trust, 5),
                                    100
                                ],
                                k=1
                            )[0]

                            if vip is None:
                                print("❌ No VIP accepted the invitation.")
                                time.sleep(1.5)
                                continue

                            success = True
                            break

                        if success:

                            print("\n═══════════════════════════════════════════════")
                            print("🎉 VIP FOUND!")
                            print("═══════════════════════════════════════════════\n")

                            print(f"👑 {vip.name} has arrived.")
                            print(f"💼 {vip.occupation}")
                            print(f"⭐ Standard : {vip.getstandard()}")
                            print(f"🤝 Trust : {vip.trust}/100\n")

                            print("Agency Cut has been fixed at 30%.")
                            

                            girl.sex(vip, 30, self,True)
                            # Store whether this VIP was previously undiscovered
                            newvip = (vip.trust == 0)

                            

                            # Unlock animation if first encounter
                            if newvip:

                                print("""
══════════════════════════════════════════════════════════════════════════════
                        🌟 NEW VIP DISCOVERED 🌟
══════════════════════════════════════════════════════════════════════════════
                            """)

                                time.sleep(1.5)

                                print("🔍 Updating Network Database", end="", flush=True)

                                for _ in range(6):
                                    time.sleep(0.4)
                                    print(".", end="", flush=True)

                                print()

                                time.sleep(1)

                                print(f"""
🎉 Congratulations!

👑 {vip.name}
💼 {vip.occupation}

has been added to your exclusive Los Angeles VIP Network.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✔ Future encounters unlocked
✔ VIP profile unlocked
✔ Trust progression unlocked

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

                                

                            # Increase trust after the first meeting
                            vip.updatetrust(5)

                            self.update()

                            

                        else:

                            print("""
══════════════════════════════════════════════════════════════

💔 Unfortunately none of the invited VIPs accepted tonight.

The Crimson Room reservation has expired.

Unfortunately the booking fee is non-refundable.

Better luck next time.

══════════════════════════════════════════════════════════════
""")

                        girl.setdefaultrate(self.defaultrate)

                        self.update()

                        time.sleep(2)

                        self.mmstripclub()
                        return
                        
                        

                        

                    elif choice == 4:

                        isabella = self.clients[4]

                        # ──────────────────────────────────────────────────────────────
                        # Trust Requirement
                        # ──────────────────────────────────────────────────────────────
                        if isabella.trust < 70:

                            print(f"""
══════════════════════════════════════════════════════════════════════════════
                         🌊 SKYLINE TERRACE 🌊
                      South Beach Celebrity Circle
══════════════════════════════════════════════════════════════════════════════

🔒 ACCESS DENIED

Isabella Rossi doesn't trust your agency enough
to introduce you to South Beach's elite social circle.

Only agencies with exceptional reputation and loyalty
are granted access to this exclusive members-only lounge.
(gain trust in Yacht Club)

──────────────────────────────────────────────────────────────────────────────

Required Trust : 70
Current Trust  : {isabella.trust}

──────────────────────────────────────────────────────────────────────────────

💬 Isabella Rossi

"Earn my trust first.
Miami's elite don't socialize with strangers."

══════════════════════════════════════════════════════════════════════════════
""")

                            input("Press Enter to Return...")
                            self.mmstripclub()
                            return

                        # ──────────────────────────────────────────────────────────────
                        # Menu
                        # ──────────────────────────────────────────────────────────────

                        print("""
══════════════════════════════════════════════════════════════════════════════
                       🌊 SKYLINE TERRACE
                 South Beach Celebrity Circle
══════════════════════════════════════════════════════════════════════════════

Reservation Fee : $60000

Isabella Rossi will privately contact her exclusive
South Beach network in search of celebrities interested
in joining your agency.

⚠ Reservation fee is NON-REFUNDABLE.

[1] Begin Celebrity Search
[0] Return

══════════════════════════════════════════════════════════════════════════════
""")
                        while True:
                            try:
                                choice = int(input("Choose ► "))
                                break
                            except:
                                print("❌ Invalid input. Please enter a valid number.")
                                continue

                        if choice == 0:
                            self.mmstripclub()
                            return

                        if self.coin < 60000:
                            print("\n❌ You don't have enough money.")
                            time.sleep(2)
                            self.mmstripclub()
                            return

                        self.coin -= 60000
                        isabella.updatetrust(5)

                        print("\nIsabella Rossi has activated her South Beach connections.\n")

                        print("Please wait", end="", flush=True)

                        for i in range(6):
                            time.sleep(0.5)
                            print(".", end="", flush=True)

                        print("\n")

                        # ──────────────────────────────────────────────────────────────
                        # Hidden Search
                        # ──────────────────────────────────────────────────────────────

                        found = []

                        for i in range(10):
                            print(len(found))

                            # 1 in 3 chance
                            if not random.randint(1, 3) == 1:
                                continue

                            celeb = self.randomgirl(1,True)

                            duplicate = False

                            # Already recruited?
                            for girl in self.girls:
                                if girl.name == celeb.name:
                                    duplicate = True
                                    break

                            # Already found during THIS search?
                            if not duplicate:
                                for girl in found:
                                    if girl.name == celeb.name:
                                        duplicate = True
                                        break

                            if duplicate:
                                continue

                            found.append(celeb)
                            

                            if len(found) == 4 and not found == []:
                                break

                                

                        # ──────────────────────────────────────────────────────────────
                        # Nobody Found
                        # ──────────────────────────────────────────────────────────────

                        if len(found) == 0:

                            print("""
══════════════════════════════════════════════════════════════════════════════

Unfortunately none of the contacted celebrities
accepted Isabella's invitation.

The scouting fee has been consumed.

Isabella Rossi:
"South Beach never guarantees success."

══════════════════════════════════════════════════════════════════════════════
                    """)

                            self.update()
                            time.sleep(2)
                            self.mmstripclub()
                            return

                        # ──────────────────────────────────────────────────────────────
                        # Celebrity Selection
                        # ──────────────────────────────────────────────────────────────

                        print("""
══════════════════════════════════════════════════════════════════════════════

Several celebrities have expressed interest
in joining your agency.

Choose one to negotiate with.

══════════════════════════════════════════════════════════════════════════════
                    """)

                        girl = self.listgirls(found, "celebrity")

                        if girl is None:
                            return

                        self.girls.append(girl)

                        print(f"""
══════════════════════════════════════════════════════════════════════════════

🎉 Congratulations!

⭐ {girl.name} has officially joined your agency.

South Beach's elite have begun recognizing your influence.

══════════════════════════════════════════════════════════════════════════════
                    """)

                        self.update()

                        time.sleep(2)
                        self.mmstripclub()
                    
                        pass

                    elif choice == 0:
                        self.mm()
                        return

                    else:
                        print("❌ Invalid Choice!")
                

                except Exception as e:
                     print (e)
                     print("❌ Please enter a valid number!")
    def mmphoto(self,redirect=0,skipper=True):
        signedcelebs = 0

        for girl in self.girls:
            if girl.effectivelevel >= 40:
                signedcelebs += 1

        owner = self.clients[1]
        if skipper:
            print(r"""
                        ██╗   ██╗██╗ ██████╗███████╗
                        ██║   ██║██║██╔════╝██╔════╝
                        ██║   ██║██║██║     █████╗
                        ╚██╗ ██╔╝██║██║     ██╔══╝
                         ╚████╔╝ ██║╚██████╗███████╗
                          ╚═══╝  ╚═╝ ╚═════╝╚══════╝
══════════════════════════════════════════════════════════════════════════════
                           ★ SUN • SURF • SIN ★
══════════════════════════════════════════════════════════════════════════════""")
            for i in range(39):
                x = ["🌊", "🏖️", "🛥️", "🌴", "🍹"]
                print(x[i%5], end="", flush=True)
                time.sleep(1.7 / 39)   # Total animation ≈ 1.7 seconds

            print()
        if redirect==0:
            print(fr"""
══════════════════════════════════════════════════════════════════════════════
                          🎬 SOUTH BEACH STUDIOS
══════════════════════════════════════════════════════════════════════════════

        ★ Welcome to the World's Greatest Entertainment Hub ★

Studio Owner      : {owner.name}
Reputation        : {owner.trust}/100
Signed Celebrities: {signedcelebs}

──────────────────────────────────────────────────────────────────────────────

[1] 🌴 Vice Recruitment
    Fresh Faces • Agency Contracts • Rising Stars

[2] 📸 Vice Photoshoots
    Designer Brands • Cover Shoots • Prestige

[3] 🌅 Vice Auditions
    Luxury Contracts • Casting Calls • Stardom

[4] 🚪 Return

──────────────────────────────────────────────────────────────────────────────

      "Every superstar was once an unknown face."

══════════════════════════════════════════════════════════════════════════════
""")
        while True:
                # try:
                    choice = int(input(" Select Destination :► ")) if redirect==0 else redirect
                    if choice == 1:
                        print(r"""
══════════════════════════════════════════════════════════════════════════════
                    👙✨ BOOBY RECRUITMENT ✨👙
══════════════════════════════════════════════════════════════════════════════

           🥥 Discover the next generation of Hollywood talent. 🥥

[1] 👑 VIP Society
    Heiresses • Celebrity Circle • Elite Beauties            💰 $60,000

[2] 📱 Creator Space
    Influencers • Lifestyle Creators • Internet Stars        💰 $30,000

[3] 🎬 Studio Talent
    Models • Dancers • Aspiring Actresses                    💰 $15,000

[4] 🎓 College Circuit
    College Girls • Campus Leaders • Exchange Students       💰 $7,500

[5] ☕ Everyday Life
    Professionals • Baristas • Hidden Gems                   💰 $3,000

[6] 🚪 Return

══════════════════════════════════════════════════════════════════════════════
""")
                        while True:
                            try:
                                sub_choice = int(input("Choose a recruitment tier :► "))
                                if sub_choice in [1, 2, 3, 4, 5, 6]:
                                    break
                                else:
                                    print("❌ Invalid choice. Please select a valid option.")
                            except ValueError:
                                print("❌ Invalid input. Please enter a valid number.")
                        if sub_choice == 6:
                            self.mmphoto(0,False)
                            return
                        if self.coin < [60000, 30000, 15000, 7500, 3000][sub_choice - 1]:
                            print("❌ Insufficient funds for this recruitment tier.")
                            continue
                        self.coin -= [60000, 30000, 15000, 7500, 3000][sub_choice - 1]
                        if sub_choice == 6:
                            self.mmphoto(0,False)
                        elif sub_choice in [1, 2, 3, 4, 5]:
                            females=self.recruitgirls(4,sub_choice)
                            girl=self.recruitlist(females)
                            if girl == None:
                                self.mmphoto(1,False)
                                return
                            print(f"\n🎬 {girl.name} has officially signed with your agency!")
                            print("👏 Welcome to the Hollywood family!")    
                            self.girls.append(girl)
                            self.update()
                            time.sleep(2)
                            self.mmphoto(1,False)
                    elif choice == 2:
                        girls=self.checkgirl("mm")
                        girl=self.listgirls(girls,"photo")
                        if girl==None:
                            self.mmphoto(0,False)
                            return
                        girl.setdefaultrate(7000)
                        print(f"💵 Enter the percentage cut you want to take from shoot:► ", end="")
                        while True:
                            try:
                                cut = int(input())
                                if 0 <= cut <= 100:
                                    break
                                else:
                                    print("❌ Invalid percentage. Please enter a value between 0 and 100.")
                            except ValueError:
                                print("❌ Invalid input. Please enter a valid integer percentage.")
                        girl.photo(cut,self)
                        time.sleep(2)
                        self.mmphoto(2,False)
                    elif choice == 3:
                        print(r"""
══════════════════════════════════════════════════════════════════════════════
                        🌴✨  VICE  ✨🌴
                ★ Where Legends Meet The Sunset ★
══════════════════════════════════════════════════════════════════════════════
                

[1] 🌊 Beach Productions
    Create Campaigns • Hire Talent • Begin Shooting

[2] 🍹 Sunset Premiere
    Launch Projects • Public Buzz • Audience Reviews

[3] 🌅 Vice Collaborations
    Luxury Brands • Influencers • Sponsorships

[4] 🚪 Return

══════════════════════════════════════════════════════════════════════════════
""")
                        while True:
                            try:
                                sub_choice = int(input("Choose an option :► "))
                                if sub_choice in [1, 2, 3, 4]:
                                    break
                                else:
                                    print("❌ Invalid choice. Please select a valid option.")
                            except ValueError:
                                print("❌ Invalid input. Please enter a valid number.")
                        if sub_choice == 4:
                            self.mmphoto(0,False)
                            return
                        elif sub_choice == 2:
                            

                            print(r"""
══════════════════════════════════════════════════════════════════════════════
                    🌍 GLOBAL DISTRIBUTION NETWORK 🌍
══════════════════════════════════════════════════════════════════════════════

Choose a city for your next theatrical release.

[1] 🌴 Los Angeles      📦 Distribution Fee : 15% of Budget
[2] 🌊 Miami            📦 Distribution Fee : 12% of Budget
[3] 🎰 Las Vegas        📦 Distribution Fee : 20% of Budget

[0] 🚪 Return

══════════════════════════════════════════════════════════════════════════════
                            """)

                            choice = int(input("Choose ► "))

                            if choice == 0:
                                return

                            elif choice == 1:
                                city = "ReleasedLA"
                                cityname = "Los Angeles"
                                citycode="la"
                                percent = 15

                            elif choice == 2:
                                city = "ReleasedMM"
                                cityname = "Miami"
                                citycode="mm"
                                percent = 12

                            elif choice == 3:
                                city = "ReleasedLV"
                                cityname = "Las Vegas"
                                citycode="lv"
                                percent = 20

                            else:
                                print("❌ Invalid choice.")
                                return


                            print(f"""
══════════════════════════════════════════════════════════════════════════════
                🎬 AVAILABLE FOR {cityname.upper()} 🎬
══════════════════════════════════════════════════════════════════════════════
                            """)

                            allmovies = []
                            

                            with open(filepath("movies.csv"), "r", newline="", encoding="utf-8") as file:

                                reader = csv.DictReader(file)
                                for row in reader:
                                    newmovie=movie(self,row["Name"],row["MovieHouse"],row["Genre"],int(row["Hype"]),0,int(row["Budget"]),row["OriginCity"],row["LeadActress"])
                                    newmovie.releasedla = row["ReleasedLA"]
                                    newmovie.releasedmm = row["ReleasedMM"]
                                    newmovie.releasedlv = row["ReleasedLV"]
                                    newmovie.totalrevenue = int(math.floor(float(row["TotalRevenue"])))
                                    newmovie.netprofit = int(math.floor(float(row["NetProfit"])))
                                    newmovie.status = row["Status"]
                                    newmovie.audiencescore = int(math.floor(float(row["AudienceScore"])))
                                    newmovie.criticscore = int(math.floor(float(row["CriticScore"])))
                                    allmovies.append(newmovie)
                            available=[]
                            num=1
                            for moviex in allmovies:
                                if city == "ReleasedLA" and not moviex.releasedla == "True":
                                    available.append(moviex)
                                    
                                    
                                elif city == "ReleasedMM" and not  moviex.releasedmm == "True":
                                    available.append(moviex)
                                    
                                elif city == "ReleasedLV" and not moviex.releasedlv == "True":
                                    available.append(moviex)

                                else:
                                    continue
                                cost = moviex.budget * percent / 100
                                print(f"""[{num}] 🎬 {moviex.name}    by   {moviex.house} 
    🎭 {moviex.genre}            🔥 Hype: {moviex.hype}/100
    🌟 Starring : {moviex.lead}
    📦 Distribution Fee: ${cost:,}
──────────────────────────────────────────────────────────────────────────────""")
                                num+=1

                            print("[0] 🚪 Return")
                            print("══════════════════════════════════════════════════════════════════════════════")
                            while True:
                                try:
                                    choice = int(input("\nChoose Movie ► "))
                                    if choice == 0:
                                        self.mmphoto(3,False)
                                        return
                                    if 1 <= choice <= len(available):
                                        break
                                    else:
                                        print("❌ Invalid choice. Please select a valid option.")
                                except ValueError:
                                    print("❌ Invalid input. Please enter a valid number.")

                            selected = available[choice-1]
                            selected.rerelease(self,citycode)
                            
                            self.update()
                            time.sleep(0.5)
                            self.mmphoto(3,False)

                            


                        elif sub_choice==1:
                            print(r"""
══════════════════════════════════════════════════════════════════════════════
                      🌴 NOW TRENDING IN VICE 🌴
══════════════════════════════════════════════════════════════════════════════

      🌊 South Beach's hottest opportunities have arrived.
    Sign a campaign before the competition beats you to it.

──────────────────────────────────────────────────────────────────────────────
""")
                            movielist=[]
                            for i in range(4):
                                a=movie(self)
                                a.market(random.randint(1,3))
                                movielist.append(a)
                                a.output(i+1)
                                
                            while True:
                                try:
                                    choice = int(input("Choose a movie to produce :► "))
                                    if choice in [1, 2, 3, 4]:
                                        break
                                    else:
                                        print("❌ Invalid choice. Please select a valid option.")
                                except ValueError:
                                    print("❌ Invalid input. Please enter a valid number.")
                            movielist[choice-1].proceed(self)
                            self.update()
                            self.mmphoto(3,False)
                        elif sub_choice==3:
                            self.actressagency()
                            self.update()
                            self.mmphoto(3,False)
                            

                            
                    elif choice == 4:
                        self.mm()
                        return
                    else:
                        print("❌ Invalid choice. Please select a valid option.")


                #except:
                    # print("❌ Invalid input. Please enter a valid number.")
                    # continue
                    
        pass
    def mmyacht(self):
        origin=self.coin
        
        print(f"""
══════════════════════════════════════════════════════════════════════════════
                      🛥 SOUTH BEACH YACHTS 🛥
               "Luxury Begins Before Departure"
══════════════════════════════════════════════════════════════════════════════

[1] 🌊 Azure Breeze
    Capacity : 3 Girls
    Cost : $40,000
    VIP Bonus: +0

[2] 🛥 Ocean Majesty
    Capacity : 5 Girls
    Cost : $90,000
    VIP Bonus: +8

[3] 👑 Poseidon's Dream
    Capacity : 8 Girls
    Cost : $180,000
    VIP Bonus: +15

[4] 🚪 Return
══════════════════════════════════════════════════════════════════════════════
""")
        while True:
            try:
                yacht_choice = int(input("Choose your yacht ► "))
                if yacht_choice == 4:
                    self.mm()
                    return
                if yacht_choice in [1,2,3]:
                    break
                print("❌ Invalid choice.")
            except:
                print("❌ Please enter a valid number.")
                continue

        yacht_options = [
            None,
            {"name": "Azure Breeze", "capacity": 3, "cost": 40000, "factor": 0},
            {"name": "Ocean Majesty", "capacity": 5, "cost": 90000, "factor": 8},
            {"name": "Poseidon's Dream", "capacity": 8, "cost": 180000, "factor": 15}
        ]
        yacht = yacht_options[yacht_choice]
        if self.coin < yacht["cost"]:
            print(f"""
══════════════════════════════════════════════════════════════════════════════
❌ Insufficient funds for {yacht["name"]}.
💰 Required : ${yacht["cost"]:,}
══════════════════════════════════════════════════════════════════════════════
""")
            input("Press Enter to return...")
            self.mm()
            return
        self.coin -= yacht["cost"]
        yachtfactor = yacht["factor"]
        print(f"✅ {yacht['name']} booked for ${yacht['cost']:,}.")

        # Select girls
        available = [g for g in self.girls if g.city == "mm" and not g.jail and not g.preg]
        if len(available) == 0:
            self.coin=origin
            print("❌ No girls available in Miami.")
            input("Press Enter...")
            self.mm()
            return
        selected = self.listgirlsmult(available, "party", limit=yacht["capacity"])
        if selected is None:
            self.mm()
            return

        for girl in selected:
            girl.partyhealth = 3

        # Alcohol
        print(f"""
══════════════════════════════════════════════════════════════════════════════
🥂 ALCOHOL COLLECTION
══════════════════════════════════════════════════════════════════════════════

[1] 🍺 Imported Beer          Cost : $5,000    Bonus : +4
[2] 🍷 Vintage Wine           Cost : $12,000   Bonus : +8
[3] 🥃 Premium Whiskey        Cost : $20,000   Bonus : +12
[4] 🍾 Dom Pérignon Champagne Cost : $35,000   Bonus : +16
[5] 💎 Billionaire Reserve    Cost : $60,000   Bonus : +20
══════════════════════════════════════════════════════════════════════════════
""")
        while True:
            try:
                alc_choice = int(input("Choose alcohol package ► "))
                if 1 <= alc_choice <= 5:
                    break
            except:
                pass
        alc_options = [None, {"name":"Imported Beer","cost":5000,"factor":4}, {"name":"Vintage Wine","cost":12000,"factor":8}, {"name":"Premium Whiskey","cost":20000,"factor":12}, {"name":"Dom Pérignon Champagne","cost":35000,"factor":16}, {"name":"Billionaire Reserve","cost":60000,"factor":20}]
        alc = alc_options[alc_choice]
        if self.coin < alc["cost"]:
            print("❌ Insufficient funds.")
            self.coin += yacht["cost"]  # refund yacht
            self.coin=origin
            self.mm()
            return
        self.coin -= alc["cost"]
        alcoholfactor = alc["factor"]

        # DJ
        print(f"""
══════════════════════════════════════════════════════════════════════════════
🎧 HIRE A DJ
══════════════════════════════════════════════════════════════════════════════

[1] 🎧 DJ Luna      Cost : $10,000   Bonus : +5
[2] 🔥 DJ Vortex    Cost : $25,000   Bonus : +10
[3] 🌟 DJ Eclipse   Cost : $50,000   Bonus : +15
[4] 🚫 No DJ        Bonus : +0
══════════════════════════════════════════════════════════════════════════════
""")
        while True:
            try:
                dj_choice = int(input("Choose DJ ► "))
                if 1 <= dj_choice <= 4:
                    break
            except:
                pass
        dj_options = [None, {"name":"DJ Luna","cost":10000,"factor":5}, {"name":"DJ Vortex","cost":25000,"factor":10}, {"name":"DJ Eclipse","cost":50000,"factor":15}, {"name":"No DJ","cost":0,"factor":0}]
        dj = dj_options[dj_choice]
        if self.coin < dj["cost"]:
            print("❌ Insufficient funds.")
            self.coin=origin
            # simple refund not implemented for brevity, but follow style
            self.mm()
            return
        self.coin -= dj["cost"]
        djfactor = dj["factor"]

        # Load JSON
        with open("D:\\py things\\python  dem\\flirt.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            yachtline = data.get("yachtline", [])

        # Party start
        print(f"""
══════════════════════════════════════════════════════════════════════════════
                    🌊 LUXURY YACHT PARTY BEGINS 🌊
══════════════════════════════════════════════════════════════════════════════

{yacht['name']} sets sail from South Beach...
{len(selected)} stunning girls aboard.
{alc['name']} flowing. {dj['name']} on the decks.
Golden sunset over the ocean...

""")
        time.sleep(2)

        original_rate = self.defaultrate
        self.defaultrate = 900

        total_income = 0
        events = 0
        vip_count = 0
        active = selected[:]

        atmosphere_msgs = [
            "🌅 The yacht sails beneath a golden sunset.",
            "🌊 Dolphins race beside the yacht.",
            "🍾 Another bottle of Dom Pérignon is opened.",
            "🎧 The DJ drops a new beat.",
            "📸 Influencers livestream the luxury.",
            "🔥 Fire dancers entertain guests.",
            "🛥 Luxury yachts pass nearby.",
            "🌴 South Beach glows in the distance.",
            "💎 A celebrity boards from a speedboat."
        ]

        while active:
            time.sleep(2)
            if random.random() < 0.3:
                print(random.choice(atmosphere_msgs)+"\n")
                time.sleep(0.8)

            girl = random.choice(active)
            client_name = random.choice(["Ethan Brooks","Alexander Hayes","Marcus Kane","Damien Voss","Julian Pierce","Rafael Santos","Leonardo Vale","Sebastian Cross","Dominic Vale","Victor Lang","Prince Omar","Billionaire Ruiz"])

            matching = [entry for entry in yachtline if entry.get("persona1") == girl.persona1]
            if not matching:
                matching = yachtline
            entry = random.choice(matching)

            # Event choice
            categories = ["POUR", "DANCE", "LOVE", "HOOKUP", "SWIMSUIT", "VIP"]
            weights = [50, 50, 50, 50, 50, yachtfactor + alcoholfactor + djfactor]
            event = random.choices(categories, weights=weights, k=1)[0]

            if event == "POUR":
                earnings = 1800*(1+alcoholfactor//4)
                dialogue = random.choice(entry["replies"].get("pour", ["Cheers to the night!"]))
                print(f"🍾 {girl.name} serves premium pour to {client_name}.")
            elif event == "DANCE":
                earnings = 900*(1+djfactor//4)
                dialogue = random.choice(entry["replies"].get("dance", ["The rhythm takes over..."]))
                print(f"💃 {girl.name} dances under the sunset lights.")
            elif event == "LOVE":
                earnings = 2700*(1+girl.effectivelevel//10)
                dialogue = random.choice(entry["replies"].get("love", ["This feels magical..."]))
                print(f"❤️ {girl.name} shares a romantic moment with {client_name}.")
            elif event == "HOOKUP":
                earnings = 2160*(1+girl.effectivelevel//8)
                dialogue = random.choice(entry["replies"].get("hookup", ["Private cabin time..."]))
                print(f"🔥 {girl.name} enjoys a steamy hookup with {client_name}.")
            elif event == "SWIMSUIT":
                earnings = 720*(1+yachtfactor//4)
                dialogue = random.choice(entry["replies"].get("swimsuit", ["Ocean breeze feels perfect..."]))
                print(f"👙 {girl.name} models swimsuit by the pool deck.")
            else:  # VIP
                earnings = 7000*(1+girl.effectivelevel//10)
                vip_count += 1
                dialogue = random.choice(entry["replies"].get("vip", ["VIP treatment for elite guest."]))
                print(f"👑 VIP {client_name} arrives for exclusive time with {girl.name}.")
            time.sleep(1)
            print(f"   {dialogue}")
            print(f"   +${earnings}\n")
            total_income += earnings
            events += 1

            # Stamina
            reduce_chance = 0
            if event == "HOOKUP":
                reduce_chance = 20
            elif event == "DANCE":
                reduce_chance = 15
            elif event == "VIP":
                reduce_chance = 10
            elif random.random() < 0.25:  # drunk chance
                reduce_chance = 100
                print(f"🥂 {girl.name} enjoys too much champagne.")

            if random.randint(1,21) <= reduce_chance:
                girl.partyhealth -= 1

            if girl.partyhealth <= 0:
                print(f"💤 {girl.name} is exhausted and retires to her luxury cabin.")
                active.remove(girl)
                time.sleep(1)

        # Summary
        
        expenses = yacht["cost"] + alc["cost"] + dj["cost"]
        net = total_income
        profit=total_income-expenses
        avg_per_girl = total_income // len(selected) if selected else 0
        mvp = max(selected, key=lambda g: 1)  # placeholder, could track per girl but simple

        print(f"""
══════════════════════════════════════════════════════════════════════════════
                    🌴 SOUTH BEACH YACHT PARTY COMPLETE 🌴
══════════════════════════════════════════════════════════════════════════════

Yacht                  : {yacht['name']}
Alcohol Package        : {alc['name']}
DJ                     : {dj['name']}
Girls Attended         : {len(selected)}
Total Events           : {events}
VIP Encounters         : {vip_count}
Total Earnings         : ${total_income:,}
Expenses               : ${expenses:,}
Net Profit             : ${profit:,}
Average per Girl       : ${avg_per_girl:,}
MVP Girl               : {mvp.name if selected else 'N/A'}
Current Balance        : ${self.coin + net:,}

The yacht returns to port under starlit skies...
""")

        self.coin += net
        self.defaultrate = original_rate
        self.update()
        input("\nPress Enter to return to the Miami Complex...")
        self.mm()
    
    def mmshop(self,redirect=0):
        avg = 0
        count = 0

        for client in self.clients:
            if client.city == "mm":
                avg += client.trust
                count += 1

        avg //= count

        if avg < 20:
            status = "Unknown Face"
        elif avg < 40:
            status = "Rising Prospect"
        elif avg < 60:
            status = "Miami Insider"
        elif avg < 80:
            status = "Beach Favorite"
        elif avg < 95:
            status = "Miami Elite"
        else:
            status = "Living Legend"

        if redirect == 0:
            print(f'''
══════════════════════════════════════════════════════════════════════════════
                   🌊 OCEANFRONT BOUTIQUE 🌊
                ☀️ Where Paradise Meets Luxury ☀️
══════════════════════════════════════════════════════════════════════════════

╭──────────────────────────────────────────────────────────────╮
│ 💎 1. Riviera Couture                                       │
│    Exclusive resort fashion & handcrafted luxury pieces.    │
├──────────────────────────────────────────────────────────────┤
│ 🌺 2. Paradise Beauty Atelier                               │
│    Tropical cosmetic enhancements & radiant transformations.│
├──────────────────────────────────────────────────────────────┤
│ 👜 3. Coastal Essentials                                    │
│    Premium travel accessories & vacation necessities.       │
├──────────────────────────────────────────────────────────────┤
│ 👙 4. Bikini Boulevard                                      │
│    Style the perfect beachside look.              │         │
├──────────────────────────────────────────────────────────────┤             
│ 🌴 4. Return                                                │
╰──────────────────────────────────────────────────────────────╯

══════════════════════════════════════════════════════════════════════════════

        💰 Cash          : ${self.coin}
        🌊 Miami Status  : {status}

══════════════════════════════════════════════════════════════════════════════
''',end="\n")
        try:
            while True: 
                num = int(input("Choose a service ►")) if redirect == 0 else redirect
                if num not in [1, 2, 3, 4, 5]:
                    print("❌ Invalid service selected. Please choose a valid option.")
                    continue
                break
            if num == 5:
                self.mm()
                return

            elif num == 1:
                print(f'''
══════════════════════════════════════════════════════════════════════════════
                        🌊 OCEANFRONT BOUTIQUE 🌊
                            Riviera Couture
══════════════════════════════════════════════════════════════════════════════
        ''')
                self.shopbox("mmitem")

            elif num == 2:
                print(f'''
══════════════════════════════════════════════════════════════════════════════
                        🌊 OCEANFRONT BOUTIQUE 🌊
                        Paradise Beauty Atelier
══════════════════════════════════════════════════════════════════════════════
        ''')
                self.shopbox("mmbeauty")

            elif num == 3:
                print(f'''
══════════════════════════════════════════════════════════════════════════════
                        🌊 OCEANFRONT BOUTIQUE 🌊
                            Coastal Essentials
══════════════════════════════════════════════════════════════════════════════
        ''')
                self.shopbox("ess")
            elif num == 4:
                print(f'''
══════════════════════════════════════════════════════════════════════════════
                        🌊 OCEANFRONT BOUTIQUE 🌊
                            Bikini Boulevard
══════════════════════════════════════════════════════════════════════════════
        ''')
                girl = self.listgirls(self.checkgirl("mm"))
                if girl == None:
                    self.mmshop()
                    return
                self.rejuvenate(girl)

            else:
                print("❌ Invalid service selected.")
                return
            while True:
                try:        
                    choice = int(input("Choose an item :► "))
                    if (choice == 6 and num in [1, 3]) or (choice == 4 and num == 2):
                        break

                        
                    elif num==1 and 1<=choice <=5:
                        self.purchase("mmitem",choice)
                        
                    elif num==2 and 1<=choice <=3:
                        self.purchase("mmbeauty",choice)
                        time.sleep(1.5)
                        self.mmshop(2)
                        
                    elif num==3 and 1<=choice <=5:
                        
                        self.purchase("ess",choice)
                    else :
                        print("Invalid choice. Please select a valid item number.")
                    
                except Exception as e:
                    print(e)
                      
                    print("bruh that aint a number -_- flag here")
            self.mmshop() 

        except Exception as e:
            print(e)
            
            print("bruh that aint a number -_-")
            
    def mmbank(self):
        print(f'''
 ══════════════════════════════════════════════════════════════════════
              🏦 OCEAN CREST PRIVATE BANK 🏦
══════════════════════════════════════════════════════════════════════

             "Where Wealth Meets the Waves"

           🌊 South Beach • Miami • Since 1989

        ╭──────────────────────────────────────────╮
        │      Welcome, Valued Client.             │
        │   Your assets are our highest priority.  │
        ╰──────────────────────────────────────────╯

        💰 Available Balance : ${self.coin}
        🏦 Outstanding Loan  : ${self.loan}
        📈 Interest Rate     : 5% / Collection
        ⭐ Client Status      : Platinum

═══════════════════════════════════════════════════════

    [1] 💵 Apply for a Loan
    [2] 💳 Repay Outstanding Debt
    [3] 📊 View Financial Report
    [4] 🚪 Return

═══════════════════════════════════════════════════════''')
        try:
            num=int(input())
            if num==1:
                self.addloan()
            elif num==2:
                self.volrepay()
            elif num==3:
                self.viewfinancialreport()
            elif num==4:
                
                pass
            self.mm()
        except Exception as e:
            print(e)
            
            print("bruh that aint a number -_-")
            return

    def lv(self):
        print(f'''\n\n\n\n\n\n
══════════════════════════════════════════════════════════════════════
                       🎰 LAS VEGAS 🎰
══════════════════════════════════════════════════════════════════════

          🌃 The Strip • Bellagio • Fremont Street

          🎲      🏨      🎰      🍾      🌆

        ╭──────────────────────────────────────────╮
        │            LAS VEGAS DISTRICT            │
        ╰──────────────────────────────────────────╯

        🏠 Businesses
        ├── [1] 🎭 Platinum Strip Club
        ├── [2] 🎲 VIP Casino Lounge
        ├── [3] 🥂 High Roller Escort Service
        ├── [4] 🍸 Neon Night Club Complex
        ├── [5] 🏦 Vegas Credit Union
        ├── [6] ✈ Airport
        ├── [7] 🌐 VIP Network
        └── [8] 🚘 Return to Headquarters
              
═══════════════════════════════════════════════════════
    Current Girls : {len(self.girls)}
    Available Cash: {self.coin}
    Outstanding Loan: {self.loan}
    Police Heat: HIGH
═══════════════════════════════════════════════════════

Choose a destination ►''',end="")
        try:
            num=int(input())
            if num==8:
                return
            elif num==1:
                self.lvstripclub()
            elif num==2:
                self.lvgamble()
            elif num==3:
                self.lvsex()
            elif num==5:
                self.lvbank()
            elif num==6:
                self.airway("lv")
            elif num==7:
                self.network()
            elif num==4:
                self.lvcomplex()
        except Exception as e:
            print(e)
            
            print("bruh that aint a number -_-")
            return
    def lvstripclub(self):
        marcobellini = self.clients[8]  # Assuming Marco Bellini is the Platinum Strip Club owner

        # Prestige based on Marco Bellini's Trust
        if marcobellini.trust >= 95:
            prestige = 5
            prestigetext = "★★★★★ Vegas Legend"

        elif marcobellini.trust >= 75:
            prestige = 4
            prestigetext = "★★★★☆ High Roller Favorite"

        elif marcobellini.trust >= 55:
            prestige = 3
            prestigetext = "★★★☆☆ Sin City Hotspot"

        elif marcobellini.trust >= 35:
            prestige = 2
            prestigetext = "★★☆☆☆ Rising Neon"

        elif marcobellini.trust >= 15:
            prestige = 1
            prestigetext = "★☆☆☆☆ Underground Gem"

        else:
            prestige = 0
            prestigetext = "☆☆☆☆☆ New Arrival"

        # Crowd Calculation
        crowd = random.randint(1, 5) * 20 * prestige

        if crowd == 0:
            crowdtext = "Empty Floor"
        elif crowd <= 40:
            crowdtext = "Quiet Lounge"
        elif crowd <= 80:
            crowdtext = "Moderate Buzz"
        elif crowd <= 200:
            crowdtext = "Busy Tables"
        elif crowd <= 400:
            crowdtext = "Packed House"
        else:
            crowdtext = "Overflowing VIP"

        

        print(f"""
══════════════════════════════════════════════════════════════════════════════
                        💃 PLATINUM STRIP CLUB 💃
                    "Where Fortune Meets Fantasy on the Strip"
══════════════════════════════════════════════════════════════════════════════

📍 Location            • The Las Vegas Strip
👑 Proprietor          • Marco Bellini
👥 Crowd Tonight       • {crowdtext} ({crowd} Guests)
⭐ Tonight's Prestige  • {prestigetext}

──────────────────────────────────────────────────────────────────────────────
                            BUILDING DIRECTORY
──────────────────────────────────────────────────────────────────────────────

[1] 💃 Main Stage                     • Ground Floor
    ◆ Live Performances ◆ High Energy Crowd ◆ Steady Revenue

[2] 🌙 Midnight Lounge                • First Floor
    ◆ Private Bookings ◆ VIP Tables ◆ Agency Operations

[3] 💎 Diamond Penthouse              • Second Floor
    ◆ High Roller Clients ◆ Luxury Contracts ◆ Elite Entertainment

[4] 🎰 Neon Royale                    • Third Floor
    ◆ Celebrity VIPs ◆ Talent Scouting ◆ Industry Connections

[0] 🚪 Return

══════════════════════════════════════════════════════════════════════════════
""")

        while True:
                try:
                    choice = int(input(" Select Destination :► "))

                    if choice == 1:
                        girls=self.checkgirl("lvstrip")
                        girl=self.listgirls(girls,"strip")
                        if girl==None:
                            self.lvstripclub()
                            return
                        girl.setdefaultrate(80)
                        clientlist=[]
                        t=0
                        if crowd == 0:
                            crowdtext = "Empty Floor"
                        elif crowd <= 40:
                            crowdtext = "Quiet Lounge"
                            t=1
                        elif crowd <= 80:
                            crowdtext = "Moderate Buzz"
                            t=2
                        elif crowd <= 200:
                            crowdtext = "Busy Tables"
                            t=3
                        elif crowd <= 400:
                            crowdtext = "Packed House"
                            t=4
                        else:
                            crowdtext = "Overflowing VIP"
                            t=5
                        for i in range(t):
                            clientlist.append(self.randomclient())
                        print(f"💵 Enter the percentage cut you want to take from crowd's payment:► ", end="")
                        while True:
                            try:
                                cut = int(input())
                                if 0 <= cut <= 100:
                                    break
                                else:
                                    print("❌ Invalid percentage. Please enter a value between 0 and 100.")
                            except ValueError:
                                print("❌ Invalid input. Please enter a valid integer percentage.")
                        
                        girl.strip(clientlist,crowd,cut,self)
                        girl.setdefaultrate(self.defaultrate)
                        time.sleep(2)
                        self.lvstripclub()
                        
                        
                        
                    elif choice == 2:
                        girls=self.checkgirl("lv")
                        girl=self.listgirls(girls,"pimp")
                        if girl==None:
                            self.lvstripclub()
                            return
                        girl.setdefaultrate(6000)
                        sampleclient=self.randomclient()
                        print(f"💼 {sampleclient.name} has requested a private session with {girl.name}")
                        print(f"👤 The standard of {sampleclient.name} is {sampleclient.getstandard()}")
                        print(f"💵 Enter the percentage cut you want to take from {sampleclient.name}'s payment:► ", end="")
                        while True:
                            try:
                                cut = int(input())
                                if 0 <= cut <= 100:
                                    break
                                else:
                                    print("❌ Invalid percentage. Please enter a value between 0 and 100.")
                            except ValueError:
                                print("❌ Invalid input. Please enter a valid integer percentage.")
                        
                        girl.sex(sampleclient, cut, self)
                        marcobellini.updatetrust(5)
                        girl.setdefaultrate(self.defaultrate)
                        time.sleep(2)
                        self.lvstripclub()
                        
                        
                        
                        pass

                    elif choice == 3:
                        
                        print("\n══════════════════════════════════════════════════════════════════════════════")
                        print(f"{'💎 Diamond Penthouse Reservation 💎':^78}")
                        print("══════════════════════════════════════════════════════════════════════════════")
                        print("🏛 Reservation Fee : $8000")
                        print("🤝 VIP Commission  : Fixed 35%")
                        print()
                        print("⚠ IMPORTANT")
                        print("• Booking does NOT guarantee meeting a high roller.")
                        print("• Staff will attempt to invite elite guests.")
                        print("• Maximum Attempts : 5")
                        print("• Reservation fee is NON-REFUNDABLE.")
                        print("══════════════════════════════════════════════════════════════════════════════")
                        print("[1] 💎 Reserve Diamond Penthouse")
                        print("[0] 🔙 Return")
                        print("══════════════════════════════════════════════════════════════════════════════")
                        
                        try:
                            book = int(input("Choose ► "))
                        except:
                            continue

                        if book == 0:
                            self.lvstripclub()
                            continue

                        if self.coin < 8000:
                            print("\n❌ You don't have enough money to reserve the Diamond Penthouse.")
                            time.sleep(2)
                            continue

                        self.coin -= 8000

                        girls = self.checkgirl("lv")
                        girl = self.listgirls(girls, "vipsex")

                        if girl is None:
                            self.coin += 8000
                            continue

                        girl.setdefaultrate(35000)

                        print("\n💎 Reserving Diamond Penthouse...")
                        marcobellini.updatetrust(5)
                        time.sleep(1.5)

                        print("📨 Sending invitations to Vegas high rollers...")
                        time.sleep(2)

                        success = False
                        vip = None

                        for attempt in range(1, 6):

                            print(f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                            print(f"Attempt {attempt}/5")
                            print("Searching", end="", flush=True)

                            for _ in range(6):
                                time.sleep(0.4)
                                print(".", end="", flush=True)

                            print()

                            vip = random.choices(
                                [
                                    self.clients[8],
                                    self.clients[9],
                                    self.clients[10],
                                    self.clients[11],
                                    None
                                ],
                                weights=[
                                    max(self.clients[8].trust, 5),
                                    max(self.clients[9].trust, 5),
                                    max(self.clients[10].trust, 5),
                                    max(self.clients[11].trust, 5),
                                    100
                                ],
                                k=1
                            )[0]

                            if vip is None:
                                print("❌ No high roller accepted the invitation.")
                                time.sleep(1.5)
                                continue

                            success = True
                            break

                        if success:

                            print("\n═══════════════════════════════════════════════")
                            print("🎉 HIGH ROLLER FOUND!")
                            print("═══════════════════════════════════════════════\n")

                            print(f"👑 {vip.name} has arrived.")
                            print(f"💼 {vip.occupation}")
                            print(f"⭐ Standard : {vip.getstandard()}")
                            print(f"🤝 Trust : {vip.trust}/100\n")

                            print("Agency Cut has been fixed at 35%.")
                            

                            girl.sex(vip, 35, self,True)
                            # Store whether this VIP was previously undiscovered
                            newvip = (vip.trust == 0)

                            

                            # Unlock animation if first encounter
                            if newvip:

                                print("""
══════════════════════════════════════════════════════════════════════════════
                        🌟 NEW HIGH ROLLER DISCOVERED 🌟
══════════════════════════════════════════════════════════════════════════════
                            """)

                                time.sleep(1.5)

                                print("🔍 Updating Vegas Network Database", end="", flush=True)

                                for _ in range(6):
                                    time.sleep(0.4)
                                    print(".", end="", flush=True)

                                print()

                                time.sleep(1)

                                print(f"""
🎉 Congratulations!

👑 {vip.name}
💼 {vip.occupation}

has been added to your exclusive Las Vegas VIP Network.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✔ Future encounters unlocked
✔ VIP profile unlocked
✔ Trust progression unlocked

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

                                

                            # Increase trust after the first meeting
                            vip.updatetrust(5)

                            self.update()

                            

                        else:

                            print("""
══════════════════════════════════════════════════════════════

💔 Unfortunately none of the invited high rollers accepted tonight.

The Diamond Penthouse reservation has expired.

Unfortunately the booking fee is non-refundable.

Better luck next time.

══════════════════════════════════════════════════════════════
""")

                        girl.setdefaultrate(self.defaultrate)

                        self.update()

                        time.sleep(2)

                        self.lvstripclub()
                        return
                        
                        
                        

                    elif choice == 4:

                        

                        # ──────────────────────────────────────────────────────────────
                        # Trust Requirement
                        # ──────────────────────────────────────────────────────────────
                        if marcobellini.trust < 70:

                            print(f"""
══════════════════════════════════════════════════════════════════════════════
                        🎰 NEON ROYALE
                Las Vegas Celebrity Circle
══════════════════════════════════════════════════════════════════════════════

🔒 ACCESS DENIED

Marco Bellini doesn't trust your agency enough
to introduce you to Las Vegas' celebrity network.

Only agencies with exceptional reputation and loyalty
are granted access to this confidential service. (gain trust in diamond penthouse )

──────────────────────────────────────────────────────────────────────────────

Required Trust : 70
Current Trust  : {marcobellini.trust}

──────────────────────────────────────────────────────────────────────────────

💬 Marco Bellini

"Earn my trust first.
The Strip's biggest names don't gamble with amateurs."

══════════════════════════════════════════════════════════════════════════════
""")

                            input("Press Enter to Return...")
                            self.lvstripclub()
                            return

                        # ──────────────────────────────────────────────────────────────
                        # Menu
                        # ──────────────────────────────────────────────────────────────

                        print("""
══════════════════════════════════════════════════════════════════════════════
                        🎰 NEON ROYALE
                Las Vegas Celebrity Circle
══════════════════════════════════════════════════════════════════════════════

Reservation Fee : $75000

Marco Bellini will privately contact his elite
Las Vegas network in search of celebrities interested
in joining your agency.

⚠ Reservation fee is NON-REFUNDABLE.

[1] Begin Celebrity Search
[0] Return

══════════════════════════════════════════════════════════════════════════════
""")
                        while True:
                            try:
                                choice = int(input("Choose ► "))
                                break
                            except:
                                print("❌ Invalid input. Please enter a valid number.")
                                continue

                        if choice == 0:
                            self.lvstripclub()
                            return

                        if self.coin < 75000:
                            print("\n❌ You don't have enough money.")
                            time.sleep(2)
                            return

                        self.coin -= 75000
                        marcobellini.updatetrust(5)

                        print("\nMarco Bellini has activated his Vegas connections.\n")

                        print("Please wait", end="", flush=True)

                        for i in range(6):
                            time.sleep(0.5)
                            print(".", end="", flush=True)

                        print("\n")

                        # ──────────────────────────────────────────────────────────────
                        # Hidden Search
                        # ──────────────────────────────────────────────────────────────

                        found = []

                        for i in range(10):
                            print(len(found))

                            # 1 in 3 chance
                            if not random.randint(1, 3) == 1:
                                continue

                            celeb = self.randomgirl(1,True)

                            duplicate = False

                            # Already recruited?
                            for girl in self.girls:
                                if girl.name == celeb.name:
                                    duplicate = True
                                    break

                            # Already found during THIS search?
                            if not duplicate:
                                for girl in found:
                                    if girl.name == celeb.name:
                                        duplicate = True
                                        break

                            if duplicate:
                                continue

                            found.append(celeb)
                            

                            if len(found) == 4 and not found == []:
                                break

                                

                        # ──────────────────────────────────────────────────────────────
                        # Nobody Found
                        # ──────────────────────────────────────────────────────────────

                        if len(found) == 0:

                            print("""
══════════════════════════════════════════════════════════════════════════════

Unfortunately none of the contacted celebrities
accepted Marco's invitation.

The scouting fee has been consumed.

Marco Bellini:
"The Strip never guarantees success."

══════════════════════════════════════════════════════════════════════════════
                    """)

                            self.update()
                            time.sleep(2)
                            self.lvstripclub()
                            return

                        # ──────────────────────────────────────────────────────────────
                        # Celebrity Selection
                        # ──────────────────────────────────────────────────────────────

                        print("""
══════════════════════════════════════════════════════════════════════════════

Several celebrities have expressed interest
in joining your agency.

Choose one to negotiate with.

══════════════════════════════════════════════════════════════════════════════
                    """)

                        girl = self.listgirls(found, "celebrity")

                        if girl is None:
                            return

                        self.girls.append(girl)

                        print(f"""
══════════════════════════════════════════════════════════════════════════════

🎉 Congratulations!

⭐ {girl.name} has officially joined your agency.

Las Vegas' elite have begun recognizing your influence.

══════════════════════════════════════════════════════════════════════════════
                    """)

                        self.update()

                        time.sleep(2)
                        self.lvstripclub()
                    
                        pass

                    elif choice == 0:
                        self.lv()
                        return

                    else:
                        print("❌ Invalid Choice!")
                
                except Exception as e:
                     print (e)
                     print("❌ Please enter a valid number!")
    def lvsex(self):
        # High Roller Escort Service - Las Vegas
        elenamoretti = self.clients[10]  # Elena Moretti - High Roller Escort Service Owner

        print(f"""
══════════════════════════════════════════════════════════════════════════════
                        💋 HIGH ROLLER ESCORT SERVICE 💋
                    "Discretion. Luxury. Unforgettable Nights."
══════════════════════════════════════════════════════════════════════════════

📍 Location            • The Las Vegas Strip (Private)
👑 Proprietor          • Elena Moretti
⭐ Agency Reputation   • {elenamoretti.trust}/100

──────────────────────────────────────────────────────────────────────────────
""")

        # Check if agency has sufficient reputation
        if elenamoretti.trust < 40:
            print(f"""
🔒 ACCESS RESTRICTED

Elena Moretti requires higher trust before offering 
her elite high-roller clientele.

Current Trust : {elenamoretti.trust}/100
Required Trust : 40+

══════════════════════════════════════════════════════════════════════════════
""")
            input("Press Enter to Return...")
            self.lv()
            return

        # Search for VIP (max 5 attempts)
        print("\n📨 Elena is contacting her exclusive high-roller network...")
        time.sleep(1.5)

        success = False
        vip = None
        attempts = 0

        for attempt in range(1, 6):
            attempts = attempt
            print(f"Attempt {attempt}/5 - Reaching out to elite clients...", end="", flush=True)

            for _ in range(4):
                time.sleep(0.4)
                print(".", end="", flush=True)
            print()

            # All male VIPs from list with weight 10, not finding weight 40
            male_vips = [c for c in self.clients if c.gender == "M" and c.city == "lv"]
            choices = male_vips + [None] * 2  # Higher chance of none
            weights = [10] * len(male_vips) + [40] * 2

            vip = random.choices(choices, weights=weights, k=1)[0]

            if vip is not None:
                success = True
                break

        if not success:
            print("""
══════════════════════════════════════════════════════════════════════════════

💔 Unfortunately, none of the high-rollers responded tonight.

Elena Moretti: "The elite are selective. Try again tomorrow."

══════════════════════════════════════════════════════════════════════════════
""")
            elenamoretti.updatetrust(2)
            self.update()
            time.sleep(2)
            self.lv()
            return

        # VIP Found
        print(f"""
══════════════════════════════════════════════════════════════════════════════
🎉 HIGH ROLLER FOUND!
══════════════════════════════════════════════════════════════════════════════

👑 {vip.name}
💼 {vip.occupation}
⭐ Standard : {vip.getstandard()}
🤝 Trust : {vip.trust}/100

══════════════════════════════════════════════════════════════════════════════
""")

        # Select girl (actress only, Las Vegas)
        girls = self.checkgirl("actress")  # Using "actress" filter + LV condition inside checkgirl if needed
        # Filter to LV only if not already
        lv_girls = [g for g in girls if g.city == "lv"]
        if not lv_girls:
            lv_girls = girls  # fallback

        girl = self.listgirls(lv_girls, "vipsex")
        if girl is None:
            self.lv()
            return

        girl.setdefaultrate(40000)

        # Offer screen
        print(f"""
══════════════════════════════════════════════════════════════════════════════
                    💋 SERVICE SELECTION 💋
══════════════════════════════════════════════════════════════════════════════

[1] Missionary Sex          • Private & Intimate
[2] Gang Bang               • Multiple high-rollers (up to 6)
[3] Threesome               • Select 2 additional girls
[0] Cancel Booking

══════════════════════════════════════════════════════════════════════════════
""")

        while True:
            try:
                service = int(input("Choose service ► "))
                if service in [0,1,2,3]:
                    break
                print("❌ Invalid choice.")
            except:
                print("❌ Please enter a valid number.")

        if service == 0:
            girl.setdefaultrate(self.defaultrate)
            self.lv()
            return

        # MISSIONARY
        if service == 1:
            print("\n💋 Private intimate session arranged...")
            time.sleep(1)
            girl.sex(vip, 40, self, force=True)  # High cut for escort service
            vip.updatetrust(10)
            elenamoretti.updatetrust(8)

        # GANG BANG
        elif service == 2:
            print("\n🔥 Organizing Gang Bang with high-rollers...")
            time.sleep(1.5)

            additional_vips = [vip]
            max_vips = 6

            for round_num in range(1, 6):
                print(f"Round {round_num}/5 - Contacting more elite clients...", end="", flush=True)
                for _ in range(3):
                    time.sleep(0.4)
                    print(".", end="", flush=True)
                print()

                new_vip = random.choices(
                    male_vips + [None],
                    weights=[10] * len(male_vips) + [40],
                    k=1
                )[0]

                if new_vip and new_vip not in additional_vips:
                    additional_vips.append(new_vip)
                    print(f"✅ {new_vip.name} joined the party!")

                if len(additional_vips) >= max_vips:
                    break

            print(f"\n🔥 {len(additional_vips)} high-rollers ready for the session.")
            # Group sex simulation - one girl with multiple clients
            for v in additional_vips:
                girl.sex(v, 35, self, force=True)
                v.updatetrust(10)

            elenamoretti.updatetrust(12)

        # THREESOME
        elif service == 3:
            print("\n💕 Arranging Threesome...")
            additional_girls = self.listgirlsmult(self.checkgirl("actress"), "vipsex", limit=2)
            if additional_girls is None or len(additional_girls) < 2:
                print("❌ Not enough girls available.")
                girl.setdefaultrate(self.defaultrate)
                self.lv()
                return

            print(f"\n💕 Session with {girl.name} + 2 additional girls...")
            # Main girl + 2 others with the VIP
            for g in [girl] + additional_girls:
                g.setdefaultrate(35000)
                g.sex(vip, 38, self, force=True)
                g.setdefaultrate(self.defaultrate)
                vip.updatetrust(8)

            elenamoretti.updatetrust(10)

        # Cleanup
        girl.setdefaultrate(self.defaultrate)
        self.update()
        time.sleep(2)
        self.lv()
    def lvgamble(self):
        marcobellini = self.clients[8]

        print(f"""
══════════════════════════════════════════════════════════════════════════════
                    🎰 THE PLATINUM CASINO ROYALE 🎰
               "Where Sin Meets Fortune on the Neon Strip"
══════════════════════════════════════════════════════════════════════════════

📍 Location            • The Heart of The Strip
👑 Proprietor          • Marco Bellini
⭐ House Reputation    • {marcobellini.trust}/100
💎 Tonight's Vibe     • Seductive • Dangerous • Unforgettable

    ╭──────────────────────────────────────────────────────────────╮
    │  The air is thick with perfume, cigar smoke and possibility. │
    │  Crystal chandeliers cast golden light on velvet tables.     │
    │  Beautiful dealers smile with knowing eyes.                  │
    │  Every roll, every card, every spin could change your life.  │
    ╰──────────────────────────────────────────────────────────────╯

──────────────────────────────────────────────────────────────────────────────
                            CASINO FLOOR
──────────────────────────────────────────────────────────────────────────────

[1] 🃏 Blackjack              • Classic elegance meets high stakes
[2] 🎰 Slot Machines          • Neon reels and seductive jackpots
[3] 🎲 Craps                  • Loud, raw, electric energy
[4] 🎡 Roulette               • The wheel of fortune spins for you
[5] ♠ Texas Hold'em           • Face your opponents with style
[6] 💎 VIP Baccarat           • Ultra-luxury private tables
[7] 📈 Crash                  • How long will you ride the edge?
[8] 😈 Devil's Chamber        • For those who crave true danger

[0] 🚪 Return to The Strip

══════════════════════════════════════════════════════════════════════════════
""")

        while True:
            try:
                choice = int(input("Choose your game of seduction ► "))
                if 0 <= choice <= 8:
                    break
                print("❌ Please select a valid option.")
            except:
                print("❌ That's not a number.")

        if choice == 0:
            self.lv()
            return

        # BLACKJACK
        if choice == 1:
            print(f"""
══════════════════════════════════════════════════════════════════════════════
                    🃏 BLACKJACK - VELVET TABLE 🃏
               "Play smart. Look dangerous. Win beautifully."
══════════════════════════════════════════════════════════════════════════════
""")
            while True:
                try:
                    bet = int(input(f"💰 Place your bet (Balance: ${self.coin}) ► "))
                    if 0 < bet <= self.coin:
                        break
                    print("❌ Invalid bet amount.")
                except:
                    print("❌ Enter a valid number.")

            suits = ["♥️","♦️","♣️","♠️"]
            ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
            deck = [rank + suit for suit in suits for rank in ranks] * 2
            random.shuffle(deck)

            def hand_value(hand):
                val = 0
                aces = 0
                for card in hand:
                    rank = card[:len(card)-2]
                    
                    if rank in ["J","Q","K"]:
                        val += 10
                    elif rank == "A":
                        aces += 1
                    else:
                        val += int(rank)
                for _ in range(aces):
                    if val + 11 <= 21:
                        val += 11
                    else:
                        val += 1
                return val

            player_hand = [deck.pop(), deck.pop()]
            dealer_hand = [deck.pop(), deck.pop()]

            print(f"\nYour hand: {player_hand[0]}\t{player_hand[1]} (Value: {hand_value(player_hand)})")
            print(f"Dealer shows: {dealer_hand[0]}")

            while hand_value(player_hand) < 21:
                action = input("\n[1] Hit(pick urself)  [2] Stand(dealer picks) ► ")
                if action == "1":
                    player_hand.append(deck.pop())
                    print(f"Your hand: {'\t'.join(player_hand)} (Value: {hand_value(player_hand)})")
                    if hand_value(player_hand) > 21:
                        print("💥 You bust!")
                        self.coin -= bet
                        self.update()
                        break
                elif action == "2":
                    break

            if hand_value(player_hand) <= 21:
                print(f"\nDealer reveals: {'\t'.join(dealer_hand)}")
                while hand_value(dealer_hand) < 17:
                    dealer_hand.append(deck.pop())
                    print(f"Dealer draws: {'\t'.join(dealer_hand)} (Value: {hand_value(dealer_hand)})")

                player_val = hand_value(player_hand)
                dealer_val = hand_value(dealer_hand)

                if dealer_val > 21 or player_val > dealer_val:
                    print(f"🎉 You win! +${bet * 2}")
                    self.coin += bet * 2
                elif player_val == dealer_val:
                    print("🤝 Push.")
                else:
                    print(f"💸 Dealer wins. -${bet}")
                    self.coin -= bet

                self.update()

            input("\nPress Enter to continue...")

        # SLOTS
        elif choice == 2:
            print(f"""
══════════════════════════════════════════════════════════════════════════════
                    🎰 NEON DREAM SLOTS 🎰
               "Spin slow. Dream fast. Win forever."
══════════════════════════════════════════════════════════════════════════════
""")
            symbols = ["💎","🍒","🔔","⭐","7️⃣","👑","🌹","🔥"]
            while True:
                try:
                    bet = int(input(f"💰 Bet per spin (Balance: ${self.coin}) ► "))
                    if 0 < bet <= self.coin:
                        break
                except:
                    pass

                print("❌ Invalid bet.")

            spins = 0
            while True:
                spins += 1
                print(f"\nSpin {spins}...", end="", flush=True)
                for _ in range(8):
                    time.sleep(0.15)
                    print("█", end="", flush=True)
                print()
                colorlist=["🔴","🟠","🟡","🟢","🔵","🟣"]
                for i in range(61):
                    if i==20:
                        reel1 = random.choice(symbols)
                        print(f" : {reel1}\n")
                    elif i==40:
                        reel2 = random.choice(symbols)
                        print(f" : {reel2}\n")
                    elif i==60:
                        reel3 = random.choice(symbols)
                        print(f" : {reel3}\n")
                    else: 
                        time.sleep(0.05)
                        print(f"\r{random.choice(colorlist)}", end="",flush=True)

                
                

                print(f"    {reel1}  {reel2}  {reel3}")

                if reel1 == reel2 == reel3:
                    multiplier = 20 if reel1 == "💎" else 12 if reel1 == "7️⃣" else 8
                    win = bet * multiplier
                    print(f"🎰 JACKPOT! You won ${win}!")
                    self.coin += win
                elif reel1 == reel2 or reel2 == reel3:
                    win = bet * 3
                    print(f"💎 Nice win! +${win}")
                    self.coin += win
                else:
                    print("💸 Better luck next spin.")
                    self.coin -= bet

                self.update()

                cont = input("\nSpin again? (y/n) ► ").lower()
                if cont != "y":
                    break

        # CRAPS
        elif choice == 3:
            print(f"""
══════════════════════════════════════════════════════════════════════════════
                    🎲 CRAPS - THE DICE PIT 🎲
               "Roll hot. Bet bold. Feel the heat."
══════════════════════════════════════════════════════════════════════════════
""")
            while True:
                try:
                    bet = int(input(f"💰 Bet on Pass Line (Balance: ${self.coin}) ► "))
                    if 0 < bet <= self.coin:
                        break
                except:
                    pass

            print("\n🎲 Come Out Roll...")
            time.sleep(1)

            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            total = dice1 + dice2

            print(f"🎲 {dice1} + {dice2} = {total}")

            if total in [7,11]:
                print("🎉 Natural win!")
                self.coin += bet
            elif total in [2,3,12]:
                print("💸 Craps - you lose.")
                self.coin -= bet
            else:
                point = total
                print(f"📍 Point is {point}. Roll until you hit it or 7.")

                while True:
                    dice1 = random.randint(1,6)
                    dice2 = random.randint(1,6)
                    total = dice1 + dice2
                    print(f"🎲 {dice1} + {dice2} = {total}")

                    if total == point:
                        print("🎉 You hit the point! Win!")
                        self.coin += bet
                        break
                    elif total == 7:
                        print("💀 Seven out. You lose.")
                        self.coin -= bet
                        break
                    else:
                        print("🎲 Press Enter to roll again...")
                        input()

            self.update()
            input("\nPress Enter to continue...")

        # ROULETTE
        elif choice == 4:
            print(f"""
══════════════════════════════════════════════════════════════════════════════
                    🎡 ROULETTE - GOLDEN WHEEL 🎡
               "The ball spins. Your fate waits."
══════════════════════════════════════════════════════════════════════════════
""")
            bets = {}
            while True:
                print("\n[1] Red   [2] Black   [3] Odd   [4] Even   [5] Single Number")
                try:
                    opt = int(input("Choose bet type ► "))
                    
                    if opt == 5:
                        num = int(input("Pick number (0-36) ► "))
                        bet_amt = int(input("Bet amount ► "))
                        if bet_amt <= self.coin:
                            bets[num] = bet_amt
                            self.coin -= bet_amt

                        break
                    else:
                        bet_amt = int(input("Bet amount ► "))
                        if bet_amt <= self.coin:
                            self.coin -= bet_amt
                            if opt == 1: bets["red"] = bet_amt
                            elif opt == 2: bets["black"] = bet_amt
                            elif opt == 3: bets["odd"] = bet_amt
                            elif opt == 4: bets["even"] = bet_amt
                        break
                except:
                    print("❌ Invalid.")

            print("\n🎡 The wheel is spinning...")
            for _ in range(12):
                time.sleep(0.2)
                print("◉", end="", flush=True)
            print()

            result = random.randint(0,36)
            color = "red" if result in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36] else "black" if result != 0 else "green"

            print(f"🎰 Ball landed on {result} ({color.upper()})")

            winnings = 0
            for btype, amt in bets.items():
                if btype == result or (btype == "red" and color == "red") or (btype == "black" and color == "black") or (btype == "odd" and result % 2 == 1) or (btype == "even" and result % 2 == 0 and result != 0):
                    if btype == result:
                        winnings += amt * 36
                    else:
                        winnings += amt * 2

            if winnings > 0:
                print(f"🎉 You won ${winnings}!")
                self.coin += winnings
            else:
                print("💸 Better luck next spin.")

            self.update()
            input("\nPress Enter to continue...")

        # TEXAS HOLD'EM
        elif choice == 5:
            print(f"""
══════════════════════════════════════════════════════════════════════════════
                    ♠ TEXAS HOLD'EM - HIGH ROLLER TABLE ♠
               "Read the table. Trust your instincts."
══════════════════════════════════════════════════════════════════════════════

    The private poker room glows with soft golden light.
    Crystal glasses catch reflections from the chandelier.
    The felt table feels rich beneath your fingers.
    Marco Bellini watches from the shadows with a knowing smile.

""")
            while True:
                try:
                    ante = int(input(f"💰 Place your Ante (Balance: ${self.coin}) ► "))
                    if 0 < ante <= self.coin:
                        break
                    print("❌ Invalid ante amount.")
                except:
                    print("❌ Please enter a valid number.")

            self.coin -= ante
            self.update()

            suits = ["♥️","♦️","♣️","♠️"]
            ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
            deck = [r + s for s in suits for r in ranks]
            random.shuffle(deck)

            player_hole = [deck.pop(), deck.pop()]
            dealer_hole = [deck.pop(), deck.pop()]

            community = []

            print(f"""
══════════════════════════════════════════════════════════════════════════════
            ♠ TEXAS HOLD'EM ♠
Dealer
{dealer_hole[0]} 🂠
────────────────────────────────────────
Your Hand
{player_hole[0]} {player_hole[1]}
══════════════════════════════════════════════════════════════════════════════
""")

            input("Press Enter to see the Flop...")

            # Flop
            for _ in range(3):
                community.append(deck.pop())

            print(f"""
══════════════════════════════════════════════════════════════════════════════
            ♠ TEXAS HOLD'EM ♠
Dealer
{dealer_hole[0]} 🂠
────────────────────────────────────────
Flop
{' '.join(community)}
══════════════════════════════════════════════════════════════════════════════
""")

            action = input("\n[1] Continue  [2] Fold ► ")
            if action == "2":
                print("💸 You folded. Dealer takes the pot.")
                input("\nPress Enter to continue...")
                

            # Turn
            community.append(deck.pop())

            print(f"""
══════════════════════════════════════════════════════════════════════════════
            ♠ TEXAS HOLD'EM ♠
Dealer
{dealer_hole[0]} 🂠
────────────────────────────────────────
Turn
{' '.join(community)}
══════════════════════════════════════════════════════════════════════════════
""")

            action = input("\n[1] Continue  [2] Fold ► ")
            if action == "2":
                print("💸 You folded. Dealer takes the pot.")
                input("\nPress Enter to continue...")
                

            # River
            community.append(deck.pop())

            print(f"""
══════════════════════════════════════════════════════════════════════════════
            ♠ TEXAS HOLD'EM ♠
Dealer
{dealer_hole[0]} 🂠
────────────────────────────────────────
River
{' '.join(community)}
══════════════════════════════════════════════════════════════════════════════
""")

            input("\nPress Enter for showdown...")

            print(f"""
══════════════════════════════════════════════════════════════════════════════
            ♠ SHOWDOWN ♠
Dealer Hole
{dealer_hole[0]} {dealer_hole[1]}
────────────────────────────────────────
Your Hole
{player_hole[0]} {player_hole[1]}
────────────────────────────────────────
Community
{' '.join(community)}
══════════════════════════════════════════════════════════════════════════════
""")

            def get_hand_rank(cards):
                # cards is list of "rank suit" strings
                rank_map = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
                vals = [rank_map[c[:len(c)-2]] for c in cards]
                suits = [c[-1] for c in cards]
                vals_sorted = sorted(vals, reverse=True)

                # Flush check
                suit_count = {}
                for s in suits:
                    suit_count[s] = suit_count.get(s,0) + 1
                flush_suit = None
                for s,c in suit_count.items():
                    if c >= 5:
                        flush_suit = s
                        break

                flush_cards = [i for i,v in enumerate(suits) if v == flush_suit][:5] if flush_suit else []
                if flush_cards:
                    flush_vals = sorted([vals[i] for i in flush_cards], reverse=True)

                # Straight check
                unique_vals = sorted(set(vals), reverse=True)
                straight = False
                straight_high = 0
                for i in range(len(unique_vals)-4):
                    if unique_vals[i] - unique_vals[i+4] == 4:
                        straight = True
                        straight_high = unique_vals[i]
                        break
                # Wheel straight
                if not straight and set([14,5,4,3,2]).issubset(set(unique_vals)):
                    straight = True
                    straight_high = 5

                # Count ranks
                rank_count = {}
                for v in vals:
                    rank_count[v] = rank_count.get(v,0) + 1

                counts = sorted(rank_count.values(), reverse=True)

                # Royal Flush
                if flush_suit and straight and straight_high == 14:
                    return (9, 14)  # Royal

                # Straight Flush
                if flush_suit and straight:
                    return (8, straight_high)

                # Four of a kind
                if counts[0] == 4:
                    four_rank = [k for k,v in rank_count.items() if v==4][0]
                    kicker = max([k for k,v in rank_count.items() if v==1])
                    return (7, four_rank, kicker)

                # Full House
                if counts[0] == 3 and counts[1] >= 2:
                    three = [k for k,v in rank_count.items() if v==3][0]
                    pair = [k for k,v in rank_count.items() if v>=2 and k != three][0]
                    return (6, three, pair)

                # Flush
                if flush_suit:
                    return (5, tuple(flush_vals))

                # Straight
                if straight:
                    return (4, straight_high)

                # Three of a kind
                if counts[0] == 3:
                    three = [k for k,v in rank_count.items() if v==3][0]
                    kickers = sorted([k for k,v in rank_count.items() if v==1], reverse=True)[:2]
                    return (3, three, kickers[0], kickers[1])

                # Two Pair
                if counts[0] == 2 and counts[1] == 2:
                    pairs = sorted([k for k,v in rank_count.items() if v==2], reverse=True)[:2]
                    kicker = max([k for k,v in rank_count.items() if v==1])
                    return (2, pairs[0], pairs[1], kicker)

                # One Pair
                if counts[0] == 2:
                    pair = [k for k,v in rank_count.items() if v==2][0]
                    kickers = sorted([k for k,v in rank_count.items() if v==1], reverse=True)[:3]
                    return (1, pair, kickers[0], kickers[1], kickers[2])

                # High Card
                return (0, tuple(sorted(vals, reverse=True)[:5]))

            player_best = get_hand_rank(player_hole + community)
            dealer_best = get_hand_rank(dealer_hole + community)

            hand_names = {
                9: "Royal Flush",
                8: "Straight Flush",
                7: "Four of a Kind",
                6: "Full House",
                5: "Flush",
                4: "Straight",
                3: "Three of a Kind",
                2: "Two Pair",
                1: "One Pair",
                0: "High Card"
            }

            print(f"""
Player Best Hand  : {hand_names[player_best[0]]}
Dealer Best Hand  : {hand_names[dealer_best[0]]}
""")

            if player_best > dealer_best:
                print("🎉 You win the pot!")
                self.coin += ante * 2
            elif player_best == dealer_best:
                print("🤝 Split pot.")
                self.coin += ante
            else:
                print("💸 Dealer wins the hand.")

            self.update()
            input("\nPress Enter to continue...")

            if input("\nPlay another hand? (y/n) ► ").lower() != "y":
                self.lvgamble()
                

        # BACCARAT
        elif choice == 6:
            print(f"""
══════════════════════════════════════════════════════════════════════════════
                    💎 VIP BACCARAT - GOLD ROOM 💎
               "Elegance. Tension. Pure luxury."
══════════════════════════════════════════════════════════════════════════════

    The private Baccarat salon glows with soft golden light.
    Crystal chandeliers cast reflections on polished mahogany tables.
    The felt is deep emerald. The air smells of aged cognac and success.
    Elena Moretti watches from the shadows with a knowing smile.

""")
            while True:
                print("""
[1] Bet on Player
[2] Bet on Banker
[3] Bet on Tie
[0] Return to Casino
""")
                try:
                    side_choice = int(input("Choose betting side ► "))
                    if side_choice in [0,1,2,3]:
                        break
                    print("❌ Invalid choice.")
                except:
                    print("❌ Please enter a valid number.")

                if side_choice == 0:
                    self.lvgamble()
                    return

            if side_choice == 1:
                side = "Player"
            elif side_choice == 2:
                side = "Banker"
            else:
                side = "Tie"

            while True:
                try:
                    bet = int(input(f"💰 Minimum $100000. Place your wager on {side} (Balance: ${self.coin}) ► "))
                    if bet >= 100000 and bet <= self.coin:
                        break
                    print("❌ Invalid wager.")
                except:
                    print("❌ Please enter a valid number.")

            self.coin -= bet
            self.update()

            suits = ["♥️","♦️","♣️","♠️"]
            ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
            deck = [r + s for s in suits for r in ranks] * 6
            random.shuffle(deck)

            def baccarat_value(card):
                rank = card[:-2]
                if rank in ["10","J","Q","K"]:
                    return 0
                elif rank == "A":
                    return 1
                else:
                    return int(rank)

            player_hand = [deck.pop(), deck.pop()]
            banker_hand = [deck.pop(), deck.pop()]

            player_total = (baccarat_value(player_hand[0]) + baccarat_value(player_hand[1])) % 10
            banker_total = (baccarat_value(banker_hand[0]) + baccarat_value(banker_hand[1])) % 10

            print(f"""
══════════════════════════════════════════════════════════════════════════════
                💎 VIP BACCARAT 💎
────────────────────────────────────────────
PLAYER
{player_hand[0]} {player_hand[1]}
Total : {player_total}
────────────────────────────────────────────
BANKER
{banker_hand[0]} {banker_hand[1]}
Total : {banker_total}
══════════════════════════════════════════════════════════════════════════════
""")

            # Third card rules
            player_third = None
            banker_third = None

            # Player third card
            time.sleep(1)
            if player_total <= 5:
                player_third = deck.pop()
                player_total = (player_total + baccarat_value(player_third)) % 10
                print(f"Player draws third card: {player_third}")
                print(f"New Player Total: {player_total}")

            # Banker third card
            if banker_total <= 2:
                banker_third = deck.pop()
            elif banker_total == 3 and (player_third is None or baccarat_value(player_third) != 8):
                banker_third = deck.pop()
            elif banker_total == 4 and player_third and baccarat_value(player_third) in [2,3,4,5,6,7]:
                banker_third = deck.pop()
            elif banker_total == 5 and player_third and baccarat_value(player_third) in [4,5,6,7]:
                banker_third = deck.pop()
            elif banker_total == 6 and player_third and baccarat_value(player_third) in [6,7]:
                banker_third = deck.pop()

            if banker_third:
                banker_total = (banker_total + baccarat_value(banker_third)) % 10
                print(f"Banker draws third card: {banker_third}")
                time.sleep(1)
                print(f"New Banker Total: {banker_total}")

            print(f"""
══════════════════════════════════════════════════════════════════════════════
                FINAL RESULTS
────────────────────────────────────────────
PLAYER TOTAL : {player_total}
BANKER TOTAL : {banker_total}
══════════════════════════════════════════════════════════════════════════════
""")

            winner = "Player" if player_total > banker_total else "Banker" if banker_total > player_total else "Tie"

            if winner == side:
                if side == "Player":
                    payout = bet * 2
                    print("🎉 Player wins!")
                elif side == "Banker":
                    payout = int(bet * 1.95)
                    print("💎 Banker wins!")
                else:
                    payout = bet * 9
                    print("🤝 Tie!")
                self.coin += payout
                print(f"💰 You won ${payout}!")
            else:
                print(f"💔 {winner} wins. Your {side} bet is lost.")

            self.update()

            input("\npress enter to continue ► ")
            
            self.lvgamble()
                

        # CRASH
        elif choice == 7:
            print(f"""
══════════════════════════════════════════════════════════════════════════════
                    📈 CRASH - THE EDGE OF FORTUNE 📈
               "Cash out before it all disappears."
══════════════════════════════════════════════════════════════════════════════

    The high-stakes Crash pit pulses with neon energy.
    Tension is thick in the air.
    High rollers watch the multiplier climb with hungry eyes.
    One wrong second and everything vanishes.

""")
            while True:
                try:
                    bet = int(input(f"💰 Place your wager (Balance: ${self.coin}) ► "))
                    if 0 < bet <= self.coin:
                        break
                    print("❌ Invalid wager.")
                except:
                    print("❌ Please enter a valid number.")

            self.coin -= bet
            self.update()

            # Generate hidden crash point once
            crash_roll = random.random()
            if crash_roll < 0.45:
                crash_point = random.uniform(1.10, 2.80)
            elif crash_roll < 0.75:
                crash_point = random.uniform(2.80, 6.50)
            elif crash_roll < 0.90:
                crash_point = random.uniform(6.50, 15.0)
            elif crash_roll < 0.97:
                crash_point = random.uniform(15.0, 35.0)
            else:
                crash_point = random.uniform(35.0, 120.0)

            print("\n🚀 The rocket is launching...")
            time.sleep(1.2)

            multiplier = 1.00
            cashed = False
            cashout_mult = 0.0

            while multiplier < crash_point:
                print(f"📈 Current Multiplier: {multiplier:.2f}x", end="\r")
                time.sleep(0.28)

                multiplier += random.uniform(0.08, 0.45)

                if multiplier >= crash_point:
                    break

                print(f"""
══════════════════════════════════════════════════════════════════════════════
                    📈 CURRENT MULTIPLIER
                      {multiplier:.2f}x
══════════════════════════════════════════════════════════════════════════════

[1] 💰 CASH OUT NOW
[2] 🚀 KEEP GOING
""")
                try:
                    action = int(input("Choose action ► "))
                    if action == 1:
                        cashed = True
                        cashout_mult = multiplier
                        break
                except:
                    pass

            if cashed:
                winnings = int(bet * cashout_mult)
                self.coin += winnings
                self.update()
                print(f"""
══════════════════════════════════════════════════════════════════════════════
                    💰 SUCCESSFUL CASH OUT 💰
══════════════════════════════════════════════════════════════════════════════

Cash-out Multiplier : {cashout_mult:.2f}x
Wager               : ${bet:,}
Profit              : ${winnings - bet:,}
New Balance         : ${self.coin:,}

The crowd cheers as you walk away richer.
""")
            else:
                print(f"""
══════════════════════════════════════════════════════════════════════════════
                    💥 MARKET CRASH 💥
══════════════════════════════════════════════════════════════════════════════

Final Multiplier    : {crash_point:.2f}x
You failed to cash out in time.

The rocket exploded.
You lost your entire wager of ${bet:,}.

Better luck next round, high roller.
""")

            self.update()

            while True:
                try:
                    again = int(input("\n[1] Play Again  [0] Return to Casino ► "))
                    if again in [0,1]:
                        break
                except:
                    pass

            if again == 0:
                self.lvgamble()
                return

        # DEVIL'S CHAMBER
        elif choice == 8:
            print(f"""
══════════════════════════════════════════════════════════════════════════════
                    😈 DEVIL'S CHAMBER 😈
               "One wager. Infinite possibilities."
══════════════════════════════════════════════════════════════════════════════

    The heavy obsidian doors close behind you with a final thud.
    Crimson candles flicker to life one by one along the walls.
    The air tastes of smoke, aged whiskey, and something ancient.
    A single black velvet table waits in the center of the room.
    A deep, velvety voice echoes from the shadows.

    "Welcome back, mortal...
     The Devil has been expecting you."

""")
            time.sleep(2.2)

            while True:
                try:
                    bet = int(input(f"💰 Place your wager with the Devil (Balance: ${self.coin}) ► "))
                    if 0 < bet <= self.coin:
                        break
                    print("❌ The Devil does not accept empty promises.")
                except:
                    print("❌ The Devil demands a number.")

            self.coin -= bet
            self.update()

            print("\n🔥 The candles burn brighter...")
            time.sleep(1.8)

            # Weighted outcome pool
            outcome_roll = random.random()

            if outcome_roll < 0.28:
                # Money outcomes
                money_roll = random.random()
                if money_roll < 0.35:
                    print("😈 The Devil claims his due.")
                    print("💸 You lost everything you wagered.")
                elif money_roll < 0.65:
                    win = bet * 2
                    print("🔥 The Devil is in a playful mood.")
                    print(f"💰 You doubled your wager. +${win:,}")
                    self.coin += win
                elif money_roll < 0.82:
                    win = bet * 3
                    print("🌹 The flames dance in approval.")
                    print(f"💎 Triple the wager. +${win:,}")
                    self.coin += win
                elif money_roll < 0.92:
                    win = bet * 5
                    print("👑 The Devil smiles.")
                    print(f"✨ Five times your wager. +${win:,}")
                    self.coin += win
                elif money_roll < 0.97:
                    win = bet * 10
                    print("🔥 The room shakes with power.")
                    print(f"💥 TEN TIMES! +${win:,}")
                    self.coin += win
                else:
                    win = bet * 25
                    print("🌌 The Devil laughs with delight.")
                    print(f"💫 LEGENDARY 25x WIN! +${win:,}")
                    self.coin += win

            elif outcome_roll < 0.48:
                # Trust & VIP events
                trust_roll = random.random()
                if trust_roll < 0.4:
                    marcobellini.updatetrust(8)
                    print("👑 Marco Bellini has taken notice of your courage.")
                    print("🤝 Marco's Trust +8")
                elif trust_roll < 0.7:
                    random_vip = random.choice(self.clients)
                    random_vip.updatetrust(12)
                    print(f"🌟 {random_vip.name} respects your boldness.")
                    print(f"🤝 {random_vip.name}'s Trust +12")
                elif trust_roll < 0.85:
                    marcobellini.updatetrust(-6)
                    print("😈 The Devil whispers lies into Marco's ear.")
                    print("💔 Marco's Trust -6")
                else:
                    print("🌌 A mysterious VIP watches from the shadows.")
                    print("🔮 Your reputation grows in unseen circles.")
                    for c in self.clients:
                        if random.random() < 0.3:
                            c.updatetrust(5)

            elif outcome_roll < 0.65:
                # Item events
                item_roll = random.random()
                if item_roll < 0.45:
                    # Give random item
                    possible_items = [k for k in self.inventory if self.inventory[k][3] < 5]
                    if possible_items:
                        gifted = random.choice(possible_items)
                        self.inventory[gifted][3] += 1
                        print(f"🌹 The Devil gifts you {self.inventory[gifted][0]}.")
                        print("👜 Item added to your inventory.")
                elif item_roll < 0.75:
                    # Lose random item
                    owned_items = [k for k in self.inventory if self.inventory[k][3] > 0]
                    if owned_items:
                        lost = random.choice(owned_items)
                        self.inventory[lost][3] -= 1
                        print(f"😈 The Devil takes {self.inventory[lost][0]} as tribute.")
                        print("🖤 Item removed.")
                else:
                    print("🔥 The Devil offers a deal too good to refuse.")
                    print("💎 A rare exclusive item materializes before you.")
                    rare_key = random.choice(list(self.inventory.keys()))
                    self.inventory[rare_key][3] += 2
                    print(f"🌟 You received two {self.inventory[rare_key][0]}!")

            elif outcome_roll < 0.80:
                # Girl events
                if self.girls:
                    lucky_girl = random.choice(self.girls)
                    girl_roll = random.random()
                    if girl_roll < 0.35:
                        lucky_girl.level = min(30, lucky_girl.level + 6)
                        lucky_girl.getboost()
                        print(f"🌟 {lucky_girl.name} feels a surge of confidence.")
                        print(f"📈 {lucky_girl.name}'s level increased!")
                    elif girl_roll < 0.65:
                        lucky_girl.upgradecupsize()
                        print(f"💖 {lucky_girl.name}'s beauty blossoms.")
                    elif girl_roll < 0.85:
                        lucky_girl.trust = min(100, lucky_girl.trust + 15)
                        print(f"❤️ {lucky_girl.name} feels closer to you.")
                    else:
                        print(f"🖤 The Devil whispers to {lucky_girl.name}...")
                        lucky_girl.trust = max(0, lucky_girl.trust - 12)
                        print(f"💔 {lucky_girl.name}'s trust in you decreased.")

            elif outcome_roll < 0.92:
                # Financial & world events
                world_roll = random.random()
                if world_roll < 0.4:
                    print("🌍 The economy smiles upon you.")
                    bonus = bet * 3
                    self.coin += bonus
                    print(f"💵 Mysterious donation of ${bonus:,}")
                elif world_roll < 0.7:
                    print("🏦 Your loan interest mysteriously vanishes.")
                    self.loan = max(0, self.loan - 8000)
                else:
                    print("💸 The Devil collects a hidden tax.")
                    self.coin = max(0, self.coin - int(bet * 0.6))

            else:
                # Legendary events
                legend_roll = random.random()
                if legend_roll < 0.4:
                    print("🌌 The room freezes in time.")
                    print("😈 The Devil appears before you.")
                    print("💫 He offers you one wish...")
                    print("""
[1] Wealth     [2] Power     [3] Fame
""")
                    wish = input("Choose your wish ► ")
                    if wish == "1":
                        self.coin += bet * 80
                        print("💰 The Devil grants you overwhelming wealth.")
                    elif wish == "2":
                        for g in self.girls:
                            if random.random() < 0.6:
                                g.level = min(30, g.level + 8)
                        print("🔥 Your girls grow stronger under dark blessing.")
                    else:
                        for c in self.clients:
                            c.updatetrust(18)
                        print("🌟 Your name echoes through the Strip.")
                elif legend_roll < 0.75:
                    print("🔥 The candles burn blue.")
                    print("🌟 A legendary 100x payout appears!")
                    self.coin += bet * 99
                else:
                    print("☠️ The Devil laughs darkly.")
                    print("💀 You feel a curse settle upon you.")
                    self.coin = max(0, self.coin - bet * 2)
                    if self.girls:
                        cursed = random.choice(self.girls)
                        cursed.trust = max(0, cursed.trust - 25)
                        print(f"🖤 {cursed.name} has been touched by darkness.")

            self.update()

            print(f"""
══════════════════════════════════════════════════════════════════════════════
    The candles dim once more.
    The heavy doors creak open behind you.

    "Until next time, mortal..."
══════════════════════════════════════════════════════════════════════════════
""")

            while True:
                try:
                    again = int(input("\n[1] Return to the Devil  [0] Leave the Chamber ► "))
                    if again in [0,1]:
                        break
                except:
                    pass

            if again == 0:
                self.lvgamble()
                return
        # Return to menu after any game
        self.lvgamble()
    def lvcomplex(self):
        avg = 0
        count = 0

        for client in self.clients:
            if client.city == "lv":
                avg += client.trust
                count += 1

        avg //= count

        if avg < 20:
            status = "Unknown Face"
        elif avg < 40:
            status = "Rising Prospect"
        elif avg < 60:
            status = "Casino Regular"
        elif avg < 80:
            status = "High Roller"
        elif avg < 95:
            status = "Vegas Royalty"
        else:
            status = "Living Legend"
        print(f'''
══════════════════════════════════════════════════════════════════════════════

                  🍸 NEON NIGHT CLUB COMPLEX 🍸
               ✨ Where Every Night Makes Legends ✨

══════════════════════════════════════════════════════════════════════════════

╭──────────────────────────────────────────────────────────────╮
│ 🎉 1. VIP Party Lounge                                       │
│    Host elite parties & entertain Vegas high rollers.        │
├──────────────────────────────────────────────────────────────┤
│ 👠 2. Sin City Casting                                       │
│    Discover Beauties • Exclusive Talent • Luxury Agency      │
├──────────────────────────────────────────────────────────────┤
│ 💎 3. Diamond Noir                                           │
│    Luxury fashion, beauty & exclusive nightlife couture.     │
├──────────────────────────────────────────────────────────────┤
│ 🎰 4. Return                                                 │
╰──────────────────────────────────────────────────────────────╯

══════════════════════════════════════════════════════════════════════════════

        💰 Cash          : ${self.coin}
        🎲 Vegas Status  : {status}

══════════════════════════════════════════════════════════════════════════════

Choose a destination ►''', end="")
        try:
            num = int(input())
            if num == 4:
                self.lv()
                self.update()
                return
            elif num == 3:
                self.lvshop()
                self.update()
            elif num==2:
                self.lvhire()
                self.update()
            elif num==1:
                self.lvparty()
                self.update()
        except Exception as e:
            print(e)
            
            print("bruh that aint a number -_-")
            return
    def lvshop(self,redirect=0):
        avg = 0
        count = 0

        for client in self.clients:
            if client.city == "lv":
                avg += client.trust
                count += 1

        avg //= count

        if avg < 20:
            status = "Unknown Face"
        elif avg < 40:
            status = "Rising Prospect"
        elif avg < 60:
            status = "Casino Regular"
        elif avg < 80:
            status = "High Roller"
        elif avg < 95:
            status = "Vegas Royalty"
        else:
            status = "Living Legend"

        print(f'''
══════════════════════════════════════════════════════════════════════════════
                        ♦️ DIAMOND NOIR ♦️
                ♠️ Dress Like You Own the Strip ♠️
══════════════════════════════════════════════════════════════════════════════

    ╭──────────────────────────────────────────────────────────────╮
    │ 💎 1. Diamond Collection                                    │
    │    Elite evening couture & casino luxury fashion.           │
    ├──────────────────────────────────────────────────────────────┤
    │ 👑 2. Sin Beauty Atelier                                    │
    │    Exclusive beauty enhancements for Vegas royalty.         │
    ├──────────────────────────────────────────────────────────────┤
    │ 🍷 3. Midnight Essentials                                   │
    │    Premium nightlife accessories & luxury necessities.      │
    ├──────────────────────────────────────────────────────────────┤
    │ 💋 4. Vixen Suite                                           │
    │    Prepare irresistible looks for the city's elite.         │ 
    ├──────────────────────────────────────────────────────────────┤     
    │ 🎰 5. Return                                                │
    ╰──────────────────────────────────────────────────────────────╯

══════════════════════════════════════════════════════════════════════════════

            💰 Cash          : ${self.coin}
            🎰 Vegas Status  : {status}

══════════════════════════════════════════════════════════════════════════════
    ''', end="\n")

        try:
            while True:
                num = int(input("Choose a service ►")) if redirect == 0 else redirect   
                if num not in [1, 2, 3, 4, 5]:
                    print("❌ Invalid service selected. Please choose a valid option.")
                    continue
                break
            if num == 5:
                self.lvcomplex()
                return

            elif num == 1:
                print(f'''
══════════════════════════════════════════════════════════════════════════════
                            ♦️ DIAMOND NOIR ♦️
                            Diamond Collection
══════════════════════════════════════════════════════════════════════════════
    ''')
                self.shopbox("lvitem")

            elif num == 2:
                print(f'''
══════════════════════════════════════════════════════════════════════════════
                            ♦️ DIAMOND NOIR ♦️
                            Sin Beauty Atelier
══════════════════════════════════════════════════════════════════════════════
    ''')
                self.shopbox("lvbeauty")

            elif num == 3:
                print(f'''
══════════════════════════════════════════════════════════════════════════════
                            ♦️ DIAMOND NOIR ♦️
                            Midnight Essentials
══════════════════════════════════════════════════════════════════════════════
    ''')        
                self.shopbox("ess")
            elif num == 4:
                print(f'''
══════════════════════════════════════════════════════════════════════════════
                            ♦️ DIAMOND NOIR ♦️
                                Vixen Suite
══════════════════════════════════════════════════════════════════════════════
    ''')
                girl = self.listgirls(self.checkgirl("lv"))
                if girl == None:
                    self.lvshop()
                    return
                self.rejuvenate(girl)
                

            else:
                print("❌ Invalid service selected.")
                return

            while True:
                try:
                    choice = int(input("Choose an item :► "))

                    if (choice == 6 and num in [1, 3]) or (choice == 4 and num == 2):
                        break

                    elif num == 1 and 1 <= choice <= 5:
                        self.purchase("lvitem", choice)
                        

                    elif num == 2 and 1 <= choice <= 3:
                        self.purchase("lvbeauty", choice)
                        time.sleep(1.5)
                        self.lvshop(2)
                        

                    elif num == 3 and 1 <= choice <= 5:
                        self.purchase("ess", choice)
                        

                    else:
                        print("❌ Invalid choice. Please select a valid item number.")

                except Exception as e:
                    print(e)
                    
                    print("bruh that aint a number -_- flag here")

            self.lvshop()

        except Exception as e:
            print(e)
            
            print("bruh that aint a number -_-")
    def lvparty(self):
        print(f"""
══════════════════════════════════════════════════════════════════════════════
                    🌃 VIP PENTHOUSE PARTY LOUNGE 🌃
               "Where the Strip's Elite Come to Play"
══════════════════════════════════════════════════════════════════════════════

💎 Location            • Private Penthouse overlooking The Strip
🍾 Entry Fee           • $25,000
👑 Host                • Marco Bellini
⭐ Vibe                • Luxury • Neon • Sin City Glamour

    The penthouse pulses with deep bass. Crystal chandeliers reflect
    off floor-to-ceiling windows showing the glittering Vegas skyline.
    Beautiful girls in designer dresses mingle with billionaires,
    celebrities, and high-rollers.

""")

        if self.coin < 25000:
            print("""
❌ You don't have enough cash for the entry fee.
💰 Required : $25,000
""")
            input("Press Enter to return...")
            self.lvcomplex()
            return

        self.coin -= 25000
        self.update()

        print("✅ Entry fee paid. The party begins...")

        available = [g for g in self.girls if g.city == "lv" and g.jail == False and g.preg == False]

        if  len(available)==0:
            print("❌ No girls available in Las Vegas.")
            input("Press Enter...")
            self.lvcomplex()
            return

        selected = self.listgirlsmult(available, "party", limit=min(len(available),5))

        if selected==None:
            self.lvcomplex()
            return

        # Assign party health
        for girl in selected:
            girl.partyhealth = 3

        total_income = 0
        events = 0

        print(f"""
══════════════════════════════════════════════════════════════════════════════
                    🎉 THE PARTY BEGINS 🎉
══════════════════════════════════════════════════════════════════════════════

{len(selected)} beautiful girls are now working the room.
Champagne flows. The DJ drops the beat. The night is young.

""")

        active = selected[:]

        while active:
            time.sleep(2)

            girl = random.choice(active)
            client_name = random.choice(["Ethan Brooks","Alexander Hayes","Marcus Kane","Damien Voss","Julian Pierce","Rafael Santos","Leonardo Vale","Sebastian Cross","Dominic Vale","Victor Lang"])
            
            # Load partytext
            with open("D:\\py things\\python  dem\\flirt.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                partytext = data.get("partytext", [])

            # Find matching dialogue
            matching = [entry for entry in partytext if entry["persona1"] == girl.persona1 and entry["nation"] == girl.nation]
            if not matching:
                matching = partytext

            entry = random.choice(matching)
            category = random.choice(["love","flirt","rizz","drunk","dance"])
            dialogue = random.choice(entry["replies"][category]).replace("{self.name}",girl.name).replace("{client.name}",client_name)

            # Money and stamina
            if category == "love":
                earnings = int(self.defaultrate)
                total_income += earnings
                print(f"💖 {girl.name} shares an intimate moment with {client_name}.")
                time.sleep(1)
                print(f"   {dialogue}")
                print(f"   +${earnings}\n")
            elif category == "flirt":
                earnings = int(self.defaultrate * 0.5)
                total_income += earnings
                print(f"🌹 {girl.name} flirts heavily with {client_name}.")
                time.sleep(1)
                print(f"   {dialogue}")
                print(f"   +${earnings}\n")
            elif category == "dance":
                earnings = int(self.defaultrate * 0.3)
                total_income += earnings
                print(f"💃 {girl.name} owns the dance floor near {client_name}.")
                time.sleep(1)
                print(f"   {dialogue}")
                print(f"   +${earnings}\n")
            elif category == "drunk":
                girl.partyhealth -= 1
                print(f"🥂 {girl.name} has had way too much champagne.")
                time.sleep(1)
                print(f"   {dialogue}")
                print("   No earnings this round.\n")
            elif category == "rizz":
                girl.partyhealth -= 1
                print(f"😎 {client_name} flirts with {girl.name}.")
                time.sleep(1)
                print(f"   {dialogue}")
                print("   No earnings this round.\n")

            events += 1

            if girl.partyhealth <= 0:
                print(f"💤 {girl.name} is exhausted and leaves the party.")
                active.remove(girl)
                time.sleep(1.2)

        # Party end
        net = total_income
        print(f"""
══════════════════════════════════════════════════════════════════════════════
                    🌃 VIP PARTY HAS ENDED 🌃
══════════════════════════════════════════════════════════════════════════════

Girls Attended     : {len(selected)}
Total Events       : {events}
Total Earnings     : ${total_income:,}
Party Cost         : $25,000
Net Profit         : ${net:,}
Current Balance    : ${self.coin + net:,}

The girls return looking satisfied and richer.
""")

        self.coin += net
        self.update()

        input("\nPress Enter to return to the Lounge...")
        self.lvcomplex()
    def lvhire(self):
        print(f'''
══════════════════════════════════════════════════════════════════════════════
                 🌃 SIN CITY CASTING 🌃
          "Every Queen Starts Somewhere."
══════════════════════════════════════════════════════════════════════════════

[1] 💎 Penthouse Society
    Billionaire Daughters • Casino Heiresses • Elite Beauties
                                                💰 $60,000

[2] 🎰 Casino Hostesses
    VIP Dealers • High Roller Girls • Luxury Staff
                                                💰 $30,000

[3] 💃 Vegas Showgirls
    Performers • Dancers • Strip Icons
                                                💰 $15,000

[4] 🍸 Cocktail Lounges
    Bartenders • Party Girls • Nightlife Beauties
                                                💰 $7,500

[5] 🌙 After Midnight
    Waitresses • Tourists • Hidden Gems
                                                💰 $3,000

[6] 🚪 Return
══════════════════════════════════════════════════════════════════════════════
''')
        while True:
            try:
                sub_choice = int(input("Choose a recruitment tier :► "))
                if sub_choice in [1, 2, 3, 4, 5, 6]:
                    break
                else:
                    print("❌ Invalid choice. Please select a valid option.")
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")

        if sub_choice == 6:
            self.lv()
            return

        fees = [60000, 30000, 15000, 7500, 3000]
        if self.coin < fees[sub_choice - 1]:
            print("❌ Insufficient funds for this recruitment tier.")
            self.lvhire()
            return

        self.coin -= fees[sub_choice - 1]
        print(f"\n💎 Scouting the {['Penthouse Society','Casino Hostesses','Vegas Showgirls','Cocktail Lounges','After Midnight'][sub_choice-1]}...")
        time.sleep(1.5)

        females = self.recruitgirls(4, sub_choice)
        girl = self.recruitlist(females)

        if girl == None:
            self.lvhire()
            return

        print(f"\n🎉 {girl.name} has officially joined your Las Vegas agency!")
        print("🌃 Welcome to the Strip.")
        self.girls.append(girl)
        self.update()
        time.sleep(2)
        self.lvhire()
    def lvbank(self):
        print(f'''
══════════════════════════════════════════════════════════════════════
                  🏦 DIAMOND CROWN CAPITAL 🏦
══════════════════════════════════════════════════════════════════════

            "Fortunes Are Made Under Neon Lights."

             🎰 Las Vegas Boulevard • Since 1983

╭──────────────────────────────────────────────────────────╮
│                  Welcome, Valued Client.                 │
│      Every empire deserves a bigger stake.               │
╰──────────────────────────────────────────────────────────╯

        💰 Available Balance : ${self.coin}
        🏦 Outstanding Loan  : ${self.loan}
        📈 Interest Rate     : 5% / Collection
        ⭐ Client Status      : Platinum

═══════════════════════════════════════════════════════════════

    [1] 💵 Apply for a Loan
    [2] 💳 Repay Outstanding Debt
    [3] 📊 View Financial Report
    [4] 🚪 Return

═══════════════════════════════════════════════════════════════''')
        try:
            num=int(input())
            if num==1:
                self.addloan()
            elif num==2:
                self.volrepay()
            elif num==3:
                self.viewfinancialreport
            elif num==4:
                pass
            self.lv()
        except Exception as e:
            print(e)
            
            print("bruh that aint a number -_-")
            return
    def network(self):

        cityinfo = {
            "la": {
                "name": "🌴 LOS ANGELES",
                "rank": "Hollywood Insider",
                "icon": "🌴"
            },
            "mm": {
                "name": "🌊 MIAMI",
                "rank": "Beach Favorite",
                "icon": "🌊"
            },
            "lv": {
                "name": "🎰 LAS VEGAS",
                "rank": "High Roller",
                "icon": "🎰"
            }
        }

        

        info = cityinfo[self.city]

        local = []

        for client in self.clients:
            if client.incity(self.city) and client.trust > 0:
                local.append(client)

        print(f"""
══════════════════════════════════════════════════════════════════════════════
                        🌐 VIP UNDERWORLD NETWORK
                    "Power Is Measured In Connections"
══════════════════════════════════════════════════════════════════════════════

    {info["name"]}
    👥 Known Contacts : {len(local)}
    ⭐ Network Rank   : {info["rank"]}

══════════════════════════════════════════════════════════════════════════════
    """)

        if len(local) == 0:

            print("""
 Nobody in this city knows your name yet.

💼 Complete business deals.
🤝 Earn trust.
🌐 Unlock influential contacts.

══════════════════════════════════════════════════════════════════════════════

                        ↩ [0] Return

══════════════════════════════════════════════════════════════════════════════
    """)

            try:
                if int(input("Choose ► ")) == 0:
                    return
            except:
                return

        for i, client in enumerate(local):

            icon = self.occemoji(client.occupation)

            filled = client.trust // 10
            bar = "█" * filled + "░" * (10 - filled)

            print(f"""[{i+1}] {icon} {client.name}
    {client.occupation}
    🤝 Trust : {bar} {client.trust}/100 • {client.trusttitle()}

──────────────────────────────────────────────────────────────────────────────""")

        print(f"""

══════════════════════════════════════════════════════════════════════════════

                👤 [1-{len(local)}] View Contact
                ↩  [0] Return

══════════════════════════════════════════════════════════════════════════════
    """)
        while True:

            try:
                choice = int(input("Choose ► "))

                if choice == 0:
                    if self.city == "la":
                        self.la()   
                    elif self.city == "mm":
                        self.mm()
                    elif self.city == "lv":
                        self.lv()
                    return

                if 1 <= choice <= len(local):

                    print("\n" * 3)

                    local[choice - 1].intro()

                    input("\nPress Enter to return to the network...")

                    print("\n" * 4)

                    self.network()
                    return

                else:
                    print("❌ Invalid Contact ID.")

            except Exception as e:
                print(e)
                print("bruh that aint a number -_-")
    def occemoji(self,job):

        job = job.lower()

        if "strip" in job:
            return "💃"
        elif "casino" in job:
            return "🎲"
        elif "escort" in job:
            return "💋"
        elif "photo" in job:
            return "📸"
        elif "fashion" in job or "boutique" in job:
            return "👗"
        elif "club" in job:
            return "🍸"
        elif "yacht" in job:
            return "🛥"
        elif "bank" in job:
            return "🏦"
        elif "casting" in job:
            return "🎬"
        return "👤"
    def airway(self, city):#updation done

        fare = 5000

        airports = {
            "la": (
                "🛫 Los Angeles International Airport (LAX)",
                [
                    ("🌊 Miami", "Miami International Airport (MIA)"),
                    ("🎰 Las Vegas", "Harry Reid International Airport (LAS)")
                ]
            ),

            "mm": (
                "🛫 Miami International Airport (MIA)",
                [
                    ("🌴 Los Angeles", "Los Angeles International Airport (LAX)"),
                    ("🎰 Las Vegas", "Harry Reid International Airport (LAS)")
                ]
            ),

            "lv": (
                "🛫 Harry Reid International Airport (LAS)",
                [
                    ("🌴 Los Angeles", "Los Angeles International Airport (LAX)"),
                    ("🌊 Miami", "Miami International Airport (MIA)")
                ]
            )
        }

        current, dest = airports[city]

        print(f"""
══════════════════════════════════════════════════════════════════════
                            ✈ IMPERIAL AIRWAYS ✈
══════════════════════════════════════════════════════════════════════

    Current Airport

        {current}

    ╭──────────────────────────────────────────────────────────────╮
    │                  Available Destinations                      │
    ╰──────────────────────────────────────────────────────────────╯

    [1] {dest[0][0]}
        {dest[0][1]}
        💵 Travel Cost : ${fare}

    [2] {dest[1][0]}
        {dest[1][1]}
        💵 Travel Cost : ${fare}

    [3] 🚪 Return to City

══════════════════════════════════════════════════════════════════════
     """, end="")
        if self.coin < fare:
            print("\n\n🚫 Insufficient funds for travel. Please earn more before flying.")
            print("Returning to the city menu...")
            time.sleep(3)
            self.la()
            return 
        else:
            try:
                choice = int(input("Choose your destination ►"))
                if choice == 1:
                    self.coin -= fare
                    if city == "la":
                        self.city = "mm"
                        self.travelanimation("mm")
                        self.update()

                        self.mm()
                        
                    elif city == "mm":
                        self.city = "la"
                        self.travelanimation("la")
                        self.update()
                        self.la()
                        
                    elif city == "lv":
                        self.city = "la"
                        self.travelanimation("la")
                        self.update()
                        self.la()
                    
                        
                elif choice == 2:
                    self.coin -= fare
                    if city == "la":
                        self.city = "lv"
                        self.travelanimation("lv")
                        self.update()
                        self.lv()
                       
                    elif city == "mm":
                        self.city = "lv"
                        self.travelanimation("lv")
                        self.update()
                        self.lv()
                        
                    elif city == "lv":
                        self.city = "mm"
                        self.travelanimation("mm")
                        self.update()
                        self.mm()
                    
                elif choice == 3:
                    if city == "la":
                        self.la()
                    elif city == "mm":
                        self.mm()
                    elif city == "lv":
                        self.lv()
                else:
                    print("Invalid choice. Please select a valid destination.")
            except Exception as e:
                print(e)
                
                print("bruh that aint a number -_-")
                return
    def travelanimation(self, city):

        cities = {

            "la": {
                "title": "🌴 LOS ANGELES 🌴",
                "welcome": "🎬 Welcome to Los Angeles — Where Dreams Become Legends.",
                "messages": [
                    "🎬 Rolling out the Hollywood red carpet",
                    "🌴 Cruising beneath endless palm trees",
                    "⭐ Spotting celebrities on Sunset Boulevard",
                    "📸 Preparing luxury photoshoots",
                    "🚘 Driving through Beverly Hills",
                    "🍷 Reserving VIP rooftop parties",
                    "💄 Touching up tomorrow's superstars",
                    "🎭 Opening the city's hottest nightclubs",
                    "🏖 Catching the Pacific sunset",
                    "✨ The City of Angels is calling"
                ]
            },

            "mm": {
                "title": "🌊 MIAMI 🌊",
                "welcome": "🌴 Welcome to Miami — Paradise Never Sleeps.",
                "messages": [
                    "🛥 Docking billionaire yachts",
                    "🌊 Flying over crystal blue waters",
                    "🏖 Preparing South Beach nightlife",
                    "🍹 Mixing tropical cocktails",
                    "🌺 Catching the ocean breeze",
                    "🦩 Flamingos welcome you home",
                    "☀️ Chasing the golden sunset",
                    "💎 Unlocking luxury beach resorts",
                    "🎧 Warming up the beach clubs",
                    "🌴 Paradise awaits..."
                ]
            },

            "lv": {
                "title": "🎰 LAS VEGAS 🎰",
                "welcome": "♠ Welcome to Las Vegas — Fortune Favors the Bold.",
                "messages": [
                    "🎲 Shuffling blackjack tables",
                    "🎰 Warming up slot machines",
                    "🍾 Chilling champagne for VIPs",
                    "💎 Unlocking the high roller lounge",
                    "♠ Calling the city's biggest gamblers",
                    "🌃 Neon lights illuminate the Strip",
                    "🥂 Reserving penthouse suites",
                    "💵 Counting stacks of casino cash",
                    "🎭 Raising the curtains for tonight's show",
                    "👑 Sin City never sleeps"
                ]
            }
        }

        data = cities[city]

        print("\n" + "═"*70)
        print(data["title"].center(70))
        print("═"*70 + "\n")

        for msg in random.sample(data["messages"], 5):
            print(msg, end="", flush=True)
            for _ in range(3):
                time.sleep(0.35)
                print(".", end="", flush=True)
            print(" ✔")

        print("\n" + "═"*70)
        print(data["welcome"].center(70))
        print("═"*70)
        time.sleep(1.5)
    def load(self, city="la"):#updation done
        town={"la":"Los Angeles","mm":"Miami","lv":"Las Vegas"}


        messages = [
            f"Connecting to the {town.get(city)} nightlife",
            "Reserving VIP clients",
            "Preparing tonight's hottest lineup",
            "Paying off local authorities",
            "Opening underground operations"
        ]

        print("""
    ███████╗███████╗██╗  ██╗    ██████╗ ██████╗ ██╗██╗   ██╗███████╗
    ██╔════╝██╔════╝╚██╗██╔╝    ██╔══██╗██╔══██╗██║██║   ██║██╔════╝
    ███████╗█████╗   ╚███╔╝     ██║  ██║██████╔╝██║██║   ██║█████╗
    ╚════██║██╔══╝   ██╔██╗     ██║  ██║██╔══██╗██║╚██╗ ██╔╝██╔══╝
    ███████║███████╗██╔╝ ██╗    ██████╔╝██║  ██║██║ ╚████╔╝ ███████╗
    ╚══════╝╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚══════╝
    """)

        print("════════════════════════════════════════════════════════════════════")
        print("                 💋 E N T E R I N G   S E X   D R I V E 💋")
        print("════════════════════════════════════════════════════════════════════\n")

        for msg in messages:
            print(msg, end="", flush=True)

            for _ in range(3):
                time.sleep(0.4)
                print(".", end="", flush=True)

            print(" ✔")

        print("\n════════════════════════════════════════════════════════════════════")
        print(f"             🌃 Welcome to {town.get(city)}. Own the Night. 🌃")
        print("════════════════════════════════════════════════════════════════════")

        time.sleep(1)
        if city=="la":
            self.la()
        elif city=="mm":
            self.mm()
        elif city=="lv":
            self.lv()
    def volrepay(self):#updation done
        print(f"Your current balance is ${self.coin} and your outstanding loan is ${self.loan}.")
        try:
            repay_amount = int(input("Enter the amount you wish to repay: "))
            if 0 < repay_amount <= self.coin:
                if repay_amount > self.loan:
                    print(f"You are trying to repay more than your outstanding loan. Repaying only ${self.loan}.")
                    repay_amount = self.loan
                self.coin -= repay_amount
                self.loan -= repay_amount
                print(f"Successfully repaid ${repay_amount}. New balance: ${self.coin}, Outstanding loan: ${self.loan}.")
                print("Returning to the city...")
                self.update()
                time.sleep(2)
                if self.city == "la":
                    self.la()
                elif self.city == "mm":
                    self.mm()
                elif self.city == "lv":
                    self.lv()
            else:
                print("Invalid repayment amount. Please enter a positive number not exceeding your available cash.")
        except Exception as e:
            print(e)
            
            print("Invalid input. Please enter a valid number.")
    def getrux(self):
        return {

        # ==============================
        # LOS ANGELES BEAUTY ATELIER
        # ==============================

        "labeauty1": [
            "🍒 Bombshell Package",
            "Permanently increases the girl's Boob Size by +1 cup.",
            15000,
            0
        ],

        "labeauty2": [
            "💋 Siren Face",
            "Permanently increases the girl's Face Rating by +4.",
            28000,
            0
        ],

        "labeauty3": [
            "✨ Hollywood Hottie",
            "Permanently increases both Boob Size by +1 cup and Face Rating by +4.",
            40000,
            0
        ],

        # ==============================
        # MIAMI BEAUTY ATELIER
        # ==============================

        "mmbeauty1": [
            "👙 Beach Bombshell",
            "Permanently increases the girl's Boob Size by +1 cup.",
            18000,
            0
        ],

        "mmbeauty2": [
            "☀️ Sun-Kissed Glow",
            "Permanently increases the girl's Face Rating by +4.",
            33000,
            0
        ],

        "mmbeauty3": [
            "🌺 Paradise Diva",
            "Permanently increases both Boob Size by +1 cup and Face Rating by +4.",
            47000,
            0
        ],

        # ==============================
        # LAS VEGAS BEAUTY ATELIER
        # ==============================

        "lvbeauty1": [
            "💎 Diamond Bombshell",
            "Permanently increases the girl's Boob Size by +1 cup.",
            25000,
            0
        ],

        "lvbeauty2": [
            "💋 Vegas Vixen",
            "Permanently increases the girl's Face Rating by +4.",
            40000,
            0
        ],

        "lvbeauty3": [
            "👑 Sin City Queen",
            "Permanently increases both Boob Size by +1 cup and Face Rating by +4.",
            60000,
            0
        ],

        # ==============================
        # ESSENTIAL COLLECTION
        # ==============================

        "ess1": [
            "💊 Morning Luxe Pill",
            "Permanent. Prevents conception with 50% effectiveness.",
            4000,
            0
        ],

        "ess2": [
            "📀 Magnum Gold Condom",
            "Permanent. Prevents conception with 100% effectiveness.",
            7000,
            0
        ],

        "ess3": [
            "🔒 Cuffs of Passion",
            "Equippable. Prevents arrest while equipped.",
            9000,
            0
        ],

        "ess4": [
            "🍼 Baby Bliss Bottle",
            "Permanent. Once used, its permanent for her and she receives a baby.",
            15000,
            0
        ],

        "ess5": [
            "🖤 Walk of No Shame",
            "Consumable. Ends an in-game pregnancy.",
            20000,
            0
        ],

        # ==============================
        # LOS ANGELES SIGNATURE COLLECTION
        # ==============================

        "laitem1": [
            "💄 Scarlet Kiss Lipstick",
            "While equipped: +2 Level and Party earnings +20%.",
            12000,
            0
        ],

        "laitem2": [
            "👗 Starlight Gown",
            "While equipped: +5 Level in Los Angeles.",
            18000,
            0
        ],

        "laitem3": [
            "🖤 Velvet Vixen Lingerie",
            "While equipped: +7 Level in Los Angeles, +5 elsewhere.",
            28000,
            0
        ],

        "laitem4": [
            "🌹 Midnight Rose Perfume",
            "While equipped: +4 Level in LA and Party earnings +50%.",
            35000,
            0
        ],

        "laitem5": [
            "⛓ Rodeo Slut Choker",
            "While equipped: +20 Level in Los Angeles, +15 elsewhere.",
            75000,
            0
        ],

        # ==============================
        # MIAMI SIGNATURE COLLECTION
        # ==============================

        "mmitem1": [
            "👙 South Beach Bikini",
            "While equipped: +5 Level in Miami. Yacht earnings +20%.",
            12000,
            0
        ],

        "mmitem2": [
            "🩱 Ocean Muse Swimsuit",
            "While equipped: +8 Level in Miami, +5 elsewhere.",
            22000,
            0
        ],

        "mmitem3": [
            "🕶 Ocean Temptress Shades",
            "While equipped: +3 Level in Miami. Photoshoot earnings +40%.",
            35000,
            0
        ],

        "mmitem4": [
            "🌺 Tropical Desire Perfume",
            "While equipped: +5 Level in Miami. Yacht earnings +50%.",
            50000,
            0
        ],

        "mmitem5": [
            "💋 Paradise Slut Collar",
            "While equipped: +20 Level in Miami, +15 elsewhere.",
            100000,
            0
        ],

        # ==============================
        # LAS VEGAS SIGNATURE COLLECTION
        # ==============================

        "lvitem1": [
            "💎 Feminique Corset",
            "While equipped: +8 Level in Las Vegas, +5 elsewhere. Casino earnings +20%.",
            15000,
            0
        ],

        "lvitem2": [
            "👗 Diamond Diva Dress",
            "While equipped: +10 Level in Las Vegas.",
            28000,
            0
        ],

        "lvitem3": [
            "🖤 Sin City Lingerie",
            "While equipped: +12 Level in Las Vegas, +7 elsewhere.",
            42000,
            0
        ],

        "lvitem4": [
            "🍷 Midnight Sin Perfume",
            "While equipped: +6 Level in Las Vegas. Casino earnings +50%.",
            65000,
            0
        ],

        "lvitem5": [
            "👑 Sin Darling Slut Crown",
            "While equipped: +25 Level in Las Vegas, +18 elsewhere.",
            125000,
            0
        ]
    }
    def shopbox(self, intent):

        shops = {
            "laitem": ("laitem", 5),
            "mmitem": ("mmitem", 5),
            "lvitem": ("lvitem", 5),
            "labeauty": ("labeauty", 3),
            "mmbeauty": ("mmbeauty", 3),
            "lvbeauty": ("lvbeauty", 3),
            "ess": ("ess", 5)
        }

        prefix, total = shops[intent]

        INNER = 74

        for i in range(1, total + 1):

            item = self.inventory[f"{prefix}{i}"]

            title = f"[{i}] {item[0]}"
            price = f"$ {item[2]}"

            left =self.pad(title, INNER - wcswidth(price))
            bio =self.pad("✦ " + item[1], INNER)
            if not "beauty" in intent:
                own =self.pad(f"👜 In Wardrobe : {item[3]}", INNER)

            print("╭" + "─"*INNER + "╮")
            print(f"│{left}{price}│")
            print(f"│{bio}│")
            if not "beauty" in intent:
                print(f"│{own}│")
            print("╰" + "─"*INNER + "╯")

        ret =self.pad(f"[{total+1}] 🌴 Return", INNER)

        print("╭" + "─"*INNER + "╮")
        print(f"│{ret}│")
        print("╰" + "─"*INNER + "╯")
    def purchase(self, intent, choice):

        shops = {
            "laitem": ("laitem", 5),
            "mmitem": ("mmitem", 5),
            "lvitem": ("lvitem", 5),
            "labeauty": ("labeauty", 3),
            "mmbeauty": ("mmbeauty", 3),
            "lvbeauty": ("lvbeauty", 3),
            "ess": ("ess", 5)
        }

        cities = {
            "la": "Los Angeles",
            "mm": "Miami",
            "lv": "Las Vegas"
        }

        prefix, total = shops[intent]

        if choice < 1 or choice > total:
            print("❌ Invalid choice. Please select a valid item number.")
            return

        item_key = f"{prefix}{choice}"
        item = self.inventory[item_key]

        # ==========================================================
        # BEAUTY ITEMS
        # ==========================================================

        if "beauty" in intent:

            girls = self.checkgirl("beauty")

            if girls == []:
                print(f"❌ No girl in {cities[self.city]} is available for a beauty upgrade right now.")
                return

            girl = self.listgirls(girls)

            if self.coin < item[2] and not girl==None:
                print("❌ Insufficient funds to purchase this beauty enhancement.")
                return
            if  girl==None:
                if "la" in intent:
                    self.lashop(2)
                elif "mm" in intent:
                    self.mmshop(2)
                elif "lv" in intent:
                    self.lvshop(2)
            elif girl.glowup(item_key):

                self.coin -= item[2]
                self.inventory[item_key][3] += 1
                self.update()
                print(f"✨ {girl.name} has successfully received {item[1]}.")
                print(f"💰 ${item[2]} deducted. Remaining Balance: ${self.coin}.")
                return
            else:
                print(f"❌ {girl.name}'s upgrade  was unsuccessful.")
                return


        # ==========================================================
        # ESSENTIAL 4 (BABY BIRTH)
        # ==========================================================

        if intent == "ess" and choice == 4:

            girls = self.checkgirl("birth")

            if girls == []:
                print(f"❌ No girl in {cities[self.city]} is available for childbirth right now.")
                return

            girl = self.listgirls(girls)
            if  girl==None:
                if self.city == "la":
                    self.lashop(3)
                elif self.city == "mm":
                    self.mmshop(3)
                elif self.city == "lv":
                    self.lvshop(3)

            if self.coin < item[2]:
                print("❌ Insufficient funds to purchase this service.")
                return

            self.coin -= item[2]
            self.inventory[item_key][3] += 1

            girl.deliver()
            self.update()

            print(f"👶 {girl.name} has successfully completed childbirth.")
            print(f"💰 ${item[2]} deducted. Remaining Balance: ${self.coin}.")
            time.sleep(1.5)
            if self.city == "la":
                self.lashop(3)
            elif self.city == "mm":
                self.mmshop(3)
            elif self.city == "lv":
                self.lvshop(3)
            return

        # ==========================================================
        # ESSENTIAL 5 (ABORTION)
        # ==========================================================

        if intent == "ess" and choice == 5:

            girls = self.checkgirl("abortion")

            if girls == []:
                print(f"❌ No girl in {cities[self.city]} is available for this procedure right now.")
                return

            girl = self.listgirls(girls)
            if  girl==None:
                if self.city == "la":
                    self.lashop(3)
                elif self.city == "mm":
                    self.mmshop(3)
                elif self.city == "lv":
                    self.lvshop(3)

            if self.coin < item[2]:
                print("❌ Insufficient funds to purchase this service.")
                return

            self.coin -= item[2]
            self.inventory[item_key][3] += 1

            girl.abort()
            self.update()

            print(f"🏥 {girl.name} has successfully undergone the procedure.")
            print(f"💰 ${item[2]} deducted. Remaining Balance: ${self.coin}.")
            time.sleep(1.5)
            if self.city == "la":
                self.lashop(3)
            elif self.city == "mm":
                self.mmshop(3)
            elif self.city == "lv":
                self.lvshop(3)
            return
            

        # ==========================================================
        # NORMAL PURCHASE (ITEMS + ESS1/ESS2/ESS3)
        # ==========================================================

        if self.coin < item[2]:
            print("❌ Insufficient funds to purchase this item.")
            return

        self.coin -= item[2]
        self.inventory[item_key][3] += 1
        self.update()

        print(f"✅ Successfully purchased {item[0]} for ${item[2]}.")
        print(f"💰 Remaining Balance: ${self.coin}.")
    def checkgirl(self, intent):

        cities = {
            "la": "Los Angeles",
            "mm": "Miami",
            "lv": "Las Vegas"
        }
        finallist=[]

        if intent == "beauty":
            for girl in self.girls:
                if girl.city == self.city and girl.jail==False and girl.preg==False and (girl.level<30 or girl.cup != "G"):
                    finallist.append(girl)
        elif intent == "birth"  or intent == "abortion":
            for girl in self.girls:
                if girl.city == self.city and girl.jail==False and girl.preg==True:
                    finallist.append(girl)
        elif intent=="hollywood":
            for girl in self.girls:
                if girl.city == self.city and girl.jail==False and girl.preg==False and girl.effectivelevel>=15 and girl.cup not in ["A","B"]:
                    finallist.append(girl)
        elif intent=="la":
            for girl in self.girls:
                if girl.city == "la" and girl.jail==False:
                    finallist.append(girl)
        elif intent=="mm":
            for girl in self.girls:
                if girl.city == "mm" and girl.jail==False: 
                    finallist.append(girl)
        elif intent=="lv":
            for girl in self.girls:
                if girl.city == "lv" and girl.jail==False:
                    finallist.append(girl)
        elif intent=="lastrip":
            for girl in self.girls:
                if girl.city == "la" and girl.jail==False and 18<=girl.age<=30:
                    finallist.append(girl)
        elif intent=="mmstrip":
            for girl in self.girls:
                if girl.city == "mm" and girl.jail==False and 18<=girl.age<=30:
                    finallist.append(girl)
        elif intent=="actress":
            for girl in self.girls:
                if girl.city == self.city and girl.jail==False and girl.preg==False and girl.effectivelevel>=40:
                    finallist.append(girl)

        print (f"💎 {len(finallist)} girl(s) available")
        return finallist
    def listgirls(self, girls=[],purp="simple"):

        girls = sorted(girls,
                    key=lambda girl: girl.effectivelevel,
                    reverse=True)
        k={"la":"💎","mm":"🌺","lv":"🎀"}
        ki=k[self.city]
        if purp=="simple":
            purpose="AVAILABLE GIRLS FOR SELECTION"
        elif purp=="strip":
            ki="🎀"
            purpose="STRIP THE STAR OF THE NIGHT"
        elif purp=="pimp":
            ki="🖤"
            purpose="PICK A GIRL TO COMMIT A SIN"
        elif purp=="vipsex":
            ki="🌹"
            purpose="VIP CONTRACT SELECTION"
        elif purp=="celebrity":
            ki="🌟"
            purpose="HOLLYWOOD CELEBRITY SHOWCASE"
        elif purp=="photo":
            ki="📸"
            purpose="SELECT THE HOTTIE OF tHE DAY"

        print("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
        title = f"{ki} {purpose} {ki}"
        print(f"║{title:^109}║")
        print("╠════╦══════════════════════════╦═══════════╦══════════╦════════════════════════════╦═══════════════════════════╣")
        print("║ 🆔 ║ 👩 Name                  ║ 💖 Beauty ║ 👙 Cup   ║ 👗 Wearing                 ║ 🛡 Using                   ║")
        print("╠════╬══════════════════════════╬═══════════╬══════════╬════════════════════════════╬═══════════════════════════╣")
        i=0
        for girl in girls:
            i+=1

            name = girl.name[:24]
            beauty = girl.effectivelevel
            cup = girl.cup
            if girl.boost==None:
                wearing = "Nothing"
            else:
                wearing = self.inventory[girl.boost][0]
            if girl.guard==None:
                guard = "Nothing"
            else:
                guard = self.inventory[girl.guard][0]

            # wearing = "Nothing" if girl.boost is None else self.inventory[girl.boost][0]
            # guard = "Nothing" if girl.guard is None else self.inventory[girl.guard][0]

            wearing = removeemoji(wearing)[:26]
            guard = removeemoji(guard)[:26]

            print(
                f"║ {i:^2} "
                f"║ {name:<24} "
                f"║ {beauty:^9} "
                f"║ {cup:^8} "
                f"║ {wearing:<26} "
                f"║ {guard:<26}║"
            )
        

        print("╠════╬══════════════════════════╬═══════════╬══════════╬════════════════════════════╬═══════════════════════════╣")
        print(
                f"║ {i+1:^2} "
                f"║ {"Return":<24} "
                f"║ {"x":^9} "
                f"║ {"x":^8} "
                f"║ {"xxx":^26} "
                f"║ {"xxx":^26}║"
            )
        print("╚════╩══════════════════════════╩═══════════╩══════════╩════════════════════════════╩═══════════════════════════╝")
        
        
       

        while True:
            try:
                choice = int(input("\n✨ Select Girl ID : "))
                if 1 <= choice <= len(girls):
                    return girls[choice-1]
                elif choice == len(girls) + 1:
                    return None

                print("❌ Invalid Girl ID.")

            except Exception as e:
                print(e)
                
                print("❌ Please enter a valid number.")
    def listgirlsmult(self, girls=[],purp="simple",limit=1):
        finallist=[]
        if len(girls) < limit:
            print(f"❌ Not enough girls available for {purp} selection.")
            return None
        

        girls = sorted(girls,
                    key=lambda girl: girl.effectivelevel,
                    reverse=True)
        k={"la":"💎","mm":"🌺","lv":"🎀"}
        ki=k[self.city]
        if purp=="simple":
            purpose="AVAILABLE GIRLS FOR SELECTION"
        elif purp=="strip":
            ki="🎀"
            purpose="STRIP THE STAR OF THE NIGHT"
        elif purp=="pimp":
            ki="🖤"
            purpose="PICK A GIRL TO COMMIT A SIN"
        elif purp=="vipsex":
            ki="🌹"
            purpose="VIP CONTRACT SELECTION"
        elif purp=="celebrity":
            ki="🌟"
            purpose="HOLLYWOOD CELEBRITY SHOWCASE"
        elif purp=="photo":
            ki="📸"
            purpose="SELECT THE HOTTIE OF tHE DAY"
        elif purp=="cast":
            ki="🎬"
            purpose="CASTING CALL SELECTION"
        elif purp=="party":
            ki="🎊"
            purpose="PARTY ALL NIGHT"

        print("╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
        title = f"{ki} {purpose} {ki}"
        print(f"║{title:^109}║")
        print("╠════╦══════════════════════════╦═══════════╦══════════╦════════════════════════════╦═══════════════════════════╣")
        print("║ 🆔 ║ 👩 Name                  ║ 💖 Beauty ║ 👙 Cup   ║ 👗 Wearing                 ║ 🛡 Using                   ║")
        print("╠════╬══════════════════════════╬═══════════╬══════════╬════════════════════════════╬═══════════════════════════╣")
        i=1
        for i, girl in enumerate(girls, start=1):

            name = girl.name[:24]
            beauty = girl.effectivelevel
            cup = girl.cup
            if girl.boost==None:
                wearing = "Nothing"
            else:
                wearing = self.inventory[girl.boost][0]
            if girl.guard==None:
                guard = "Nothing"
            else:
                guard = self.inventory[girl.guard][0]

            # wearing = "Nothing" if girl.boost is None else self.inventory[girl.boost][0]
            # guard = "Nothing" if girl.guard is None else self.inventory[girl.guard][0]

            wearing = removeemoji(wearing)[:26]
            guard = removeemoji(guard)[:26]

            print(
                f"║ {i:^2} "
                f"║ {name:<24} "
                f"║ {beauty:^9} "
                f"║ {cup:^8} "
                f"║ {wearing:<26} "
                f"║ {guard:<26}║"
            )
        print("╚════╩══════════════════════════╩═══════════╩══════════╩════════════════════════════╩═══════════════════════════╝")
        
        
       
        if len(girls)==limit:
            print(f"\n✨ Automatically selecting all {limit} available girls for {purp}.")
            print(f"✅ Selected girls: {[girl.name for girl in girls]}")
            time.sleep(1.5)
            return girls
        i=0
        while True and i<limit:
            try:
                choice = int(input("\n✨ Select Girl ID : "))
                if 1 <= choice <= len(girls) and girls[choice-1] not in finallist:
                    finallist.append(girls[choice-1])
                    print(f"✅ Selected {girls[choice-1].name}. ({i+1}/{limit})")
                    i += 1
                elif girls[choice-1] in finallist:
                    print(f"❌ {girls[choice-1].name} has already been selected. Please choose a different girl.")
                elif choice == len(girls) + 1:
                    return None
                else:
                    print("❌ Invalid Girl ID.")

            except Exception as e:
                print(e)
                
                print("❌ Please enter a valid number.")
        print(f"\n✅ Successfully selected {', '.join([girl.name for girl in finallist])} for {purp}.")
        return finallist
    def recruitlist(self,girls):
        print("╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
        title = "🌟 AVAILABLE RECRUITS 🌟"
        print(f"║{title:^123}║")
        print("╠════╦══════════════════════════╦═══════════╦══════════╦═══════════╦═══════════════════════════╦══════════════════════════════╣")
        print("║ 🆔 ║ 👩 Name                  ║ 💖 Beauty ║ 👙 Cup   ║ 🌍 Nation ║      🎭 Personality       ║    👗 Wearing     🛡 Using    ║")
        print("╠════╬══════════════════════════╬═══════════╬══════════╬═══════════╬═══════════════════════════╬══════════════════════════════╣")
        i=1
        for girl in girls:

            personality = girl.persona1+" • "+girl.persona2
            guard= "Nothing" if girl.guard is None else removeemoji(self.inventory[girl.guard][0])[:14]
            boost= "Nothing" if girl.boost is None else removeemoji(self.inventory[girl.boost][0])[:14]

            print(
                f"║ {str(i):^2} ║ "
                f"{girl.name:<24} ║ "
                f"{girl.effectivelevel:^9} ║ "
                f"{girl.cup:^8} ║ "
                f"{girl.nation:^9} ║ "
                f"{personality:^25} ║ "
                f"{boost:^14} {guard:^14}║"
            )
            i+=1

        print("╠════╩══════════════════════════╩═══════════╩══════════╩═══════════╩═══════════════════════════╩══════════════════════════════╣")
        print("║                                              [0] 🔙 Return                                                                  ║")
        print("╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝")
        print()
        print("Choose Recruit ► ", end="")

        while True:
            try:
                choice = int(input())
                if 1 <= choice <= len(girls):
                    return girls[choice-1]
                elif choice == 0:
                    return None
            except Exception as e:
                print(e)
                
                print("❌ Please enter a valid number.")
        
    def rejuvenate(self, girl):
        k={"la":"💎","mm":"🌺","lv":"🎀"}
        ki=k[self.city]

        print("╔═════════════════════════════════════════════════════════════════════════╗")
        print(f"║                   {ki} VELVET VIXEN SUITE {ki}                              ║")
        print("╠════╦══════════════════════════════════════╦══════════════╦══════════════╣")
        print("║ ID ║ 👜 Item Name                         ║ ✨ Category  ║ 📦 Owned     ║")
        print("╠════╬══════════════════════════════════════╬══════════════╬══════════════╣")

        available = {}
        sl = 1

        for key, item in self.inventory.items():

            # Skip if player owns none
            if item[3] <= 0:
                continue

            # Skip currently equipped items
            if key == girl.boost or key == girl.guard:
                continue

            # Decide category
            if "beauty" in key or key in ["ess4", "ess5"]:
                category = "💋 Beauty"
                continue

            elif key.startswith("ess"):
                category = "🛡 Guard"

            else:
                category = "👗 Outfit"

            name = removeemoji(item[0])[:36]

            available[sl] = key

            print(
                f"║ {sl:^2} "
                f"║ {name:<36} "
                f"║ {category:<11} "
                f"║ {item[3]:^12} ║"
            )

            sl += 1

        print("╠════╩══════════════════════════════════════╩══════════════╩══════════════╣")

        print(
            f"║ {sl:^2} "
            f"║ {'🔙 Return':<65} ║"
        )

        print("╚═════════════════════════════════════════════════════════════════════════╝")

        while True:

            try:

                choice = int(input("\n✨ Select Item ID : "))

                # Return
                if choice == sl:
                    if self.city == "la":
                        self.lashop(4)
                    elif self.city == "mm":
                        self.mmshop(4)
                    elif self.city == "lv":
                        self.lvshop(4)
                    return

                if choice not in available:
                    print("❌ Invalid Item ID.")
                    continue

                selected_key = available[choice]

                # ---------------------- GUARD ----------------------

                if selected_key.startswith("ess"):

                    # Return previous guard
                    if girl.guard is not None:
                        self.inventory[girl.guard][3] += 1

                    # Equip new guard
                    girl.guard = selected_key

                    # Remove one from inventory
                    self.inventory[selected_key][3] -= 1

                    print(f"\n🛡 {girl.name} is now using {self.inventory[selected_key][0]}.")
                    print("✅ Equipment updated successfully.")
                    return

                # ---------------------- OUTFIT ----------------------

                else:

                    # Return previous outfit
                    pastboost = girl.boost

                    if pastboost is not None:
                        self.inventory[pastboost][3] += 1

                    girl.boost = selected_key
                    self.inventory[selected_key][3] -= 1
                    girl.getboost()

                    print(f"\n👗 {girl.name} is now wearing {self.inventory[selected_key][0]}.")
                    print("✅ Wardrobe updated successfully.")
                    self.update()
                    time.sleep(1.5)
                    if self.city == "la":
                        self.lashop(4)
                    elif self.city == "mm":
                        self.mmshop(4)
                    elif self.city == "lv":
                        self.lvshop(4)
                    return

            except ValueError:
                print("❌ Please enter a valid number.")
    def recruitgirls(self, amount, tier, celebonly=False, nationonly=None):
        

        girls = []
        names = set()

        while len(girls) < amount:

            girl = self.randomgirl(
                tier=tier,
                celebonly=celebonly,
                nationonly=nationonly
            )

            if girl.name in names:
                continue

            names.add(girl.name)
            girls.append(girl)
            

        return girls

    def randomgirl(self,tier,celebonly=False,nationonly=None):
        with open("D:\\py things\\python  dem\\flirt.json", "r", encoding="utf-8") as file:
            dialx = json.load(file)
            dialogue = dialx.get("girls")
            b=True
            while b:
                newgirl = random.choice(dialogue)
                b=False
                for girlx in self.girls:
                    if girlx.name == newgirl[0]:
                        b=True
                        break
        with open("D:\\py things\\python  dem\\flirt.json", "r", encoding="utf-8") as file:
            dialy = json.load(file)
            dialogue = dialy.get("celebs")
            b=True
            while b:
                newceleb = random.choice(dialogue)
                b=False
                for girlx in self.girls:
                    if girlx.name == newceleb[0]:
                        b=True
                        break
        
        persona1=["Sweet","Shy","Tsundere","Bossy","Playful","Elegant","Cold"]
        persona2=["Girl Next Door","Goth","Mommy","Tomboy","Party Girl","Office Lady","Princess"]        
        if celebonly==True:
            fresher=girl(newceleb[0],random.randint(21,25),self.defaultrate,f"{self.city}item{random.choice([3,5])}",False,False,self.city,random.choices(["D","DD","DDD"],weights=[5,3,2],k=1)[0],"ess1",0,"clean",30,"neutral",random.choice(persona1),random.choice(persona2),newceleb[1],random.randint(22,25))     
        elif tier==1 :
            x=random.randint(1,6)
            if x<4:
                fresher=girl(newgirl[0],random.randint(21,25),self.defaultrate,None,False,False,self.city,random.choices(["D","DD","DDD"],weights=[5,3,2],k=1)[0],None,0,"clean",30,"neutral",random.choice(persona1),random.choice(persona2),newgirl[1],random.randint(22,25))
            elif x<6:   
                fresher=girl(newgirl[0],random.randint(21,25),self.defaultrate,f"{self.city}item{random.choice([2,3])}",False,False,self.city,random.choices(["D","DD","DDD"],weights=[5,3,2],k=1)[0],None,0,"clean",30,"neutral",random.choice(persona1),random.choice(persona2),newgirl[1],random.randint(22,25))
            elif x==6:
                fresher=girl(newceleb[0],random.randint(21,25),self.defaultrate,f"{self.city}item{random.choice([3,5])}",False,False,self.city,random.choices(["D","DD","DDD"],weights=[5,3,2],k=1)[0],"ess1",0,"clean",30,"neutral",random.choice(persona1),random.choice(persona2),newceleb[1],random.randint(22,25))
        elif tier==2:
            x=random.randint(1,3)
            if x<3:
                fresher=girl(newgirl[0],random.randint(16,20),self.defaultrate,None,False,False,self.city,random.choices(["C","D","DD"],weights=[4,4,2],k=1)[0],None,0,"clean",30,"neutral",random.choice(persona1),random.choice(persona2),newgirl[1],random.randint(20,22))
            elif x==3:
                fresher=girl(newgirl[0],random.randint(18,22),self.defaultrate,f"{self.city}item{random.choice([2,4])}",False,False,self.city,random.choices(["C","D","DD"],weights=[4,4,2],k=1)[0],None,0,"clean",30,"neutral",random.choice(persona1),random.choice(persona2),newgirl[1],random.randint(20,22))        
        elif tier==3:
            fresher=girl(newgirl[0],random.randint(11,15),self.defaultrate,None,False,False,self.city,random.choices(["B","C","D"],weights=[4,4,2],k=1)[0],None,0,"clean",30,"neutral",random.choice(persona1),random.choice(persona2),newgirl[1],random.randint(18,22))
        elif tier==4:
            fresher=girl(newgirl[0],random.randint(7,10),self.defaultrate,None,False,False,self.city,random.choices(["A","B","C"],weights=[5,3,2],k=1)[0],None,0,"clean",30,"neutral",random.choice(persona1),random.choice(persona2),newgirl[1],random.randint(18,20))


        elif tier==5:
            
            fresher=girl(newgirl[0],6,self.defaultrate,None,False,False,self.city,random.choices(["A","B","C"],weights=[6,3,1],k=1)[0],None,0,"clean",30,"neutral",random.choice(persona1),random.choice(persona2),newgirl[1],random.randint(18,20))
        
        return fresher

                


        
                    
    
    def pad(self,text, width):
        
        
        return text + " " * max(0, width - wcswidth(text))
    def randomclient(self):
        listedmaleclients=["Akira","Brandon","Cameron","Dante","Ethan","Felix","Gideon","Hector","Isaac","Jasper","Kai","Lorenzo","Maverick","Nico","Orion","Phoenix","Quentin","Rafael","Sebastian","Tobias","Jaxon","Xander","Zane","Liam","Noah","Elijah","James","William","Benjamin","Lucas","Henry","Alexander","Michael","Ethan","Daniel","Matthew","Aiden","Joseph"]
        newclient=client(random.choice(listedmaleclients),"M",random.randint(18,50),random.randint(1,10),"la",random.randint(1,10)/100,"nah",random.randint(1,10),"nah","nah",30)
        return newclient
        

    def main(self):
        print('''
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║          ██████╗ ██╗███╗   ███╗██████╗                       ║
║          ██╔══██╗██║████╗ ████║██╔══██╗                      ║
║          ██████╔╝██║██╔████╔██║██████╔╝                      ║
║          ██╔═══╝ ██║██║╚██╔╝██║██╔═══╝                       ║
║          ██║     ██║██║ ╚═╝ ██║██║                           ║
║          ╚═╝     ╚═╝╚═╝     ╚═╝╚═╝                           ║
║                                                              ║
║              💎  A N D   P A Y  💎                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
''')
        time.sleep(5)
        while True:
            print(f'''
╭──────────────────────────────────────────────────────────────╮
│                     ✦ PIMP & PAY ✦                           │
│               Underground Business Network                   │
╰──────────────────────────────────────────────────────────────╯

┌──────────────────────────────────────────────────────────────┐
│  💰 CASH          │ ${self.coin}                                  │
│  🏦 LOAN          │ ${self.loan}                                      │
│  👑 STATUS        │ Street Rookie                           │
│  👯 WORKERS       │ {len(self.girls)}                                       │
│  🚔 POLICE HEAT   │ LOW                                     │
│  📅 DAY           │ {self.count}                                       │
└──────────────────────────────────────────────────────────────┘

═══════════════ UNDERGROUND OPERATIONS ═══════════════

〔1〕👠 Recruit Talent
〔2〕📋 View Agency
〔3〕🏦 Bank & Loans
〔4〕💵 Private Clients
〔5〕📈 Inflation Office
〔6〕🌎 Sex Drive Network
〔7〕🚪 Save & Quit Game
''')
            while True:
                try:
                    yup = int(input("Choose an option :► "))
                    if 1 <= yup <= 7:
                        pass
                    else:
                        print("❌ Invalid choice. Please select a valid operation number.")
                        continue
                except Exception as e:
                    print(e)
                    
                    print("bruh that aint a number -_-")
                    continue

                
                if(yup==1):
                    self.addgirl()
                elif(yup==2):
                    self.view()
                elif(yup==3):
                    self.addloan()
                elif(yup==4):
                    self.globalpimp()
                elif(yup==5):
                    print("enter the amount u wanna inflate entry with :3\nyour girls are gonna be happy:3\n")
                    try: 
                        self.inflate(int(input()))
                    except IOError:
                        print("bruh u suck in numbers ;-;")
                elif(yup==7):
                    self.update()
                    
                    exit()
                elif(yup==6):
                    if a.city=="la":
                        a.load("la")
                    elif a.city=="mm":
                        a.load("mm")
                    elif a.city=="lv":
                        a.load("lv")
                
            

a=system()
a.la()
# b=movie()
# b.system=a
# b.market(3)
# b.output()
# b.proceed(a)