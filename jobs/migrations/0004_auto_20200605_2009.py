# Generated by Django 3.0.2 on 2020-06-05 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_applied', models.DateTimeField(auto_now_add=True, null=True)),
                ('applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.Applicant')),
                ('companies', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.Companies')),
            ],
        ),
    ]
