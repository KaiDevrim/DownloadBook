import requests

currentImage = 1
baseURL = "https://vtext-cdn.vhlcentral.com/vtext_descubre2ev1/ebook/m/img/page/landscape/0"

while (currentImage > 0 and currentImage < 385):
    if (currentImage > 0 and currentImage < 11):
        baseURL = "https://vtext-cdn.vhlcentral.com/vtext_descubre2ev1/ebook/m/img/page/landscape/000"
        betterURL = (baseURL + str(currentImage) + '.jpg')
        print (baseURL + str(currentImage) + ".jpg")
        currentImage += 1
        
        
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
        r = requests.get(betterURL, headers=headers)
        print(r.status_code)
        print(r.headers)
        open('./images/page' + str(currentImage) + '.jpg', 'wb').write(r.content)
    elif (currentImage >= 11 and currentImage < 100):
        baseURL = "https://vtext-cdn.vhlcentral.com/vtext_descubre2ev1/ebook/m/img/page/landscape/00"
        betterURL = (baseURL + str(currentImage) + '.jpg')
        print (baseURL + str(currentImage) + ".jpg")
        currentImage += 1
        
        
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
        r = requests.get(betterURL, headers=headers)
        print(r.status_code)
        print(r.headers)
        open('./images/page' + str(currentImage) + '.jpg', 'wb').write(r.content)
    elif (currentImage >= 100):
        baseURL = "https://vtext-cdn.vhlcentral.com/vtext_descubre2ev1/ebook/m/img/page/landscape/0"
        betterURL = (baseURL + str(currentImage) + '.jpg')
        print (baseURL + str(currentImage) + ".jpg")
        currentImage += 1
        
        
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
        r = requests.get(betterURL, headers=headers)
        print(r.status_code)
        print(r.headers)
        open('./images/page' + str(currentImage) + '.jpg', 'wb').write(r.content)

    else:
        print("Did it work?")
