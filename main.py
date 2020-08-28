import requests

currentImage = 350
baseURL = "https://vtext-cdn.vhlcentral.com/vtext_descubre2ev2/ebook/data/swf/des2e_v2/0"

while (currentImage > 0 and currentImage < 392):
    if (currentImage > 0 and currentImage < 11):
        baseURL = "https://vtext-cdn.vhlcentral.com/vtext_descubre2ev2/ebook/data/swf/des2e_v2/000"
        betterURL = (baseURL + str(currentImage) + '.swf')
        print(baseURL + str(currentImage) + ".swf")
        currentImage += 1

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
        r = requests.get(betterURL, headers=headers)
        print(r.status_code)
        print(r.headers)
        open('./images/page' + str(currentImage) + '.swf', 'wb').write(r.content)
    elif (currentImage >= 11 and currentImage < 100):
        baseURL = "https://vtext-cdn.vhlcentral.com/vtext_descubre2ev2/ebook/data/swf/des2e_v2/00"
        betterURL = (baseURL + str(currentImage) + '.swf')
        print(baseURL + str(currentImage) + ".swf")
        currentImage += 1

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
        r = requests.get(betterURL, headers=headers)
        print(r.status_code)
        print(r.headers)
        open('./images/page' + str(currentImage) + '.swf', 'wb').write(r.content)
    elif (currentImage >= 100):
        baseURL = "https://vtext-cdn.vhlcentral.com/vtext_descubre2ev2/ebook/data/swf/des2e_v2/0"
        betterURL = (baseURL + str(currentImage) + '.swf')
        print(baseURL + str(currentImage) + ".swf")
        currentImage += 1

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
        r = requests.get(betterURL, headers=headers)
        print(r.status_code)
        print(r.headers)
        open('./images/page' + str(currentImage) + '.swf', 'wb').write(r.content)

    else:
        print("Did it work?")
