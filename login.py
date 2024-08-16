# from telethon import sync
from helpers.utils import add_default_args, get_args
import argparse
import helpers.tele_client as tele_client


parser = argparse.ArgumentParser(description="Run: python login.py --phone +849xxxxxxx --api_id xxxxxxx --api_hash xxxxxxxxxxxxxxxxx")
parser = add_default_args(parser)
args = get_args(parser)

client = tele_client.create(args)
client.start()
if client.is_user_authorized():
    print('OK')
else:
    print('Error')
client.disconnect()
