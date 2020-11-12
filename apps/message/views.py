import requests

from rest_framework.views import APIView
from rest_framework.response import Response

from django_redis import get_redis_connection

from utils.Response import SuccessResponse, ErrorResponse, SerializerErrorResponse
from utils.Sms import SEND_SMS
from utils.Time import get_timestamp, NowTimeToUTC
from utils.Random import get_noncestr
from utils.Sign import sha1
from utils.Format import to_JSON_Format


from .serializer import SendSerializer, SmsSerializer, SignatureSerializer
from . import models
from . import tasks

################### Message 首页 #####################

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

		# result = SEND_SMS(phone)

		# result.send()

		# conn.set(result.phone, result.code, ex=5*60)

		conn.set(phone, 123456, ex=5 * 60)

		stamp = get_timestamp()
		conn.set('stamp_{phone}'.format(phone=phone), stamp, ex=expired)

		# return SuccessResponse(msg='发送成功', data=result.get_data())

		return SuccessResponse(msg='发送成功')


################### 表单提交 #####################

class SendView(APIView):
	def post(self, request, *argw, **kwargs):
		serializer = SendSerializer(data=request.data)
		if not serializer.is_valid():
			return SerializerErrorResponse(serializer)
		
		phone = serializer.validated_data.get('phone')
		result = models.Message.objects.filter(phone=phone).exists()

		conn = get_redis_connection()
		conn.delete(phone)

		if not result:
			serializer.save()
			return SuccessResponse(data=serializer.data, msg='保存成功')
		return ErrorResponse(code=2, msg='不能重复提交')


################### 公众号签名 #####################

class SignatureView(APIView):

	def post(self, request, *args, **kwargs):

		serializer = SignatureSerializer(data=request.data)
		if not serializer.is_valid():
			return SerializerErrorResponse(serializer)

		url = serializer.validated_data.get('url')

		timestamp = get_timestamp()
		noncestr = get_noncestr()

		appId = 'wxce983ca717e38e20'
		secret = 'f4ae9773db09eb9da16e7cda040443a0'

		data = {
			"debug": False,
			"appId": appId, # 必填，公众号的唯一标识
			"timestamp": timestamp, # 必填，生成签名的时间戳
			"nonceStr": noncestr, # 必填，生成签名的随机串
			"signature": '', # 必填，签名
			"jsApiList": [
				'updateAppMessageShareData',  # 1.4 分享到朋友
				'updateTimelineShareData',  # 1.4分享到朋友圈
				],
			"share":{
				"link": url,
				"title": '"7"许未来：送祝福 赢好礼',
				'desc': '国寿安保基金7岁啦！值此生日之际，诚邀您参与活动赢好礼。',
				"imgUrl": '{url}img/logo.jpg'.format(url=url[0: url.rfind('/') + 1])
			}
		} 

		conn = get_redis_connection()
		token = conn.get('access_token')

		if not token:
			params = {
				"grant_type": 'client_credential',
				"appid": appId,
				"secret": secret
			}
			r = requests.get('https://api.weixin.qq.com/cgi-bin/token', params=params)
			if r.status_code != 200:
				return ErrorResponse(msg='获取access_token失败')

			if 'errcode' in r.json().keys():
				return ErrorResponse(msg=r.json().get('errmsg'))

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
		data['access_token'] = access_token
		data['jsapi_ticket'] = jsapi_ticket

		return SuccessResponse(data=data, msg='获取成功')


class VisitHistoryView(APIView):

	def post(self, request, *args, **kwargs):
		if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取 ip
			client_ip = request.META['HTTP_X_FORWARDED_FOR']
			client_ip = client_ip.split(",")[0]  # 所以这里是真实的 ip
		else:
			client_ip = request.META['REMOTE_ADDR']  # 这里获得代理 ip
		print(client_ip)
		ip_exist = models.Visit.objects.filter(address=client_ip)
		if not ip_exist:
			models.Visit.objects.create(address=client_ip)
			return SuccessResponse(msg='记录成功')
		return ErrorResponse(msg='记录已存在')
