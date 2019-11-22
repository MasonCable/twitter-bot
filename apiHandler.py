import requests
from twitter import *

class ApiFunctions:
    pass
    # def __init__(self, post, hashtag):
    #     self.post = post
    #     self.hashtag = tag
    #     self.twit = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret)) 

    # def makePost(self):
    #     pass

    #     # Get your "home" timeline
    # twit.statuses.home_timeline()

    # # Get a particular friend's timeline
    # twit.statuses.user_timeline(screen_name="billybob")

    # # to pass in GET/POST parameters, such as `count`
    # twit.statuses.home_timeline(count=5)

    # # to pass in the GET/POST parameter `id` you need to use `_id`
    # twit.statuses.oembed(_id=1234567890)

    # # Update your status
    # twit.statuses.update(
    #     status="Using @sixohsix's sweet Python Twitter Tools.")

    # # Send a direct message
    # twit.direct_messages.new(
    #     user="billybob",
    #     text="I think yer swell!")

    # # Get the members of tamtar's list "Things That Are Rad"
    # twit.lists.members(owner_screen_name="tamtar", slug="things-that-are-rad")

    # # An *optional* `_timeout` parameter can also be used for API
    # # calls which take much more time than normal or twitter stops
    # # responding for some reason:
    # twit.users.lookup(
    #     screen_name=','.join(A_LIST_OF_100_SCREEN_NAMES), _timeout=1)

    # # Overriding Method: GET/POST
    # # you should not need to use this method as this library properly
    # # detects whether GET or POST should be used, Nevertheless
    # # to force a particular method, use `_method`
    # twit.statuses.oembed(_id=1234567890, _method='GET')

    # # Send images along with your tweets:
    # # - first just read images from the web or from files the regular way:
    # with open("example.png", "rb") as imagefile:
    #     imagedata = imagefile.read()
    # # - then upload medias one by one on Twitter's dedicated server
    # #   and collect each one's id:
    # t_upload = Twitter(domain='upload.twitter.com',
    #     auth=OAuth(token, token_secret, consumer_key, consumer_secret))
    # id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
    # id_img2 = t_upload.media.upload(media=imagedata)["media_id_string"]
    # # - finally send your tweet with the list of media ids:
    # twit.statuses.update(status="PTT ★", media_ids=",".join([id_img1, id_img2]))

    # # Or send a tweet with an image (or set a logo/banner similarily)
    # # using the old deprecated method that will probably disappear some day
    # params = {"media[]": imagedata, "status": "PTT ★"}
    # # Or for an image encoded as base64:
    # params = {"media[]": base64_image, "status": "PTT ★", "_base64": True}
    # twit.statuses.update_with_media(**params)

    # # Attach text metadata to medias sent, using the upload.twitter.com route
    # # using the _json workaround to send json arguments as POST body
    # # (warning: to be done before attaching the media to a tweet)
    # t_upload.media.metadata.create(_json={
    # "media_id": id_img1,
    # "alt_text": { "text": "metadata generated via PTT!" }
    # })
    # # or with the shortcut arguments ("alt_text" and "text" work):
    # t_upload.media.metadata.create(media_id=id_img1, text="metadata generated via PTT!")
