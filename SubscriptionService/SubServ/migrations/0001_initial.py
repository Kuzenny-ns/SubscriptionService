# Generated by Django 4.1.3 on 2022-11-28 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productID', models.AutoField(primary_key=True, serialize=False)),
                ('productType', models.CharField(max_length=50)),
                ('productFormFactor', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('serviceID', models.AutoField(primary_key=True, serialize=False)),
                ('serviceName', models.CharField(max_length=50)),
                ('serviceDescription', models.CharField(max_length=350)),
                ('servicePhotoURL', models.CharField(max_length=1000)),
                ('serviceCategory', models.CharField(blank=True, max_length=50)),
                ('servicePrice', models.DecimalField(decimal_places=2, max_digits=6)),
                ('serviceFrequncy', models.IntegerField()),
                ('serviceProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubServ.product')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=50)),
                ('userlogin', models.CharField(max_length=50)),
                ('userEmail', models.EmailField(db_index=True, max_length=254)),
                ('userPassword', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('subscriptionID', models.AutoField(primary_key=True, serialize=False)),
                ('subscriptionTimeSpan', models.DateField()),
                ('subscriptionAddress', models.CharField(max_length=50)),
                ('subscriptionService', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubServ.service')),
                ('subscriptionSubscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubServ.user')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('providerID', models.AutoField(primary_key=True, serialize=False)),
                ('providerName', models.CharField(max_length=50)),
                ('providerDescription', models.CharField(max_length=350)),
                ('providerService', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubServ.service')),
                ('providerUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubServ.user')),
            ],
        ),
    ]