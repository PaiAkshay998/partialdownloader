import requests
from moviepy.editor import VideoFileClip, concatenate_videoclips

url = ''
count = 1
fileformat = 'ts'
just_merge = True

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = requests.get(url)
        if len(response.content) < 200:
          return False
        file.write(response.content)
    return True

try:
  while True and (not just_merge):
    print(count)
    continue_download = download(url.format(count), "./downloaded_files/{}.{}".format(count, fileformat))
    if not continue_download:
      break
    count += 1
except Exception as e:
	print(e)

print("merging file")
files = [VideoFileClip('./downloaded_files/{}.{}'.format(i, fileformat)) for i in range(1, count)]
final_video = concatenate_videoclips(files)
final_video.write_videofile("./final_video.mp4")

