# -*- coding: utf-8 -*-

# from .context import use_hello
import unittest
from . import context
instagram_type = context.instagram_type

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_converter(self):
        with open("instagram_sample_img.json") as f:
            js_str = "".join(f.readlines())
        insta_obj = instagram_type.instagran_parse_json_to_obj(js_str)
        assert insta_obj.media == get_media()
        assert insta_obj.is_video == is_video()
        assert insta_obj.caption == get_caption()
        assert insta_obj.profile_url == get_profile_url()
        assert insta_obj.username == get_username()
        assert insta_obj.full_name == get_full_name()

def get_media():
    return "https://scontent-sjc3-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/138405654_1288650451513528_1400045062359081667_n.jpg?_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_cat=104&_nc_ohc=uu4Ew2gj2NkAX--Oh6n&tp=1&oh=e6a2c4b42002edbe6b9e86f1cdd490fe&oe=60330E41"
def is_video():
    return False
def get_caption():
    return "*\n*\n【美女navi ☻*】\n*\n*\n今回ご紹介させていただく方は❤︎\nまぁみ(小田愛実) さん ▶︎▷ @maaaami79\n * \n * \n# Repost\n.\n.\n#gyda \n.\n.\n.\n.\nまぁみ(小田愛実) さんのアカウントには\n他にも素敵な投稿が(*´﹀`)\nぜひ覗いてみてくださいね🧡\n*\n*\n*\n掲載希望の方は⇒\n@bijo_navi ❤︎と\n# ビジョナビ タグ付けお願いします☺︎!!\n*\n*\n次回もお楽しみに...😍\n*\n*\n#美肌 #カラコン #金髪 #ロングヘア\n#スタイル抜群 #巻き髪　\n#ギャルメイク #笑顔 #振り向き美人\n#アイメイク #マツエク #美意識\n#赤リップ #コスメ #naturalbeauty\n#セルフィー #美容 #リップ #howto\n#ヘアスタイル #おしゃれ女子\n#大人メイク #メイク #オトナ女子\n#美意識向上 #大人可愛い\n#セルフィー女子 #女子力アップ"
def get_profile_url():
    return "https://scontent-sjc3-1.cdninstagram.com/v/t51.2885-19/s150x150/75538167_873843176344950_17146810820722688_n.jpg?_nc_ht=scontent-sjc3-1.cdninstagram.com&_nc_ohc=d2FdoF2A0mUAX_L4zd4&tp=1&oh=6a404a439e7c61aaa5e2323a0b8158f8&oe=6032700C"
def get_username():
    return "bijo_navi"
def get_full_name():
    return "美女navi ☻*"

if __name__ == '__main__':
    unittest.main()
