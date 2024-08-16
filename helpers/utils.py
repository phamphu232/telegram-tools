def add_default_args(parser):
    parser.add_argument("-v", "--verbose", action="store_true", help="Show verbose")
    parser.add_argument("-p", "--phone", type=str, help="Phone(format ex: +841234567899)")
    parser.add_argument("-ai", "--api_id", type=str, help="App Id - https://my.telegram.org/apps")
    parser.add_argument("-ah", "--api_hash", type=str, help="App Id - https://my.telegram.org/apps")
    parser.add_argument("--proxy_type", type=str, help="Proxy type - socks4, socks5, http")
    parser.add_argument("--proxy_host", type=str, help="Proxy host")
    parser.add_argument("--proxy_port", type=str, help="Proxy port")
    parser.add_argument("--proxy_user", type=str, help="Proxy username")
    parser.add_argument("--proxy_pass", type=str, help="Proxy password")
    return parser

def get_args(parser):
    # args = parser.parse_args()
    args, unknown = parser.parse_known_args()

    if not args.phone:
        print(f"--phone argument is required")
        exit()

    if not args.api_id:
        print(f"--api_id argument is required")
        exit()

    if not args.api_hash:
        print(f"--api_hash argument is required")
        exit()

    return args

def exit_app(client, message=None):
    if message:
        print(message)
    client.disconnect()
    exit()