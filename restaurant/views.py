from rest_framework import viewsets,permissions
from django.contrib.auth.models import User  # Import the correct User model
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from .models import MenuItem,Menu,Booking
from rest_framework import generics
from .serializers import MenuItemSerializer,BookingSerializer
from rest_framework.authtoken.models import Token

    


# Create your views here. 
# @api_view['GET','POST']
class MenuItemsView(generics.ListCreateAPIView):
 queryset = Menu.objects.all()
 serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
 queryset = Menu.objects.all()
 serializer_class = MenuItemSerializer
 
class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

   def get_queryset(self):
        user = self.request.user
        token = Token.objects.get(user=user)
        return Token.objects.filter(user=user)