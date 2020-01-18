# coding: utf-8
# 2019/12/9 @ tongshiwei

# header
# 出现反爬虫，first step 加 header

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
raw_cookie = "BAIDUID=B0D2F60A4A0B828FB4F332AC0C7BE9CB:FG=1; pgv_pvi=3205965824; pgv_si=s6243888128; BIDUPSID=B0D2F60A4A0B828FB4F332AC0C7BE9CB; PSTM=1493694994; BDRCVFR[eZLhj6h0pMs]=mbxnW11j9Dfmh7GuZR8mvqV; BD_HOME=0; BD_UPN=123253; BD_CK_SAM=1; PSINO=2; BDSVRTM=113; H_PS_PSSID=1439_21124_17001; BD_LAST_QID=13945703765811159509"

cookies = {}
for line in raw_cookie.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

headers = {
    'User-Agent': user_agent,
}
