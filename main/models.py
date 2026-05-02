from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300, default='')
    description = models.TextField()
    category = models.CharField(max_length=100, default='')
    tools_used = models.TextField(default='')
    key_features = models.TextField(default='')
    role = models.TextField(default='')
    challenges = models.TextField(default='')
    lessons_learned = models.TextField(default='')
    image_path = models.CharField(max_length=200, blank=True, default='')
    link = models.URLField(blank=True, null=True)
    link_label = models.CharField(max_length=100, default='View Project')
    github_link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return f"{self.category} — {self.name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-received_at']

    def __str__(self):
        return f"{self.name} — {self.subject}"
