import csv

from django.core.management.base import BaseCommand

from Passenger.models import User_war_struck


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("csv_file")

    def handle(self, *args, **kwargs):
        csv_file = kwargs["csv_file"]

        with open(csv_file, encoding="utf-8") as f:

            reader = csv.DictReader(f)

            for row in reader:

                if User_war_struck.objects.filter(
                    username=row["user"]
                ).exists():

                    self.stdout.write(
                        f"{row['user']} exists"
                    )
                    continue

                user = User_war_struck.objects.create_user(

                    username=row["username"],

                    email=row["email"],

                    password=row["password"],

                    phone=row["phone"],

                    NationalCode=row["national_code"],

                    Job_title=row["job"],
                )

                self.stdout.write(
                    self.style.SUCCESS(
                        f"{user.username} imported"
                    )
                )