import argparse
import json
import logging
import helpers.tele_client as tele_client

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, UserStatusOffline, UserStatusRecently, UserStatusLastMonth, UserStatusLastWeek
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.channels import GetParticipantsRequest
from datetime import datetime, timedelta
from helpers.utils import add_default_args, get_args

logging.basicConfig(level=logging.WARNING)


def get_group(args):
    client = tele_client.create(args)
    client.connect()
    if not client.is_user_authorized():
        print(f'User authorization failed, please run: python login.py --phone {args.phone} --api_id {args.api_id} --api_hash {args.api_hash}')
    else:
        get_data_group(client, args.phone)


def get_data_group(client, phone):
    print('getting data ' + phone)
    chats = []
    last_date = None
    chunk_size = 200
    groups = []

    query = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(query.chats)
    for chat in chats:
        try:
            # if chat.megagroup is not None and chat.access_hash is not None:
            if int(getattr(chat, 'participants_count', 0)) > 0:
                groups.append(chat)
                # print(f"\n\n")
                # print(chat)
        except Exception as e:
            print(e)
            continue

    results = []
    for group in groups:
        try:
            tmp = {
                'group_id': str(group.id),
                'access_hash': str(getattr(group, 'access_hash', None)),
                'title': str(group.title),
            }
            results.append(tmp)

            # if group.megagroup == True:
            if getattr(group, 'megagroup', None) == True:
                get_data_user(client, group, phone)
        except Exception as e:
            print(e)
            print('error save group')
    with open('data/group/' + phone + '.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)


def get_data_user(client, group, phone):
    group_id = str(group.id)
    print(group_id)

    while_condition = True
    my_filter = ChannelParticipantsSearch('')
    offset = 0
    all_participants = []
    
    while while_condition:
        participants = client(GetParticipantsRequest(channel=group,  offset= offset, filter = my_filter, limit=200, hash=0))
        
        all_participants.extend(participants.users)
        offset += len(participants.users)
        
        print(len(participants.users))
        
        if len(participants.users) < 1 :
            while_condition = False
            
    results = []
    today = datetime.now()
    last_week = today + timedelta(days=-7)
    last_month = today + timedelta(days=-30)
    path_file = 'data/user/' + phone + "_" + group_id + '.json'

    for user in all_participants:
        # if group_id == '2191418392':
        #     print(f"\n\n")
        #     print(user)
        # print(type(user.status))
        try:
            if isinstance(user.status, UserStatusRecently):
                date_online_str = 'online'
            else:
                date_online = None
                if isinstance(user.status, UserStatusLastMonth):
                    date_online = last_month
                if isinstance(user.status, UserStatusLastWeek):
                    date_online = last_week
                if isinstance(user.status, UserStatusOffline):
                    date_online = user.status.was_online

                if date_online is not None:
                    date_online_str = date_online.strftime("%Y%m%d")
                else:
                    date_online_str = 'None'
            tmp = {
                'user_id': str(user.id),
                'access_hash': str(user.access_hash),
                'username': str(user.username),
                'first_name': str(user.first_name),
                'last_name': str(user.last_name),
                'phone': str(user.phone),
                'bot': str(user.bot),
                'contact': str(user.contact),
                'mutual_contact': str(user.mutual_contact),
                "date_online": date_online_str
            }
            results.append(tmp)
        except Exception as e:
            print("Error get user", e)
    with open(path_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)


parser = argparse.ArgumentParser(description="Run: python get_data.py --phone +849xxxxxxx --api_id xxxxxxx --api_hash xxxxxxxxxxxxxxxxx")
parser = add_default_args(parser)
args = get_args(parser)
get_group(args)
