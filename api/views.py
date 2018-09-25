from django.http import HttpResponse, JsonResponse
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json

from api.models import Post, RoadData
# Create your views here.

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #이부분에서 Creating a ModelSerializer without either the 'fields' attribute or the 'exclude' attribute has been deprecated since 3.3.0 에러남 그래서 아래 추가
        fields = '__all__'

class RoadDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadData
        #이부분에서 Creating a ModelSerializer without either the 'fields' attribute or the 'exclude' attribute has been deprecated since 3.3.0 에러남 그래서 아래 추가
        fields = '__all__'

class get_all_post(GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class push_post(GenericAPIView, mixins.ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        Post.objects.create(title='테스트1', content='테스트 내용 1')
        return self.list(request, *args, **kwargs)

    def post(self, request):
        if request.method == "POST":
            request_data = ((request.body).decode('utf-8'))
            request_data = json.loads(request_data)
            content = request_data['content']
            return HttpResponse(content)

class get_all_road_data(GenericAPIView, mixins.ListModelMixin):
    queryset = RoadData.objects.all()
    serializer_class = RoadDataSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class get_road_data(GenericAPIView, mixins.ListModelMixin):
    queryset = RoadData.objects.all()
    serializer_class = RoadDataSerializer

    def get(self, request, *args, **kwargs):
        from django.core import serializers

        from_date = request.GET.get('from')
        to_date = request.GET.get('to')
        start_id = request.GET.get('start_id')
        end_id = request.GET.get('end_id')

        result = RoadData.objects.filter(date__range=(from_date, to_date), start_id=start_id, end_id=end_id)
        #return self.list(request, *args, **kwargs)
        #return HttpResponse(result.values())
        json_data = serializers.serialize('json', list(result), fields = '__all__')
        return HttpResponse(json_data, content_type="application/json")

@api_view(['GET', 'POST'])
def test_post(request, format=None):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def save_road_data(request, format=None):
    if request.method == 'POST':
        serializer = RoadDataSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)