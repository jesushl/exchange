from django.db import models


class  ExchangeSource(models.Model):
    banco_de_mexico = 'BM'
    fixer = 'FR'
    diario='DO'
    AVAILABLE_EXCHANGES = [
        (banco_de_mexico, 'Banco de Mexico'),
        (fixer, 'Fixer'),
        (diario, 'Diario Oficial de la Federacion'),
    ]
    AVAILABLE_EXCHANGES_dict = {
        banco_de_mexico: "Banco de Mexico",
        fixer: "Fixer",
        diario: "Diario oficial"
    }
    name = models.CharField(
        max_length=2,
        choices=AVAILABLE_EXCHANGES,
        null=False,
        blank=False
    )
    def __str__(self):
        return self.AVAILABLE_EXCHANGES_dict[self.name]
    
class Exchange(models.Model):
    exchange = models.ForeignKey(
        ExchangeSource,
        on_delete=models.CASCADE,# not sure if is ok but if a source is not relevant is ok remove it ... i guess
        null=False,
        blank=False
    )
    price = models.FloatField()
    date_from_source = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        _ = "source: {self.exchange}  value: {self.value}, last_updated: {self.date_from_source}"
        return _.format(self=self)
