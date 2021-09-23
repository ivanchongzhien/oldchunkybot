# OldChunky Bot
OldChunky Bot is a multipurpose bot designed as a personal project for my personal server.

## Commands
* ### help
  lists available commands and information
* ### hello
  greets user with a random insult
* ### roll
  rolls a random number between 0-100
* ### inspire
  outputs a random inspirational quote
* ### pgjoke
  outputs a random programmer joke
* ### joke
  outputs a random dad joke
* ### votd
  outputs the Bible verse of the day
* ### bible
  outputs a random Bible verse
* ### poll [description]
  starts a poll in the channel with the description entered by the user
  * Only yes/no options represented by a green and red button respectively.
* ### movie
  pings all users who have subscribed to the Movie Squad role

* ### dota
  pings all user with the role indicating that they played Dota 2
  * users can respond to the invitation to play by either reacting "OK" or "No" on the bot message
* ### water
  * user requested feature to remind users currently online to drink water
* ### ping
  outputs user ping
* ### reactroles [role]
  outputs a special message which allows users to obtain the specified role by reacting to that message
  * permissions: roles higher than the bot's role(e.g. admin roles, moderator roles) cannot be assigned


### How this bot is kept running:
Since the bot is hosted on a free online service, it normally terminates after one hour of inactivity. To bypass this issue, I used Uptime Robot, another service to ping the bot server at regular intervals to prevent it from terminating.

