from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = "Category"
    
    
class Blog(models.Model):


    STATUS_CHOICES = (
        [0,'draft'],
        [2,'Active']
    )

    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=200)
    fk_author = models.ForeignKey(User,on_delete=models.CASCADE)
    fk_category = models.ForeignKey(Category,on_delete = models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    shortdescription = models.TextField(max_length = 300)
    blog_body = models.TextField(max_length = 2000)
    is_featured = models.BooleanField(default = False)
    status = models.IntegerField(choices = STATUS_CHOICES,default = 0)
    updated_at = models.DateTimeField(auto_now = True)
    created_at = models.DateTimeField(auto_now_add = True)
    deleted_at = models.DateTimeField(blank=True,null=True)


    def __str__(self):
        return self.title
