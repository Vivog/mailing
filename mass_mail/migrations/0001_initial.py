# Generated by Django 4.1.1 on 2022-09-26 10:05

from django.db import migrations, models
import mass_mail.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(upload_to=mass_mail.models.Attachments.directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='BCC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Прихована копія')),
            ],
            options={
                'verbose_name': 'Прихована копія',
                'verbose_name_plural': 'Прихована копії',
            },
        ),
        migrations.CreateModel(
            name='CC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Копія')),
            ],
            options={
                'verbose_name': 'Копія',
                'verbose_name_plural': 'Копії',
            },
        ),
        migrations.CreateModel(
            name='Replay_to',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Адреси для відповіді')),
            ],
            options={
                'verbose_name': 'Адреси для відповіді',
                'verbose_name_plural': 'Адреси для відповіді',
            },
        ),
        migrations.CreateModel(
            name='TO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Отримувач')),
            ],
            options={
                'verbose_name': 'Отримувач',
                'verbose_name_plural': 'Отримувачі',
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, verbose_name='Тема листа')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('body', models.CharField(max_length=5500, verbose_name='Текст повідомлення')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Час формування листа')),
                ('attachments', models.ManyToManyField(to='mass_mail.attachments', verbose_name='Вкладення')),
                ('bcc', models.ManyToManyField(to='mass_mail.bcc', verbose_name='Прихована копія')),
                ('cc', models.ManyToManyField(to='mass_mail.cc', verbose_name='Копія')),
                ('replay_to', models.ManyToManyField(to='mass_mail.replay_to', verbose_name='Адреси для відповіді')),
                ('to', models.ManyToManyField(to='mass_mail.to', verbose_name='Отримувач')),
            ],
            options={
                'verbose_name': 'Лист',
                'verbose_name_plural': 'Листи',
                'ordering': ['-published', 'subject'],
            },
        ),
    ]