from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serialilzer import TodoSerializer, TimingTodoSerializer
from .models import TODO, TimingTodo
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.paginator import Paginator
from .helpers import paginate

# Create your views here.
@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'message': "Success",
            'method_name': "GET Method"
        })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message': "Success",
            'method_name': "POST Method"
        })
    elif request.method == 'PATCH':
        return Response({
            'status': 200,
            'message': "Success",
            'method_name': "PATCH Method"
        })
    else:
        return Response({
            'status': 400,
            'message': "Error",
            'method_name': "Invalid Method"
        })


@api_view(['GET'])
def get_todo(request):
    todo_objs = TODO.objects.all()
    serializer = TodoSerializer(todo_objs, many=True)

    return Response({
        'status': True,
        'message': 'Todo fetched',
        'data': serializer.data
    })


@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': "Success",
                'data': serializer.data
            })

        return Response({
            'status': False,
            'message': "Error",
            'data': serializer.errors
        })
    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': "Error",
            'method_name': "Something went wrong"
        })


@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status': False,
                'message': "uid is  required!!",
                'data': {} 
            })
        
        obj = TODO.objects.get(uid = data.get('uid'))
        serializer = TodoSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Success',
                'data': serializer.data
            })

        return Response({
            'status': False,
            'message': "Error",
            'data': serializer.errors
        })
    except Exception as e:
        print(e)
        return Response({
            'status': False,
            'message': "Error",
            'method_name': "Something went wrong"
        })


class TodoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.user)
        todo_objs = TODO.objects.filter(user = request.user)
        page = request.GET.get('page', 2)
        page_obj = Paginator(todo_objs, page)
        results = paginate(todo_objs, page_obj, page)
        print(results)
        serializer = TodoSerializer(results['results'], many=True)

        return Response({
            'status': True,
            'message': 'Todo fetched',
            'data': {'data': serializer.data, 'pagination': results['pagination']}
        })
    
    def post(self, request):
        try:
            data = request.data
            data['user'] = request.user.id
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': "Success",
                    'data': serializer.data
                })

            return Response({
                'status': False,
                'message': "Error",
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': "Error",
                'method_name': "Something went wrong"
            })
    
    def patch(self, request):
        try:
            data = request.data
            if not data.get('uid'):
                return Response({
                    'status': False,
                    'message': "uid is  required!!",
                    'data': {} 
                })
        
            obj = TODO.objects.get(uid = data.get('uid'))
            serializer = TodoSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'Success',
                    'data': serializer.data
                })

            return Response({
                'status': False,
                'message': "Error",
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': "Error",
                'method_name': "Something went wrong"
            })


class TodoViewSet(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['GET'])
    def get_date_to_todo(self, request):
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs, many = True)
        return Response({
            'status': True,
            'message': 'Timing todo fetched',
            'data': serializer.data
        })

    @action(detail=False, methods=['post'])
    def add_date_to_todo(self, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                
                return Response({
                    'status': True,
                    'message': 'Success',
                    'data': serializer.data
                })

            return Response({
                'status': False,
                'message': "Error",
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': "Error",
                'method_name': "Something went wrong"
            })
