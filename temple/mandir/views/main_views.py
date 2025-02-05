from django.shortcuts import render,redirect,get_object_or_404 
from ..models import Event,Blogs,Committee,CommitteeMember,EventImage
from ..forms import EventForm,blogform,committeeform,memberform
from django.contrib.auth.decorators import login_required


@login_required
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()

            for image in request.FILES.getlist('images'):#save garna
                EventImage.objects.create(event=event, image=image)

            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'main/add_event.html', {'form': form})

def event_list(request):
    event=Event.objects.all().order_by('-created_at')
    return render(request,'main/event_list.html',{'event':event})

def edit_event(request,event_id):
    event=get_object_or_404(Event,pk=event_id,user=request.user)
    if request.method=='POST':
        form=EventForm(request.POST,request.FILES,instance=event)
        if form.is_valid():
            event=form.save(commit=False)
            event.user=request.user
            event.save()
            return redirect('event_list')
    else:
        form=EventForm(instance=event)
    return render(request,'main/edit_event.html',{'from':form})

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

def list_committee(request):
    form=Committee.objects.all().order_by('-created_at')
    return render(request,'main/list_committee.html',{'form':form})

@login_required
def add_committee(request):
    if request.method=='POST':
        form=committeeform(request.POST)
        if form.is_valid():
            committee=form.save(commit=False)
            committee.user=request.user
            committee.save()
            return redirect('add_committee')
    else:
        form=committeeform()
    return render(request,'main/add_committee.html',{'form':form})


def edit_committee(request):
    pass

def delete_committee(request):
    pass

def list_member(request):
    form=CommitteeMember.objects.all().order_by("-c_id")
    return render(request,"main/list_member.html",{'form':form})