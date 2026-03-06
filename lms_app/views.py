from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.shortcuts import render
#from django.views.decorators.csrf import @csrf_exempt

#def add_book(request):
def home(request):
 return render(request, 'home.html')
# Create your views here.
#from django.shortcuts import render,redirect
#from .models import Book
#@csrf_exempt
def add_book(request):
    if request.method=="POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        qty=request.POST.get('quantity')

        Book.objects.create(
            title=title,
            author=author,
            quantity=qty
        )
        return redirect('books')
        return Response({'message':"Book added Successfully"})
    return render(request,'add_book.html')

def books(request):
    query = request.GET.get('q')

    if query:
        data = Book.objects.filter(title__icontains=query)
    else:
        data = Book.objects.all()

    return render(request,'books.html',{'books':data})


#ef books(request):
 #   data=Book.objects.all()
  #  return render(request,'books.html',{'books':data})

#def delete_book(request,id):

def edit_book(request,id):
     book = Book.objects.get(id=id)

     if request.method == "POST":
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.quantity = request.POST['quantity']
        book.save()
        return redirect('books')

     return render(request,'edit_book.html',{'book':book})

@api_view(['GET','POST','PUT','DELETE'])
def api_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


# GET all books + POST new book


    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



# GET single + UPDATE + DELETE
@api_view(['GET','PUT','DELETE'])
def api_book_detail(request,id):

    book = Book.objects.filter(id=id).first()

    if not book:
        return Response({"error":"Book not found"}, status=404)


    # GET single
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)


    # PUT update
    if request.method == 'PUT':
        serializer = BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)


    # DELETE
    if request.method == 'DELETE':
        book.delete()
        return Response({"message":"Deleted successfully"})
@api_view(['GET','POST'])
def api_add_book(request):

    # ---------- GET ----------
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    # ---------- POST ----------
    elif request.method == "POST":
        title = request.data.get('title')
        author = request.data.get('author')
        qty = request.data.get('quantity')

        book = Book.objects.create(
            title=title,
            author=author,
            quantity=qty
        )

        return Response({
            "message": "Book added successfully",
            "id": book.id
        })


@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=400)

    user = User.objects.create_user(
        username=username,
        password=password
    )
    return Response({"message":"User created successfully"})
def login_page(request):
    return render(request, 'login.html')
