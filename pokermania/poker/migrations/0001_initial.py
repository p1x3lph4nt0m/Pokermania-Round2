# Generated by Django 5.1.5 on 2025-02-22 09:21

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='custom_user_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_permissions_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('file', models.FileField(max_length=5000, upload_to='static/bots/')),
                ('path', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('wins', models.IntegerField(default=0)),
                ('total_games', models.IntegerField(default=0)),
                ('chips_won', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('winner', models.TextField()),
                ('total_chips_exchanged', models.IntegerField(default=0)),
                ('bot1_wins', models.IntegerField(default=0)),
                ('bot2_wins', models.IntegerField(default=0)),
                ('total_rounds', models.IntegerField(default=5)),
                ('played_at', models.DateTimeField(auto_now_add=True)),
                ('rounds_data', models.JSONField(max_length=100000)),
                ('bot1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_bot1', to='poker.bot')),
                ('bot2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches_as_bot2', to='poker.bot')),
            ],
            options={
                'ordering': ['-played_at'],
            },
        ),
        migrations.CreateModel(
            name='TestBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('file', models.FileField(upload_to='test_bots/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('chips_won', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('total_games', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TestMatch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('opponent_name', models.TextField()),
                ('winner', models.TextField()),
                ('total_chips_exchanged', models.IntegerField()),
                ('test_bot_wins', models.IntegerField()),
                ('opponent_wins', models.IntegerField()),
                ('played_at', models.DateTimeField(auto_now_add=True)),
                ('rounds_data', models.JSONField(max_length=100000)),
                ('bot1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_matches', to='poker.testbot')),
            ],
            options={
                'ordering': ['-played_at'],
            },
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.IntegerField()),
                ('winner', models.TextField()),
                ('chips_exchanged', models.IntegerField()),
                ('replay_data', models.JSONField(max_length=100000)),
                ('hole_cards', models.JSONField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rounds', to='poker.match')),
            ],
            options={
                'ordering': ['round_number'],
                'unique_together': {('match', 'round_number')},
            },
        ),
    ]
