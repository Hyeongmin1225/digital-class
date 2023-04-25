
#문자열로 주어진 URL 주소 정보로 부터 도메인 이름을 반환

from urllib.parse import urlparse

url = input("Enter a URL: ")

parsed_url = urlparse(url)
domain = parsed_url.netloc

print("Domain name:", domain)