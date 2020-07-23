#google_images_download 라이브러리 오류 발생 시 https://blog.naver.com/mininuke7303/221955398976 사이트 참조

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"skinny man", 'limit':80,"print_urls":True, "format":"jpg"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
