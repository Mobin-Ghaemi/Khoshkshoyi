# Generated by Django 5.0.3 on 2024-08-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_open_open_alter_sefaresh_vaziat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sefaresh',
            name='vaziat',
            field=models.CharField(choices=[('در حال شست و شو ', 'در حال شست و شو'), ('اماده ی تحویل', 'اماده ی تحویل'), ('تحویل مشتری داده شد', 'تحویل مشتری داده شد ')], default='0', max_length=30, verbose_name='وضعیت سفارش :'),
        ),
    ]
