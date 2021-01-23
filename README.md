# instagram_type Module Repository

## usage

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
