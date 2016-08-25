from urllib2 import urlopen
from bs4 import BeautifulSoup
from random import randint

youtube = 'https://www.youtube.com'
url = '/watch?v=xVPvzX-AeSM'
lucky_digit = 55

out = open('test.txt', 'w')

for i in range(0, lucky_digit):
    response = urlopen(youtube + url)

    html = response.read()
    bs = BeautifulSoup(html, 'html.parser')
    tags = bs.find_all('a', attrs={'class': 'content-link'})
    t = 0

    for tag in tags:
        my_str = '[' + str(t) + ']' + tag['href'] + " - " + tag['title'].encode('ascii', 'ignore') + '\n'
        out.write(my_str)
        t += 1

    rand = randint(0, len(tags) - 1) # chose a random video ( fun results )
    # rand = 0 # for next autoplay video

    url = tags[rand]['href']    # get the value of the next link
    curr = tags[rand]['title']  # get the title of that link
    curr_url = tags[rand]['href']  # get the title of that link

    out.write('\n-------- Chosen: ' + tags[rand]['title'].encode('ascii', 'ignore') + ' [' + str(rand) + ']--------\n\n')
    # print str(i/float(lucky_digit )) + '%\n'    # percentage
    print '\r[{0}] {1}%'.format('#'*(i/10), i)


print '\n'
print(curr)
print(youtube + curr_url)

out.close()