from rest_framework.generics import ListAPIView;
from rest_framework.response import Response;
from rest_framework.renderers import JSONRenderer;
from rest_framework.authentication import SessionAuthentication, BasicAuthentication;
from rest_framework.permissions import IsAuthenticated;
from timeline.models import TimelineEvent;
from .serializers import TimelineSerialzier;


class TimelineAPIView(ListAPIView):
    #renderer_classes = (JSONRenderer, );
    queryset = TimelineEvent.objects.all();
    serializer_class = TimelineSerialzier;
    authentication_classes = (SessionAuthentication, BasicAuthentication);
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        Data = {
            'events':TimelineEvent.objects.filter(slide_type__exact=''),
            'title':TimelineEvent.objects.filter(slide_type__exact='title').first()
        }
        Serialized = self.serializer_class(Data);
        return Response(Serialized.data);
