# Generated by Django 4.0.2 on 2023-05-16 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Invitation',
                'verbose_name_plural': 'Invitations',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('invitation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.invitation')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
    ]