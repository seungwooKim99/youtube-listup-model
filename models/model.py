import numpy as np
import pandas as pd
import requests
import json
import datetime
import html

class getExcel():
  def __init__(self, channelId):
    self.channelId = channelId
    
  def get_excel(self):
    channelId = ''
    channelId = self.channelId
    
    with open('database.json') as json_file:
      dbJson = json.load(json_file)
    apiUrl = 'https://www.googleapis.com/youtube/v3/search?&part=snippet&maxResults=50&order=date'
    key = dbJson['apiKey']
    nextPageToken = ''

    titleArr = []
    publishedAtArr = []
    descriptionArr = []
    fullVideoUrlArr = []
    videoIds = []
    fullVideoUrl = 'https://www.youtube.com/watch?v='
    channelTitle = 'temp'

    while True:
        totalVideoRes = requests.get(apiUrl+'&channelId='+channelId+'&key='+key+'&pageToken='+nextPageToken)
        
        # 잘못된 api 호출로 response가 비어있나?
        if 'error' in totalVideoRes.json():
            return 'null'
            break
            
        # 요 아래로 리스트업 작업
        for data in totalVideoRes.json()['items']:
            if data['id']['kind'] == 'youtube#video':
                channelTitle = data['snippet']['channelTitle']
                titleArr.append(data['snippet']['title'])
                descriptionArr.append(data['snippet']['description'])
                videoUrl = data['id']['videoId']
                videoIds.append(videoUrl)
                fullVideoUrlArr.append(fullVideoUrl+videoUrl)

                publishedAtStr = data['snippet']['publishedAt']
                temp = publishedAtStr[:-1]
                tempDate = datetime.datetime.fromisoformat(temp)
                tempIsoDate = tempDate.timestamp() + 32400 # 한국 시간대 +09:00
                publishedAtArr.append(datetime.datetime.fromtimestamp(tempIsoDate).strftime('%Y-%m-%d'))
        # 더이상 조회할 영상이 없으면 Break
        if 'nextPageToken' not in totalVideoRes.json():
            break
        nextPageToken = totalVideoRes.json()['nextPageToken']
        
    result_pd = pd.DataFrame()
    result_pd['제목'] = titleArr
    result_pd['업로드날짜'] = publishedAtArr
    result_pd['설명'] = descriptionArr
    result_pd['링크'] = fullVideoUrlArr
    result_pd['videoId'] = videoIds

    result_pd.loc[:, '제목'] = result_pd.loc[:, '제목'].apply(lambda x: html.unescape(x))
    result_pd.loc[:, '설명'] = result_pd.loc[:, '설명'].apply(lambda x: html.unescape(x))

    result_pd.to_excel('data/'+channelTitle+'_listup.xlsx', sheet_name=channelTitle, encoding='utf-8-sig')
    print('result created!')
    return 'data/'+str(channelTitle)+'_listup.xlsx'
