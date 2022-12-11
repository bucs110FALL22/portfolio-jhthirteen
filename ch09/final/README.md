# CS110 Final Exam

## SHORT DESCRIPTION *(1 or 2 sentences describing your program)*
Automates buying tickets to NBA games based on any player you are interested in watching. Provides their season averages and upcoming games, then generates a seatgeek link allowing you to purchase tickets. Run by /portfolio-jhthirteen-1/ch09/final python3 main.py

## KNOWN BUGS AND INCOMPLETE PARTS *(list any known bugs or non-working parts)*
For some players (I can't seem to figure out why this only effects some, I"m assuming it has to do with some aspect of the player stats API updating process), the statistics are slightly off, but not by much

## REFERENCES *(any resources you use outside of class materials)*
For accessing dictionary values in a list (way the json data was returned): https://pythonexamples.org/python-list-of-dictionaries/
For working with the datetime library and getting time periods two weeks in advance: https://bobbyhadz.com/blog/python-add-weeks-to-date
Seatgeek API Documentation: https://platform.seatgeek.com/#events
Balldontlie API Documentation: https://www.balldontlie.io/#attributes
Replacing spaces with dashes for url purposes: https://stackoverflow.com/questions/5861361/replace-spaces-with-dash-and-remove-prefix-from-string

## MISCELLANEOUS COMMENTS *(anything else you would like the grader to know)*
This works with any active NBA player as long as they are rostered, if a name is spelled wrong or they are not a player, the script will prompt you to re-enter. Used seatgeek API which required registration for an access key and balldontlie which required no registration.
Added is a sample output of what the script produces: https://replit.com/@JackHunter9/portfolio-jhthirteen-1#ch09/final/SampleOutput.png