const Discord = require('discord.js');
const bot = new Discord.Client();

const PREFIX = "!";
const token = "NzMzMzgzNTI2MzU4OTc0NTI0.XxCwLA.24KW5ynrYV2qwdKQRKlAfvDS6fY";
bot.on("ready", ()=>{
    console.log("This bot is online!");

})
bot.on('message', msg=>{
    if(msg.content === "TOP LANE KINGDOME"){
        msg.reply("TRULY");
    }
    let args = msg.content.substring(PREFIX.length).split("");
    switch(args[0]){
        case 'stats':
            if(args[1] === 'champ'){
                msg.reply('work in progress');
            }
        break;
    }
})
bot.login(token);