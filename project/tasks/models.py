from django.db import models

class Task(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
