# Generated by Django 2.2.11 on 2020-05-27 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datamodel", "0002_auto_20200527_1047"),
    ]

    operations = [
        migrations.RenameField(
            model_name="klantadres", old_name="aoa_huisletter", new_name="huisletter",
        ),
        migrations.RenameField(
            model_name="klantadres", old_name="aoa_huisnummer", new_name="huisnummer",
        ),
        migrations.RenameField(
            model_name="klantadres",
            old_name="aoa_huisnummertoevoeging",
            new_name="huisnummertoevoeging",
        ),
        migrations.RenameField(
            model_name="klantadres", old_name="aoa_postcode", new_name="postcode",
        ),
        migrations.RenameField(
            model_name="klantadres",
            old_name="wpl_woonplaats_naam",
            new_name="woonplaats_naam",
        ),
        migrations.RemoveField(model_name="klantadres", name="aoa_identificatie",),
        migrations.RemoveField(
            model_name="klantadres", name="gor_openbare_ruimte_naam",
        ),
        migrations.RemoveField(
            model_name="klantadres", name="inp_locatiebeschrijving",
        ),
        migrations.RemoveField(model_name="klantadres", name="natuurlijkpersoon",),
        migrations.RemoveField(model_name="klantadres", name="vestiging",),
        migrations.AddField(
            model_name="klantadres",
            name="landcode",
            field=models.CharField(
                default="",
                help_text="De code, behorende bij de landnaam, zoals opgenomen in de Land/Gebied-tabel van de BRP.",
                max_length=4,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="klantadres",
            name="straatnaam",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
