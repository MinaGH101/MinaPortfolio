from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Projects
from .forms import MessageForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

class HomeView(View):
    def get(self, request):
        pass
        
        return render(request, template_name='home/home.html')
    
class ServicesView(View):
    def get(self, request):
        pass 
    
        return render(request, 'home/services.html')
    
class ProjectsView(View):
    def get(self, request):
        projects = Projects.objects.all()
        return render(request, 'home/projects.html', context={'projects':projects})
    
class MessageView(View):
    form_class = MessageForm
    def get(self, request):
        form = self.form_class()
        return render(request, 'home/message.html', context={'form':form})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'your message has recieved successfully!')
            cd = form.cleaned_data
            subject = 'portfolio_message'
            body = {'first_name': cd['first_name'], 'last_name': cd['last_name'], 'email': cd['email'], 'message': cd['message']}
            # message = "\n".join(body.values())
            send_mail(subject=subject, message=str(body),
                      from_email= settings.EMAIL_HOST_USER, recipient_list=['migholami101@gmail.com',], fail_silently=False)
            
        return redirect('home:message')
            
    
class ButtomView(View):
    def get(self, request):
        return render(request, 'home/bottom.html')



