import discord
from discord import colour
from discord import embeds
from discord.abc import GuildChannel
from discord.ext import commands
import datetime
import asyncio
import random

client = commands.Bot(command_prefix = "&")
intents = discord.Intents(messages=True, guilds = True, reactions = True)



client.remove_command("help")

@client.event
async def on_ready():
	print("Bot is ready")


#gaw start cmd
@client.command()
@commands.has_permissions(manage_messages = True)
async def gstart(ctx, mins : int, member : discord.Member, * , prize:str ):
	await discord.TextChannel.trigger_typing()




	#def convert(time):

		#pos = ["s", "m", "h", "d", "y"]

		#time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : f"{3600*24}", "y" : f"{3600*24*365}"}

		#unit = time[-1]

		#if unit not in pos:
			#return -1
		#try:
		#	val = int(time[:-1])
		#except:
		#	return -2


		#return val * time_dict[unit]

	embed = discord.Embed(title = f"🎉{prize}🎉", description = f"Donated by : {member.mention}", color = discord.Colour.random())
	ends = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins * 60)
	embed.add_field(name = "Ends At:", value = f"{ends} UTC")
	embed.set_footer(text = f"Ends in {mins} min(s) from now!")
	my_msg = await ctx.send("<a:giveaway:862239615241945108> Crown Dank Memers gaw <a:giveaway:862239615241945108>", embed = embed)
	await my_msg.add_reaction("<a:giveaway:862239615241945108>")
	await ctx.message.delete()
	await asyncio.sleep(mins*60)
	await ctx.trigger_typing()
	new_msg = await ctx.channel.fetch_message(my_msg.id)



	users = await new_msg.reactions[0].users().flatten()
	users.pop(users.index(client.user))

	winner = random.choice(users)
	

	await my_msg.reply(f"Congratulations! {winner.mention}, you won {prize}!")

#gaw end cmd
@client.command()
@commands.has_permissions(manage_messages = True)
async def gend(ctx, msg_id : int):
	await ctx.trigger_typing()

	new_msg_1 = await ctx.channel.fetch_message(msg_id)



	users = await new_msg_1.reactions[0].users().flatten()
	users.pop(users.index(client.user))

	winner = random.choice(users)


	link = discord.Message.jump_url(msg_id)
	await asyncio.sleep(5)
	await ctx.send(f"Congratulations! {winner.mention}, you won the gaw, {link} !")




#reply on members
@client.event
async def on_message(msg):
	if 'members' in msg.content:
		await msg.trigger_typing()
		link = await msg.channel.create_invite(max_age = 0)
		true_members = msg.guild.member_count
		embed = discord.Embed(title = "Member count" , colour = discord.Colour.random())
		embed.add_field(name = "What we want?" , value = f"We have {true_members} members help us reach 500 members.")
		embed.add_field(name = "Note:", value = f"Invite Friends when??! {link} " )
		await msg.reply(embed = embed)
	elif 'Members' in msg.content:
		await msg.trigger_typing()
		link = await msg.channel.create_invite(max_age = 0)
		true_members = msg.guild.member_count
		embed = discord.Embed(title = "Member count" , colour = discord.Colour.random())
		embed.add_field(name = "What we want?" , value = f"We have {true_members} members help us reach 500 members.")
		embed.add_field(name = "Note:", value = f"Invite Friends when??! {link} " )
		await msg.reply(embed = embed)


#reroll cmd
@client.command(aliases = ['r'])
@commands.has_permissions(manage_messages = True)
async def reroll(ctx, msg_id : int):
	await ctx.trigger_typing()
	await asyncio.sleep(5)

	new_msg_1 = await ctx.channel.fetch_message(msg_id)



	users = await new_msg_1.reactions[0].users().flatten()
	users.pop(users.index(client.user))

	winner = random.choice(users)
	await asyncio.sleep(5)


	await ctx.send(f"Congratulations! {winner.mention}, you won the reroll for the gaw with the id of {msg_id}!")


