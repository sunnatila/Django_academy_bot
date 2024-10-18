from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

class TGUsers(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    group_number = models.ForeignKey(to='test_panel.Group', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        verbose_name_plural = "Telegram bot foydalanuvchilari"
        verbose_name = "Telegram bot foydalanuvchi "
        db_table = 'tg_users'


class Test(models.Model):
    topic = models.ForeignKey(to='test_panel.Topic', on_delete=models.CASCADE)
    image = models.CharField(max_length=255, null=True, blank=True)
    question = models.CharField(max_length=255)
    variant_a = models.CharField(max_length=255)
    variant_b = models.CharField(max_length=255)
    variant_c = models.CharField(max_length=255)
    variant_d = models.CharField(max_length=255)
    right_variant = models.CharField(max_length=255)

    objects = models.Manager()

    def __str__(self):
        return f"{self.pk} - {self.topic}"

    class Meta:
        verbose_name_plural = "Testlar"
        verbose_name = "Test "
        db_table = 'tests'

class Result(models.Model):
    student = models.ForeignKey(TGUsers, on_delete=models.CASCADE)
    test_topic = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test_topic_results')
    test_count = models.IntegerField()
    test_right_variants = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='right_variant_results')
    total_percent = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return f"{self.pk} - {self.student.name}"

    class Meta:
        verbose_name_plural = "Natijalar"
        verbose_name = "Natija "
        db_table = 'results'


class Group(models.Model):
    group_number = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return f"{self.group_number}"

    class Meta:
        verbose_name_plural = "Guruhlar"
        verbose_name = "Guruh "
        db_table = 'groups'

class Topic(models.Model):
    topic_name = models.CharField(max_length=100)

    objects = models.Manager()

    def __str__(self):
        return f"{self.pk} - {self.topic_name}"

    class Meta:
        verbose_name_plural = "Mavzular"
        verbose_name = "Mavzu "
        db_table = 'topics'

class Lesson(models.Model):
    group_number = models.ForeignKey(Group, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    vidio_id = models.CharField(max_length=255, null=True, blank=True)
    vd_name = models.CharField(max_length=255)
    vd_description = models.TextField()

    objects = models.Manager()

    def __str__(self):
        return f"{self.pk} - {self.topic}"

    class Meta:
        verbose_name_plural = "Darslar"
        verbose_name = "Dars "
        db_table = 'lessons'


