import requests

from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
from django_redis import get_redis_connection
from django.forms.models import model_to_dict

from utils.Response import BasicView, SuccessResponse, ErrorResponse, SerializerErrorResponse
from utils.Sms import SEND_SMS
from utils.Time import get_timestamp, NowTimeToUTC
from utils.Random import get_noncestr
from utils.Sign import sha1

from .serializer import SendSerializer, SmsSerializer
from . import models
from . import tasks

########## message module
class IndexView(APIView):
	def get(self, request, *args, **kwargs):
		# 即时任务
		nid = tasks.add.delay(1, 2)
		# 定时任务
		task = tasks.jian.apply_async(args=[10, 5], eta=NowTimeToUTC(seconds=10))

		return Response({'位置': 'message module', '即时任务ID': nid.id, '定时任务ID': task.id}, status=200)

################### 发送验证码 #####################

class SmsView(APIView):

	serializer_class = SmsSerializer
	
	def post(self, request, *args, **kwargs):
		
		serializer = self.serializer_class(data=request.data)

		if not serializer.is_valid():
			return SerializerErrorResponse(serializer)

		phone = serializer.validated_data.get('phone')

		conn = get_redis_connection()
		
		stamp = conn.get('stamp_{phone}'.format(phone=phone))

		# 过期时间(秒)
		expired = 60

		if stamp:
			a = get_timestamp()
			b = int(stamp.decode('utf-8'))
			c = expired - (a - b)
			return ErrorResponse(code=2, msg='请稍候再试({0}s)!'.format(c))

		result = SEND_SMS(phone, debug=False)

		conn.set(result['phone'], result['code'], ex=5*60)

		stamp = get_timestamp()
		conn.set('stamp_{phone}'.format(phone=result['phone']), stamp, ex=expired)

		print("\033[1;31;40m{text}\033[0m".format(text=result))

		return SuccessResponse(msg='发送成功')

################### 表单提交 #####################

class SendView(APIView):
	serializer_class = SendSerializer

	def post(self, request, *argw, **kwargs):
		print(request.data.dict())

		serializer = self.serializer_class(data=request.data)
		if not serializer.is_valid():
			return SerializerErrorResponse(serializer)
		
		phone = serializer.validated_data.get('phone')
		result = models.Message.objects.filter(phone=phone).exists()
		if not result:
			res = serializer.save()
			res.create_time = res.create_time.strftime('%Y-%m-%d %H:%M:%S')
			return SuccessResponse(data=model_to_dict(res), msg='保存成功')
		return ErrorResponse(code=2, msg='不能重复提交')

################### 公众号签名 #####################

class SignatureView(APIView):
	def post(self, request, *args, **kwargs):

		url = request.data.get('url')
		timestamp = get_timestamp()
		noncestr = get_noncestr()

		data = {
			"debug": False,
			"appId": 'wxa4d1e1b8e398da74', # 必填，公众号的唯一标识
			"timestamp": timestamp, # 必填，生成签名的时间戳
			"nonceStr": noncestr, # 必填，生成签名的随机串
			"signature": '', # 必填，签名
			"jsApiList": [
				'onMenuShareAppMessage',    # 1.0 分享到朋友
				'onMenuShareTimeline',  # 1.0 分享到朋友
				'updateAppMessageShareData',  # 1.4 分享到朋友
				'updateTimelineShareData',  # 1.4分享到朋友圈
				],
			"share":{
				"link": url,
				"title": '7许未来',
				'desc': '国寿安保基金7周年献礼',
				"imgUrl": '{url}img/logo.jpg'.format(url=url[0: url.rfind('/') + 1])
			}
		} 

		conn = get_redis_connection()
		token = conn.get('access_token')

		if not token:
			params = {
				"grant_type":'client_credential',
				"appid":'wxa4d1e1b8e398da74',
				"secret":'2d40727f812daccfa6649b69fd79ba3c',
			}
			r = requests.get('https://api.weixin.qq.com/cgi-bin/token', params=params)
			if r.status_code != 200:
				return ErrorResponse(msg='获取access_token失败')
			token = r.json().get('access_token')
			conn.set('access_token', token, ex=2*60*60)
			token = conn.get('access_token')
		
		access_token = token.decode('utf-8')

		ticket = conn.get('ticket')

		if not ticket:
			params = {
				"access_token":access_token,
				"type":'jsapi'
			}
			q = requests.get('https://api.weixin.qq.com/cgi-bin/ticket/getticket', params=params)
			if q.status_code != 200:
				return ErrorResponse(msg='获取jsapi_ticket失败')
			print(q.json())
			ticket = q.json().get('ticket')
			conn.set('ticket', ticket, ex=2*60*60)
			ticket = conn.get('ticket')
		
		jsapi_ticket = ticket.decode('utf-8')

		sign_data = {
			"url": url,
			"timestamp": timestamp,
			"noncestr": noncestr,
			"jsapi_ticket": jsapi_ticket
		}

		temp = '&'.join(["{0}={1}".format(k, sign_data[k]) for k in sorted(sign_data)])
		
		data['signature'] = sha1(temp)

		return SuccessResponse(data=data, msg='获取成功')