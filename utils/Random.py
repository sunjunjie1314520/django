from random import choice

def get_noncestr(length = 32):
        """
        生成32位随机字符串
        :return:
        """
        seeds = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        random_str = []
        for i in range(length):
            random_str.append(choice(seeds))
        return ''.join(random_str)

def generate_trade_no(length = 28):
        """
        生成28位订单号
        :return:
        """
        seeds = '0123456789'
        random_str = []
        for i in range(length):
            random_str.append(choice(seeds))
        return ''.join(random_str)

if __name__ == "__main__":
    _str = generate_trade_no()
    print(_str)