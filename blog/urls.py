from django.urls import path

from . import views

urlpatterns = [
    # URLs for blog post
    path('blog/', views.PostList.as_view(), name='post_list'),
    path(
        'blog/<int:year>/<int:month>/<str:slug>',
        views.post_detail,
        name='post_detail'
        ),
    path('blog/create/', views.PostCreate.as_view(), name='post_create'),
    path(
        'blog/<int:year>/<int:month>/<str:slug>/update',
        views.PostUpdate.as_view(),
        name="post_update"
    ),
    path(
        'blog/<int:year>/<int:month>/<str:slug>/delete',
        views.PostDelete.as_view(),
        name="post_delete"
    ),
]

urlpatterns += [
    # URLs for category
    path('category/', views.category_list, name='category_list'),
    path('category/<str:slug>', views.category_detail, name='category_detail'),
    path(
        'category/create/',
        views.CategoryCreate.as_view(),
        name='category_create'
        ),
    path(
        'category/<str:slug>/update',
        views.CategoryUpdate.as_view(),
        name="category_update"
    ),
    path(
        'category/<str:slug>/delete',
        views.CategoryDelete.as_view(),
        name="category_delete"
    ),
]
