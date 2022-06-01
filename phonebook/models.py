from core.db import Base
from sqlalchemy import Column, Integer, String

class Post(Base):
    __tablename__ = "posts"


class Phone(Base):
    __tablename__ = "phones"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    number = Column(String) # 0079991234567
    # ??? # тип звонящего
    # Официальный телефон bool?
    # ссылка на подтверждение

    # number: 0079037011109
    # name: Билайн задолженность #aproved

class PhoneComment(Base):
    id = Column(Integer, primary_key=True)
    number = Column(String)
    # status [negative/positive
    # comment # text(500)
    # источник (сайт такой-то)

    # number: 0079037011109
    # comment: Предупредили о необходимости внести оплату за тариф
    # comments[1002]

# text:
# Хлопец с украинским акцентом Представился сотрудником сбербанка (Scam call) reported by Петр
# Под видом проверки от имени сбербанка узнают номера карт, счетов, кабинетов и пароли



# class Contact(Base):
#     __tablename__ = 'phonebook'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     number = Column(String(20), nullable=False)



# class Persone(models.Model):
#     name = models.CharField("Contact name", max_length=70)
#
#     def __str__(self):
#         return self.name
#
#     def all_phones_to_string(self):
#         return ", ".join([phone.phone for phone in self.phones.all()])
#
#
# class Phone(models.Model):
#     phone = models.CharField(
#         verbose_name="Phone",
#         max_length=12
#     )
#     contact = models.ForeignKey(
#         Persone,
#         related_name="phones",
#         on_delete=models.CASCADE
#     )
#
#     def __str__(self):
#         return self.phone