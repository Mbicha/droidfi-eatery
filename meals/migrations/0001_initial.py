# Generated by Django 3.2 on 2021-05-10 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combination', models.CharField(max_length=200)),
                ('amount', models.IntegerField(default=0)),
                ('image', models.FileField(null=True, upload_to='images/', verbose_name='')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]