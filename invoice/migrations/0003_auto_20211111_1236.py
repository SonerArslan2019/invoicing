# Generated by Django 3.2.9 on 2021-11-11 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20211111_0833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('CURRENT', 'CURRENT'), ('EMAIL_SENT', 'EMAIL_SENT'), ('OVERDUE', 'OVERDUE'), ('PAID', 'PAID')], default='CURRENT', max_length=100),
        ),
    ]
