# Generated by Django 2.2.1 on 2019-06-12 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0006_auto_20190611_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='btitle',
            field=models.CharField(max_length=20, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.BookInfo', verbose_name='书名'),
        ),
    ]
