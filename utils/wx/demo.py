from utils.wx.WXBizDataCrypt import WXBizDataCrypt, get_session_key


def decode_info(iv, encryptedData, appId, sessionKey):
    # appId = 'wx4f4bc4dec97d474b'
    # sessionKey = 'tiihtNczf5v6AKRyjwEUhQ=='
    # encryptedData = 'CiyLU1Aw2KjvrjMdj8YKliAjtP4gsMZMQmRzooG2xrDcvSnxIMXFufNstNGTyaGS9uT5geRa0W4oTOb1WT7fJlAC+oNPdbB+3hVbJSRgv+4lGOETKUQz6OYStslQ142dNCuabNPGBzlooOmB231qMM85d2/fV6ChevvXvQP8Hkue1poOFtnEtpyxVLW1zAo6/1Xx1COxFvrc2d7UL/lmHInNlxuacJXwu0fjpXfz/YqYzBIBzD6WUfTIF9GRHpOn/Hz7saL8xz+W//FRAUid1OksQaQx4CMs8LOddcQhULW4ucetDf96JcR3g0gfRK4PC7E/r7Z6xNrXd2UIeorGj5Ef7b1pJAYB6Y5anaHqZ9J6nKEBvB4DnNLIVWSgARns/8wR2SiRS7MNACwTyrGvt9ts8p12PKFdlqYTopNHR1Vf7XjfhQlVsAJdNiKdYmYVoKlaRv85IfVunYzO0IKXsyl7JCUjCpoG20f0a04COwfneQAGGwd5oa+T8yO5hzuyDb/XcxxmK01EpqOyuxINew=='
    # iv = 'r7BXXKkLb8qrSNn05n0qiA=='

    pc = WXBizDataCrypt(appId, sessionKey)

    print(pc.decrypt(encryptedData, iv))
    # {'phoneNumber': '17875513387', 'purePhoneNumber': '17875513387', 'countryCode': '86', 'watermark': {'timestamp': 1632971199, 'appid': 'wxa100b18ea46591d8'}}


if __name__ == '__main__':
    appid = "wxa100b18ea46591d8"
    secret = "7dcd8ba894530a580cd8c58ae3ad24e8"

    code = "061nQj000UBsvM1Kq30004v9xo4nQj0e"
    # response_dict = get_session_key(code, appid, secret)
    # print(response_dict["session_key"], response_dict["openid"])
    session_key = r"NZd5PocJMD4\/cSKyxT56yQ=="

    phone_iv = "v1fl8B9Klse1Eu2Eap8nEg=="
    phone_encryptedData = "4QExEXfeLglb3jNEqrtA8PVbr4F2lTS3qoR07EQobA2yG+3HHm8TlPYxLA3ehUxYEiRgXl6+JA1Afw2M/djum7sD6XYziWnnyZW2S+0776oEPNR+n4ZROq+ZvpjUDQLTJEsMiFn4LzGNoOSyUJpO0T+q0bsPxTT50xfiU9wcUhbm86M/IwcyUT6VEGc7xMi5Q5QUe2KSqdiyF4MA+Ujs7w=="

    decode_info(phone_iv, phone_encryptedData, appid, session_key)
