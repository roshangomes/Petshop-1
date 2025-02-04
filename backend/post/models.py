import uuid

from django.db import models
from django.utils.timesince import timesince
from django.core.exceptions import ValidationError
from account.models import User


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at',)
    
    def created_at_formatted(self):
        return timesince(self.created_at)


class PostAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_attachments')
    created_by = models.ForeignKey(User, related_name='post_attachments', on_delete=models.CASCADE)

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        else:
            return ''




class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default='Lovely Pet')
    description = models.TextField(blank=True, null=True)
    contact_information = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=4000.00)
    category = models.CharField(max_length=50, default='Cat')

    breed = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True, help_text="Age in months")
    vaccinated = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Weight in kg")
    microchipped = models.BooleanField(default=False)
    trained = models.BooleanField(default=False)
    health_certificate = models.BooleanField(default=False)

    body = models.TextField(blank=True, null=True)
    attachments = models.ManyToManyField('PostAttachment', blank=True)
    is_private = models.BooleanField(default=False)
    
    likes = models.ManyToManyField('Like', blank=True)
    likes_count = models.IntegerField(default=0)
    comments = models.ManyToManyField('Comment', blank=True)
    comments_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Automatically update likes_count and comments_count when saving the post
        self.likes_count = self.likes.count()
        self.comments_count = self.comments.count()
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ('-updated_at', '-created_at',)  # Order posts by updated_at and created_at in descending order

    
    def created_at_formatted(self):
        return timesince(self.created_at)





class Trend(models.Model):
    hashtag = models.CharField(max_length=255)
    occurences = models.IntegerField()


class EventAttachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='event_attachments')
    created_by = models.ForeignKey(User, related_name='event_attachments', on_delete=models.CASCADE)   

    
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, related_name='organized_events', on_delete=models.CASCADE)
    registered_users = models.ManyToManyField(User, related_name='registered_events', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    attachments = models.ManyToManyField('EventAttachment', related_name='events', blank=True)

    class Meta:
        ordering = ('-date',)

    def created_at_formatted(self):
        return timesince(self.created_at)    
    def registration_count(self):
        return self.registrations.count()
    
def validate_file_extension(value):
    if not value.name.endswith(('.pdf', '.jpg', '.jpeg', '.png')):
        raise ValidationError("Only PDF and image files (JPG, PNG) are allowed.")


class EventRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    address = models.TextField()
    selected_event = models.CharField(max_length=100)  # Event title
    pet_type = models.CharField(max_length=50)
    pet_name = models.CharField(max_length=50)
    pet_dob = models.DateField()
    vaccination_card = models.FileField(upload_to='vaccination_cards/')
    agree_to_terms = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.selected_event}"
 

 
class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey('Post', related_name='bookmarks', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='bookmarks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')
        ordering = ('-created_at',)

    def created_at_formatted(self):
        return timesince(self.created_at)
    
