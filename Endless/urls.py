from django.urls import path
from Endless.views import (SignUp, PostListView, HelloDjango, PostDetailView, 
PostCreateView, PostUpdateView, PostDeleteView, addLike, addComment, ExploreView, toggleFollow, UserProfile, EditProfile
)
urlpatterns = [
    # path('', HelloDjango.as_view(), name = 'hello'),
    path('', PostListView.as_view(), name = 'posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('post/new/', PostCreateView.as_view(), name = 'make_post'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name = 'edit_post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name = 'delete_post'),
    path('auth/signup', SignUp.as_view(), name='signup'),
    path('like', addLike, name='addLike'),
    path('comment', addComment, name='addComment'),
    path('user_profile/<int:pk>/', UserProfile.as_view(), name='profile'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
    path('explore', ExploreView.as_view(), name='explore'),
    path('togglefollow', toggleFollow, name='togglefollow'),

]