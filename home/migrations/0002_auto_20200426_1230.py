# Generated by Django 3.0.5 on 2020-04-26 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField(blank=True, null=True)),
                ('links', models.URLField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Destination',
        ),
    ]
