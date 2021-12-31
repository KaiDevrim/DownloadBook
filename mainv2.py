import subprocess

# https://vtext-cdn.vhlcentral.com/vtext_descubre2ev3/ebook/m/img/page/landscape/0001.jpg
# https://vtext-cdn.vhlcentral.com/vtext_descubre2ev2/ebook/m/img/page/landscape/0001.jpg
# Final Page = 469


url = ''
current_page = 1
final = 469
while current_page <= final:
    current_page += 1
    if current_page < 10 and current_page > 0:
        url = 'https://vtext-cdn.vhlcentral.com/vtext_descubre2ev3/ebook/m/img/page/landscape/{}.jpg'.format('000'+str(current_page))
        subprocess.call(['wget', url])
    elif current_page < 100 and current_page >= 10:
        url = 'https://vtext-cdn.vhlcentral.com/vtext_descubre2ev3/ebook/m/img/page/landscape/{}.jpg'.format('00'+str(current_page))
        subprocess.call(['wget', url])
    elif current_page <= 469 and current_page >= 100:
        url = 'https://vtext-cdn.vhlcentral.com/vtext_descubre2ev3/ebook/m/img/page/landscape/{}.jpg'.format('0'+str(current_page))
        subprocess.call(['wget', url])