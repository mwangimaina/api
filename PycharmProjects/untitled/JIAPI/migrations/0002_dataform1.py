# Generated by Django 2.0.6 on 2018-06-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JIAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataForm1',
            fields=[
                ('_id', models.IntegerField(primary_key=True, serialize=False)),
                ('event_date', models.CharField(max_length=30)),
                ('start_time', models.CharField(max_length=30)),
                ('stop_time', models.CharField(max_length=30)),
                ('s_county', models.CharField(max_length=30)),
                ('sub_county', models.CharField(max_length=30)),
                ('s_village', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=30)),
                ('s_activity', models.CharField(max_length=30)),
                ('s_output', models.CharField(max_length=30)),
                ('s_cost', models.CharField(max_length=30)),
                ('facility_name', models.CharField(max_length=30)),
                ('facility_type', models.CharField(max_length=30)),
                ('lat', models.CharField(max_length=30)),
                ('lon', models.CharField(max_length=30)),
                ('officer_name', models.CharField(max_length=30)),
            ],
        ),
    ]
