import argparse
import logging
import os
from helpers.utils import add_default_args, get_args
from helpers.tele_client import create
from telethon import functions
from telethon.tl.types import InputPeerUser

root_path = os.path.dirname(os.path.abspath(__file__))
print(root_path)

logging.basicConfig(level=logging.WARNING)

parser = argparse.ArgumentParser(description="Run: python get_data.py --phone +849xxxxxxx --api_id xxxxxxx --api_hash xxxxxxxxxxxxxxxxx --user_id xxxxx --access_hash xxxxx --username xxxxx")
parser = add_default_args(parser)
parser.add_argument("--user_id", type=str, help="User id")
parser.add_argument("--access_hash", type=str, help="Access hash")
parser.add_argument("--username", type=str, help="Username")

args = get_args(parser)

if not args.user_id:
    print(f"--user_id argument is required")
    exit()

if not args.access_hash:
    print(f"--access_hash argument is required")
    exit()

if not args.username:
    print(f"--username argument is required")
    exit()

client = create(args)
client.connect()
user_to_add = InputPeerUser(int(args.user_id), int(args.access_hash))
result = client(functions.contacts.AddContactRequest(
    id=user_to_add,
    first_name=args.username,
    last_name='',
    phone='',
    add_phone_privacy_exception=True
))
print(f'Add {args.username} to contact successfully')
# print(result.stringify())