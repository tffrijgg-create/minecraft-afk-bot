const mineflayer = require('mineflayer');

function createBot() {
    const bot = mineflayer.createBot({
        host: 'boltsurvival.play.hosting',
        port: 31425,
        username: 'ServerStayAliveBot',
        version: '1.21'
    });

    bot.on('kick', (reason) => {
        console.log(`Kicked for: ${reason}. Reconnecting in 10 seconds...`);
        setTimeout(createBot, 10000);
    });

    bot.on('error', (err) => console.log('Error encountered:', err));
}

createBot();

