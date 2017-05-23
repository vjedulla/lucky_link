from urllib2 import urlopen
from bs4 import BeautifulSoup
from random import randint

youtube = 'https://www.youtube.com'
url = '/watch?v=YfFhxA2JFOA'
lucky_digit = 2
randomOrFirst = True

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

    if randomOrFirst:
        rand = randint(0, len(tags) - 1) # chose a random video ( fun results )
    else:
        rand = 0 # for next autoplay video

    url = tags[rand]['href']    # get the value of the next link
    curr = tags[rand]['title']  # get the title of that link
    curr_url = tags[rand]['href']  # get the title of that link

    out.write('\n-------- Chosen: ' + tags[rand]['title'].encode('ascii', 'ignore') + ' [' + str(rand) + ']--------\n\n')

    print '\r[{0}] {1:.0f}%'.format('#'*(i/10), (((i + 1)**1.0)/lucky_digit) * 100)


print '\n'
print(curr)
print(youtube + curr_url)

out.close()
