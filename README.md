# ๐บ Youtube Listup Model
์ ํ๋ธ ์ฑ๋ ID๋ฅผ ์๋ ฅํ๋ฉด, ํด๋น ์ฑ๋์ ์๋ก๋ ๋ ๋์์์ ์ ๋ณด๋ฅผ
์์ ํ์ผ๋ก ๋ฆฌ์คํธ์ ํด์ฃผ๋ ์๋น์ค ์๋๋ค.

์์์ ์ ๋ชฉ, ์๋ก๋ ๋ ์ง, ์ค๋ช, ๋งํฌ, videoId๋ฅผ ์ ๊ณตํด ์ค๋๋ค.

# ๐ป Deployed Service
pythonanywhere์ ํตํด ํด๋ผ์ฐ๋ ์์ ๋ฐฐํฌ๋ฅผ ํ์ต๋๋ค.

[์ ํ๋ธ ๋ฆฌ์คํธ์ ๋ชจ๋ธ ๋งํฌ](http://sonic886.pythonanywhere.com/)

## ๐ง Tech Stack

* Python
    * Pandas์ ๊ฐ์ ๋ฐ์ดํฐ ๋ถ์ ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ์ด์ฉํด Listup ํ ์์๋ก ์ ์ฅ
* Flask
    * Backend API & Frontend ํ๋์ ์๋ฒ๋ก ๊ตฌ๋
* Youtube API v3
    * channelId๋ฅผ ํ๋ผ๋ฏธํฐ๋ก ๋ฐ๋ ์ ํ๋ธ API๋ฅผ ํตํด ํด๋น ์ฑ๋์ ๋ํ ์ ๋ณด๋ฅผ Json ํํ๋ก ์๋ต๋ฐ์
