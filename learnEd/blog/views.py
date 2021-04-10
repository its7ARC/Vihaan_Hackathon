#ModelsImport
from .models import Topic,Blog,Profile

#PageRenderImport
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#AuthenticationImport
from django.contrib.auth import authenticate,login
from .forms import LoginForm,UserRegistrationForm,UserEditForm,ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#postgresSearch
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


# Views

#SitePages

def search(request):
	return render(request,'blog/search.html',{})

def dynamicSearch(request):
	keyword = request.GET.get('keyword',False)
	#search
	search_vector = SearchVector('name',) 
	search_query = SearchQuery(keyword)
	topics = Topic.objects.annotate(search=search_vector,rank=SearchRank(search_vector, search_query) ).filter(search = search_query).order_by('-rank')
	topics = topics[0:8]

	topics2 = []
	for topic in topics:
		topics2.append(topic.name)
	data = {
		'topics':topics2,
	}
	return JsonResponse(data)



def searchProcess(request):
	blogs = None
	upvote = None
	bookmark = None
	try:
		#Postgres Search 

		#Handling basic spelling errors in topic names
		search_vector = SearchVector('name',) 
		search_query = SearchQuery(request.POST['title'])
		topics = Topic.objects.annotate(search=search_vector,rank=SearchRank(search_vector, search_query) ).filter(search = search_query).order_by('-rank')
		topic = topics[0]
		blogs = topic.blog_set.filter(draft = False).order_by('-verified')
		blog = blogs[0]

		try:
			userProfile = Profile.objects.get(user = request.user)
			upvote = Blog.objects.get(blog = blog, upvote__id = userProfile.id)
			#bookmark
		except:
			upovte = None
		
	except:
		"""
		try:
			#searching content of blogs if query not in topics
			search_vector = SearchVector('preRequisites', weight='A') + SearchVector('blogContent',weight='A')
			search_query = SearchQuery(request.POST['title'])
			blogs = Blog.objects.annotate(search=search_vector,rank=SearchRank(search_vector, search_query) ).filter(search = search_query,draft = False).order_by('-rank')
			blog = blogs[0]
			topic = request.POST['title']
		
		except:
		"""
		#If query in neither

		#AI algo for topic actually exists
		topic = Topic(name = request.POST['title'])
		topic.save()


	
	#Pagination
	"""
	paginator = Paginator(blogs,8)
	page = request.GET.get('page')
    
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		if request.is_ajax():
			return HttpResponse('')
		blogs = paginator.page(paginator.num_pages)

	if request.is_ajax():
		return render(request,'blog/blogs_ajax.html',{'section': 'blogs', 'topic':topic, 'blogs': blogs})
			
	return render(request,'blog/blogs.html',{'section': 'blogs', 'blogs': blogs,'topic':topic})		
	"""
	return render(request,'blog/blogs.html',{'topic':topic, 'blog':blog, 'upvote':upvote, 'bookmark':bookmark})


@login_required
def upvote(request):
	user = request.user
	userProfile = Profile.objects.get(user = user)
	blogId = request.GET.get('blogId',False)
	blog = Blog.objects.get(pk = blogId)
	state = 0
	try:
		alr_liked = Blog.objects.get(upvote__id = userProfile.id, blog_id = blogId)
		alr_liked.upvote.remove(userProfile)
		alr_liked.save()
		state = 0
	except:
		blog.upvote.add(userProfile)
		blog.save()
		state = 1

	
	data = {
		'state':state,
	}
	return JsonResponse(data)
	




@login_required
def writeBlog1(request):
	return render(request,'blog/writeBlog.html',{})

#for rewriting blog
@login_required
def writeBlog2(request,topicId):
	topic = get_object_or_404(Topic, pk = topicId)
	user = request.user
	userProfile = Profile.objects.get(user = user)
	
	userDraft = None
	userBlog = None

	try:
		userBlog = Blog.objects.get(topic = topic,author = userProfile,draft = False)
	except:
		userBlog = None

	return render(request,'blog/writeBlog.html',{'topic':topic,'userDraft':userDraft,'userBlog':userBlog})

#for draft to blog
@login_required
def writeBlog3(request,topicId):
	topic = get_object_or_404(Topic, pk = topicId)
	user = request.user
	userProfile = Profile.objects.get(user = user)
	
	userDraft = None
	userBlog = None
	
	try:
		userDraft = Blog.objects.get(topic = topic,author = userProfile,draft = True)
	except:
		userDraft = None

	return render(request,'blog/writeBlog.html',{'topic':topic,'userDraft':userDraft,'userBlog':userBlog})

