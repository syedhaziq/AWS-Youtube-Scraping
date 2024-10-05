from googleapiclient.discovery import build
from utils.constants_v2 import  SECRET,OUTPUT_PATH
from etls.youtube_etl import lets_connect, channel_extract,stats_extract,top_videos_extraction,load_into_csv



# youtube = build('youtube', 'v3', developerKey=SECRET)
# #api = tweepy.API(auth)

# try:
#     request  = youtube.search().list(
#         part='snippet',
#         q= 'techTFQ',
#         type= 'channel'
#     )
#     response = request.execute()
#     # for item in response['items']:
#     #     print(item)
#     #     break
#     print(response['items'][0]['id']['channelId'])
# except Exception as e:
#     print(e)

def youtube_extration():

    connection = lets_connect(SECRET)
    channels = channel_extract(connection, 'MrBeast')
    views_stats = stats_extract(connection,channels)
    top_videos = top_videos_extraction(connection, channels)

    ### loading into csv ###
    # path = load_into_csv([views_stats,top_videos], OUTPUT_PATH)

    return top_videos


a = youtube_extration()
print(a)
# print(b)
    