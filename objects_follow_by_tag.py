from main import InstaBot

print( __file__)
bot = InstaBot('username', 'PASSXX', 'follow_by_tag')  

#Todos los días menos martes y jueves a las 12 del mediodia
#Nunca más de 4 (4*10*2 interactions)
bot.follow_by_tags(['_chris_kap_', 'trasmispasos', 'max-berg-70'], 10)
bot.end()

   