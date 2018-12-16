from django.db import models
from treebeard.mp_tree import MP_Node
from mptt.models import MPTTModel, TreeForeignKey


class Bar(models.Model):
    title = models.CharField('title', max_length=255)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Category(MP_Node):
    name = models.CharField(max_length=30)
    slug = models.SlugField('slug', null=True, blank=True)
    end_element = models.BooleanField('конечный элемент', default=False)
    list_of_names = models.CharField(max_length=255, null=True, blank=True)

    node_order_by = ['name']

    def __unicode__(self):
        return 'Category: %s' % self.name


class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
