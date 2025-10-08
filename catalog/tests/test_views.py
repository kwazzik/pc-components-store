from django.test import TestCase, Client
from django.urls import reverse
from catalog.models import Employee, Brand, Product, Category
from django.contrib.auth import get_user_model

User = get_user_model()


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="pass1234",
            employee_number="ABC12345"
        )
        self.client.login(username="testuser", password="pass1234")

        self.brand = Brand.objects.create(name="Intel", country="USA")
        self.category = Category.objects.create(name="CPU")

        self.product1 = Product.objects.create(
            name="i7",
            brand=self.brand,
            price=300,
            category=self.category,
            in_stock=True,
            amount=10
        )
        self.product1.managers.add(self.user)

        self.product2 = Product.objects.create(
            name="i9",
            brand=self.brand,
            price=500,
            category=self.category,
            in_stock=False,
            amount=5
        )
        self.product2.managers.add(self.user)

    def test_index_view_counts_and_visits(self):
        response = self.client.get(reverse("catalog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("num_products", response.context)
        self.assertIn("num_employees", response.context)
        self.assertIn("num_brands", response.context)
        self.assertIn("num_visits", response.context)
        self.assertEqual(response.context["num_products"], 2)
        self.assertEqual(response.context["num_employees"], 1)
        self.assertEqual(response.context["num_brands"], 1)

        self.assertEqual(self.client.session["num_visits"], 1)

    def test_product_list_view_search(self):
        response = self.client.get(reverse("catalog:product-list"), {"name": "i9"})
        self.assertContains(response, "i9")
        self.assertNotContains(response, "i7")

    def test_brand_list_view_search(self):
        response = self.client.get(reverse("catalog:brand-list"), {"name": "Intel"})
        self.assertContains(response, "Intel")

    def test_employee_list_view_search(self):
        response = self.client.get(reverse("catalog:employee-list"), {"username": "test"})
        self.assertContains(response, "testuser")

    def test_employee_detail_view_prefetch(self):
        url = reverse("catalog:employee-detail", kwargs={"pk": self.user.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        products = response.context["employee"].products.all()
        with self.assertNumQueries(0):
            list(products)
