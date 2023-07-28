from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config['JSON_AS_ASCII'] = False

class test(Resource):
    def get(self):
        return {
	"YouTubeBigBoxs": [{
			"image": "https: //i.ytimg.com/vi/3yluDg_GnfE/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB-NoAzWEK-9CdzznuxAmXv6r0Vdw",
			"lengthTime": "9: 33",
			"title": "아침을 시작하는 5분 명상 | 아침명상, 아침 스트레칭",
			"channelName": "에일린 mind yoga"
		},
		{
			"image": "https: //i.E/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB-NoAzWEK-9CdzznuxAmXv6r0Vdw",
			"lengthTime": "9: 33",
			"title": "2아침을 시작하는 5분 명상 | 아침명상, 아침 스트레칭",
			"channelName": "에일린 mind yoga"
		},
		{
			"image": "https: //i.ytimg.com/vi/3yluDg_GnfE/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB-NoAzWEK-9CdzznuxAmXv6r0Vdw",
			"lengthTime": "9: 33",
			"title": "3아침을 시작하는 5분 명상 | 아침명상, 아침 스트레칭",
			"channelName": "에일린 mind yoga"
		},
		{
			"image": "https: //i.ytimg.com/vi/3yluDg_GnfE/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB-NoAzWEK-9CdzznuxAmXv6r0Vdw",
			"lengthTime": "9: 33",
			"title": "4아침을 시작하는 5분 명상 | 아침명상, 아침 스트레칭",
			"channelName": "에일린 mind yoga"
		}
	]

}
        
api.add_resource(test, '/test')
app.run(host='0.0.0.0', debug=False)
