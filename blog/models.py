from django.db import models


class Category(models.Model):
    """ model for category that blog post belongs to """
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    """ model for blog post """
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
        )

    def abstract(self):
        if len(self.content) > 50:
            return self.content[:50] + ' ...'
        else:
            return self.content

    def __str__(self):
        return self.title
