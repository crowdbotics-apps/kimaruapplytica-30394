# Generated by Django 3.1.7 on 2021-09-10 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(choices=[('Web', 'web'), ('Mobile', 'Mobile')], default='Web', max_length=10)),
                ('framework', models.CharField(choices=[('Django', 'Django'), ('React Native', 'React Native')], default='Django', max_length=20)),
                ('domain_name', models.CharField(blank=True, max_length=50, null=True)),
                ('screenshot', models.URLField(blank=True, null=True)),
                ('subscription', models.IntegerField(blank=True, null=True)),
                ('user', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(editable=False, null=True)),
                ('active', models.BooleanField(default=True)),
                ('user', models.IntegerField()),
                ('plan', models.IntegerField()),
                ('app', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
