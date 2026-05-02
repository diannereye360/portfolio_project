from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contactmessage'),
    ]

    operations = [
        migrations.AddField(model_name='project', name='summary', field=models.CharField(default='', max_length=300)),
        migrations.AddField(model_name='project', name='category', field=models.CharField(default='', max_length=100)),
        migrations.AddField(model_name='project', name='tools_used', field=models.TextField(default='')),
        migrations.AddField(model_name='project', name='key_features', field=models.TextField(default='')),
        migrations.AddField(model_name='project', name='role', field=models.TextField(default='')),
        migrations.AddField(model_name='project', name='challenges', field=models.TextField(default='')),
        migrations.AddField(model_name='project', name='lessons_learned', field=models.TextField(default='')),
        migrations.AddField(model_name='project', name='image_path', field=models.CharField(blank=True, default='', max_length=200)),
        migrations.AddField(model_name='project', name='github_link', field=models.URLField(blank=True, null=True)),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=0)),
            ],
            options={'ordering': ['category', 'order']},
        ),
    ]
