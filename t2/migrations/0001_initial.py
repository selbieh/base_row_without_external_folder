# Generated by Django 3.2.12 on 2022-07-25 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrunchBaseLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('url', models.CharField(max_length=255)),
                ('response', models.JSONField(default=dict)),
                ('entity_type', models.CharField(choices=[('organization', 'organization'), ('FOUNDER', 'FOUNDER')], default='', max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
