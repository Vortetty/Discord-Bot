import discord, socket, subprocess, urllib

client = discord.Client()
status = False
server_running = False
wifi_ip = None

# this will let me know when the bot is started and message my server 
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    client.get_channel(682039274429874205).send("Bot Started Up") # change the number in the get_chanel() to the id of the chanel you are testing on

# this will wait for a message to be put in the discord server.
@client.event
async def on_message(message):
    # make sure not to respond to the messages sent by the bot
    if message.author == client.user:
        return
    # make sure the message is a command
    if message.content.startswith('!') or message.content.startswith('-') or message.content.startswith('$') or message.content.startswith('^') or message.content.startswith(':') or message.content.startswith('*'):
        s = message.content # make it easy to refer to
        if server_running == False:
            print(s) # prints the command that was run into the console, disabled this if a mindustry server is running
            
        # this command will print the ip of the server to the chat, currently prints the local ip on linux, fixed in newer version     
        if s[1:] == "ip" or s == "ip":
            await message.channel.send('Checking...')
            try:
                host_name = socket.gethostname()
                host_ip = socket.gethostbyname(host_name)
                await message.channel.send("Hostname :  " + host_name)
                await message.channel.send("IP : " + host_ip)
            except:
                await message.channel.send("Unable to get Hostname and IP")
        
        # stops program
        if s[1:] == "stop" or s == "stop":
            exit()
            exit()
            exit()
            
        # starts a server and disables command printing
        if s[1:] == "hexed" or s == "hexed":
            server_running = True
            subprocess.call('echo -e "hexed" | java -jar server-release.jar', shell=True)
            
        # updates the server1
        if s[1:] == "update" or s == "update":
            subprocess.call('curl -s https://api.github.com/repos/anuken/mindustry/releases/latest | grep "browser_download_url.*server-release.jar" | cut -d : -f 2,3 | tr -d \" | wget -qi -', shell=True)


from subprocess import check_output
while wifi_ip == None:
    wifi_ip = check_output(['hostname', '-I'])
    if wifi_ip is not None:
        client.run('put your bot id here')
