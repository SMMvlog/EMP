from .models import Emp
from .serializers import EmpSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class Empview(viewsets.ModelViewSet):
    
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]