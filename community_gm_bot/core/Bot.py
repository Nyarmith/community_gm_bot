#!/usr/bin/env python3
import sqlite3 as db

class Bot:
    def __init__(self, token, db_path):
        # does db exist?
        # does token work?
        # is chat recognized?
        # any pending commands/messages?

    # generic entrypoint handler
    def handle_message(self, msg):
        # have we seen this user before?
        # what are the rules of the channel being posted in?
        # does this support or hurt the rules?
        # should admins know about this?
        # should the user be notified about this?
