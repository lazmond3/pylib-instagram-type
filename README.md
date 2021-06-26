# instagram_type Module Repository

## このリポジトリは
- https://github.com/lazmond3/pylib-discord-instagram-bot/pull/18
こちらに吸収されたので deprecated

## usage

sample for https://www.instagram.com/p/CO4WO8nnvc6/?__a=1
[sample](sample2_multiple_image.json)

```python
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
```
