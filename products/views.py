from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from profiles.models import UserProfile
from .models import Product, Category, Brand
from .forms import ProductForm, CategoryForm, BrandForm


def all_products(request):
    """ A view to show all products, includingsorting and search queries """

    brands = Brand.objects.all()
    products = Product.objects.all()
    paginator = Paginator(products, 12)    # show 12 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    selected_category = None
    selected_brand = None
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if sortkey == 'brand':
                sortkey = 'brand__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "desc":
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            paginator = Paginator(products, 12)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            selected_category = request.GET['category']
            products = products.filter(category__name__in=categories)
            paginator = Paginator(products, 12)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            selected_brand = request.GET['brand']
            products = products.filter(brand__name__in=brands)
            page_number = request.GET.get('page')
            paginator = Paginator(products, 12)
            page_obj = paginator.get_page(page_number)
            brands = Brand.objects.filter(name__in=brands)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any\
                    search criteria!")
                return redirect(reverse('products'))

            query_name = Q(name__icontains=query)
            query_description = Q(description__icontains=query)
            
            queries = query_name | query_description
            products = products.filter(queries)
            paginator = Paginator(products, 12)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_brands': brands,
        'current_sorting': current_sorting,
        'page_obj': page_obj,
        'selected_category': selected_category,
        'selected_brand': selected_brand,
        'sort': sort,
        'direction': direction,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view that shows the individual product information """

    product = get_object_or_404(Product, pk=product_id)
    in_wishlist = False
    if product.users_wishlist.filter(id=request.user.id).exists():
        in_wishlist = True
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'in_wishlist': in_wishlist,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully Added new product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product,\
                Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated Product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.\
                Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product Deleted!')
    return redirect(reverse('products'))


@login_required
def add_brand(request):
    """ Add a brand to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Added new brand!')
            return redirect(reverse('add_brand'))
        else:
            messages.error(request, 'Failed to add brand,\
                Please ensure the form is valid.')
    else:
        form = BrandForm()

    template = 'products/add_brand.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_brand(request, brand_id):
    """ Edit a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    brand = get_object_or_404(Brand, pk=brand_id)
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated Brand!')
            return redirect(reverse('admin_controls'))
        else:
            messages.error(request, 'Failed to update brand.\
                Please ensure the form is valid.')
    else:
        form = BrandForm(instance=brand)
        messages.info(request, f'You are editing {brand.friendly_name}')

    template = 'products/edit_brand.html'
    context = {
        'form': form,
        'brand': brand,
    }

    return render(request, template, context)


@login_required
def delete_brand(request, brand_id):
    """ Delete a brand from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    brand = get_object_or_404(Brand, pk=brand_id)
    brand.delete()
    messages.success(request, 'Brand Deleted!')
    return redirect(reverse('admin_controls'))


@login_required
def add_category(request):
    """ Add a category to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Added new catrgory!')
            return redirect(reverse('add_category'))
        else:
            messages.error(request, 'Failed to add category,\
                Please ensure the form is valid.')
    else:
        form = CategoryForm()

    template = 'products/add_category.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_category(request, category_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    """ Edit a product to the store """
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated Category!')
            return redirect(reverse('admin_controls'))
        else:
            messages.error(request, 'Failed to update category.\
                Please ensure the form is valid.')
    else:
        form = CategoryForm(instance=category)
        messages.info(request, f'You are editing {category.friendly_name}')

    template = 'products/edit_category.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


@login_required
def delete_category(request, category_id):
    """ Delete a category from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, 'Category Deleted!')
    return redirect(reverse('admin_controls'))
