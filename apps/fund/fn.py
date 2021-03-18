import re
import json

def loads_jsonp(jsonp):
    """
        解析jsonp数据格式为json
        :return:
        """
    try:
        return json.loads(re.match(".*?({.*}).*", jsonp, re.S).group(1))
    except:
        raise ValueError('Invalid Input')


def strHandle(jsonp):
    try:
        str_json = re.search("Data_netWorthTrend.*?(\\[.*?\\]).+?", jsonp, re.S).group(1)
        # return json.loads(str_json)[-1]
        return json.loads(str_json)
    except:
        raise ValueError('strHandle Invalid Input')
