import re
import urllib.request

def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def get_image(html):
    html=html.decode('utf-8')
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)

    imglist = imgre.findall(html)
    return imglist

html = get_html("https://tieba.baidu.com/p/4895690031")

print(get_image(html))
