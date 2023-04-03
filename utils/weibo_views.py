class WeiBoLoginAPIView(APIView):
    def get(self, request, *args, **kwargs):
        auth_url = get_auth_url()
        data = {
            "url": auth_url
        }
        print(auth_url)
        return CCAIResponse(data, status=OK)


class WeiBoCompleteAPIView(APIView):
    def get(self, request, *args, **kwargs):
        auth_url = get_auth_url()
        data = {
            "url": auth_url
        }
        print(auth_url)
        return CCAIResponse(data, status=OK)
