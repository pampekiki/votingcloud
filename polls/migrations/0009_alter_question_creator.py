# Generated by Django 3.2.dev20200814111336 on 2020-08-29 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_question_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.user'),
        ),
    ]
