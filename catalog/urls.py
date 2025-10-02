from django.urls import path

from .views import (
    index,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    EmployeeListView,
    EmployeeDetailView,
    EmployeeCreateView,
    EmployeeNumberUpdateView,
    EmployeeDeleteView,
    BrandListView,
    BrandCreateView,
    BrandUpdateView,
    BrandDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "brand/",
        BrandListView.as_view(),
        name="brand-list",
    ),
    path(
        "brand/create/",
        BrandCreateView.as_view(),
        name="brand-create",
    ),
    path(
        "brand/<int:pk>/update/",
        BrandUpdateView.as_view(),
        name="brand-update",
    ),
    path(
        "brand/<int:pk>/delete/",
        BrandDeleteView.as_view(),
        name="brand-delete",
    ),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("products/create/", ProductCreateView.as_view(), name="product-create"),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product-update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product-delete"),
    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path(
        "employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"
    ),
    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path(
        "employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"
    ),
    path("employees/create/", EmployeeCreateView.as_view(), name="employee-create"),
    path(
        "employees/<int:pk>/update/",
        EmployeeNumberUpdateView.as_view(),
        name="employee-number",
    ),
    path(
        "employees/<int:pk>/delete/",
        EmployeeDeleteView.as_view(),
        name="employee-delete",
    ),
]

app_name = "catalog"