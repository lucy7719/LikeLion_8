# Generated by Django 3.0.6 on 2020-06-29 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='작품 이름을 입력해 주세요', max_length=100)),
                ('reason', models.TextField(default='이 작품을 선정한 이유는 무엇인가요?')),
            ],
        ),
    ]
