from django import template
from ..models import Category
from django.shortcuts import get_object_or_404


register = template.Library()


@register.inclusion_tag('shop/shop_tags/categories_top_list.html', takes_context=True)
def categories_top_list(context):
    request = context['request']
    language = request.LANGUAGE_CODE
    # latest_posts = Post.published.order_by('-publish')[:count]
    fashion = get_object_or_404(Category,cciidd=1)
    electronics = get_object_or_404(Category, cciidd=2)
    gifts = get_object_or_404(Category, cciidd=3)
    home = get_object_or_404(Category, cciidd=4)
    music = get_object_or_404(Category, cciidd=5)
    sports = get_object_or_404(Category, cciidd=6)
    return {'categories_top_list': categories_top_list,
            'fashion' : fashion,
            'electronics': electronics,
            'gifts': gifts,
            'home': home,
            'music': music,
            'sports' : sports
    }


@register.inclusion_tag('shop/shop_tags/custom_banner.html')
def custom_banner():
    return {'custom_banner': custom_banner}
