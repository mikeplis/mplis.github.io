---
layout: post
title: Adjusting Fantasy Scoring Using Start Percentage
---

Lately I've been looking at using start percentage data from MyFantasyLeague in my analyses and wanted to share some of my initial observations.<!--Start percentage data is interesting because it's a pretty good proxy for a player's historical weekly ranking (which can be difficult to find). It incorporates his recent production, his opponent that week, and his health. Combining this data with weekly fantasy scores yields some interesting insights. It can show how consistent a player was or wasn't and show us some situations where we as a community had a tough time figuring out a player's value. -->

Methodology
---
I retrieved weekly start percentage data using [MFL's topStarters API endpoint](http://football.myfantasyleague.com/2014/export) and my weekly fantasy data is courtesy of [ProFootballFocus](https://www.profootballfocus.com/) (subscription required for fantasy data). All points listed assume 4 points per passing TD, 6 points for all other TD's, 1 point for every 25 passing yards, and 1 point for every 10 rushing and receiving yards. Then, for each week of the season, I multiplied a player's start percentage by the points he scored that week. For example, in week 1 of last season, Aaron Rodgers was started by 88.3% of teams and he scored 10.6 points giving him an adjusted score of 9.36. Then, I summed up each player's adjusted scores for the season and took that number as a percentage of his total points scored for the season. Using Rodgers again as an example, he finished the season with 361.1 total points and 350.3 adjusted points, giving a percentage of 97.01%.<!--This final number essentially shows what percentage of a player's points actually went towards helping his fantasy owners win their weekly matchups.--> This final percentage is what I want to focus on.

Motivation
---
I'll often look back at season-end data to remind myself how a player did last season. Most of the time, the data I look at will show how many games a player played or show some kind of per game average score to put a player's stats in better context if he was injured or something. However, this kind of data doesn't answer an important question: how much did a player help his owners win their weekly matchups? The player that really got me thinking about this question was Ben Roethlisberger. Depending on your scoring system, Roethlisberger finished in the QB4-6 range last season, but many will remember that he had those two huge games in weeks 8 and 9 that buoyed his final stats.

<table class="tablesorter">
  <thead>
    <tr>
      <th>Foo</th>
      <th>Bar</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Baz</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Qux</td>
      <td>2</td>
    </tr>
  </tbody>
</table>

