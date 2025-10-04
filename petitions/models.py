from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Petition(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    movie_title = models.CharField(max_length=200, help_text="The movie title you want to petition for")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_petitions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    @property
    def vote_count(self):
        return self.votes.count()
    
    @property
    def yes_votes(self):
        return self.votes.filter(vote_type='yes').count()
    
    @property
    def no_votes(self):
        return self.votes.filter(vote_type='no').count()

class Vote(models.Model):
    VOTE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    petition = models.ForeignKey(Petition, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=3, choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('petition', 'user')  # One vote per user per petition
    
    def __str__(self):
        return f"{self.user.username} voted {self.vote_type} on {self.petition.title}"