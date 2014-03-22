from requests import request, HTTPError

from django.core.files.base import ContentFile
import urllib2

print "1 Hola"
def update_avatar(backend, details, response, social_user, uid,
                  user, *args, **kwargs):
    print "2 hola"
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture" % response['id']
        # avatar = urllib2.urlopen(url)
        print url
        print response
        # profile = user.get_profile()
        # profile.profile_photo.save(slugify(user.username + " social") + '.jpg', 
        #                     ContentFile(avatar.read()))              
        # profile.save()