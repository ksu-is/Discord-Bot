 Project Road Map


Sprint 1

    Initiate KSU Github account
    Link Github account to the KSU-IS organization
    Edit and update Readme file
    Conduct practice examples on existing code
    
    
    
Sprint 2 

    Start by using any web browser to navigate to Discord's Developer Portal
    Click the "Applications" tab towards the top left, then click on "New Application" towards the top right
    The user can now provide the bot's name and other general information
    Navigate to the "Bot" tab and click the "Add Bot" button, which is located next to the "Build-A-Bot" description
          Tip: Make sure "Public Bot" is disabled
    Under the "Build-A-Bot" description, click the "Copy" button under "Token"
    Start your python code with your token as the first line
    
      Example:    1    # Seth's Discord Bot from Python
                  2     
                  3     TOKEN = 'insert token here'
                  4
                  5
                  


    In the Discord Developer Portal, navigate to the "OAuth2" tab and place a check in the "bot" box under "Scopes"
    Set the desired permissions roles of the bot, preferably not the administrator role
    Now copy the URL at the top of the page and paste in a new browser in order to add the Bot to the Discord server


    Now for the Python coding,
    In the console, type the command "pip install discord" to install its essential packages
    Create a new line of code above the TOKEN and type "import discord"
    Create another new line right after and type "import random"
    
    Now create a new line of code after the TOKEN and type "client = discord.CLient()"
    On the next line, type "@client.event"
    On the next line under, type "async def on_ready():"
    For the next line, indent once then type "print('We have logged in as {0.user}'.format(client))"
    The next line should contain the following: client.run(TOKEN)
    
      Example of code so far:
                  1    # Seth's Discord Bot from Python
                  2     
                  3    import discord
                  4    import random
                  5    
                  6    TOKEN = 'insert token here'
                  7
                  8    client = discord.CLient()
                  9
                  10   @client.event
                  11   sync def on_ready():
                  12       "print('We have logged in as {0.user}'.format(client))
                  13
                  14
                  15   client.run(TOKEN)
                  
                  
     After running the code, the Discord bot should now be online! 
    
     Now to code the customized messages and functions



Sprint 3

     Regularly track progress and tasks completed
     Fix and refine and errors or problems with code
     Prepare presentation to showcase working code








               
