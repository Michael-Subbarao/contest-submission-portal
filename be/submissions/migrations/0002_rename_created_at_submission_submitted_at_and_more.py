# Generated by Django 4.1.7 on 2023-03-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='created_at',
            new_name='submitted_at',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.TextField(default='No description provided.'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contest',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contest',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='submission',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]