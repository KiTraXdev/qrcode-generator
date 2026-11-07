import qrcode
import tkinter as tk
from tkinter import filedialog 
fenetre = tk.Tk()
fenetre.title("generator QRCODE")
fenetre.geometry("600x500")
fenetre.config(bg="black")
fenetre.resizable(False, False)
def toolreseaux():
    reseau.pack_forget(),
    one.pack(), 
    comu.pack_forget()
    choix.pack(),
    menu.pack(side="bottom", pady=10),
    wifi.pack_forget()
def toolcomu():
     comu.pack_forget(),
     two.pack(),
     reseau.pack_forget()
     choix2.pack(),
     menu.pack(side="bottom", pady=10)
     wifi.pack_forget()
def toolwifi():
     wifi.pack_forget()
     tree.pack()
     choix3.pack()
     reseau.pack_forget()
     comu.pack_forget()
     menu.pack(side="bottom", pady=10)
def toolmenu():
    reseau.pack()
    comu.pack()
    wifi.pack()
    choix2.pack_forget()
    two.pack_forget()
    menu.pack_forget()
    choix.pack_forget()
    one.pack_forget()
    tiktok.pack_forget()
    instagram.pack_forget()
    youtube.pack_forget()
    snapchat.pack_forget()
    discord.pack_forget()
    facebook.pack_forget()
    x.pack_forget()
    twitch.pack_forget()
    reddit.pack_forget()
    pinterest.pack_forget()
    github.pack_forget()
    linkedin.pack_forget()
    telegram.pack_forget()
    whatsapp.pack_forget()
    spotify.pack_forget()
    roblox.pack_forget()
    steam.pack_forget()
    tel.pack_forget()
    sms.pack_forget()
    sms2.pack_forget()
    email.pack_forget()
    emails.pack_forget()
    emails2.pack_forget()
    tree.pack_forget()
    wpaname.pack_forget()
    wpamdp.pack_forget()
    choix3.pack_forget()
    wifiname.pack_forget()
    wifimname.pack_forget()
    wifimmdpl.pack_forget()
    choix.delete(0, tk.END)
    choix2.delete(0, tk.END)
    tiktok.delete(0, tk.END)
    instagram.delete(0, tk.END)
    youtube.delete(0, tk.END)
    snapchat.delete(0, tk.END)
    discord.delete(0, tk.END)
    facebook.delete(0, tk.END)
    x.delete(0, tk.END)
    twitch.delete(0, tk.END)
    reddit.delete(0, tk.END)
    pinterest.delete(0, tk.END)
    github.delete(0, tk.END)
    linkedin.delete(0, tk.END)
    telegram.delete(0, tk.END)
    whatsapp.delete(0, tk.END)
    spotify.delete(0, tk.END)
    roblox.delete(0, tk.END)
    steam.delete(0, tk.END)
    tel.delete(0, tk.END)
    sms.delete(0, tk.END)
    sms2.delete(0, tk.END)
    email.delete(0, tk.END)
    emails.delete(0, tk.END)
    emails2.delete(0, tk.END)
    choix3.delete(0, tk.END)
    wpaname.delete(0, tk.END)
    wpamdp.delete(0, tk.END)
    wifiname.delete(0, tk.END)
    wifimname.delete(0, tk.END)
    wifimmdp.delete(0, tk.END)
    tiktokl.pack_forget()
    instagraml.pack_forget()
    youtubel.pack_forget()
    snapchatl.pack_forget()
    discordl.pack_forget()
    facebookl.pack_forget()
    xl.pack_forget()
    twitchl.pack_forget()
    redditl.pack_forget()
    pinterestl.pack_forget()
    githubl.pack_forget()
    linkedinl.pack_forget()
    telegraml.pack_forget()
    whatsappl.pack_forget()
    spotifyl.pack_forget()
    robloxl.pack_forget()
    steaml.pack_forget()
    tell.pack_forget()
    smsl.pack_forget()
    smsl2.pack_forget()
    emaill.pack_forget()
    emailsl.pack_forget()
    emailsl2.pack_forget()
    wpanamel.pack_forget()
    wpamdpl.pack_forget()
    wifinamel.pack_forget()
    wifimnamel.pack_forget()
    wifimmdpl.pack_forget()
