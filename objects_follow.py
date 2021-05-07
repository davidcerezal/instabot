from main import InstaBot

print( __file__)
bot = InstaBot('username', 'PASSXX', 'normal_follow')  

#Todos los días a las 10 de la mañana
#Nunca más de 4 (4*10*2 interactions)
bot.follow(['_chris_kap_', 'trasmispasos', 'algunandrea'], 10)
bot.end()

   