from main import InstaBot

print( __file__)
bot = InstaBot('username', 'PASSXX', 'unfollow')  

#Debería ir a los martes y jueves a la noche
bot.unfollow(100)
bot.end()

   