from django.urls import path
from blog import views as auth_views

urlpatterns = [
    path('', auth_views.PostListView.as_view(), name='post_list'),
    path('about/', auth_views.AboutView.as_view(), name='about'),
    path('post/<int:pk>', auth_views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', auth_views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', auth_views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', auth_views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts/', auth_views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/comment/', auth_views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', auth_views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', auth_views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish/', auth_views.post_publish, name='post_publish'),
]
