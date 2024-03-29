from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product,Category, SubCategory 
from .forms import ProductForm, CategoryForm, SubCategoryForm

def product_list(request):
    form = Product.objects.all()
    context = {'form': form}
    return render(request, 'product.html', context)

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        form.save()
        return redirect('product_list')
    else:
        form = ProductForm()
        context = {'form': form}
    return render(request, 'product_add.html', context)

def product_update(request, i):
    u = Product.objects.get(pk = i)
    if request.method == 'POST':
        new_data = ProductForm(request.POST, instance=u)
        new_data.save()
        return redirect('product_list')
    else: 
        form = ProductForm(instance=u)
        context = {'form':form}
    return render(request, 'product_update.html', context)

def product_delete(request,i):
    o = Product.objects.get(pk = i)
    o.delete()
    return redirect('product_list')

def category_list(request):
    c_list = Category.objects.all()
    context = {'category': c_list}
    return render(request, 'category.html', context)

def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        form.save()
        return redirect('category_list')
    else:
        form = CategoryForm()
        context = {'form':form}
    return render(request, 'category_add.html', context=context)

def category_update(request, i):
    u = Category.objects.get(pk=i)
    if request.method == 'POST':
        new_data = CategoryForm(request.POST, instance=u)
        new_data.save()
        return redirect('category_list')
    else:
        form = CategoryForm(instance=u)
        context = {'form': form}
    return render(request, 'category_update.html', context)

def category_delete(request, i):
    o = Category.objects.get(pk= i)
    o.delete()
    return redirect('category_list')

def subcategory_list(request):
    s_list = SubCategory.objects.all()
    context = {'s_list':s_list}
    return render(request, 'subcategory.html', context=context)

def subcategory_add(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        form.save()
        return redirect('subcategory_list')
    else:
        form = SubCategoryForm()
        context = {'form':form}
    return render(request, 'subcategory_add.html', context)

def subcategory_update(request, i):
    u = SubCategory.objects.get(pk=i)
    if request.method == "POST":
        new_data = SubCategoryForm(request.POST, instance=u)
        new_data.save()
        return redirect('subcategory_list')
    else:
        form = SubCategoryForm(instance=u)
        context = {'form':form}
    return render(request, 'subcategory_update.html', context)

def subcategory_delete(request, i):
    o = SubCategory.objects.get(pk=i)
    o.delete()
    return redirect('subcategory_list')