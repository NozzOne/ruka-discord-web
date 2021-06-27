from django.db import models

# Create your models here.

class card(models.Model):
    name = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    value = models.IntegerField()
    image = models.BinaryField()

    class Meta:
        db_table = 'card'

    def __repr__(self):
        return str(self.image)

#     CREATE TABLE public.card
# (
#     card_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
#     name character varying(255) COLLATE pg_catalog."default" NOT NULL,
#     series character varying(255) COLLATE pg_catalog."default" NOT NULL,
#     value integer NOT NULL,
#     image bytea,
#     CONSTRAINT "PK_card" PRIMARY KEY (card_id)
# )