from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='blah@blah.com', password='testpassword'):
    """Create a sample user """
    return get_user_model().objects.create_user(email=email, password=password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalizeed(self):
        """Test the email for a new user is normalized"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'test')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raised error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
            )
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Testing the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
          user=sample_user(),
          name='Cucumber',  
        )
        
        self.assertEqual(str(ingredient), ingredient.name)