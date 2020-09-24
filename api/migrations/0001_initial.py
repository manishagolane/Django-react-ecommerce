from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name ="Manisha",
                          email = "manishagolane@gmail.com",
                          is_staff = True,
                          is_superuser = True,
                          phone = "9752742797",
                          gender = "Female"
                        )

        user.set_password("1manisha@")
        user.save()

    dependencies = [


        ]


    operations = [

        migrations.RunPython(seed_data),
    ]