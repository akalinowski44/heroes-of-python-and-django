# Generated by Django 2.1.7 on 2019-04-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(default='landing_page/application/default/default.jpg', upload_to='landing_page/application')),
                ('summary', models.CharField(max_length=100)),
                ('urlCategory', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
