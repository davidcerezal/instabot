from main import InstaBot

print( __file__)
bot = InstaBot('username', 'PASSXX', 'interact')  

#Todos los días menos martes y jueves a las 12 del mediodia
bot.like(['_chris_kap_', 'trasmispasos', 'max-berg-70'], 10)
bot.end()

   