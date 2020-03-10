# from pywebcopy import save_webpage
# import pywebcopy
import wget

currentImage = 1
baseURL = "https://vtext-cdn.vhlcentral.com/vtext_descubre2ev1/ebook/m/img/page/landscape/0"
# print (baseURL + str(currentImage) + '.jpg')
# pywebcopy.config['bypass_robots'] = True
# pywebcopy.config['http_headers'] = {'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
``

while (currentImage > 0 and currentImage < 385):
    if (currentImage > 0 and currentImage < 100):
        baseURL = "https://vtext-cdn.vhlcentral.com/vtext_descubre2ev1/ebook/m/img/page/landscape/000"
        betterURL = (baseURL + str(currentImage) + '.jpg')
        print (baseURL + str(currentImage) + ".jpg")
        currentImage += 1

        wget.download(betterURL)
#         save_webpage(
#         url=betterURL,
#         project_folder='/workspace/DownloadBook/images',
#         )

    else:
        print("Did it work?")

# #req = Request('http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1', headers={'User-Agent': 'Mozilla/5.0'})


