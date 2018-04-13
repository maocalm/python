import  base64

coupon = {
    'id': '1231',
    'goods': '0001'
}

def gen_coupon(id,goods):
    coupon['id']=id
    coupon['goods']=goods
    raw ='/'.join([k + ':' + v for k ,v in coupon.items()])
    raw_64 = base64.urlsafe_b64decode(raw.encode('utf-8'))
    c_code =raw_64.decode()
    return c_code

