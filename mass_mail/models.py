from django.db import models

# Create your models here.
class Mail(models.Model):
    subject = models.CharField(max_length=100, verbose_name='Тема листа')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL', db_index=True)
    body = models.CharField(max_length=5500, verbose_name='Текст повідомлення')
    attachments = models.ManyToManyField('Attachments', verbose_name='Вкладення', blank=True)
    to = models.ManyToManyField('TO', verbose_name='Отримувач')
    cc = models.ManyToManyField('CC', verbose_name='Копія', blank=True)
    bcc = models.ManyToManyField('BCC', verbose_name='Прихована копія', blank=True)
    replay_to = models.ManyToManyField('Replay_to', verbose_name='Адреси для відповіді', blank=True)
    published = models.DateTimeField(auto_now_add=True, verbose_name='Час формування листа')

    objects = models.Manager()

    class Meta:
        verbose_name = 'Лист'
        verbose_name_plural = 'Листи'
        ordering = ['-published', 'subject']

    def __str__(self):
        return f'{self.published}_{self.subject}'

class Attachments(models.Model):

    def directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return f'attachments/{filename}'
    files = models.FileField(upload_to=directory_path)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Вкладення'
        verbose_name_plural = 'Вкладення'

    def __str__(self):
        return f'{self.files.file}'

class TO(models.Model):
    email = models.EmailField('Отримувач', unique=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Отримувач'
        verbose_name_plural = 'Отримувачі'

    def __str__(self):
        return f'{self.email}'

class CC(models.Model):
    email = models.EmailField('Копія', unique=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Копія'
        verbose_name_plural = 'Копії'

    def __str__(self):
        return f'{self.email}'

class BCC(models.Model):
    email = models.EmailField('Прихована копія', unique=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Прихована копія'
        verbose_name_plural = 'Прихована копії'

    def __str__(self):
        return f'{self.email}'

class Replay_to(models.Model):
    email = models.EmailField('Адреси для відповіді', unique=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'Адреси для відповіді'
        verbose_name_plural = 'Адреси для відповіді'

    def __str__(self):
        return f'{self.email}'
