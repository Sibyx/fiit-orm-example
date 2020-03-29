# Generated by Django 3.0.4 on 2020-03-29 20:02

import apps.core.models
from django.db import migrations, models
import django.db.models.deletion
import django_enum_choices.choice_builders
import django_enum_choices.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_allow_empty_end_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='governmentmember',
            name='government',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='government_members', to='core.Government'),
        ),
        migrations.AlterField(
            model_name='governmentmember',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='government_members', to='core.Member'),
        ),
        migrations.AlterField(
            model_name='governmentmember',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='government_members', to='core.Party'),
        ),
        migrations.AlterField(
            model_name='governmentmember',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='government_members', to='core.Role'),
        ),
        migrations.AlterField(
            model_name='inboxmessage',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='core.Member'),
        ),
        migrations.AlterField(
            model_name='party',
            name='type',
            field=django_enum_choices.fields.EnumChoiceField(choice_builder=django_enum_choices.choice_builders.value_value, choices=[('nazi', 'nazi'), ('simple', 'simple'), ('liberal', 'liberal'), ('populist', 'populist'), ('communist', 'communist'), ('conservatives', 'conservatives'), ('socialists', 'socialists'), ('nationalists', 'nationalists'), ('democrats', 'democrats')], enum_class=apps.core.models.Party.PartyEnum, max_length=13, null=True),
        ),
    ]