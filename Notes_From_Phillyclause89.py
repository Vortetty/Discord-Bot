# I can't get the discord api on my work pc, so my help if going to be limited 
# to just offering suggestions on your logical flow here

# First we'll make a bunch of functions with the code from all your if blocks
def ip_block():
    # I'm just going to print your code as a docstring here since 
    # I can't really run any of it
    print("""
        await message.channel.send('Checking...')
        try:
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            await message.channel.send("Hostname :  " + host_name)
            await message.channel.send("IP : " + host_ip)
        except:
            await message.channel.send("Unable to get Hostname and IP")
    """)
    
    
def stop_block():
    print("""
        exit()
        exit()
        exit()
    """)
        
        
def hexed_block():
    print("""
        server_running = True
        subprocess.call('echo -e "hexed" | java -jar server-release.jar', shell=True)
    """)
        
        
def update_block():
    print("""
        subprocess.call('curl -s https://api.github.com/repos/anuken/mindustry/releases/latest | grep "browser_download_url.*server-release.jar" | cut -d : -f 2,3 | tr -d \" | wget -qi -', shell=True)
    """)


# Next we make a dict holding refs to all these functions
conditions = {
    "ip": ip_block,
    "stop": stop_block,
    "hexed": hexed_block, 
    "update": update_block,
}

# I'm assuming that message.content gives you a str
# for this example, the variable message_content is your message.content

message_cotent = "!ip"

# I had to add this server_running variable to test your code, 
# since I didnt want to get the discord API
server_running = True

# instead of calling the str.startswith() methond a bunch of times,
# just check if the object in the first str index is in a tuple of 
# characters you want this block to trigger on
if message_cotent[0] in ('!', '-', '$', '^', ':', '*'):

    # Could just have s be message_cotent[1:] instead of using that acssessor a bunch
    # The or conditions you were using on s also don't make sense to me
    # if the first char in s needs to be in ('!', '-', '$', '^', ':', '*') per the outer conditional
    # then s will never == "ip" or "stop" or "hexed" or "update"
    # Unless I'm missing something just checking s[1:] or message_cotent[1:] should do the trick 
    s = message_cotent[1:]
    
    # Can just use not server_running here 
    # instead of server_running == False
    if not server_running:
        print(s) 
        
    # Finnaly we check if s is in our conditions dict and if it is then we can use it to call the function it should trigger
    if s in conditions:
        conditions[s]()    
