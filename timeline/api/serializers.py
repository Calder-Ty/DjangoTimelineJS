'''
Serializers for the Timeline Models. The Data Needed is specified
at: https://timeline.knightlab.com/docs/json-format.html#json-media
'''
from rest_framework import serializers
from timeline.models import TimelineEvent, Background
from datetime import datetime


class BackgroundSerializer(serializers.ModelSerializer):
    '''Serialzies the Background Data'''
    class Meta:
        model = Background;
        fields = (
            'url',
            'color'
            )


class DateSerializer(serializers.Serializer):
    '''Serializer for start_dates'''
    
    year = serializers.SerializerMethodField();
    month = serializers.SerializerMethodField(required=False, allow_null=True);
    day = serializers.SerializerMethodField(required=False, allow_null=True);
    # hour = serializers.SerializerMethodField(required=False, allow_null=True);
    # minute = serializers.SerializerMethodField(required=False, allow_null=True);
    # second = serializers.SerializerMethodField(required=False, allow_null=True);
    # millisecond = serializers.SerializerMethodField(required=False, allow_null=True);
    # display_date = serializers.CharField(max_length=75,required=False, allow_blank=True)
    
    def get_year(self, obj):
        return obj.year;

    def get_month(self, obj):
        return obj.month;
        
    def get_day(self, obj):
        return obj.day;

    def get_hour(self, obj):
        return obj.hour;

    def get_minute(self, obj):
        return obj.minute;

    def get_second(self, obj):
        return obj.second;

    def get_millisecond(self, obj):
        return obj.millisecond;


class EraSerializer(serializers.Serializer):
    pass


class MediaSerializer(serializers.Serializer):
    url = serializers.URLField(source="media");
    caption = serializers.CharField(source="media_caption",max_length=140, required=False, allow_blank=True);
    credit = serializers.CharField(source="media_creidt",max_length=75, required=False, allow_blank=True);
    thumbnail = serializers.URLField(source="media_thumbnail",required=False, allow_null=True);


class TextSerializer(serializers.Serializer):
    headline = serializers.CharField(max_length=75);
    text = serializers.CharField(required=False, allow_blank=True);


class SlideSerializer(serializers.Serializer):
    start_date = DateSerializer();
    end_date = DateSerializer();
    text = TextSerializer(required=False, allow_null=True, source ="*");
    media = MediaSerializer(required=False, allow_null=True, source ="*");
    group = serializers.CharField(max_length=75, required=False, allow_blank=True);
    display_date = serializers.CharField(max_length=75, required=False, allow_blank=True);
    background = BackgroundSerializer(required=False, allow_null=True);


class TitleSerializer(SlideSerializer):
    start_date = DateSerializer(required=False, allow_null=True);
    end_date = DateSerializer(required=False, allow_null=True);


class TimelineSerialzier(serializers.Serializer):
    events = SlideSerializer(many=True);
    title = TitleSerializer(required=False);
    eras = EraSerializer(required=False)
    # Hardcoding Scale to be "Human" for now
    scale = 'human'
