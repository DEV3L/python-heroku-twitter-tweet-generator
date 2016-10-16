import os
import sys

import facebook

cfg = {
    'page_id': os.environ.get('FACEBOOK_PAGE_ID'),
    'access_token': os.environ.get('FACEBOOK_USER_ACCESS_TOKEN')
}


def post_to_facebook_page(sentence):
    if not sentence:
        return

    get_api(cfg).put_wall_post(sentence)
    return sentence


def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
    graph = facebook.GraphAPI(page_access_token)
    return graph


if __name__ == '__main__':
    post_to_facebook_page(sys.argv[1] or "post some phrase")
