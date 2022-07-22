# Generated by Django 4.0.6 on 2022-07-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_watch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_model', models.CharField(max_length=100)),
                ('model_price', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('color', models.CharField(max_length=20)),
                ('diagonal', models.PositiveIntegerField()),
                ('wifi', models.BooleanField(default=True)),
            ],
        ),
    ]
