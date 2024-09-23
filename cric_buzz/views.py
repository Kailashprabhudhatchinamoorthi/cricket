from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import cric_profile_serializer
from .models import cric_profile

@api_view(['POST','PUT','GET','DELETE'])

def cric_userView(request):

        if request.method == 'GET':
            getcric_profileData=cric_profile.objects.all()
            seializeData=cric_profile_serializer(getcric_profileData, many=True)
            return Response(seializeData.data)
        
        elif request.method == 'POST':

            savecric_profileData = request.data
            seializeData=cric_profile_serializer(data=savecric_profileData)
            if seializeData.is_valid():
                seializeData.save()
                return Response(seializeData.data,status=status.HTTP_201_CREATED)
            
        elif request.method == 'PUT':

            data = request.data
            getDataById=cric_profile.objects.get(pk=data['id_new'])
            seializeData=cric_profile_serializer(getDataById,data=data,status=status.HTTP_202_ACCEPTED)
            if seializeData.is_valid():
                seializeData.save()
                return Response(seializeData.data)
        elif request.method =='DELETE':
            data = request.data
            getDataById=cric_profile.objects.get(pk=data['id_new'])
            getDataById.delete()
            return Response({"msg":"data has been deleted" +str(data['id_new'])},status=status.HTTP_204_NO_CONTENT)


# Create your views here.