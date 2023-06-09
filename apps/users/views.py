from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


from apps.users.models import User
from apps.users.serializers import UserSerializer, UserDetailSerializer, RegisterSerializer


# Create your views here.
class UserAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserDetailSerializer, )
 

    def get_serializer_class(self):
        if self.action in ('create', ):
            return RegisterSerializer
        if self.action in ('retrieve', ):
            return UserDetailSerializer
        return UserSerializer
    
