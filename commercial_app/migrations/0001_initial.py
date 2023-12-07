# Generated by Django 5.0 on 2023-12-07 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommercialProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('building_type', models.CharField(default='1', max_length=255)),
                ('ownership', models.CharField(default='ABC', max_length=255)),
                ('lot_size', models.PositiveIntegerField(default=0)),
                ('building_size', models.PositiveIntegerField(default=0)),
                ('price_per_square_meter', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_asking_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_price_offered', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_price_agreed', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('deal_status', models.CharField(default='FORSALE', max_length=255)),
                ('listing_date', models.DateField()),
                ('listing_agent_name', models.CharField(default='', max_length=255)),
                ('listing_agent_phone', models.CharField(default='000000', max_length=20)),
                ('description', models.TextField(default='')),
                ('deal_comments', models.TextField(default='')),
            ],
        ),
    ]
