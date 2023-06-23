# Generated by Django 3.2.16 on 2023-02-24 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='category',
            new_name='categ',
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=159, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('img', models.ImageField(upload_to='product')),
                ('desc', models.TextField()),
                ('stock', models.IntegerField()),
                ('available', models.BooleanField()),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categ')),
            ],
        ),
    ]