one = tk.Label(
    fenetre,
    text="[1  TIKTOK    ]\n"
         "[2  INSTAGRAM ]\n"
         "[3  YOUTUBE   ]\n"
         "[4  SNAPCHAT  ]\n"
         "[5  DISCORD   ]\n"
         "[6  FACEBOOK  ]\n"
         "[7  X         ]\n"
         "[8  TWITCH    ]\n"
         "[9  REDDIT    ]\n"
         "[10 PINTEREST ]\n"
         "[11 GITHUB    ]\n"
         "[12 LINKEDIN  ]\n"
         "[13 TELEGRAM  ]\n"
         "[14 WHATSAPP  ]\n"
         "[15 SPOTIFY   ]\n"
         "[16 ROBLOX    ]\n"
         "[17 STEAM     ]" ,
     font=("Arial", 10, "bold"),
     fg="blue",
     bg="black"
)
one.pack_forget()
two = tk.Label(
    fenetre,
    text="[1 TELEPHONE]\n[2 SMS]\n[3 EMAIL]\n[4 EMAIL sujet]",
    font=("Arial", 10 , "bold"),
    fg="green",
    bg="black"
)
two.pack_forget()
tree = tk.Label(
    fenetre,
    text="[1 WIFI WPA/WPA2]\n[2 WIFI SANS MDP]\n[3 WIFI MASQUER]",
    font=("Arial", 10 , "bold"),
    fg="red",
    bg="black"
)
tree.pack_forget()
choix2 = tk.Entry(
     fenetre,
     width=15,
     font=("Arial", 14),
     fg="black",
     bg="white"

)
choix3 = tk.Entry(
     fenetre,
     width=15,
     font=("Arial", 14),
     fg="black",
     bg="white"
)
reseau = tk.Button(
    fenetre,
    text="reseau sociaux",
    bg="blue",
    fg="white",
    width=15,
    height=2,
    command=toolreseaux,
)
reseau.pack()
comu = tk.Button(
     fenetre,
     text="communication",
    bg="green",
    fg="white",
    width=15,
    height=2,  
    command=toolcomu    
)
comu.pack()
wifi = tk.Button(
     fenetre,
     text="wifi",
    bg="red",
    fg="white",
    width=15,
    height=2,  
    command=toolwifi    
)
wifi.pack()
choix = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white",
)
choix.pack_forget()
menu = tk.Button(
    fenetre,
    text="menu",
    bg="white",
    fg="black",
    width=15,
    height=2,
    command=toolmenu  
)
menu.pack_forget()
tiktok = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
youtube = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
instagram = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
snapchat = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
discord = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
facebook = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
x = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
twitch = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
reddit = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
pinterest = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
github = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)

