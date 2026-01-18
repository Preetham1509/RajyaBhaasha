from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

def home(request):
    return render(request, 'home.html')

@api_view(['GET'])
def get_users(request):
    users=User.objects.all()
    serializers=UserSerializer(users, many=True)
    return Response(serializers.data)
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# BOOTSTRAP UI VIEWS


def user_list_ui(request):
    query = request.GET.get('q')   # get search text

    if query:
        users = User.objects.filter(name__icontains=query)
    else:
        users = User.objects.all()

    return render(request, 'user_list.html', {
        'users': users,
        'query': query
    })


def add_user_ui(request):
    if request.method == 'POST':
        User.objects.create(
            name=request.POST['name'],
            age=request.POST['age']
        )
        return redirect('user_list_ui')

    return render(request, 'user_form.html')


def edit_user_ui(request, pk):
    user = User.objects.get(pk=pk)

    if request.method == 'POST':
        user.name = request.POST['name']
        user.age = request.POST['age']
        user.save()
        return redirect('user_list_ui')

    return render(request, 'user_form.html', {'user': user})


def delete_user_ui(request, pk):
    User.objects.get(pk=pk).delete()
    return redirect('user_list_ui')



