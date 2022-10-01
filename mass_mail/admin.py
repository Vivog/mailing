from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.core.mail import EmailMessage, get_connection
from django.template.loader import render_to_string

from mass_mail.models import *


class MailAdminForm(forms.ModelForm):
    body = forms.CharField(label='Текст повідомлення', widget=CKEditorUploadingWidget())

    class Meta:
        model = Mail
        fields = '__all__'


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'published',)
    prepopulated_fields = {'slug': ('subject',), }
    save_on_top = True
    save_as = True
    form = MailAdminForm

    def save_model(self, request, obj, form, change):
        obj.save()

        subject = form.cleaned_data['subject']
        context = {'body': form.cleaned_data['body']}
        body = render_to_string('mass_mail/body.html', context)
        print(body)

        to, cc, bcc, replay_to = [], [], [], []
        for t in form.cleaned_data['to']:
            to.append(t.email)
        for c in form.cleaned_data['cc']:
            cc.append(c.email)
        for b in form.cleaned_data['bcc']:
            bcc.append(b.email)
        for r in form.cleaned_data['replay_to']:
            replay_to.append(r)

        message = EmailMessage(subject=subject, body=body, to=to, cc=cc, bcc=bcc, reply_to=replay_to, )

        for attach in form.cleaned_data['attachments']:
            if attach:
                message.attach_file(rf'{attach.files.file}')
            else:
                break

        con = get_connection()
        con.open()
        con.send_messages([message])
        con.close()

        super().save_model(request, obj, form, change)


@admin.register(Attachments)
class AttachmentsAdmin(admin.ModelAdmin):
    list_display = ('files',)


@admin.register(TO)
class TOAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(CC)
class CCAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(BCC)
class BCCAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(Replay_to)
class Replay_toAdmin(admin.ModelAdmin):
    list_display = ('email',)
