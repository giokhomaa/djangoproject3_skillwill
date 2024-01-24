# Generated by Django 4.2.1 on 2023-09-14 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='fist_name', max_length=50)),
                ('last_name', models.CharField(default='last_name', max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/')),
            ],
        ),
    ]