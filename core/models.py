from django.db import models

class Client(models.Model):
    last_name = models.CharField("Фамилия и Имя", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    visits = models.IntegerField("Количество занятий", default=8)
    payment_date = models.DateField("Дата оплаты")
    start_date = models.DateField("Дата первого занятия")
    expiry_date = models.DateField("Дата следующей оплаты")
    days_of_week = models.CharField("Дни недели", max_length=50, blank=True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"