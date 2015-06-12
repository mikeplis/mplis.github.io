from bs4 import BeautifulSoup
import urllib2
import webbrowser
import time
import sys

def find_chandler(start = 2549377):
  base_url = 'http://fantasyfootballcalculator.com/draft/{}'
  finish = 2668309
  t0 = time.time()

  for league_id in xrange(start, finish):
    try:
      url = base_url.format(league_id)
      resp = urllib2.urlopen(url, timeout=1)
      if resp.getcode() != 200:
        break
      soup = BeautifulSoup(resp.read())
      picks = soup.find_all('td')
      if len(picks) > 0:
        first_pick = picks[1].text.strip().split('\n')
        if first_pick[0] == 'Chandler':
          print 'Found him!'
          print url
          return url
      avg_t_per_league = (time.time() - t0) / (league_id - start)
      leagues_remaining = (finish - league_id)
      minutes_remaining = (avg_t_per_league * leagues_remaining) / 60
      print 'league id: {} | average time per league: {} | leagues remaining: {} | estimated minutes remaining: {}'.format(league_id, avg_t_per_league, leagues_remaining, minutes_remaining)
    except (KeyboardInterrupt, SystemExit):
      raise
    except:
      print url
  return None

if __name__ == '__main__':

  if len(sys.argv) > 1:
    draft = find_chandler(int(sys.argv[1]))
  else:
    draft = find_chandler()

  if draft is not None:
    webbrowser.open(draft)
  else:
    print "Couldn't find Chandler"