# Generated by Django 4.1.5 on 2023-01-05 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProfileDetails",
            fields=[
                ("Id", models.BigAutoField(primary_key=True, serialize=False)),
                ("Name", models.CharField(max_length=70)),
                ("Birth_Date", models.DateField()),
                (
                    "Gender",
                    models.CharField(
                        choices=[("F", "Female"), ("M", "Male"), ("O", "Other")],
                        default="i",
                        max_length=15,
                    ),
                ),
                ("Email", models.EmailField(max_length=50)),
                ("Phone", models.IntegerField(max_length=10)),
                ("Locality", models.CharField(max_length=50)),
                ("City", models.CharField(max_length=50)),
                ("State", models.CharField(max_length=50)),
                ("Zip", models.IntegerField(max_length=6)),
                ("Country", models.CharField(max_length=50)),
                (
                    "Profile_Pic",
                    models.ImageField(blank=True, upload_to="profile_pics"),
                ),
            ],
            options={"ordering": ["Id", "Name", "Birth_Date"],},
        ),
    ]
