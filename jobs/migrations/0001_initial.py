# Generated by Django 3.0.2 on 2020-06-03 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('address', models.TextField(null=True)),
                ('qualification', models.CharField(choices=[('Under Graduate', 'Under Graduate'), ('Graduate', 'Graduate'), ('Post Graduate', 'Post Graduate')], max_length=250, null=True)),
                ('experiance', models.CharField(choices=[('Fresher', 'Fresher'), ('1-3', '1-3'), ('4-6', '4-6'), ('6-10', '6-10'), ('More than 10', 'More than 10')], max_length=250, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]