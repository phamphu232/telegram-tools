import argparse
import json
import logging
import os
import time
import traceback

from helpers.utils import add_default_args, exit_app, get_args, exit_app
from helpers.tele_client import create
from datetime import datetime, timedelta
from telethon.tl.types import InputPeerChannel
from telethon.tl.types import InputPeerUser
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, FloodWaitError


def get_group_by_id(groups, group_id):
    for group in groups:
        if (int(group_id) == int(group['group_id'])):
            return group
    return None

root_path = os.path.dirname(os.path.abspath(__file__))
print(root_path)

logging.basicConfig(level=logging.WARNING)

parser = argparse.ArgumentParser(description="Run: python get_data.py --phone +849xxxxxxx --api_id xxxxxxx --api_hash xxxxxxxxxxxxxxxxx --source_gid xxxxx --target_gid xxxxx")
parser = add_default_args(parser)
parser.add_argument("-s", "--source_gid", type=str, help="Id group source")
parser.add_argument("-t", "--target_gid", type=str, help="Id group target")

args = get_args(parser)

if not args.source_gid:
    print(f"--source_gid argument is required")
    exit()

if not args.target_gid:
    print(f"--target_gid argument is required")
    exit()

client = create(args)
client.connect()

from_date_active =(datetime.now() - timedelta(days=365)).strftime('%Y%m%d')
phone = args.phone

# Get groups
group_path = root_path + '/data/group/' + phone + '.json'
if not os.path.isfile(group_path):
    print('This account with phone do not have data. Please run get_data')
    exit_app(client)

with open(group_path, 'r', encoding='utf-8') as f:
    groups = json.loads(f.read())

source_group = get_group_by_id(groups, args.source_gid)
if not source_group:
    print('Source group not found')
    exit_app(client)

# Get source users
source_users_path = root_path + '/data/user/' + phone + "_" + str(args.source_gid) + '.json'
if not os.path.isfile(source_users_path):
    print('The source_users_path not found')
    exit_app(client)

with open(source_users_path, 'r', encoding='utf-8') as f:
    source_users = json.loads(f.read())

if not source_users:
    print('The source_users empty')
    exit_app(client)

# Get target users
target_group = get_group_by_id(groups, args.target_gid)
if not target_group:
    print('Target group not found')
    exit_app(client)

target_users_path = root_path + '/data/user/' + phone + "_" + str(args.target_gid) + '.json'
if not os.path.isfile(target_users_path):
    print('The target_users_path not found')
    exit_app(client)

with open(target_users_path, 'r', encoding='utf-8') as f:
    target_users = json.loads(f.read())

if not target_users:
    print('The target_users empty')
    exit_app(client)

source_users_user_id = [user['user_id'] for user in source_users]
target_users_user_id = [user['user_id'] for user in target_users]

target_group_entity = InputPeerChannel(int(target_group['group_id']), int(target_group['access_hash']))

i = 0
for user in source_users:
    i = i + 1
    try:
        if user['user_id'] in target_users_user_id:
            continue

        user_to_add = InputPeerUser(int(user['user_id']), int(user['access_hash']))
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print(f"Add user {user['username']} to group {target_group['title']} successfully")

    except PeerFloodError as e:
        print("PeerFloodError")
        traceback.print_exc()
        exit_app(client)
    except UserPrivacyRestrictedError:
        print("UserPrivacyRestrictedError")
        continue
    except FloodWaitError as e:
        print("FloodWaitError")
        traceback.print_exc()
        exit_app(client)
    except Exception as e:
        print("Error other", e)

    time.sleep(120)
exit_app(client)
