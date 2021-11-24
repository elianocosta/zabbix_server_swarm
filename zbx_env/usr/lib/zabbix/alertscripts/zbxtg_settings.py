# -*- coding: utf-8 -*-

tg_key = "525572107:AAGqaLJiB0YM2NldSTY2W9dqSvsKNBs1lfE"  # telegram bot api key

zbx_tg_prefix = "zbxtg"  # variable for separating text from script info
zbx_tg_tmp_dir = "/var/tmp/" + zbx_tg_prefix  # directory for saving caches, uids, cookies, etc.
zbx_tg_signature = False

zbx_tg_update_messages = True
zbx_tg_matches = {
    "problem": "PROBLEM: ",
    "ok": "OK: "
}

zbx_server = "http://monitoramento.seduc.ce.gov.br"  # zabbix server full url
zbx_api_user = "Admin"
zbx_api_pass = "4pI@p1"
zbx_api_verify = True  # True - do not ignore self signed certificates, False - ignore

zbx_basic_auth = False
zbx_basic_auth_user = "zabbix"
zbx_basic_auth_pass = "zabbix"

proxy_to_zbx = None
proxy_to_tg = None

# proxy_to_zbx = "http://proxy.local:3128"
# proxy_to_tg = "https://proxy.local:3128"

# proxy_to_tg = "socks5://user1:password2@hostname:port" # socks5 with username and password
# proxy_to_tg = "socks5://hostname:port" # socks5 without username and password

google_maps_api_key = None  # get your key, see https://developers.google.com/maps/documentation/geocoding/intro

zbx_tg_daemon_enabled = True
#zbx_tg_daemon_wl_ids = [6931850, ]
zbx_tg_daemon_wl_u = ["Eliano_u2", ]
zbx_tg_daemon_enabled_users = ["Eliano_u2", ]
zbx_tg_daemon_enabled_ids = [149130114, ]

zbx_db_host = "172.31.4.204"
zbx_db_database = "zabbix_prod"
zbx_db_user = "zabbix"
zbx_db_password = "uEI7$E9yfYrH"


emoji_map = {
    "OK": "✅",
    "PROBLEM": "❗",
    "info": "ℹ️",
    "WARNING": "⚠️",
    "DISASTER": "❌",
    "bomb": "💣",
    "fire": "🔥",
    "hankey": "💩",
}
