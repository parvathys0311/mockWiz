from django.utils.text import slugify


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(str('%s %s' % (instance.firstName, instance.lastname)))

    model_class = instance.__class__
    while model_class.objects.filter(slug=slug).exists():
        count = model_class.objects.filter(slug=slug).count()
        slug = f'{slug}-{count}'

    return slug