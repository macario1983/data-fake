from faker import Faker
import random

fake = Faker("pt_BR")


for _ in range(10_000):
    nome = fake.name()
    idade = random.randint(3, 17)
    email = fake.email()
    sexo = random.choice(["M", "F"])
    print('INSERT INTO aluno (nome, idade, email, sexo) VALUES ' f"('{nome}', {idade}, '{email}', '{sexo}');")