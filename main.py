import discord, os, asyncio

class VoiceClient(discord.Client):
    async def on_ready(self):
        print(f"✅ تسجيل الدخول: {self.user}")

        guild_id = int(os.environ["SERVER_ID"])
        channel_id = int(os.environ["CHANNEL_ID"])

        guild = self.get_guild(guild_id)
        if not guild:
            print("❌ السيرفر غير موجود")
            return

        channel = guild.get_channel(channel_id)
        if not channel or not isinstance(channel, discord.VoiceChannel):
            print("❌ الروم الصوتي غير موجود أو ليس روم صوتي")
            return

        try:
            await channel.connect()
            print(f"🎧 دخلت الروم الصوتي: {channel.name}")
        except Exception as e:
            print(f"⚠️ خطأ أثناء الدخول: {e}")

# تشغيل البوت
intents = discord.Intents.default()
client = VoiceClient(intents=intents)
client.run(os.environ["TOKEN"])
