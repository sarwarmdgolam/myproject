from django.test import TestCase

from adminapp.models import Job


# Create your tests here.


class JobTests(TestCase):
    def test_job_is_created_successfully(self):
        job = Job(
            name='test_job',
        )
        job.save()


