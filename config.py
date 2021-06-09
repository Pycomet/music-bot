import os
import telegram
import time
from flask import Flask, request
import telebot
from telebot import types
from models import *
from dotenv import load_dotenv
load_dotenv()


# Logging Setup
import logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
    )

TOKEN = os.getenv('TOKEN')

DEBUG = True

SERVER_URL = os.getenv("SERVER_URL")


bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

import importdir
importdir.do("main", globals())