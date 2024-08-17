# Generated by Django 4.0.1 on 2024-07-15 06:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_notifi_count'),
        ('mycoinApp', '0006_usercoinownership_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='PushNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('message', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notification', to='authentication.user')),
            ],
        ),
    ]
