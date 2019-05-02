# Generated by Django 2.2 on 2019-04-30 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software', models.CharField(max_length=200)),
                ('softwaretype', models.CharField(max_length=50)),
                ('endofsupport', models.DateTimeField(blank=True)),
                ('disposition', models.DateTimeField(max_length=20)),
            ],
        ),
    ]