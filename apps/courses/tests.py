from django.test import TestCase
from .models import Category, Course, Module, Enrollment
from django.urls import reverse

class CategoryTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_category(self):
        pass

    def test_create_duplicate_category(self):
        pass

    def test_auto_create_slug(self):
        pass

    def test_get_categories(self):
        pass

    def test_get_category(self):
        pass


class CourseTestCase(TestCase):
    def setUp(self):
        pass

    def test_delete_author_course_stays(self):
        pass


    def test_deleted_category_course_stays(self):
        pass

    def test_create_course(self):
        pass

    def test_delete_course(self):
        """ 
        Only author can delete course.
        If course is deleted, then all modules are deleted.
        """
        pass

    def test_create_course_with_duplicate_name(self):
        pass

    def test_get_courses_from_category(self):
        pass

    def test_get_courses(self):
        pass

    def test_get_course(self):
        pass

    def test_auto_create_slug(self):
        """Slug is generated from title on creation."""
        pass

    def test_slug_not_updated_on_title_change(self):
        """Changing title does not regenerate slug."""
        pass

class ModuleTestCase(TestCase):
    def test_create_course_modules(self):
        pass

    def test_get_course_modules(self):
        pass

    def test_unique_order_per_course(self):
        """Two modules in same course cannot have same order."""
        pass

    def test_same_order_different_courses(self):
        """Two modules in different courses can have same order."""
        pass

class EnrollmentTestCase(TestCase):
    def test_create_enrollment(self):
        pass

    def test_enroll(self):
        pass

    def test_unenroll(self):
        pass

    def test_enrolled_user_can_access_lesson(self):
        pass

    def test_unenrolled_user_cannot_access_lesson(self):
        pass

    def test_duplicate_enrolls(self):
        pass

    def test_duplicate_unenrolls(self):
        pass