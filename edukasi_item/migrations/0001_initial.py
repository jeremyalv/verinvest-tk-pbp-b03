# Generated by Django 4.1.2 on 2022-11-02 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_page', '0001_initial'),
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EdukasiComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('content', models.TextField(max_length=255)),
                ('upvotes', models.IntegerField()),
                ('saved', models.IntegerField()),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_page.profile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.post')),
            ],
        ),
    ]