#splitorsteal
@client.command(aliases = ['sos'])
@commands.has_permissions(manage_messages = True)
async def splitorsteal(ctx, donor : discord.Member,dm : discord.Member, mins = 5, *, prize : str):
	await ctx.trigger_typing()
	await ctx.message.delete()
	embed = discord.Embed(title = f"<a:giveaway:862239615241945108> {prize} <a:giveaway:862239615241945108>", description = f"Donated by: {donor}", colour = discord.Colour.random())
	ends = datetime.datetime.utcnow() + datetime.timedelta(mins*60)
	embed.add_field(name = "DM:", value = dm)
	embed.add_field(name = "Ends At:", value = f"{ends} UTC")
	embed.set_footer(text = f"Ends in {mins} min(s) from now!")
	my_msg = await ctx.send("<a:giveaway:862239615241945108> Crown Dank Memers split or steal <a:giveaway:862239615241945108>", embed = embed)
	await my_msg.add_reaction("<a:giveaway:862239615241945108>")

	link = my_msg.jump_url
	try:
		await donor.send(f"Your split or steal in Crown Dank Memers, hosted by {ctx.author} has been started and the link to it is : {link}")
	except:
		f = 1 + 1
	await asyncio.sleep(mins*60)
	
	await ctx.trigger_typing()
	await asyncio.sleep(5)

	new_msg = await ctx.channel.fetch_message(my_msg.id)
	users = await new_msg.reactions[0].users().flatten()
	users.pop(users.index(client.user))

	winner1 = random.choice(users)
	winner2 = random.choice(users)

	await ctx.send(f"{winner1} , {winner2}")
	
	try:
		await winner1.send(f"Congratualtions! You are one of the winners of the split or steal, {link} , hosted in Crown Dank Memers, dm your response to {dm} in 30 seconds or you will be rerolled")
		await winner2.send(f"Congratualtions! You are one of the winners of the split or steal, {link} , hosted in Crown Dank Memers, dm your response to {dm} in 30 seconds or you will be rerolled")
		await dm.send(f"The winners of Your steal or split events, {link}, are {winner1.mention} and {winner2.mention}. Make sure that your DMs are open!")		
	except:
		await ctx.send("R.I.P There was an error delievering some dms, as one of them had their dms off")

	await my_msg.reply(f"Congratulations! {winner2.mention} and {winner1.mention} are the two winners of the split or steal.")

#sos end

@client.command(aliases = ['sosend', 'sose'])
@commands.has_permissions(manage_messages = True)
async def splitorstealend(ctx, my_msg : discord.Message):
	await ctx.trigger_typing()
	new_msg = await ctx.channel.fetch_message(my_msg.id)
	users = await new_msg.reactions[0].users().flatten()
	users.pop(users.index(client.user))

	winner1 = random.choice(users)
	winner2 = random.choice(users)
	link = my_msg.jump_url
	dm = ctx.author
	
	try:
		await winner1.send(f"Congratualtions! You are one of the winners of the split or steal, {link} , hosted in Crown Dank Memers, dm your response to {dm.mention} in 30 seconds or you will be rerolled")
		await winner2.send(f"Congratualtions! You are one of the winners of the split or steal, {link} , hosted in Crown Dank Memers, dm your response to {dm.mention} in 30 seconds or you will be rerolled")
		await dm.send(f"The winners of Your steal or split events, {link}, are {winner1.mention} and {winner2.mention}. Make sure that your DMs are open!")		
	except:
		await my_msg.reply(f"Congratulations! {winner2.mention} and {winner1.mention} are the two winners of the split or steal.")


#sos reroll

