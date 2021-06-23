from dict2obj import Dict2Obj
from debug import DEBUG
import json
from typing import List

import dict2obj

class InstagramData:
    """[summary]

    Attributes
    -----------
    media: :class:`str`
        The url for the post's media.
    is_video: :class:`boolean`
        Whether this includes a video post.
    caption: :class:`str`
        The description by the author.
    """
    def __str__(self):
        n_caption = " ".join(self.caption[:100].split("\n"))
        return(f"""
==================================================
    media: {self.media}
==================================================
    is_video: {self.is_video}
==================================================
    caption: {n_caption}
==================================================
    profile_url: {self.profile_url}
==================================================
    username: {self.username}
==================================================
    full_name: {self.full_name}
==================================================
        """)
    def __init__(self, 
    media,
    is_video,
    caption,
    profile_url,
    username,
    full_name
    ):
        """init
        media: 写真投稿に対する メイン画像 url
        is_video: ビデオかどうか
        caption: キャプション(投稿時のメッセージ)
        self.profile_url = profile_url # プロフィール画像のurl
        self.username = username # ユーザネーム(アルファベット)
        self.full_name = full_name # 表示名
        """
        self.media = media       # 写真投稿に対する メイン画像 url
        self.is_video = is_video # ビデオかどうか
        self.caption = caption # キャプション(投稿時のメッセージ)
        self.profile_url = profile_url # プロフィール画像のurl
        self.username = username # ユーザネーム(アルファベット)
        self.full_name = full_name # 表示名

def convert_long_caption(caption: str) -> str:
    lst = caption.split("\n")
    if DEBUG:
        print("lst: ", lst)
    lines = len(lst)
    if lines > 10:
        return "\n".join(lst[:10])
    else: return caption

def convert_to_instagram_type(oj) -> InstagramData:
    media = oj.graphql.shortcode_media.display_url
    if len(oj.graphql.shortcode_media.edge_media_to_caption.edges) == 0:
        caption = ""
    else:
        caption = oj.graphql.shortcode_media.edge_media_to_caption.edges[0].node.text

    caption = convert_long_caption(caption)
    is_video = oj.graphql.shortcode_media.is_video
    profile_url = oj.graphql.shortcode_media.owner.profile_pic_url
    username = oj.graphql.shortcode_media.owner.username
    full_name = oj.graphql.shortcode_media.owner.full_name
    return InstagramData(
        media = media,
        is_video = is_video,
        caption = caption,
        profile_url = profile_url,
        username = username,
        full_name = full_name
    )
def get_multiple_medias(oj) -> List[str]:
    ans = []
    for node in oj.graphql.shortcode_media.edge_sidecar_to_children.edges:
        display_url = node.node.display_url
        ans.append(display_url)
    return ans

def instagran_parse_json_to_obj(str):
    """
    __a=1 の json レスポンスを InstagramData に変換する。
    """
    dic_ = json.loads(str)
    oj = Dict2Obj(dic_)
    return convert_to_instagram_type(oj)

if __name__ == '__main__':
    import json
    with open("instagram_multi_img.json") as f:
        dic_ = json.load(f)
    oj = Dict2Obj(dic_)

    
    
    for i in get_multiple_medias(oj):
        print(i)
    # print(get_multiple_medias(oj))
