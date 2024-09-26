from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from .serializer import cric_profile_serializer
from .models import cric_profile

class Cric_userView(APIView):

    def get(self,request):
        getcric_profileData =cric_profile.objects.all()
        serializeData=cric_profile_serializer(getcric_profileData,many=True)
        return Response(serializeData.data)
    
    def post(self,request):
        data=request.data
        serializeData=cric_profile_serializer(data=data)
        if serializeData.is_valid():
            serializeData.save()
            return Response(serializeData.data, status=status.HTTP_201_CREATED)
        return Response(serializeData.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Cric_userMangaeView(APIView):
    
    def put(self,request,id):
        try:
            getDatabyId = cric_profile.objects.get(pk=id)
            serializeData=cric_profile_serializer(getDatabyId,data=request.data,partial=True)
            if serializeData.is_valid():
                serializeData.save()
                return Response(serializeData.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializeData.errors, status=status.HTTP_400_BAD_REQUEST)
        except cric_profile.DoesNotExist:
            return Response({"error": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,id):
        try:
            getDatabyId = cric_profile.objects.get(pk=id)
            getDatabyId.delete()
            return Response({"msg": f"Data has been deleted with ID:{id}"}, status=status.HTTP_204_NO_CONTENT)
        except cric_profile.DoesNotExist:
            return Response({"error": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)
