from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Employee, Product, Brand


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("employee_number",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("employee_number",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "employee_number",
                    )
                },
            ),
        )
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("brand",)


admin.site.register(Brand)