@login_required
def addBlog(request):
	user = request.user
	userProfile = Profile.objects.get(user = user)
	draftBool = bool(request.POST['draftBool'])

	
	try:
		topic = Topic.objects.get(name__iexact = request.POST['topic'])
		if(draftBool == False):
			try:
				userPreviousBlogs = Blog.objects.filter(topic = topic, author = userProfile)
				for prevBlog in userPreviousBlogs:
					prevBlog.delete()
			except:
				userPreviousBlog = None
	
		elif(draftBool == True):
			try:
				userPreviousBlog = Blog.objects.get(topic = topic, author = userProfile,draft = True)
				userPreviousBlog.delete()
			except:
				userPreviousBlog = None

	except:
		topic = Topic(name = ("%s"%request.POST['topic']))
		topic.save()
	
	submittedBlog = topic.blog_set.create(preRequisites = ("%s"%request.POST['preRequisites']), blogContent = f"{request.POST['blogContent']}", author = Profile.objects.get(user__id = int(request.POST['userId'])), verified = Profile.objects.get(user__id = int(request.POST['userId'])).verified,draft = draftBool)
	topic.save()

	#Rendering blog/draft page
	if(draftBool == False):
		try:
			userBlogs = Blog.objects.filter(author = userProfile,draft = False).order_by('-pub_date')
		except:
			userBlogs = None
		return render(request,'blog/userBlogs.html',{'userBlogs':userBlogs})

	elif(draftBool == True):
		try:
			userDrafts = Blog.objects.filter(author = userProfile,draft = True).order_by('-pub_date')
		except:
			userDrafts = None
		
		return render(request,'blog/userDrafts.html',{'userDrafts':userDrafts})
		


def aboutUs(request):
	return render(request,'blog/aboutUs.html',{})
#

@login_required
def userBlogs(request):
	user = request.user
	userProfile = Profile.objects.get(user = user)
	try:
		userBlogs = Blog.objects.filter(author = userProfile,draft = False).order_by('-pub_date')
	except:
		userBlogs = None
	return render(request,'blog/userBlogs.html',{'userBlogs':userBlogs})

@login_required
def userBlog(request,blogId):
	user = request.user
	userProfile = Profile.objects.get(user = user)
	try:
		userBlog = Blog.objects.get(pk = blogId)
		if(userBlog.draft == False):
			topic = userBlog.topic
			if(userProfile == userBlog.author):
				selfBlog = True
			else:
				selfBlog = False
		else:
			userBlog = None
	except:
		userBlog = None

	
	return render(request,'blog/userBlog.html',{'topic':topic,'userBlog':userBlog,'selfBlog':selfBlog})


@login_required
def userDrafts(request):
	user = request.user
	userProfile = Profile.objects.get(user = user)
	try:
		userDrafts = Blog.objects.filter(author = userProfile,draft = True).order_by('-pub_date')
	except:
		userDrafts = None
	return render(request,'blog/userDrafts.html',{'userDrafts':userDrafts})







#AuthenticationViews
def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request,username = cd['username'], password = cd['password'])  

			if user is not None:
				if user.is_active:
					login(request,user)
					return render(request,'blog/search.html',{'user':user})

				else:
					return HttpResponse("Disabled Account")

			else:
				form = LoginForm()
				return render(request,'blog/invalidLogin.html',{'form':form})

	else:
		form = LoginForm()

	return render(request,'blog/login.html',{'form':form})

@login_required
def userAccount(request):
	user = request.user
	profile = Profile.objects.get(user = user)

	return render(request,'blog/userAccount.html',{'user':user,'profile':profile})      #->Work this out.


#UserRegistration
def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			#Create new user object....dont save now
			new_user = user_form.save(commit = False)
			#Set chosen Password
			new_user.set_password(user_form.cleaned_data['password'])
			#Save the user object
			new_user.save()
			profile = Profile.objects.create(user = new_user)
			profile.save()
			return render(request,'blog/register_done.html',{'new_user':new_user})
	else:
		user_form = UserRegistrationForm()
	return render(request,'blog/register.html',{'user_form':user_form})



@login_required
def edit(request):
	if request.method == 'POST':
		user_form = UserEditForm(instance = request.user,data = request.POST)
		profile_form = ProfileEditForm(instance = request.user.profile,data = request.POST, files = request.FILES)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()

			user = request.user
			profile = Profile.objects.get(user = user)
			return render(request,'blog/userAccount.html',{'user':user,'profile':profile})

	else:
		user_form = UserEditForm(instance = request.user)
		profile_form = ProfileEditForm(instance = request.user.profile)

	return render(request,'blog/edit.html',{'user_form':user_form,'profile_form':profile_form})
									   




















