# Generated by Django 3.0.4 on 2020-03-30 07:12

import apps.core.models
from django.db import migrations, models
import django.db.models.deletion
import django_enum_choices.choice_builders
import django_enum_choices.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Government',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('started_at', models.DateField()),
                ('end_at', models.DateField(null=True)),
            ],
            options={
                'db_table': 'governments',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('born_at', models.DateField(null=True)),
            ],
            options={
                'db_table': 'members',
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('color', models.CharField(max_length=15, null=True)),
                ('type', django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('nazi', 'nazi'), ('liberals', 'liberals'), ('populists', 'populists'), ('communists', 'communists'), ('conservatives', 'conservatives'), ('socialists', 'socialists'), ('nationalists', 'nationalists'), ('democrats', 'democrats')], enum_class=apps.core.models.Party.PartyEnum, max_length=13, null=True)),
                ('founded_at', models.DateField(null=True)),
            ],
            options={
                'db_table': 'parties',
            },
        ),
        migrations.AlterModelManagers(
            name='permission',
            managers=[
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('permissions', models.ManyToManyField(db_table='role_permissions', to='core.Permission')),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='InboxMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('is_fake', models.BooleanField(default=False)),
                ('published_at', models.DateTimeField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='core.Member')),
            ],
            options={
                'db_table': 'inbox',
            },
        ),
        migrations.CreateModel(
            name='GovernmentMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('government', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='government_members', to='core.Government')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='government_members', to='core.Member')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='government_members', to='core.Party')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='government_members', to='core.Role')),
            ],
            options={
                'db_table': 'government_members',
            },
        ),
    ]
