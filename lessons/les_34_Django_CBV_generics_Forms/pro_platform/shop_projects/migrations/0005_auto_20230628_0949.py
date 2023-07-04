# Generated by Django 4.2.2 on 2023-06-28 09:49

from django.db import migrations

# from shop_projects.models import Project as Project_class

CATEGORY_NAME = "default"


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Category = apps.get_model("shop_projects", "Category")
    Project = apps.get_model("shop_projects", "Project")

    db_alias = schema_editor.connection.alias
    default_category, created = Category.objects.using(db_alias).get_or_create(
        name=CATEGORY_NAME,
        description="default category",
    )
    Project.objects.update(category=default_category)


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Category = apps.get_model("shop_projects", "Category")
    db_alias = schema_editor.connection.alias
    Project = apps.get_model("shop_projects", "Project")
    Project.objects.update(category=None)


class Migration(migrations.Migration):
    dependencies = [
        ("shop_projects", "0004_project_category"),
    ]

    operations = [
        migrations.RunPython(
            code=forwards_func,
            reverse_code=reverse_func,
        )
    ]
