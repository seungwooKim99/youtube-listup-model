# 📺 Youtube Listup Model
유튜브 채널 ID를 입력하면, 해당 채널에 업로드 된 동영상의 정보를
엑셀 파일로 리스트업 해주는 서비스 입니다.

영상의 제목, 업로드 날짜, 설명, 링크, videoId를 제공해 줍니다.

# 💻 Deployed Service
pythonanywhere을 통해 클라우드 상에 배포를 했습니다.

[유튜브 리스트업 모델 링크](http://sonic886.pythonanywhere.com/)

## 🔧 Tech Stack

* Python
    * Pandas와 같은 데이터 분석 라이브러리를 이용해 Listup 후 엑셀로 저장
* Flask
    * Backend API & Frontend 하나의 서버로 구동
* Youtube API v3
    * channelId를 파라미터로 받는 유튜브 API를 통해 해당 채널에 대한 정보를 Json 형태로 응답받음
