from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0021_auto_20180507_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_id', models.CharField(max_length=50, verbose_name='title id')),
                ('language', models.CharField(max_length=15, verbose_name='language')),
                ('creation_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='creation date')),
                ('published', models.BooleanField(blank=True)),
                ('publisher_is_draft', models.BooleanField()),
                ('publisher_state', models.SmallIntegerField()),
                ('opposite_number_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='publisher public id')),
                ('page_id', models.CharField(max_length=50, verbose_name='page id')),
                ('page_opposite_number_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='publisher public id')),
                ('page_publisher_is_draft', models.BooleanField()),
                ('path', models.CharField(max_length=255, verbose_name='path')),
            ],
        ),
    ]
