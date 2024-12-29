from django.db import models


class AbstractModel(models.Model):
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(AbstractModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


class Location(AbstractModel):
    name = models.CharField(max_length=256)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Post(AbstractModel):
    title = models.CharField(max_length=256)
    text = models.TextField()

    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return self.title
