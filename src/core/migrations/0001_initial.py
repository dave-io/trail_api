# Generated by Django 3.0 on 2020-12-24 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('createdBy', models.IntegerField(default=0, verbose_name='created_by')),
                ('updatedBy', models.IntegerField(default=0, verbose_name='updated_by')),
                ('isDeleted', models.BooleanField(default=False, verbose_name='is_deleted')),
                ('name', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('image', models.TextField(default='')),
                ('code', models.TextField(default='')),
                ('location', models.TextField(default='')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='SDG',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('createdBy', models.IntegerField(default=0, verbose_name='created_by')),
                ('updatedBy', models.IntegerField(default=0, verbose_name='updated_by')),
                ('isDeleted', models.BooleanField(default=False, verbose_name='is_deleted')),
                ('name', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('image', models.TextField(default='')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Program_Sdg',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('createdBy', models.IntegerField(default=0, verbose_name='created_by')),
                ('updatedBy', models.IntegerField(default=0, verbose_name='updated_by')),
                ('isDeleted', models.BooleanField(default=False, verbose_name='is_deleted')),
                ('sdgId', models.IntegerField(verbose_name='sdg_id')),
                ('programId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Program')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Program_Indicator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('createdBy', models.IntegerField(default=0, verbose_name='created_by')),
                ('updatedBy', models.IntegerField(default=0, verbose_name='updated_by')),
                ('isDeleted', models.BooleanField(default=False, verbose_name='is_deleted')),
                ('selectedIndicatorId', models.IntegerField(verbose_name='selected_indicator_id')),
                ('programSdgId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Program_Sdg')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('createdBy', models.IntegerField(default=0, verbose_name='created_by')),
                ('updatedBy', models.IntegerField(default=0, verbose_name='updated_by')),
                ('isDeleted', models.BooleanField(default=False, verbose_name='is_deleted')),
                ('description', models.TextField(default='')),
                ('SdgId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SDG')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]