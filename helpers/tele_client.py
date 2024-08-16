from telethon import TelegramClient, sync


def create(args):
    folder_session = 'session/'
    if not args.proxy_type or not args.proxy_host or not args.proxy_port:
        proxy = None
    else:
        proxy = {
            'proxy_type': args.proxy_type or None,
            'addr': args.proxy_host or None,
            'port': args.proxy_port or None,
            'username': args.proxy_user or None,
            'password': args.proxy_pass or None,
            'rdns': True
        }

    client = TelegramClient(folder_session + args.phone, args.api_id, args.api_hash, proxy=proxy)

    return client