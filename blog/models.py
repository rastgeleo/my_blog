from django.db import models
from django.shortcuts import reverse


class Category(models.Model):
    """ model for category that blog post belongs to """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=63, unique=True)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['added_date']

    def get_absolute_url(self):
        return reverse(
            'category_detail',
            kwargs={'slug': self.slug}
        )

    def get_update_url(self):
        return reverse(
            'category_update',
            kwargs={'slug': self.slug}
        )
    
    def get_delete_url(self):
        return reverse(
            'category_delete',
            kwargs={'slug': self.slug}
        )

    def __str__(self):
        return self.title


class Post(models.Model):
    """ model for blog post """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=63, unique_for_month='pub_date')
    content = models.TextField()
    pub_date = models.DateTimeField(
        'date_published',
        auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
        )

    def get_absolute_url(self):
        return reverse(
            'post_detail',
            kwargs={
                'year': self.pub_date.year,
                'month': self.pub_date.month,
                'slug': self.slug
                }
        )

    def get_update_url(self):
        return reverse(
            'post_update',
            kwargs={
                'year': self.pub_date.year,
                'month': self.pub_date.month,
                'slug': self.slug
            }
        )

    def get_delete_url(self):
        return reverse(
            'post_delete',
            kwargs={
                'year': self.pub_date.year,
                'month': self.pub_date.month,
                'slug': self.slug
            }
        )

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = 'pub_date'
        ordering = ['-pub_date', 'title']

