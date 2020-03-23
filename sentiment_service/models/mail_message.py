from django.db import models
from django.conf import settings
from ..sentiment import cal_sentiment
from ..cleantext import clean
from ..elastic import ingest


class Mail(models.Model):
    From = models.CharField(max_length=20)
    To = models.CharField(max_length=255)
    Body = models.TextField()
    Importance = models.TextField(choices=[('High', 'High'), ('Low', 'Low'), ('Normal', 'Normal')])
    Polarity = models.CharField(max_length=10, blank=True)
    Sentiment = models.CharField(max_length=10, blank=True)

    def save(self, *args, **kwargs):
        clean_text = clean(self.Body)
        self.Polarity, self.Sentiment = cal_sentiment(clean_text)
        super(Mail, self).save(*args, **kwargs)
        ingest(doc=self.create_document())

    def create_document(self):
        return {"From": self.From,
                "To": self.To,
                "Body": self.Body,
                "Impotance": self.Importance,
                "Polarity": self.Polarity,
                "Sentiment": self.Sentiment}




