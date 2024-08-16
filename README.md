# telegram-tools
telegram-tools

## Settings

```
pip3 install virtualenv
virtualenv .venv
# or
python3.7 -m venv .venv

source .venv/bin/activate
pip install -r requirements.txt

# pip3 freeze > requirements.txt
```

```
python login.py --phone +849xxxxxxxx --api_id 70xxxxx --api_hash f4ae90b2bb1bce146f77950xxxxx --proxy_type socks5 --proxy_host xxx.xxx.xx.xx --proxy_port 1080 --proxy_user <USER> --proxy_pass <PASSWORD>

python get_data.py --phone +849xxxxxxxx --api_id 70xxxxx --api_hash f4ae90b2bb1bce146f77950xxxxx --proxy_type socks5 --proxy_host xxx.xxx.xx.xx --proxy_port 1080 --proxy_user <USER> --proxy_pass <PASSWORD>

python add_contact.py --phone +849xxxxxxxx --api_id 70xxxxx --api_hash f4ae90b2bb1bce146f77950xxxxx --proxy_type socks5 --proxy_host xxx.xxx.xx.xx --proxy_port 1080 --proxy_user <USER> --proxy_pass <PASSWORD> --user_id 2027985547 --access_hash 5957960244974965584 --username Trunghau1505

python add_member.py --phone +849xxxxxxxx --api_id 70xxxxx --api_hash f4ae90b2bb1bce146f77950xxxxx --proxy_type socks5 --proxy_host xxx.xxx.xx.xx --proxy_port 1080 --proxy_user <USER> --proxy_pass <PASSWORD> --source_gid 221xxxx --target_gid xxxxxxx
```

```
# Docker

cp docker-compose.yml.example docker-compose.yml

docker compose up -d --build

docker exec -it sh -c "python login.py --phone +849xxxxxxxx --api_id 70xxxxx --api_hash f4ae90b2bb1bce146f77950xxxxx --proxy_type socks5 --proxy_host xxx.xxx.xx.xx --proxy_port 1080 --proxy_user <USER> --proxy_pass <PASSWORD>"
docker exec -it sh -c "python get_data.py --phone +849xxxxxxxx --api_id 70xxxxx --api_hash f4ae90b2bb1bce146f77950xxxxx --proxy_type socks5 --proxy_host xxx.xxx.xx.xx --proxy_port 1080 --proxy_user <USER> --proxy_pass <PASSWORD>"
docker exec -it sh -c "python add_contact.py --phone +849xxxxxxxx --api_id 70xxxxx --api_hash f4ae90b2bb1bce146f77950xxxxx --proxy_type socks5 --proxy_host xxx.xxx.xx.xx --proxy_port 1080 --proxy_user <USER> --proxy_pass <PASSWORD> --user_id 2027985547 --access_hash 5957960244974965584 --username Trunghau1505"
docker exec -it sh -c "python add_member.py --phone +849xxxxxxxx --api_id 70xxxxx --api_hash f4ae90b2bb1bce146f77950xxxxx --proxy_type socks5 --proxy_host xxx.xxx.xx.xx --proxy_port 1080 --proxy_user <USER> --proxy_pass <PASSWORD> --source_gid 221xxxx --target_gid xxxxxxx"
```