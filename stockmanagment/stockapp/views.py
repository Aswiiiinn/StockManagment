from django.shortcuts import render,redirect
from .models import Stocks
from .forms import Stockforms,searchform
from django.views import View
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin

class RegisterView(View):
    def get(self, request):
        return render(request,'register.html')
    def post(self,request):
        if request.method == "POST":
            user = request.POST.get("username")
            password = request.POST.get("password")
    
            if User.objects.filter(username =user).exists():
                return render(request,'register.html',{'error':'username already exists'})

            user =User.objects.create_user(username =user,password = password)
            user.save()
            login(request,user)
            return redirect('list_view')
        # return render(request,'register.html')
       
class LoginView(View):
    def get(self, request):
        return render(request,'login.html')
    def post(self, request):
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches
        username = request.POST.get("username")
        password = request.POST.get("password")
        userr =authenticate(request , username=username,password=password)
        if userr is not None:
            login(request,userr)
            return redirect('list_view')  
        else:
            return render(request,'login.html')  
class logoutView(LoginRequiredMixin,View):
    login_url = ''
    def get(self, request):
        logout(request)
        return redirect('login_view')

class ListView(LoginRequiredMixin,View):
    login_url = ''

    def get(self,request):
        form = Stocks.objects.all()
        item = searchform(request.POST or None)
        context = {'form': form, 'item': item}
        if request.method=='POST':
            form =Stocks.objects.filter(catagory_icontains =item['categories'].value(),item_name = item['item_name'].value())
            context = {'form': form, 'item': item}
        return render(request,'home.html',context)
class AddView(LoginRequiredMixin,View):
    login_url = ''
    def get(self,request):
        form = Stocks.objects.all()
        return render(request,'add.html',{'form':form})
    def post(self,request):
        form = Stockforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_view')

        return render(request,'add.html',{'form':form})
class updateView(LoginRequiredMixin,View):
    # permission_required = 'stockapp.add_stocks'
    login_url = ''
    def get(self,request,pk):
        stock = Stocks.objects.get(id=pk)
        form = Stockforms(instance=stock)
        return render(request,'update.html',{'form':form})
    def post(self,request,pk):
        stock = Stocks.objects.get(id=pk)
        form = Stockforms(request.POST,instance=stock) 
        if form.is_valid():
            form.save()
            return redirect('list_view')
        return render(request,'update.html',{'form':form})
class delete(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'stockapp.delete_stocks'
    login_url =''
    def get(self, request, pk):
        # Fetch the stock object with the given primary key
        stock = Stocks.objects.get(id=pk)
        return render(request, 'delete.html', {'stock': stock})

    def post(self, request, pk):
        # Fetch the stock object with the given primary key
        stock = Stocks.objects.get(id=pk)
        # Delete the stock object
        stock.delete()
        # Redirect the user to the list view after deletion
        return redirect('list_view')
