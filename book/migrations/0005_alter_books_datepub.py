# Generated by Django 4.0.4 on 2022-06-02 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_books_datepub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='datepub',
            field=models.DateTimeField(null=True),
        ),
    ]