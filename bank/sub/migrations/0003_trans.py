# Generated by Django 3.0.3 on 2021-04-04 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0002_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='trans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer_id', models.CharField(max_length=100)),
                ('payee_id', models.CharField(max_length=100)),
                ('trans_amt', models.IntegerField(default=0)),
            ],
        ),
    ]