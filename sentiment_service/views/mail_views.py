from ..models import Mail
from ..serializers import MailSerializer
from rest_framework import generics


class MailList(generics.ListCreateAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer


class MailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
