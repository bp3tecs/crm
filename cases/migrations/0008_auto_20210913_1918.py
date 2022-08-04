# Generated by Django 3.2 on 2021-09-13 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0034_auto_20210913_1918'),
        ('cases', '0007_remove_case_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.company'),
        ),
        migrations.AlterField(
            model_name='case',
            name='assigned_to',
            field=models.ManyToManyField(related_name='case_assigned_users', to='common.Profile'),
        ),
        migrations.AlterField(
            model_name='case',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case_created_by', to='common.profile'),
        ),
    ]