@client.command(aliases = ['sosr', 'sosreroll'])
@commands.has_permissions(manage_messages = True)
async def splitorstealreroll(ctx, my_msg : discord.Message , win = 2):
	await ctx.trigger_typing()
	new_msg = await ctx.channel.fetch_message(my_msg.id)
	users = await new_msg.reactions[0].users().flatten()
	users.pop(users.index(client.user))
	link = my_msg.jump_url
	if win == 1:
		winner1 = random.choice(users)
		try:
			await winner1.send((f"Congratualtions! You are the winner of the reroll of the split or steal, {link} , hosted in Crown Dank Memers, dm your response to the one to be dmed in 30 seconds or you will be rerolled"))
		except:	
			await my_msg.reply(f"Congratulations! {winner1.mention} , you  are the new winner of the split or steal.")
	elif win == 2:

		winner1 = random.choice(users)
		winner2 = random.choice(users)


		try:
			await winner1.send(f"Congratualtions! You are one of the winners of the split or steal, {link} , hosted in Crown Dank Memers, dm your response to the one to be dmed in 30 seconds or you will be rerolled")
			await winner2.send(f"Congratualtions! You are one of the winners of the split or steal, {link} , hosted in Crown Dank Memers, dm your response to the one to be dmed in 30 seconds or you will be rerolled")
		except:
			await my_msg.reply(f"Congratulations! {winner2.mention} and {winner1.mention} are the two winners of the reroll of split or steal.")

	else:
		await ctx.reply("My man, u need to gimme the no. of wins after the message id and the win should be 1 or 2 or I break. ``` *sosr <sos> <winners>```")



#kick cmd

