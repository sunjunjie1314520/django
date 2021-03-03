import re
import json


def strHandle(jsonp):
    try:
        str_json = re.search("Data_netWorthTrend.*?(\\[.*?\\]).+?", jsonp, re.S).group(1)
        # return json.loads(str_json)[-1]
        return json.loads(str_json)
    except:
        raise ValueError('strHandle Invalid Input')