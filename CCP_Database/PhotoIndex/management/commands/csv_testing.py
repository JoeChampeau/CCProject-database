import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from PhotoIndex.models import Item, AccessionNumber, DateRange, Directory

class Command(BaseCommand):
    help = 'Reading csv stuff (testing)'

    def handle(self, *args, **options):
        cc = pd.read_csv('PhotoIndex/csvs/center_csv.csv')
        cc_filtered = cc[cc["Accession #"] == cc["Accession #"]]

        def nanstring(str):
            return str if str == str else ""

        def checkIsInclude(str):
            return str != str or not (str in ["Envelope", "Note"])

        def aggregateDescs(index, desc):
            index += 1
            while index <= (len(cc.index) - 1) and cc.loc[index]["Accession #"] != cc.loc[index]["Accession #"]:
                new_desc = cc.loc[index]["Notes"]
                new_desc = new_desc if new_desc == new_desc else ""
                desc += f'{";;" if not (new_desc == "" or desc == "") else ""}{new_desc}'
                index += 1
            return desc

        for i, data in cc_filtered.iterrows():
            if not checkIsInclude(data["Number ([Street #(s)], [Block]-[Parcel/Lot])"]):
                continue
            a_num = data["Accession #"].split('.')
            accession = AccessionNumber.objects.create(year=int(a_num[0]), collection=int(a_num[1]), index=int(a_num[2]))
            accession.save()
            description = data["Description"]
            folder = Directory.objects.filter(name="Center Street").first()
            notes = aggregateDescs(i, nanstring(data["Notes"]))
            date = DateRange()
            date.save()
            new_item = Item.objects.create(accession=accession, description=description, parent=folder, notes=notes, date_range=date)
            new_item.save()