linkedin = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
telegram = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
whatsapp = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
spotify = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
roblox = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
steam = tk.Entry(
    fenetre,
    width=15,
    font=("Arial", 14),
    fg="black",
    bg="white"
)
tel = tk.Entry(
     fenetre,
     width=25,
     font=("Arial", 14),
     fg="black",
     bg="white"
)
sms = tk.Entry(
     fenetre,
     width=25,
     font=("Arial", 14),
     fg="black",
     bg="white"
)
sms2 = tk.Entry(
     fenetre,
     width=25,
     font=("Arial", 14),
     fg="black",
     bg="white"
)
email = tk.Entry(
     fenetre,
     width=25,
     font=("Arial", 14),
     fg="black",
     bg="white"
)
emails = tk.Entry(
     fenetre,
     width=25,
     font=("Arial", 14),
     fg="black",
     bg="white"
)
emails2 = tk.Entry(
     
     fenetre,
     width=25,
     font=("Arial", 14),
     fg="black",
     bg="white"
)
wpaname = tk.Entry(
     fenetre,
     width=25,
     font=("Arial", 14),
     fg="black",
     bg="white"
)
wpamdp = tk.Entry(
     fenetre,
     width=25,
     font=("Arial", 14),
     fg="black",
     bg="white"
)
wifiname = tk.Entry(
     fenetre,
     width=25,
     font=("Arial", 14),
     fg="black",
     bg="white"
)
wifimname = tk.Entry(
     fenetre,
     width=25,
     font=("Arial", 14),
     fg="black",
     bg="white"
)
wifimmdp = tk.Entry(
     fenetre,
     width=25,
     font=("Arial", 14),
     fg="black",
     bg="white"
)
tiktokl = tk.Label(


     fenetre,
     text="tiktok \n veuilleiz entre votre pseudo",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
instagraml = tk.Label(


     fenetre,
     text="instagram\n veuilleiz entre votre pseudo",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
youtubel = tk.Label(


     fenetre,
     text="youtube \n veuilleiz entre votre pseudo",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
snapchatl = tk.Label(
     fenetre,
     text="snapchat \n veuilleiz entre votre pseudo",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
discordl = tk.Label(
     fenetre,
     text="discord \n veuilleiz entre votre code",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
facebookl = tk.Label(
     fenetre,
     text="facebook \n veuilleiz entre votre pseudo",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
xl = tk.Label(
     fenetre,
     text="X \n veuilleiz entre votre pseudo",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
twitchl = tk.Label(
     fenetre,
     text="twitch \n veuilleiz entre votre pseudo",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
redditl = tk.Label(
     fenetre,
     text="reddit \n veuilleiz entre votre pseudo",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
githubl = tk.Label(
     fenetre,
     text="github \n veuilleiz entre votre pseudo",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
pinterestl = tk.Label(
     fenetre,
     text="pinterest \n veuilleiz entre votre pseudo",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
linkedinl = tk.Label(
     fenetre,
     text="linkedin \n veuilleiz entre votre pseudo",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
telegraml = tk.Label(
     fenetre,
     text="telegram \n veuilleiz entre votre pseudo",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
whatsappl = tk.Label(
     fenetre,
     text="whatsapp \n veuilleiz entre votre numero de telephone \n format requit : 612345678",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
spotifyl = tk.Label(
     fenetre,
     text="spotify \n veuilleiz entre votre identifiant",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
robloxl = tk.Label(
     fenetre,
     text="roblox \n veuilleiz entre votre identifiant",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
steaml = tk.Label(
     fenetre,
     text="steam \n veuilleiz entre votre identifiant",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
tell = tk.Label(
     fenetre,
     text="telephone \n veuilleiz entre votre numero de telephone \n format requit : 612345678",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
smsl = tk.Label(
     fenetre,
     text="sms \n veuilleiz entre votre numero de telephone \n format requit : 612345678",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
smsl2 = tk.Label(
     fenetre,
     text="veuillez entrer un message",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
emaill = tk.Label(
     fenetre,
     text="email \n veuillez entrer une adresse mail \n sous se format test@exemple.com ",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
emailsl = tk.Label(
     fenetre,
     text="email avec subject \n veuillez entrer une adresse mail \n sous se format test@exemple.com ",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
emailsl2 = tk.Label(
     fenetre,
     text="veuillez mettre un sujet",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
wpanamel = tk.Label(
     fenetre,
     text=" wifi wpa/wpa2 \n nom du wifi",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
wpamdpl = tk.Label(
     fenetre,
     text=" mot de passe du wifi",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
wifinamel = tk.Label(
     fenetre,
     text=" wifi sans mdp \n nom du wifi",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
wifimnamel = tk.Label(
     fenetre,
     text=" wifi masquer \n nom du wifi",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
wifimmdpl = tk.Label(
     fenetre,
     text=" mot de passe du wifi",
     font=("Arial", 15, "bold"),
     fg="white",
     bg="black"
)
def tool(event):
    value = choix.get()
    value2 = choix2.get()
    value3 = choix3.get()
    if value == "1":
        tiktokl.pack()
        tiktok.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "2":
        instagraml.pack()
        instagram.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "3":
        youtubel.pack()
        youtube.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "4":
        snapchatl.pack()
        snapchat.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "5":
        discordl.pack()
        discord.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "6":
       facebookl.pack()
       facebook.pack()
       choix.pack_forget()
       one.pack_forget()
    elif value == "7":
        xl.pack()
        x.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "8":
        twitchl.pack()
        twitch.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "9":
        redditl.pack()
        reddit.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "10":
       pinterestl.pack()
       pinterest.pack()
       choix.pack_forget()
       one.pack_forget()
    elif value == "11":
        githubl.pack()
        github.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "12":
        linkedinl.pack()
        linkedin.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "13":
        telegraml.pack()
        telegram.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "14":
        whatsappl.pack()
        whatsapp.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "15":
        spotifyl.pack()
        spotify.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "16":
        robloxl.pack()
        roblox.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value == "17":
        steaml.pack()
        steam.pack()
        choix.pack_forget()
        one.pack_forget()
    elif value2 == "1":
         tell.pack()
         tel.pack()
         choix2.pack_forget()
         two.pack_forget()
    elif value2 == "2":
        smsl.pack()
        sms.pack()
        smsl2.pack()
        sms2.pack()
        choix2.pack_forget()
        two.pack_forget()
    elif value2 == "3":
         emaill.pack()
         email.pack()
         choix2.pack_forget()
         two.pack_forget()
    elif value2 == "4":
         emailsl.pack()
         emails.pack()
         emailsl2.pack()
         emails2.pack()
         choix2.pack_forget()
         two.pack_forget()
    elif value3 == "1":
         wpanamel.pack()
         wpaname.pack()
         wpamdpl.pack()
         wpamdp.pack()
         choix3.pack_forget()
         tree.pack_forget()
    elif value3 == "2":
        wifinamel.pack()
        wifiname.pack()
        choix3.pack_forget()
        tree.pack_forget()   
    elif value3 == "3":
        wifimnamel.pack()
        wifimname.pack()
        wifimmdpl.pack()
        wifimmdp.pack()
        choix3.pack_forget()
        tree.pack_forget()   
choix.bind("<Return>", tool)
choix2.bind("<Return>", tool)
choix3.bind("<Return>", tool)
def tiktokqr(event):

    nametiktok = tiktok.get()

    lien = f"https://www.tiktok.com/@{nametiktok}"

    wn = qrcode.make(lien)

    chemin = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Image PNG", "*.png")],
        initialfile="QRCODE_tiktok.png",
        title="enresgister le QR code "
    ) 

    if chemin:
       
       wn.save(chemin)
def youtubeqr(event):
    nameyoutube = youtube.get()
    lien = f"https://www.youtube.com/@{nameyoutube}"
    wn = qrcode.make(lien)
    chemin = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Image PNG", "*.png")],
            initialfile="QRCODE_youtube.png",
            title="enresgister le QR code "
        ) 
    if chemin:
      wn.save(chemin)
def instagramqr(event):
    name = instagram.get()
    lien = f"https://www.instagram.com/{name}/"
    wn = qrcode.make(lien)
    chemin = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Image PNG", "*.png")],
            initialfile="QRCODE_instagram.png",
            title="enresgister le QR code "
        ) 
    if chemin:
           wn.save(chemin)
def snapchatqr(event):
    name = snapchat.get()
    lien = f"https://www.snapchat.com/add/{name}"
    wn = qrcode.make(lien)
    chemin = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Image PNG", "*.png")],
            initialfile="QRCODE_snapchat.png",
            title="enresgister le QR code "
        ) 
    if chemin:
           wn.save(chemin)
def discordqr(event):
    name = discord.get()
    lien = f"https://discord.gg/{name}"
    wn = qrcode.make(lien)
    chemin = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Image PNG", "*.png")],
            initialfile="QRCODE_discord.png",
            title="enresgister le QR code "
        ) 
    if chemin:
           wn.save(chemin)
def facebookqr(event):
    name = facebook.get()
    lien = f"https://www.facebook.com/{name}"
    wn = qrcode.make(lien)
    chemin = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Image PNG", "*.png")],
            initialfile="QRCODE_facebook.png",
            title="enresgister le QR code "
        ) 
    if chemin:
           wn.save(chemin)
def xqr(event):
    name = x.get()
    lien = f"https://x.com/{name}"
    wn = qrcode.make(lien)
    chemin = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Image PNG", "*.png")],
            initialfile="QRCODE_X.png",
            title="enresgister le QR code "
        ) 
    if chemin:
           wn.save(chemin)
def twitchqr(event):
    name = twitch.get()
    lien = f"https://www.twitch.tv/{name}"
    wn=qrcode.make(lien)
    chemin = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Image PNG", "*.png")],
            initialfile="QRCODE_twitch.png",
            title="enresgister le QR code "
        ) 
    if chemin:
           wn.save(chemin)
def redditqr(event):
    name=reddit.get()
    lien=f"https://www.reddit.com/user/{name}/"
    wn=qrcode.make(lien)
    chemin = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Image PNG", "*.png")],
            initialfile="QRCODE_reddit.png",
            title="enresgister le QR code "
        ) 
    if chemin:
           wn.save(chemin)
def pinterestqr(event):
    name=pinterest.get()
    lien=f"https://www.pinterest.com/{name}/"
    wn=qrcode.make(lien)
    chemin = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Image PNG", "*.png")],
            initialfile="QRCODE_pinterest.png",
            title="enresgister le QR code "
        ) 
    if chemin:
           wn.save(chemin)
def githubqr(event):
    name=github.get()
    lien=f"https://github.com/{name}"
    wn=qrcode.make(lien)
    chemin = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Image PNG", "*.png")],
            initialfile="QRCODE_github.png",
            title="enresgister le QR code "
        ) 
    if chemin:
           wn.save(chemin)
def linkedinqr(event):
    name=linkedin.get()
    lien=f"https://www.linkedin.com/in/{name}/"
    wn=qrcode.make(lien)
    chemin = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Image PNG", "*.png")],
            initialfile="QRCODE_linkedin.png",
            title="enresgister le QR code "
        ) 
    if chemin:
           wn.save(chemin)
def telegramqr(event):
    name=telegram.get()
    lien=f"https://t.me/{name}"
    wn=qrcode.make(lien)
    chemin = filedialog.asksaveasfilename(
             defaultextension=".png",
             filetypes=[("Image PNG", "*.png")],
             initialfile="QRCODE_telegram.png",
             title="enresgister le QR code "
         ) 
    if chemin:
            wn.save(chemin)
def whatsappqr(event):
     name=whatsapp.get()
     lien=f"https://wa.me/33{name}"
     wn=qrcode.make(lien)
     chemin = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Image PNG", "*.png")],
        initialfile="QRCODE_whatsapp.png",
        title="enresgister le QR code "
         ) 
     if chemin:
            wn.save(chemin)
def spotifyqr(event):
    name=spotify.get()
    lien=f"https://open.spotify.com/user/{name}"
    wn=qrcode.make(lien)
    chemin = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Image PNG", "*.png")],
        initialfile="QRCODE_spotify.png",
        title="enresgister le QR code "
             ) 
    if chemin:
        wn.save(chemin)
def robloxqr(event):
     name=roblox.get()
     lien=f"https://www.roblox.com/users/{name}/profile"
     wn=qrcode.make(lien)
     chemin = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Image PNG", "*.png")],
        initialfile="QRCODE_roblox.png",
        title="enresgister le QR code "
              ) 
     if chemin:
         wn.save(chemin)
def steamqr(event):
     name=steam.get()
     lien=f"https://steamcommunity.com/profiles/{name}/"
     wn=qrcode.make(lien)
     chemin = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Image PNG", "*.png")],
        initialfile="QRCODE_steam.png",
        title="enresgister le QR code "
              ) 
     if chemin:
         wn.save(chemin)
def telqr(event):
     name=tel.get()
     lien= f"tel:+33{name}"
     wn=qrcode.make(lien)
     chemin = filedialog.asksaveasfilename(
             defaultextension=".png",
             filetypes=[("Image PNG", "*.png")],
             initialfile="QRCODE_telephone.png",
             title="enresgister le QR code "
                   ) 
     if chemin:
              wn.save(chemin)
def smsqr(event):
     name=sms.get()
     mess=sms2.get()
     lien= f"SMSTO:+33{name}:{mess}"
     wn=qrcode.make(lien)
     chemin = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("Image PNG", "*.png")],
        initialfile="QRCODE_sms.png",
        title="enresgister le QR code "
                        ) 
     if chemin:
        wn.save(chemin)
def emailqr(event):
     name = email.get()
     lien = f"mailto:{name}"
     wn=qrcode.make(lien)
     chemin = filedialog.asksaveasfilename(
             defaultextension=".png",
             filetypes=[("Image PNG", "*.png")],
             initialfile="QRCODE_email.png",
             title="enresgister le QR code "
                             ) 
     if chemin:
             wn.save(chemin)
def emailsqr(event):
     name=emails.get()
     mess=emails2.get()
     lien=f"mailto:{name}?subject={mess}"
     wn=qrcode.make(lien)
     chemin = filedialog.asksaveasfilename(
             defaultextension=".png",
             filetypes=[("Image PNG", "*.png")],
             initialfile="QRCODE_emailsubject.png",
             title="enresgister le QR code "
                             ) 
     if chemin:
             wn.save(chemin)
def wpaqr(event):
     name=wpaname.get()
     mdp=wpamdp.get()
     lien=f"WIFI:T:WPA;S:{name};P:{mdp};;"
     wn=qrcode.make(lien)
     chemin = filedialog.asksaveasfilename(
             defaultextension=".png",
             filetypes=[("Image PNG", "*.png")],
             initialfile="QRCODE_wpa/wpa2.png",
             title="enresgister le QR code "
                             ) 
     if chemin:
             wn.save(chemin)
def wifiqr(event):
     name=wifiname.get()
     lien=f"WIFI:T:nopass;S:{name};;"
     wn=qrcode.make(lien)
     chemin = filedialog.asksaveasfilename(
             defaultextension=".png",
             filetypes=[("Image PNG", "*.png")],
             initialfile="QRCODE_wifi_sans_mdp.png",
             title="enresgister le QR code "
                             ) 
     if chemin:
             wn.save(chemin)
def wifimqr(event):
     name=wifimname.get()
     mdp=wifimmdp.get()
     lien=f"WIFI:T:WPA;S:{name};P:{mdp};H:true;;"
     wn=qrcode.make(lien)
     chemin = filedialog.asksaveasfilename(
             defaultextension=".png",
             filetypes=[("Image PNG", "*.png")],
             initialfile="QRCODE_wifi_masquer.png",
             title="enresgister le QR code "
                             ) 
     if chemin:
             wn.save(chemin)
tiktok.bind("<Return>", tiktokqr)
youtube.bind("<Return>", youtubeqr)
instagram.bind("<Return>", instagramqr)
snapchat.bind("<Return>", snapchatqr)
discord.bind("<Return>", discordqr)
facebook.bind("<Return>", facebookqr)
x.bind("<Return>", xqr)
twitch.bind("<Return>", twitchqr)
reddit.bind("<Return>", redditqr)
pinterest.bind("<Return>", pinterestqr)
github.bind("<Return>", githubqr)
linkedin.bind("<Return>", linkedinqr)
telegram.bind("<Return>", telegramqr)
whatsapp.bind("<Return>", whatsappqr)
spotify.bind("<Return>", spotifyqr)
roblox.bind("<Return>", robloxqr)
steam.bind("<Return>", steamqr)
tel.bind("<Return>", telqr)
sms2.bind("<Return>", smsqr)
sms.bind("<Return>", smsqr)
email.bind("<Return>", emailqr)
emails.bind("<Return>", emailsqr )
emails2.bind("<Return>", emailsqr )
wpaname.bind("<Return>", wpaqr )
wpamdp.bind("<Return>", wpaqr )
wifiname.bind("<Return>", wifiqr )
wifimname.bind("<Return>", wifimqr )
wifimmdp.bind("<Return>", wifimqr )
fenetre.mainloop()

