from flask import Flask

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
from social_media.source_code.api.social_media.admin_apis import creating_profile, creating_post, delete_a_post, comments, likes
from social_media.source_code.api.social_media.functional_apis import get_comments, information_of_user_id, posts_of_particular_user_id