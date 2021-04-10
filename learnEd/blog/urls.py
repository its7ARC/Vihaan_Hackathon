from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


	#Django Auth View ->#path('login/',auth_views.LoginView.as_view(),name = 'login'),

app_name = 'blog'
urlpatterns = [
	#SiteUrl's
	path('',views.search,name = 'search'),
	path('searchProcess/',views.searchProcess,name = 'searchProcess'),
	path('dynamicSearch/',views.dynamicSearch,name = 'dynamicSearch'),
	path('upvote/',views.upvote,name = 'upvote'),
	path('writeBlog/',views.writeBlog1,name = 'writeBlog1'),
	path('writeBlog/<int:topicId>/',views.writeBlog2,name = 'writeBlog2'),
	path('writeBlog3/<int:topicId>/',views.writeBlog3,name = 'writeBlog3'),
	path('addBlog/',views.addBlog,name = 'addBlog'),
	path('aboutUs/',views.aboutUs,name = 'aboutUs'),

	#AuthenticationUrl's
	#path('',include('django.contrib.auth.urls')),
	path('login/',views.user_login,name='login'),
	path('logout/',auth_views.LogoutView.as_view(),name = 'logout'),
	path('userAccount/',views.userAccount,name='userAccount'),
	path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
	path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name = 'password_change_done'),
	#PasswordReset
	path('password_reset/',auth_views.PasswordResetView.as_view(),name = 'password_reset'),
	path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name = 'password_reset_done'),
	path('reset/uidb64/<token>/',auth_views.PasswordResetConfirmView.as_view(),name = 'password_reset_confirm'),
	path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name = 'password_reset_complete'),
	path('register/',views.register,name = 'register'),

	path('edit/',views.edit, name = 'edit'),
	path('userBlogs/',views.userBlogs,name='userBlogs'),
	path('userBlog/<int:blogId>/',views.userBlog,name = 'userBlog'),
	path('userDrafts/',views.userDrafts,name = 'userDrafts'),
	
]