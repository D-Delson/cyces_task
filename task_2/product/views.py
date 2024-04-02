from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Product,Category, SubCategory 
from .config import PAGINATION_LIMIT

class ProductListView(ListView):
    model = Product
    template_name = 'product.html'
    paginate_by = PAGINATION_LIMIT

class ProductCreateView(CreateView):
    model = Product
    fields = [ 'name', 'price', 'category', 'subcategory']
    template_name = 'product_add.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'category', 'subcategory']
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class CategoryListView(ListView):
    model = Category
    template_name = 'category.html'
    paginate_by = PAGINATION_LIMIT

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'subcategory']
    template_name = 'category_add.html'
    success_url = reverse_lazy('category_list')
 
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'subcategory']
    template_name = 'category_update.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
class SubCategoryListView(ListView):
    model = SubCategory
    template_name = 'subcategory.html'
    paginate_by = PAGINATION_LIMIT

class SubCategoryCreateView(CreateView):
    model = SubCategory
    fields = ['name']
    template_name = 'subcategory_add.html'
    success_url = reverse_lazy('subcategory_list')

class SubCategoryUpdateView(UpdateView):
    model = SubCategory
    fields = ['name']
    template_name = 'subcategory_update.html'
    success_url = reverse_lazy('subcategory_list')

class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    success_url = reverse_lazy('subcategory_list')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

# def product_list(request):
#     form = Product.objects.all()
#     context = {'form': form}
#     return render(request, 'product.html', context)
    
# def product_add(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         form.save()
#         return redirect('product_list')
#     else:
#         form = ProductForm()
#         context = {'form': form}
#     return render(request, 'product_add.html', context)
    
# def product_update(request, i):
#     u = Product.objects.get(pk = i)
#     if request.method == 'POST':
#         new_data = ProductForm(request.POST, instance=u)
#         new_data.save()
#         return redirect('product_list')
#     else: 
#         form = ProductForm(instance=u)
#         context = {'form':form}
#     return render(request, 'product_update.html', context)

# def product_delete(request,i):
#     o = Product.objects.get(pk = i)
#     o.delete()
#     return redirect('product_list')

# def category_list(request):
#     c_list = Category.objects.all()
#     context = {'category': c_list}
#     return render(request, 'category.html', context)
    
# def category_add(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         form.save()
#         return redirect('category_list')
#     else:
#         form = CategoryForm()
#         context = {'form':form}
#     return render(request, 'category_add.html', context=context)

# def category_update(request, i):
#     u = Category.objects.get(pk=i)
#     if request.method == 'POST':
#         new_data = CategoryForm(request.POST, instance=u)
#         new_data.save()
#         return redirect('category_list')
#     else:
#         form = CategoryForm(instance=u)
#         context = {'form': form}
#     return render(request, 'category_update.html', context)

# def category_delete(request, i):
#     o = Category.objects.get(pk= i)
#     o.delete()
#     return redirect('category_list')

# def subcategory_list(request):
#     s_list = SubCategory.objects.all()
#     context = {'s_list':s_list}
#     return render(request, 'subcategory.html', context=context)

# def subcategory_add(request):
#     if request.method == 'POST':
#         form = SubCategoryForm(request.POST)
#         form.save()
#         return redirect('subcategory_list')
#     else:
#         form = SubCategoryForm()
#         context = {'form':form}
#     return render(request, 'subcategory_add.html', context)

# def subcategory_update(request, i):
#     u = SubCategory.objects.get(pk=i)
#     if request.method == "POST":
#         new_data = SubCategoryForm(request.POST, instance=u)
#         new_data.save()
#         return redirect('subcategory_list')
#     else:
#         form = SubCategoryForm(instance=u)
#         context = {'form':form}
#     return render(request, 'subcategory_update.html', context)
    
# def subcategory_delete(request, i):
#     o = SubCategory.objects.get(pk=i)
#     o.delete()
#     return redirect('subcategory_list')