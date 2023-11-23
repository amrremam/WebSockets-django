from channels.consumer import SyncConsumer


class EchoConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("connect event is called")
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("new event is received")
        print(event)

    def websocket_disconnect(self, event):
        print("connection is disconnected")
        print(event)
