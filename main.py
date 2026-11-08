import time
from javascript import require

mineflayer = require('mineflayer')

def create_bot():
    bot = mineflayer.createBot({
        'host': 'boltsurvival.play.hosting',
        'port': 31425,
        'username': 'ServerStayAliveBot',
        'version': '1.21'
    })

    @bot.on('kick')
    def on_kick(reason, loggedIn):
        print(f"Kicked: {reason}. Reconnecting in 10 seconds...")
        time.sleep(10)
        create_bot()

create_bot()
while True:
    time.sleep(1)
