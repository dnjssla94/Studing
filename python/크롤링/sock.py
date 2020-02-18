import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

google_ip = socket.gethostbyname("google.com")
sock.connect((google_ip, 80))

sock.send("GET / HTTP/1.1\n".encode())
sock.send("\n".encode())

buffer = sock.recv(4096)
buffer = buffer.decode().replace("\r\n","\n")
sock.close()

print(buffer)

#\r\n: 캐지리리턴. c 스타일에선 이렇게 해야 엔터가 완성됨 파이썬은 \n만.

'''
HTTP/1.1 200 OK
Date: Tue, 24 Dec 2019 01:40:36 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2019-12-24-01; expires=Thu, 23-Jan-2020 01:40:36 GMT; path=/; domain=.google.com
Set-Cookie: NID=194=b633uB-JosEY7I7tOW20fmiqijLS5lWCdsI3-aBBcPFf6oKsFIxGs9woaWPeVPm7PX9jtVzw2IPnXNiJVN8b4F1QsD6IPTU8FlfukcYNBRU_Bh8VWqDMbyJFtxsE9nCJlDFjt8Kq41tvpf0T_TAcnyyyKbTjKVI86VIMTqaY7Xw; expires=Wed, 24-Jun-2020 01:40:36 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

62a2
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/logos/doodles/2019/happy-holidays-2019-day-2-6753651837108239-law.gif" itemprop="image"><meta content="&#53356;&#47532;&#49828;&#47560;&#49828; &#51060;&#48652;" property="twitter:title"><meta content="&#53356;&#47532;&#49828;&#47560;&#49828; &#51060;&#48652;! #GoogleDoodle" property="twitter:description"><meta content="&#53356;&#47532;&#49828;&#47560;&#49828; &#51060;&#48652;! #GoogleDoodle" property="og:description"><meta content="summary_large_image" property="twitter:card"><meta content="@GoogleDoodles" property="twitter:site"><meta content="https://www.google.com/logos/doodles/2019/happy-holidays-2019-day-2-6753651837108239-2xa.gif" property="twitter:image"><meta content="https://www.google.com/logos/doodles/2019/happy-holidays-2019-day-2-6753651837108239-2xa.gif" property="og:image"><meta content="1000" property="og:image:width"><meta content="360" property="og:image:height"><meta content="https://www.google.com/logos/doodles/2019/happy-holidays-2019-day-2-6753651837108239-2xa.gif" property="og:url"><meta content="video.other" property="og:type"><title>Google</title><script nonce="FTMvC8yyYOD/hLJYCFBhBg==">(function(){window.google={kEI:'lGwBXp2kFYrYhwOl_IOwBg',kEXPI:'0,18168,1335578,5663,731,223,4726,378,207,467,2487,250,10,713,338,175,364,1119,35,3,278,4,60,315,426,209,10,400,292,1128776,143,1197771,378,38,329080,1294,12383,4855,32692,15247,867,28684,369,3314,5505,8384,1699,3159,1362,4323,4968,3021,4746,2902,216,6196,1719,1496,312,1976,2044,8909,1901,3396,2054,920,873,1217,1710,1,1264,2736,3694,11306,2883,21,318,235,3912,1,368,2778,520,399,992,1285,8,2796,967,612,14,1279,2212,202,39,289,149,1103,840,520,315,1156,48,157,663,3438,260,52,1137,2,2063,606,789,1050,184,595,1702,1947,244,503,429,44,999,3,101,327,1284,16,84,417,2426,1639,607,474,1339,683,65,1039,3092,135,773,1548,524,7,728,592,1574,1169,710,1314,19,182,91,1254,6513,2244,588,257,215,367,359,681,1043,2458,1226,755,707,842,2723,370,1274,108,591,385,270,26,1001,653,40,441,809,99,2,318,115,538,685,139,116,118,694,1,465,366,128,1746,525,356,1158,9,933,78,458,1977,27,4,3,7,46,361,63,162,206,2,659,129,1670,65,1,109,13,2,14,145,138,329,113,373,959,492,5,26,230,781,189,6,15,169,29,77,569,258,8,61,388,514,160,25,112,648,22,54,7,20,307,151,1026,157,5859137,1873,1342,1802679,4194851,2801171,549,333,444,1,2,80,1,900,896,1,8,1,2,2551,1,748,141,59,736,563,1,4265,1,1,1,1,137,1,782,3,5,12,77,8,1,14,5,2,3,3,1,3,5,3,3,3,3,3,1,3,3,3,3,25,11,1,1,3,1,2,4,3,3,1,1,1,7,8,2,6,28,2,2,2,2,3,1,7,6,2,25,23,2,2,23964457',authuser:0,kscs:'c9c918f0_lGwBXp2kFYrYhwOl_IOwBg',kGL:'KR',kBL:'v77x'};google.sn='webhp';google.kHL='ko';google.jsfs='Ffpdje';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return b};google.https=function(){return"https:"==window.location.protocol};google.ml=function(){return null};google.time=function(){return(new Date).getTime()};google.log=function(a,b,e,c,g){if(a=google.logUrl(a,b,e,c,g)){b=new Image;var d=google.lc,f=google.li;d[f]=b;b.onerror=b.onload=b.onabort
'''