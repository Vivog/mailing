# Generated by Django 4.1.1 on 2022-09-26 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mass_mail', '0002_alter_attachments_options_alter_mail_attachments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='attachments',
            field=models.ManyToManyField(blank=True, to='mass_mail.attachments', verbose_name='Вкладення'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='bcc',
            field=models.ManyToManyField(blank=True, to='mass_mail.bcc', verbose_name='Прихована копія'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='cc',
            field=models.ManyToManyField(blank=True, to='mass_mail.cc', verbose_name='Копія'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='replay_to',
            field=models.ManyToManyField(blank=True, to='mass_mail.replay_to', verbose_name='Адреси для відповіді'),
        ),
        migrations.AlterField(
            model_name='mail',
            name='to',
            field=models.ManyToManyField(to='mass_mail.to', verbose_name='Отримувач'),
        ),
    ]