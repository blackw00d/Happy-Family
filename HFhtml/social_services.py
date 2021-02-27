from HappyFamily.settings import VK_GROUP_ID, VK_ACCESS_TOKEN, INSTAGRAM_GROUP_ID, INSTAGRAM_LOGIN, INSTAGRAM_PASSWORD
import json
import requests
from instagrapi import Client


def check_vk_subscribe(vk_id):
    """ Проверка подписки на группу в ВК """
    if vk_id is None:
        return 'Не подписан'

    vk_group_id = VK_GROUP_ID
    vk_access_token = VK_ACCESS_TOKEN
    check_subscribe_url = f"https://api.vk.com/method/groups.getMembers?group_id={vk_group_id}&access_token" \
                          f"={vk_access_token}&v=5.92"
    vk_id_url = f"https://api.vk.com/method/users.get?user_ids={vk_id}&access_token={vk_access_token}&v=5.92"
    user_data = json.loads(requests.post(vk_id_url).text)

    if user_data['response'] is not None:
        vk_id = user_data['response'][0]['id']
        subscribe = json.loads(requests.post(check_subscribe_url).text)
        if subscribe['response'] is not None:
            return 'Подписан' if vk_id in subscribe['response']['items'] else 'Не подписан'
    return 'Не подписан'


def check_instagram_subscribe(instagram_id):
    """ Проверка подписки в Instagram """
    if instagram_id is None:
        return 'Не подписан'

    cl = Client()
    cl.login(INSTAGRAM_LOGIN, INSTAGRAM_PASSWORD)
    user = cl.user_id_from_username(instagram_id)
    user_followers = cl.user_followers(INSTAGRAM_GROUP_ID).keys()

    return 'Подписан' if user in user_followers else 'Не подписан'
