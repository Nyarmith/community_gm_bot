"""
Community Bot Launcher

Parameters:
- key
- database file path (if empty, initializes a new one)

Exit Codes:
0 - Normal Shutdown
1 - Unexpected Error
2 - Invalid Token
20 - Restart
"""
import argparse
import discord
from discord.ext import commands
import sys

from core import Bot
from core import init_logger

def run_bot(args):
    bot = Bot(args.token, args.database, debug=args.debug)
    print("Loading loggers...")
    bot.logger = init_logger(bot, args.debug)
    bot.logger.debug("Loaded loggers.")

    if bot.config["token"] is None:
        bot.logger.error("Invalid token!")
        bot.shutdown_mode = 2
        sys.exit(bot.shutdown_mode)
      
    bot.logger.debug("Loading extensions...")
    bot.load_extension("mysterybot.core.cog_manager")
    #bot.load_extnesion("mysterybot.core.timer")
    
    print('''
          ///"\
          |6 6|
          \ - /
   .@@@. __) (__                                                   _ _ 
   @6 6@/  \./  \         ___ ___  _ __ ___  _ __ ___  _   _ _ __ (_) |_ _   _ 
   @ = @ :  :  : \       / __/ _ \| '_ ` _ \| '_ ` _ \| | | | '_ \| | __| | | |
   _) (_'|  :  |) )     | (_| (_) | | | | | | | | | | | |_| | | | | | |_| |_| |
 /' \./ '\  :  |_/       \___\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|_|\__|\__, |
/ /\ _ /\ \=o==|)                             _           _              |___/ 
\ \ )  (/ /%|%%'           __ _ _ __ ___     | |__   ___ | |_
 '7/    \7%%|%%'          / _` | '_ ` _ \    | '_ \ / _ \| __|
   |    |`%%|%%'         | (_| | | | | | |   | |_) | (_) | |_
   |    |`%%|%%'          \__, |_| |_| |_|___|_.__/ \___/ \__|
   |    | %%|%%           |___/         |_____|
   |_.._| /_|_\
            ''')
    bot.logger.info("Running bot")
    try:
        bot.run(bot.config["token"])
    except KeyboardInterrupt:
        bot.logger.info("Shutting down bot...")
        bot.shutdown_mode = 0
    finally:
        sys.exit(bot.shutdown_mode)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="community_gm_bot - Discord Bot")
    parser.add_argument("--debug", "-d", help="Enable debug mode.", action="store_true")
    parser.add_argument("--token", "-t", help="Bot token.", required=True)
    parser.add_argument("--database", "-d", help="Bot owner id.", required=True)
    args = parser.parse_args()
    args = parser.parse_args()
    
    run_bot(args)
