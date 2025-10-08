from django.test import TestCase
from django.urls import reverse
from catalog.models import Brand, Category, Employee, Product

class BrandModelTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="TestBrand", country="USA")

    def test_str_method(self):
        self.assertEqual(str(self.brand), "TestBrand")

    def test_brand_ordering(self):
        brand2 = Brand.objects.create(name="AnotherBrand")
        brands = list(Brand.objects.all())
        self.assertEqual(brands, sorted(brands, key=lambda b: b.name))


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="TestCategory")

    def test_str_method(self):
        self.assertEqual(str(self.category), "TestCategory")

    def test_category_ordering(self):
        cat2 = Category.objects.create(name="AnotherCategory")
        categories = list(Category.objects.all())
        self.assertEqual(categories, sorted(categories, key=lambda c: c.name))


class EmployeeModelTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="EmployeeBrand")
        self.employee = Employee.objects.create_user(
            username="testuser",
            password="password123",
            employee_number="EMP001",
            brand=self.brand,
            first_name="John",
            last_name="Doe"
        )

    def test_str_method(self):
        self.assertEqual(str(self.employee), "testuser (John Doe)")

    def test_get_absolute_url(self):
        url = reverse("catalog:employee-detail", kwargs={"pk": self.employee.pk})
        self.assertEqual(self.employee.get_absolute_url(), url)


class ProductModelTest(TestCase):
    def setUp(self):
        self.brand = Brand.objects.create(name="ProductBrand")
        self.category = Category.objects.create(name="ProductCategory")
        self.employee = Employee.objects.create_user(
            username="manager",
            password="password123",
            employee_number="EMP002"
        )
        self.product = Product.objects.create(
            name="TestProduct",
            brand=self.brand,
            price=99.99,
            in_stock=True,
            amount=10,
            category=self.category
        )
        self.product.managers.add(self.employee)

    def test_str_method(self):
        self.assertEqual(str(self.product), "TestProduct")

    def test_product_relations(self):
        self.assertEqual(self.product.brand, self.brand)
        self.assertEqual(self.product.category, self.category)
        self.assertIn(self.employee, self.product.managers.all())

    def test_default_values(self):
        product2 = Product.objects.create(
            name="TestProduct2",
            brand=self.brand,
            price=50,
            category=self.category
        )
        self.assertFalse(product2.in_stock)
        self.assertEqual(product2.amount, 0)
