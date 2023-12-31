# Generated by Django 4.2.4 on 2023-08-08 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_alter_jobposting_expected_cgpa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='qualified_round',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='rounds',
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='applicant',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='data.userprofile'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='job_posting',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='data.jobposting'),
        ),
    ]
