from django.shortcuts import render
from rest_framework import viewsets
from app1.models import Financialdata,Analytics
from app1.serializers import FinancialdataSerializer,AnalyticsSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,action

# Create your views here.


class FinancialdataView(viewsets.ModelViewSet):
    queryset = Financialdata.objects.all()
    serializer_class = FinancialdataSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    

    @action(detail=True,methods=['get'])
    def analytics(self,request,pk=None):
        try:
            financialdata = Financialdata.objects.get(pk=pk)
            ana = Analytics.objects.filter(financialdata=financialdata)
            analytics_serializer = AnalyticsSerializer(ana,many=True,context={'request':request})
            return Response(analytics_serializer.data)
        except Exception as e:
            return Response({
                'message':'acc_holder data not exist'
            })


@api_view(['POST'])
def user_logout(request):
    try:
        # Delete the user's token to logout
        request.user.auth_token.delete()
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AnalyticsView(viewsets.ModelViewSet):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



