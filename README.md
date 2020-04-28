# Asi4nBot
Personal general use discord bot

Current features:
- Random meme message commands
- Command to move all members to a channel (/movehere)
- Search wolframalpha (/wolfram)
- Display when users delete their own message
- Counting how many times a string has been sent in messages by any person in the guild
- Election organization

Planned features:
???

## Current list of user commands
Command prefex = '/'

### Message commands
- clear {num}: clears the last num messages (including the one used to invoke the command)
- dinner: @'s the 'dinner squad' role (specific to my personal server)
- echo {message}: echos message
- jason {num}: random quotes from Jason Kwan
- nuke: nukes the server
- tsar_bomba: was the BIGGEST bomb ever created
- source: gives a link to this repository
  
### Moderator commands
- movehere - moves all users in voice to the channel of the person who called it
  
### Math commands
- wolfram {message} - searches the wolframalpha database (aliases: 'wr', 'query', 'q')

### Counter commands
- forbid {word}: adds word to the txt file of words to count
- unforbid {word}: removes word from the txt file of words to count
- check {@member}: shows the number of forbidden words they have sent
