# 【channels】（第4步）创建应用的消费者
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json


class AsyncConsumer(AsyncWebsocketConsumer):

    async def connect(self, *args, **kwargs):  # 连接时触发
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'notice_%s' % self.room_name  # 直接从用户指定的房间名称构造Channels组名称，不进行任何引用或转义。

        # 将新的连接加入到群组
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):  # 断开时触发
        # 将关闭的连接从群组中移除
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):  # 接收消息时触发
        text_data_json = json.loads(text_data)

        print(1, text_data_json)
        message = text_data_json['message']

        # 信息群发
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'system_message',
                'message': message
            }
        )

    # Receive message from room group
    async def system_message(self, event):
        print(2, event)
        message = event.get('message')

        # Send message to WebSocket单发消息
        data = {
            'message': message
        }
        await self.send(text_data=json.dumps(data, ensure_ascii=False))


def send_group_msg(room_name, message):
    # 从Channels的外部发送消息给Channel

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'notice_{room_name}',  # 构造Channels组名称
        {
            "type": "system_message",
            "message": message,
        }
    )
