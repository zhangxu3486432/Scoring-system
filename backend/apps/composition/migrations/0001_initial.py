# Generated by Django 2.1.7 on 2019-03-25 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompositionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='编号')),
                ('name', models.CharField(max_length=256, verbose_name='作品名称')),
                ('competition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='competition.CompetitionModel')),
            ],
        ),
    ]
