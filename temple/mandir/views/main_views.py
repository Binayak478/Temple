from django.shortcuts import render,redirect,get_object_or_404 
from ..models import Event,Blogs
from ..forms import eventform,blogform

def add_event(request):
    if request.method=='POST':
       form=eventform(request.POST,request.FILES)
       if form.is_valid():
           event=form.save(commit=False)
           event.user=request.user
           event.save()
           return redirect("event_list")
    else:
        form=eventform()
    
    return render(request,'add_event.html',{'form':form})

def event_list(request):
    event=Event.objects.all().order_by('-created_at')
    return render(request,'event_list.html',{'event':event})

def edit_event(request,event_id):
    event=get_object_or_404(Event,pk=event_id,user=request.user)
    if request.method=='POST':
        form=eventform(request.POST,request.FILES,instance=event)
        if form.is_valid():
            event=form.save(commit=False)
            event.user=request.user
            event.save()
            return redirect('event_list')
    else:
        form=eventform(instance=event)
    return render(request,'add_event.html',{'from':form})

def delete_event(request,event_id):
    event=get_object_or_404(Event,pk=event_id,user=request.user)
    if request.method=='POST':
        event.delete()
        return redirect('event_list')
    return render(request,'delete_tweet.html',{'event':event})


def list_blog(request):
    blog=Blogs.objects.all().order_by('-created_at')
    return render(request,'list_blog.html',{'blog':blog})

def add_blog(request):
    if request.method=='POST':
        form=blogform(request.POST,request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.user=request.user
            blog.save()
            return redirect("list_blog")
    else:
        form=blogform()
        
    return render(request,'add_blog.html',{'form':form})

def edit_blog(request,blog_id):
    blog=get_object_or_404(Blogs,pk=blog_id,user=request.user)
    if request.method=='POST':
        form=blogform(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.user=request.user
            blog.save()
            return redirect("list_blog")
    else:
        form=blogform(instance=blog)
        
    return render(request,'add_blog.html',{'form':form})

def delete_blog(request,blog_id):
    blog=get_object_or_404(Blogs,pk=blog_id,user=request.user)
    if request.method=='POST':
        blog.delete()
        return redirect("list_blog")
    return render(request,'delete_blog.html',{'blog':blog})