@client.command(aliases = ['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member,*, reason = "none"):
	await ctx.trigger_typing()
    #check = False
   # for i in member.roles:
       # if i in ctx.author.roles[1:]:
          #  check = True

    		#if(check):
        		#await ctx.send('Cant kick Moderators/Admins')
    		#else:
	await member.send(f"You have been kicked from Crown Dank Memers by {ctx.author} and the reason provided was {reason}")
	await member.kick(reason = reason)
	await ctx.send(f"{ctx.author.mention} has kicked {member.mention} from Crown Dank Memers and the reason provided was {reason}")


#false ban cmd
@client.command(aliases = ['bann'])
@commands.has_permissions(manage_messages = True)
async def bon(ctx, member : discord.Member):
	await ctx.trigger_typing()
	msg = await ctx.send(f"{ctx.author.mention} has banned {member.mention} using my long ppppppppp")
	await msg.add_reaction("<a:abanhammer:851715377255677972>")
	await member.send(f"Sry to say but you have been banned <a:abanhammer:851715377255677972> from Crown Dank Memers by {ctx.author.mention}")

#purge cmd
@client.command(aliases = ['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 1):
	await ctx.channel.purge(limit = amount + 1)




#mute members
@client.command(aliases = ['m'])
@commands.has_permissions(kick_members = True)
async def mute(ctx,member : discord.Member, time = 60, * , reason = "N/A" ):
	await ctx.trigger_typing()
	muted_role = ctx.guild.get_role(868397565249470464)
	time = int(time)
	await member.add_roles(muted_role)
	await ctx.send(f"{ctx.author.mention} has muted {member.mention} successfully for {time}.")
	await member.send(f"You have been muted in Crown Dank Memers for {time} by {ctx.author}.")


	await asyncio.sleep(time*60)
	unmute = await member.remove_role(muted_role)



#unmute members

@client.command(aliases=['um'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member : discord.Member):
	await ctx.trigger_typing()
	muted_role = ctx.guild.get_role(868397565249470464)
	await member.remove_role(muted_role)

#unban users
@client.command(aliases = ['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx,*, member):
	await ctx.trigger_typing()
	banned_users = await ctx.guild.bans()
	member_name, member_disc = member.split("#")

	for banned_entry in banned_users:
		user = banned_entry.user
		if(user.name, user.discriminator) == (member_name,member_disc):
		
			await ctx.guild.unban(user)
			await ctx.send(member_name + f" has been unbanned successfully by {ctx.author.mention}")
			await member.send(f"You have been unbanned from Crown Dank Memers by {ctx.author}")
			return
	await ctx.send(f"{member} was not found.")

#Ban command
@client.command(aliases = ['b'])
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
	
    check = False
    for i in member.roles:
        if i in ctx.author.roles[1:]:
            check = True

    if(check):
        ctx.send('Cant ban Moderators/Admins')
    else:
        await member.ban(reason=reason)
        my_msg = await ctx.send(f'{member.mention} has been banned!')
        await my_msg.add_reaction("<a:abanhammer:851715377255677972>")
        await member.send(f"You have been banned from Crown Dank Memers by {ctx.author} and the reason provided was {reason}")


#USER INFO
@client.command(aliases=['user', 'info'])
@commands.has_permissions(administrator = True)
async def whois(ctx, member:discord.Member):
	await ctx.trigger_typing()
	embed = discord.Embed(title = member.name, description = member.mention , color = discord.Colour.random())

	Role = discord.Member.roles
	top_role = discord.Member.top_role
	created = discord.Member.created_at
	#created = int(created)
	#created = datetime.datetime(created)
	roles = Role
	Top_role = top_role

	embed.add_field(name = "ID", value = member.id, inline = True)
	embed.add_field(name = "Roles", value = ", ".join(role.mention for role in reversed(member.roles) if role.name != "@everyone"), inline = True)
	embed.add_field(name = "Top Role", value = f"{member.top_role.mention}", inline = True)
	embed.add_field(name = "Account was created on:", value = f"{member.created_at}")
	embed.set_thumbnail(url = member.avatar_url)
	embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
	await ctx.send(embed = embed)


#role info
@client.command(aliases = ['rinfo'])
@commands.has_permissions(administrator = True)
async def roleinfo(ctx, role : discord.Role ):
	await ctx.trigger_typing()

	#colours = ["red", "purple", "blue", "green"]
	#colour = random.choice(colours)
	embed = discord.Embed(title = role.name, color = discord.Colour.random())
	embed.add_field(name = "ID", value = role.id , inline = True)
	embed.add_field(name = "Mentionable by users :", value = role.mentionable, inline = True)
	embed.add_field(name = "Created at:", value = role.created_at, inline = True)
	#embed.add_field(name = "Can add reactions:", value = role.Permissions.add_reaction(), inline = True)
	#embed.add_field(name = "Admin:", value = role.permissions.administrator, inline = True)
	#embed.add_field(name = "Can attach files:", value = role.permissions.attach_files, inline = True)
	#embed.add_field(name = "Can ban members:", value = role.permissions.ban_members, inline = True)
	#embed.add_field(name = "Can change nickname:", value = role.permissions.change_nickname, inline = True)
	#embed.add_field(name = "Can connect:", value = role.permissions.connect, inline = True)
	#embed.add_field(name = "Can create instant invite:", value = role.permissions.creat_instant_invite, inline = True)
	#embed.add_field(name = "Can deafen members:", value = role.permissions.deafen_members, inline = True)
	#embed.add_field(name = "Can embed links:", value = role.permissions.embed_links, inline = True)
	#embed.add_field(name = "Can kick members:", value = role.permissions.kick_members, inline = True)
	#embed.add_field(name = "Can manage chanels:", value = role.permissions.manage_channels, inline = True)
	#embed.add_field(name = "Can manage emojis:", value = role.permissions.manage_emojis, inline = True)
	#embed.add_field(name = "Can manage server:", value = role.permissions.manage_guild, inline = True)
	#embed.add_field(name = "Can manage messages:", value = role.permissions.manage_messages, inline = True)
	#embed.add_field(name = "Can manage nicknames:", value = role.permissions.manage_nicknames, inline = True)
	#embed.add_field(name = "Can manage permissions:", value = role.permissions.manage_permissions, inline = True)
	#embed.add_field(name = "Can manage roles:", value = role.permissions.manage_roles, inline = True)
	#embed.add_field(name = "Can manage webhooks:", value = role.permissions.manage_webhooks, inline = True)
	#embed.add_field(name = "Can mention everyone/here:", value = role.permissions.mention_everyone, inline = True)
	#embed.add_field(name = "Can move members:", value = role.permissions.move_members, inline = True)
	#embed.add_field(name = "Can mute members:", value = role.permissions.mute_members, inline = True)
	#embed.add_field(name = "Is priority speaker:", value = role.permissions.priority_speaker, inline = True)
	#embed.add_field(name = "Can read message history:", value = role.permissions.read_message_history, inline = True)
	#embed.add_field(name = "Can read messages:", value = role.permissions.read_messages, inline = True)
	#embed.add_field(name = "Can request to speak:", value = role.permissions.request_to_speak, inline = True)
	#embed.add_field(name = "Can send messages:", value = role.permissions.send_messages, inline = True)
	#embed.add_field(name = "Can send tts messages:", value = role.permissions.send_tts_messages, inline = True)
	#embed.add_field(name = "Can speak:", value = role.permissions.speak, inline = True)
	#embed.add_field(name = "Can stream:", value = role.permissions.stream, inline = True)
	#embed.add_field(name = "Can use external emojis:", value = role.permissions.use_external_emojis, inline = True)
	#embed.add_field(name = "Can use slash commands:", value = role.permissions.use_slash_commands, inline = True)
	#embed.add_field(name = "Can use voice activation:", value = role.permissions.use_voice_activation, inline = True)
	#embed.add_field(name = "Can view audit log:", value = role.permissions.view_audit_log, inline = True)
	#embed.add_field(name = "Can view channel:", value = role.permissions.view_channel, inline = True)
	#embed.add_field(name = "Can view guild insights:", value = role.permissions.view_guild_insights, inline = True)
	embed.add_field(name = "Position in Hierarchy:", value = role.position, inline = True)
	embed.add_field(name = "Managed by an integration:", value = role.managed)
	embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

	await ctx.send(embed = embed)


#info on text channel
@client.command(aliases = ['t'])
async def textchannel(ctx, text : discord.TextChannel):
	await ctx.trigger_typing()
	embed = discord.Embed(title = f"{text.name}", color = discord.Colour.random())
	embed.add_field(name = "ID", value = text.id , inline = True)
	embed.add_field(name = "Category that they fall under:", value = text.category, inline = True)
	embed.add_field(name = "Category ID", value = text.category_id)
	embed.add_field(name = "Created at:", value = text.created_at)
	#l_m = text.last_message
	#l_m1 = l_m.jump_url
	#embed.add_field(name = "Last Message", value = l_m1)
	embed.add_field(name = "Slowmode:", value = text.slowmode_delay)
	embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")

	await ctx.send(embed = embed)

#ping pong
@client.command(aliases = ['pong' , 'latency'])
async def ping(ctx):
	await ctx.trigger_typing()
	pong = format(round(client.latency, 1)*1000)
	embed = discord.Embed(title = "My pong is:", color = discord.Colour.random())
	embed.add_field(name = "pong!", value =  f"{pong} ms" )

	await ctx.send(embed = embed)


#serverinfo
@client.command(aliases = ['sinfo', 'guildinfo'])
@commands.has_permissions(kick_members = True)
async def serverinfo(ctx):
	await ctx.trigger_typing()
	s_name = ctx.guild.name
	s_id = s_name.id
	owner = s_name.owner
	owner_id = owner.id
	embed = discord.Embed(title = f"{s_name} info", description = f"{owner.mention}", colour = discord.Colour.random())
	embed.add_field(name = "Server ID:", value = s_id , inline = False)
	embed.add_field(name = "Owner ID:", value = owner_id)
	embed.add_field(name = "Total number of channels:", value = ctx.guild.channel_count)


@client.command
async def test(ctx):
	await ctx.send("bruh")



#help
@client.command(aliases = ['h', 'help me'])
async def help(ctx , f = 0):
	await discord.TextChannel.trigger_typing()
	embed = discord.Embed(title = "I am here to help u", description = "y u reading this just read from below", colour = discord.Colour.random())
	embed.add_field(name = "gstart" , value = "This command starts a gaw. The cmd includes: ```*gstart <time in mins> <donor> <prize> ```")
	embed.add_field(name = "gend", value = "This command ends a gaw. The cmd needs: ```*gend <gaw_id>```")
	embed.add_field(name = "greroll" , value = "This command rerolls the winner of a gaw. This cmd needs: ```*greroll <gaw_id>")
	embed.add_field(name = "splitorsteal / sos", value = "This command starts a split or steal. This cmd requires: ```*sos <donor> <the one who needs to be dmed> <time(default is 5m) in minutes> <prize> ```")
	embed.add_field(name = "splitorstealend / sose", value = "This command ends a split or steal. It requires: ```*sos <sos_id>```")
	embed.add_field(name = "splitorstealreroll / sosreroll", value = "This command rerolls a split or steal. It needs: ```*sosr <sos_id> ```")
	embed.add_field(name = "bann / bon", value = "This command is just for fun and requires : ```*bon <member> <reason (this is optional)>```")
	embed.add_field(name = "kick / k", value = "This command kicks a member and requires: ```*k <member> <reason (this is optional) > ```")
	embed.add_field(name = "ban / b", value  = "This command, as u might have guessed, **bans** a member. It requires: ```*b <member>``` ")
	embed.add_field(name = "purge / clear / c", value = "This command clears the specified number of msgs and needs: ```*c <no. of msgs>```")
	embed.add_field(name = "mute / m", value = "This command mutes a member. It needs: ```*mute <member> <time(optional)> <reason(optional)>```")
	embed.add_field(name = "unmute / um" , value = "This command unmutes a member. It needs: ```*um <member>```")
	embed.add_field(name="unba	n / ub" , value = "This command unbans a member. It requires: ```*ub <member>```")
	embed.add_field(name = "whois / user / info" , value = "This command gives a detailed info on the member and requires: ```*user <member> ```")
	embed.add_field(name="roleinfo / rinfo", value = "This command gives info of a role and needs: ```*rinfo <role (if the role is ping role, pls refrain from pinging it)> ")
	embed.add_field(name = "serverinfo / sinfo / guildinfo" , value = "This command returns the major characteristics of the server and it requires just the cmd.")
	embed.add_field(name = "textchannl / t ", value = "This returns the characteristics of a text channel. It requires: ```*t <textchannel> ```")
	embed.add_field(name = "ping / pong / latency", value = "This returns the bot's latency and requires just the cmd.")
	embed.add_field(name = "freeloader / fl" , value = "This command tempbans the user that has been recorded as a freeloader for 7 dyas and needs: ```*fl <user>```")
	await ctx.send(embed = embed)

#error-handling
@client.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.MissingPermissions):
		await ctx.reply("Bruh, you dont have the required perms")
	elif isinstance(error,commands.MissingRequiredArgument):
		await ctx.reply("Bruh, you didnt tell me everything.")
	elif isinstance(error, commands.CommandNotFound):
		await ctx.reply("Bruh, wat ya sayin'?")
	else:
		raise error






@client.command(aliases = ['fl'])
@commands.has_permissions(ban_members = True)
async def freeloader(ctx, member : discord.Member):
	await ctx.trigger_typing()
	await member.ban(reason = "freeloading")
	await ctx.send(f"Banned {member}")
	try:
		member.send(f"U were freeloading and have been banned from {ctx.guild.name} for 7 days. **So don't freeload**")
	except:
		f = 1+1
	await asyncio.sleep(604800)
	await ctx.guild.unban(member)



client.run("ODY4NzQ3MDkyNDE4NTIzMTQ3.YP0Jxw.hDbH-VEBKgz2w4435AlftH-GkcI")