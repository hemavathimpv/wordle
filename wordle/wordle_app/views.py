import pandas as pd
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import WordleNames


class WordleNamesViews(APIView):
    def post(self,request):

        if request.data.get('file'):
            file = request.data.get('file')
            print(file.name.split('.')[-1])
            df = pd.read_csv(file,sep=" ",header=None)
            for i in range(len(df)):
                WordleNames.objects.create(name=df[0][i])
                return Response("created",status=status.HTTP_200_OK)

        else:
            name = request.data.get('name')
            """
            if entered name is in uppercase it will convert to lowercase
            """
            names = name.lower()

            if len(names) == 5:
                if WordleNames.objects.filter(name=names).exists():
                    raise ValueError("name already exists")
            else:
                raise ValueError("string should contain only 5 character")
            return Response("Done")

