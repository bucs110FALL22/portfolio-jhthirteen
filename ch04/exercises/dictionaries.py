my_article = "When Jim Boeheim gets hungry after home games, he picks up the phone and calls his favorite restaurant, Saint Urban, which always agrees to stay open late until he arrives. If the Syracuse Orange are on a hot streak, Boeheim will delay his arrival, to enjoy the festive moment and mingle with fans who still treat the veteran coach with five Final Four appearances and 10 Big East titles like he's a king in this city of approximately 142,000 people. But last season, there were a number of more subdued and stoic late nights, as the program wrestled through the first losing record of Boeheim's 46-year tenure. If they win, it's a great dinner, Adam Weitsman, Boeheim's best friend and a program booster who oftens tags along, said. If it's a loss, it's the worst dinner ever because we just sit there, quiet. He doesn't say a thing, you know? While the rumblings of the 77-year-old Syracuse men's basketball coach's retirement have lingered for years, they have never seemed stronger than now, as the 2022-23 season -- the 20th anniversary of Boeheim's 2003 national championship run with Carmelo Anthony & Co. -- approaches. However, the more pressing question for a program that has been led by the Hall of Fame coach since 1976 is this: How will Syracuse move forward in a new chapter for men's college basketball without Boeheim?"

sub = {
  "Jim": "Old man",
  "dinner":"post-loss meal",
  "championship":"cinderella win",
  "coach":"general",
  "city":"cuse",
  "Orange":"Otto",
  "Saint Urban":"McDonalds",
  "hot":"cold",
  "mingle":"do yoga",
  "king":"queen"
}

for k in sub: #k variable for key 
  my_article = my_article.replace(k, sub[k]) #replace goes through entire string looking for each key variable on its iteration 
print(my_article)