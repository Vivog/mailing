from django.shortcuts import render
from django.core.mail import EmailMessage

# Create your views here.
def single_mail():
    em = EmailMessage(subject='Test', body='Testing', to=['vivog2017@gmail.com'])
    em.send()
    return em

# class ContactsView(ListView, SuccessMessageMixin):
#     model = MainInfo
#     template_name = 'site_app/contacts.html'
#     context_object_name = 'contacts'
#     success_message = 'Ваш лист успішно відправлено'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update(CONTEXT)
#         context['form'] = ContactForm()
#
#         return context
#
#     def get_queryset(self):
#         return MainInfo.objects.filter(fio=FIO)
#
#     def post(self, request):
#         if request.method == 'POST':
#             form = ContactForm(request.POST)
#             if form.is_valid():
#                 messages.success(request, 'Ваш лист успішно відправлено')
#                 subject = "From Resume_Site"
#                 body = {
#
#                     'name': f"Відправник: {form.cleaned_data['name']}",
#                     'email': f"Скринька відправника: {form.cleaned_data['email']}",
#                     'text': 'Текст повідомлення: ',
#                     'message': form.cleaned_data['message'],
#                 }
#                 message = "\n".join(body.values())
#                 try:
#                     send_mail(subject, message,
#                                'vivog2022@ukr.net',
#                               ['vivog2022@ukr.net'], fail_silently=False)
#                 except BadHeaderError:
#                     return HttpResponse('Знайдено невірний заголовок')
#                 return redirect("site_app:contacts")
#
#         form = ContactForm()
#         return render(request, "site_app/contacts.html", {'form': form})