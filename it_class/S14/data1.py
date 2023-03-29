from faker import Faker
from faker.providers import job

fake = Faker("ro_RO")

for i in range(2):
    print(fake.name())

print(fake.address())

for i in range(2):
    print(fake.job())

