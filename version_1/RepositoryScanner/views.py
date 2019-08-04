from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from RepositoryScanner.investigator import RepositoryInvestigator
import requests

# Create your views here.


class KeywordBasedInvestigation(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def post(self,request):
        try:
            data = JSONParser().parse(request)
            keyword = data["keyword"]
            response = RepositoryInvestigator(keyword=keyword)
            statusCode = response['status_code']
            content = response['json_response']
        except:
            statusCode = 444
            content = {"ErrorCode" : 444,
                        "ErrorMessage" : "POST_body - Suspicious activity found."
                        }
        return Response(status=statusCode, data= content)



class ListBasedInvestigation(APIView):
    def post(self,request):
        try:
            data = JSONParser().parse(request)
            key_list = data["key_list"]
        except:
            statusCode = 444
            content = {"ErrorCode" : 444,
                        "ErrorMessage" : "POST_body - Suspicious activity found."
                        }
        return Response(status=statusCode, data= content)
