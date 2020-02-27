import discord, socket, subprocess, urllib

client = discord.Client()
status = False
wifi_ip = None

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!') or message.content.startswith('$') or message.content.startswith('^') or message.content.startswith('\\') or message.content.startswith(':') or message.content.startswith('|'):
        s = message.content
        print(s)
        if s[1:] == "ip" or s == "ip":
            await message.channel.send('Checking...')
            try:
                host_name = socket.gethostname()
                host_ip = socket.gethostbyname(host_name)
                await message.channel.send("Hostname :  " + host_name)
                await message.channel.send("IP : " + host_ip)
            except:
                await message.channel.send("Unable to get Hostname and IP")
        if s[1:] == "stop" or s == "stop":
            exit()
            exit()
            exit()
        if s[1:] == "hexed" or s == "hexed":
            subprocess.call('echo -e "hexed" | java -jar server.jar', shell=True)
        if s[1:] == "update" or s == "update":
            subprocess.call('curl -s https://api.github.com/repos/anuken/mindustry/releases/latest | grep "browser_download_url.*server-release.jar" | cut -d : -f 2,3 | tr -d \" | wget -qi -', shell=True)


from subprocess import check_output
while wifi_ip == None:
    wifi_ip = check_output(['hostname', '-I'])
    if wifi_ip is not None:
        client.run('put your bot id here')
