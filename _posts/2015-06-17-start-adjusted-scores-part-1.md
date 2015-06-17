---
layout: post
title: Adjusting Fantasy Scoring Using Start Percentage - Quarterbacks
---

Lately I've been looking at start percentage data from MyFantasyLeague as part my analyses. I've found that combining it with a player's weekly scores can help answer an important question: how much did a player help his owners win their weekly matchups? Players can be inconsistent, mixing huge games with mediocre or even terrible games, making it very difficult to know when to start or sit him. Those big weeks can skew his stats, meaning that end-of-season rankings won't tell the whole story.

## Methodology

I retrieved weekly start percentage data using [MFL's API](http://football.myfantasyleague.com/2014/export) and my weekly fantasy data is courtesy of [ProFootballFocus](https://www.profootballfocus.com/) (subscription required for fantasy data). All points listed assume 4 points per passing TD, 6 points for all other TD's, 1 point for every 25 passing yards, and 1 point for every 10 rushing and receiving yards.

For each week of the season, I multiplied a player's start percentage by the points he scored. For example, in week 1, Aaron Rodgers was started by 88.3% of teams and he scored 10.6 points giving him an adjusted score of 9.36. 

Then, I summed up each player's adjusted scores for the season and took that number as a percentage of his total points scored. Using Rodgers again as an example, he finished the season with 361.1 total points and 350.3 adjusted points, giving a percentage of 97.01%. This number essentially shows what percentage of a player's points actually went towards helping his owners win.

To make it easier for me to talk about this data, I've named this percentage Mike's Awesome Percentage (or MAWP for short). Yes, I'm actually calling it that. I spent way longer than I care to admit trying to come up with some cool name for this number, and I kept writing "Mike's Awesome Percentage" as a placeholder because I'm a programmer and [therefore terrible at naming things](https://twitter.com/codinghorror/status/506010907021828096). I couldn't come up with anything good, and [as an Archer fan I chuckle every time I see MAWP](https://www.youtube.com/watch?v=Tekhh7Iy-sM), so I'm just going to go with it.

I haven't done any in-depth work with MAWP, so I have no idea if it has any predictive value, but I do think it has a lot of exploratory value. It emphasizes players that might require a closer look. Below is some data on most of the 2014 QB's along with their MAWP values (the raw data can be found [here](https://raw.githubusercontent.com/mplis/mplis.github.io/master/_data/start_qb.csv)). I've also included my thoughts on a couple of players whose MAWP values helped shape my opinion of them going into this season.

{% include sortedTable.html data=site.data.start_qb table_id="qb" initial_sort=3 %}

### Nick Foles
Foles is a player that jumps out at me when looking at this data. His PPG wasn't very good, but his MAWP is higher than I would have thought. So I decided to take a closer look at his numbers from last season.

First, his PPG is skewed by his week 9 score of 8.1. He was injured early in the 2nd quarter, so he was actually on his way to a solid game. If you throw out that week, Foles' PPG would be 18.2, which would bump him up to 14th. 

Looking at the games he played in full, there's only one truly bad game: week 4 at San Francisco. I'm not one to throw away an outlier just because it's an outlier; a bad game is still a bad game. However, I think Foles' MAWP reflects the confidence his owners had in him. He was playing pretty well before that game and continued to play well after that game, averaging just over 20 points outside of week 4, which translate to low-QB1 numbers.

I know the Rams offense is a bit different from the Eagles offense, but Foles is currently coming off the board as the QB23 on FantasyFootballCalculator which seems too low to me. The Rams have a decent group of WR's that have arguably been held back by their QB's and offensive coordinator the past couple of seasons. They also bolstered their offensive line and running game in the draft, so I think Foles could be a good value in 2015.

### Ben Roethlisberger

Big Ben's 2014 season was actually what compelled me to begin looking at start percentage data. Roethlisberger finished as the QB6  last season (even higher in leagues that award 6 points per passing TD) so someone just looking at his final stats could easily think that his current price of QB7 makes him a good value. However, he had two huge games in weeks 8 and 9 that buoyed his numbers. Some argued that owning a guy that can have huge weeks is very valuable, but my hypothesis was that a lot of owners didn't even start Roethlisberger those weeks.

Roethlisberger had a [preseason ADP](http://fantasyfootballcalculator.com/adp.php?format=standard&year=2014&teams=12&view=graph&pos=qb) of QB17 in 2014, so it's not surprising that his start percentage was only around 33% in week 1. His usage fluctuated between 20% and 55% for the next few weeks, with the high values likely being due to great matchups (e.g. Tampa Bay the week after they got torched by the Falcons on TNF), falling back down to the low 30's in advance of his week 8 blowup. That's right folks, only one-third of owners benefited from one of the highest single-game scores of the 2014 season. Not only was Roethlisberger's start percentage so low when he had his biggest game, it only jumped up to 65% the following week (just the 13th highest usage rate that week) when he had his 2nd biggest game. His usage predictably skyrocketed the following week, but he was only a fringe QB1 at best the rest of the season.

There are certainly reasons to like Big Ben this season. Getting to play with studs Antonio Brown and Le'Veon Bell, along with the anticipated development of Martavis Bryant, bode well for his 2015 outlook. However, those players were all there last season and Roethlisberger still only managed pedestrian numbers outside of weeks 8 and 9. His high 2014 stats but low MAWP suggest a lot of his owners saw him put up tons of points on their benches. I think I'm going to be avoiding Roethlisberger at his current price. 


### Conclusion

MAWP is great at flagging players that may require a closer look, whose end-of-season stats maybe tell a misleading story. In future posts, I'll take a look at the other skill positions and see if there are any insights to be gained. Also, I believe I've only started to scratch the surface of what start percentage data can be used for and I have some ideas for how to take this analysis even further.