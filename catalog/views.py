from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Employee, Product, Brand
from .forms import (EmployeeCreationForm, ProductForm, EmployeeNumberUpdateForm,
                    ProductSearchForm, EmployeeSearchForm, BrandSearchForm)


@login_required
def index(request):
    """View function for the home page of the site."""

    num_employees = Employee.objects.count()
    num_products = Product.objects.count()
    num_brand = Brand.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_employees": num_employees,
        "num_products": num_products,
        "num_brands": num_brand,
        "num_visits": num_visits + 1,
    }

    return render(request, "catalog/index.html", context=context)


class BrandListView(LoginRequiredMixin, generic.ListView):
    model = Brand
    context_object_name = "brand_list"
    template_name = "catalog/brand_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BrandListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["search_form_brand"] = BrandSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Brand.objects.filter().order_by("id")
        form = BrandSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class BrandCreateView(LoginRequiredMixin, generic.CreateView):
    model = Brand
    fields = "__all__"
    success_url = reverse_lazy("catalog:brand-list")


class BrandUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Brand
    fields = "__all__"
    success_url = reverse_lazy("catalog:brand-list")


class BrandDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Brand
    success_url = reverse_lazy("catalog:brand-list")


class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name_param = self.request.GET.get("name")
        context["search_form_product"] = ProductSearchForm(
            initial={"name": name_param}
        )
        return context

    def get_queryset(self):
        queryset = Product.objects.all().order_by("id")
        form = ProductSearchForm(self.request.GET)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            if name:
                return queryset.filter(name__icontains=name)
        return queryset


class ProductDetailView(LoginRequiredMixin, generic.DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product-list")


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product-list")


class ProductDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product-list")


class EmployeeListView(LoginRequiredMixin, generic.ListView):
    model = Employee
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username")
        context["search_form_employee"] = EmployeeSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Employee.objects.all().order_by("id")
        form = EmployeeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__icontains=form.cleaned_data["username"]
            )
        return queryset


class EmployeeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Employee
    queryset = Employee.objects.all().prefetch_related("products__brand")


class EmployeeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Employee
    form_class = EmployeeCreationForm


class EmployeeNumberUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Employee
    form_class = EmployeeNumberUpdateForm
    success_url = reverse_lazy("catalog:employee-list")


class EmployeeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Employee
    success_url = reverse_lazy("")
