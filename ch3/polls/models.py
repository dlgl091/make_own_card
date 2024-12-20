from django.db import models

# Create your models here.

class TemplateCard(models.Model):
    card_no = models.IntegerField(primary_key=True)  # cardNo
    card_name = models.CharField(max_length=20)     # cardName
    category = models.CharField(max_length=10)      # category
    img_link = models.URLField(unique=True, max_length=200)  # imgLink
    reg_date = models.DateTimeField(auto_now_add=True)  # regDate (자동 생성 시간)

    class Meta:
        db_table = 'templateCard'  # 테이블 이름 지정
        verbose_name = 'Template Card'
        verbose_name_plural = 'Template Cards'

    def __str__(self):
        return self.card_name


class GeneratedCard(models.Model):
    gen_no = models.AutoField(primary_key=True)  # genNo (자동 증가)
    card_no = models.ForeignKey(
        TemplateCard,
        on_delete=models.CASCADE,
        db_column='cardNo'  # MySQL의 cardNo와 매핑
    )
    category = models.CharField(max_length=10)  # category
    gen_img_link = models.URLField(unique=True, max_length=200)  # genImgLink
    gen_date = models.DateTimeField(auto_now_add=True)  # genDate (자동 생성 시간)

    class Meta:
        db_table = 'generatedCard'  # 테이블 이름 지정
        verbose_name = 'Generated Card'
        verbose_name_plural = 'Generated Cards'

    def __str__(self):
        return f"GeneratedCard {self.gen_no}"
