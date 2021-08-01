# Generated by Django 3.2.4 on 2021-07-31 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('emailid', models.CharField(max_length=100)),
                ('phoneno', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('dob', models.DateField()),
                ('technicalskills', models.CharField(max_length=100)),
                ('projects', models.TextField()),
                ('internship', models.CharField(max_length=300)),
                ('schoolname', models.CharField(default='ABC', max_length=50)),
                ('schoolqualification', models.CharField(max_length=50)),
                ('schoolduration', models.IntegerField()),
                ('collegename', models.CharField(default='ABC', max_length=50)),
                ('collegequalification', models.CharField(max_length=50)),
                ('collegeduration', models.IntegerField()),
                ('graduatedcollegename', models.CharField(default='ABC', max_length=50)),
                ('graduatequalification', models.CharField(max_length=50)),
                ('graduateduration', models.IntegerField()),
                ('hobbies', models.CharField(max_length=300)),
                ('languagesknown', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=30)),
                ('certification', models.TextField()),
                ('state', models.CharField(max_length=100)),
                ('maritalstatus', models.CharField(max_length=40)),
                ('summary', models.TextField()),
            ],
        ),
    ]
