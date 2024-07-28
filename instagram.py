from instabot import Bot
bot = Bot()
bot.login(username = "your_username", password = "your_password")
bot.follow("id_name")
bot.upload_photo("Imagepath.extenstion")
bot.unfollow("id_name")
bot.send_message("Type your msg here", ["username1", "username2"])
followers = bot.get_user_followers("your_username")
for foll in followers:
    print(bot.get_user_info(foll))
following = bot.get_user_following("your_username")
for folling in following:
    print(bot.get_user_info(folling))