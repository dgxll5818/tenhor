import requests
import time
from xml.etree import ElementTree

# 这里修改为你网站的 sitemap 地址
SITEMAP_URL = ""

def get_urls():
print(f"正在读取 Sitemap: {SITEMAP_URL}")
try:
r = requests.get(SITEMAP_URL, timeout=20)
root = ElementTree.fromstring(r.content)
# 提取所有 <loc> 标签中的 URL
urls = [loc.text for loc in root.findall(".//{[可疑链接已删除]}loc")]
return urls
except Exception as e:
print(f"获取失败: {e}")
return []

def start():
urls = get_urls()
print(f"找到 {len(urls)} 个页面，开始模拟访问...")
for url in urls:
try:
# 模拟浏览器头部，避免被 WAF 拦截
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Cache-Warmer/1.0'}
res = requests.get(url, headers=headers, timeout=10)
print(f"已请求: {url} | 状态码: {res.status_code}")
time.sleep(0.2) # 稍微停顿，保护服务器
except:
print(f"请求失败: {url}")

if name == "main":
start()
