# Generated by Django 4.1.1 on 2022-09-26 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mass_mail', '0003_alter_mail_attachments_alter_mail_bcc_alter_mail_cc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bcc',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Прихована копія'),
        ),
        migrations.AlterField(
            model_name='cc',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Копія'),
        ),
        migrations.AlterField(
            model_name='replay_to',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Адреси для відповіді'),
        ),
        migrations.AlterField(
            model_name='to',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Отримувач'),
        ),
    ]