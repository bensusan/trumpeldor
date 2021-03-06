# Generated by Django 2.1.4 on 2019-06-16 07:58

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AmericanQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', django.contrib.postgres.fields.jsonb.JSONField()),
                ('indexOfCorrectAnswer', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('description', models.TextField()),
                ('picturesURLS', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('videosURLS', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('kind', models.CharField(choices=[('FT', 'FeedbackText'), ('FR', 'FeedbackRating')], default='FT', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('feedback', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Server.Feedback')),
            ],
        ),
        migrations.CreateModel(
            name='Hint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('HT', 'HintText'), ('HP', 'HintPicture'), ('HV', 'HintVideo')], default='HT', max_length=2)),
                ('data', models.TextField()),
                ('description', models.TextField()),
                ('attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Server.Attraction')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.TextField()),
                ('about_app', models.TextField()),
                ('how_to_play', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('fileURL', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('data', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boundaries', django.contrib.postgres.fields.jsonb.JSONField()),
                ('loginHours', models.IntegerField(default=36)),
                ('scoreRules', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField()),
                ('points', models.ManyToManyField(to='Server.Attraction')),
                ('subTrack', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Server.Track')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.TextField()),
                ('playersAges', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('score', models.IntegerField(default=0)),
                ('attractionsDone', models.ManyToManyField(to='Server.Attraction')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Server.Track')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('socialNetwork', models.TextField()),
                ('lastSeen', models.DateTimeField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FindTheDifferences',
            fields=[
                ('entertainment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Server.Entertainment')),
                ('pictureURL', models.TextField()),
                ('differences', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            bases=('Server.entertainment',),
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('entertainment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Server.Entertainment')),
                ('piecesURLS', django.contrib.postgres.fields.jsonb.JSONField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
            bases=('Server.entertainment',),
        ),
        migrations.CreateModel(
            name='SlidingPuzzle',
            fields=[
                ('entertainment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Server.Entertainment')),
                ('piecesURLS', django.contrib.postgres.fields.jsonb.JSONField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
            ],
            bases=('Server.entertainment',),
        ),
        migrations.CreateModel(
            name='TakingPicture',
            fields=[
                ('entertainment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Server.Entertainment')),
            ],
            bases=('Server.entertainment',),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('name', 'socialNetwork')},
        ),
        migrations.AddField(
            model_name='trip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Server.User'),
        ),
        migrations.AddField(
            model_name='feedbackinstance',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Server.Trip'),
        ),
        migrations.AddField(
            model_name='entertainment',
            name='attraction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Server.Attraction'),
        ),
        migrations.AddField(
            model_name='americanquestion',
            name='attraction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Server.Attraction'),
        ),
        migrations.AlterUniqueTogether(
            name='feedbackinstance',
            unique_together={('feedback', 'trip')},
        ),
    ]
