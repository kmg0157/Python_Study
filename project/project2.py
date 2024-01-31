import socket
import requests
import re

# 내부 IP 확인
in_addr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
in_addr.connect(("8.8.8.8", 80))
internal_ip = in_addr.getsockname()[0]
in_addr.close()
print("내부 IP:", internal_ip)

# 외부 IP 확인
try:
    req = requests.get("https://ipinfo.io/ip")
    external_ip = req.text.strip()
    print("외부 IP:", external_ip)
except Exception as e:
    print("외부 IP를 가져오는 중 오류 발생:", e)
