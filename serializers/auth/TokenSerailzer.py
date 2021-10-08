from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Here we will add custom claims
class MyTokeObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token =  super(MyTokeObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email

        return token