from social_auth.models import UserSocialAuth

def user_picture(request):
	if (request.user.id):
		fbUserId = UserSocialAuth.objects.filter(user=request.user.id).get().uid
		fbUserPic = "http://graph.facebook.com/%s/picture?type=large" % fbUserId
		return {'fbUserPic':fbUserPic}
	else:
		return ''