from django.test import TestCase
from django.utils import timezone

from .models import Course, Step
# Create your tests here.

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
        title="Python Regular Expressions",
        description = "Learn to write regular expressions in Python",
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)

class StepModelTests(TestCase):
    def test_step_creation(self):
        step = Step.objects.create(
        title="Step n°1",
        descrition = "Let's start this course the right way",
        content = "content",
        order = 1,
        course = self.course,
        )
        self.assertIn(step, self.course.step_set.all())
