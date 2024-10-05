from googleapiclient.discovery import build
import isodate
import time
import pandas as pd
from utils.constants_v2 import  SECRET, POST_FIELDS,OUTPUT_PATH

def lets_connect(SECRET):
    youtube = build('youtube', 'v3', developerKey=SECRET)

    return youtube

def channel_extract(connection, channel):

    try:
        request  = connection.search().list(
            part='snippet',
            q= channel,
            type= 'channel'
        )
        response = request.execute()
        # for item in response['items']:
        #     print(item)
        #     break
        #print(response['items'][0]['id']['channelId'])
        channel_id = response['items'][0]['id']['channelId']

        return channel_id
    except Exception as e:
        print(e)

def stats_extract(connection, channels):
    #views_stats=[]
    try:
        request = connection.channels().list(
            part = 'statistics',
            id = channels
        )

        response = request.execute()
        
        views_stats = {key:response['items'][0]['statistics'][key] for key in response['items'][0]['statistics'].keys() if key in POST_FIELDS}
       
        return views_stats
       
    except Exception as e:
        print(e)
        
def top_videos_extraction(connection, channels):
    try:

        ##### fetching play list id ############
        request = connection.channels().list(
            part = 'contentDetails',
            id = channels
        )

        response = request.execute()

        playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        print(f'playlist id is{playlist_id}')

        ##### fetching video ids ##########

        videoids = []
        next_page_token = None
        i = 0
        while True:
            playlist_videos  = connection.playlistItems().list(
                part = 'snippet',
                playlistId = playlist_id,
                maxResults=50,
                pageToken= next_page_token
            )

            playlist_videos_= playlist_videos.execute()

            #print(playlist_videos_['items'])

            videoids_ = [item['snippet']['resourceId']['videoId'] for item in playlist_videos_['items']]
            videoids.extend(videoids_)
            next_page_token = playlist_videos_.get('nextPageToken')
            print(f'The token is {next_page_token} and the number is {i}')
            
            # i+=1
            #print(videoids)
            if i == 15:
                break
            i +=1
            # if not next_page_token:
            #     break

        ###### fetching video statistics #############

        video_statistics_ = []
        print(len(videoids))

        for id in videoids:

            video_stats = connection.videos().list(
                part = 'statistics,snippet,contentDetails',
                id = id
            )

            response = video_stats.execute()

            #print(response['items'][0]['snippet']['title'])
            #print(response['items'][0]['statistics']['viewCount'])
            if isodate.parse_duration(response['items'][0]['contentDetails']['duration']).total_seconds() > 60:
                stats = {
                    'title':response['items'][0]['snippet']['title'],
                    'viewcount':response['items'][0]['statistics']['viewCount'],
                    'likecount':response['items'][0]['statistics']['likeCount'],
                    'dislikecount':response['items'][0]['statistics']['favoriteCount'],
                    'commentcount':response['items'][0]['statistics']['commentCount']
                }
                video_statistics_.append(stats)
                # print(video_statistics_)
            else:
                #print('hello')
                pass
            #print(response)
            #time.sleep(3)
            

        # video_statistics_ = sorted(video_statistics_, key=lambda x:int(x['viewcount']),reverse=True)  
        print(video_statistics_)  
        return video_statistics_
        


    except Exception as e:
        print(e)


def load_into_csv(args, OUTPUT_PATH):
    views_stats, top_videos_stats = args
    print(views_stats)
    views_stats_df = pd.DataFrame(views_stats, index=[0])
    top_videos_stats_df = pd.DataFrame(top_videos_stats)

    path = OUTPUT_PATH
    views_stats_df.to_csv(f'{OUTPUT_PATH}/view_stats.csv', index = False)
    top_videos_stats_df.to_csv(f'{OUTPUT_PATH}/top_videos_stats.csv', index = False)
    
    return path


