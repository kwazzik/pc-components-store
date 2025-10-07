from django.test import TestCase
from catalog.forms import (
    EmployeeCreationForm,
    EmployeeNumberUpdateForm,
    ProductForm,
    ProductSearchForm,
    EmployeeSearchForm,
    BrandSearchForm,
    validate_employee_number,
)
from catalog.models import Brand, Category

class EmployeeNumberValidationTest(TestCase):
    def test_valid_employee_number(self):
        valid_number = "ABC12345"
        self.assertEqual(validate_employee_number(valid_number), valid_number)

    def test_invalid_length(self):
        with self.assertRaisesMessage(Exception, "Employee number must be exactly 8 characters"):
            validate_employee_number("ABC1234")

    def test_invalid_prefix_lowercase(self):
        with self.assertRaisesMessage(Exception, "First 3 characters must be uppercase letters"):
            validate_employee_number("abc12345")

    def test_invalid_prefix_nonalpha(self):
        with self.assertRaisesMessage(Exception, "First 3 characters must be uppercase letters"):
            validate_employee_number("A1C12345")

    def test_invalid_suffix_non_digit(self):
        with self.assertRaisesMessage(Exception, "Last 5 characters must be digits"):
            validate_employee_number("ABC12A45")


class EmployeeCreationFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {
            "username": "testuser",
            "password1": "StrongPass123",
            "password2": "StrongPass123",
            "employee_number": "ABC12345",
            "first_name": "John",
            "last_name": "Doe",
        }
        form = EmployeeCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_employee_number(self):
        form_data = {
            "username": "testuser",
            "password1": "StrongPass123",
            "password2": "StrongPass123",
            "employee_number": "abc12345",  # invalid
            "first_name": "John",
            "last_name": "Doe",
        }
        form = EmployeeCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("employee_number", form.errors)


class EmployeeNumberUpdateFormTest(TestCase):
    def test_form_valid_data(self):
        form_data = {"employee_number": "XYZ67890"}
        form = EmployeeNumberUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_employee_number(self):
        form_data = {"employee_number": "XYZ6789"}  # invalid length
        form = EmployeeNumberUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("employee_number", form.errors)


class ProductFormTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="Brand1")
        self.category = Category.objects.create(name="Category1")

    def test_form_valid(self):
        form_data = {
            "name": "Product1",
            "brand": self.brand.pk,
            "price": "100.00",
            "in_stock": True,
            "amount": 5,
            "category": self.category.pk,
            "managers": [],
        }
        form = ProductForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_form_invalid_missing_name(self):
        form_data = {
            "brand": self.brand.pk,
            "price": "100.00",
            "in_stock": True,
            "amount": 5,
            "category": self.category.pk,
            "managers": [],
        }
        form = ProductForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)


class SearchFormsTest(TestCase):
    def test_product_search_form(self):
        form = ProductSearchForm(data={"model": "RTX"})
        self.assertTrue(form.is_valid())

        form = ProductSearchForm(data={})
        self.assertTrue(form.is_valid())

    def test_employee_search_form(self):
        form = EmployeeSearchForm(data={"username": "john"})
        self.assertTrue(form.is_valid())

        form = EmployeeSearchForm(data={})
        self.assertTrue(form.is_valid())

    def test_brand_search_form(self):
        form = BrandSearchForm(data={"name": "Intel"})
        self.assertTrue(form.is_valid())

        form = BrandSearchForm(data={})
        self.assertTrue(form.is_valid())
