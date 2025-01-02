from django.db import models

# Create your models here.

class TemplateCard(models.Model):
    cardNo = models.IntegerField(primary_key=True)  # cardNo
    cardName = models.CharField(max_length=20)     # cardName
    category = models.CharField(max_length=10)      # category
    imgLink = models.URLField(unique=True, max_length=200)  # imgLink
    regDate = models.DateTimeField(auto_now_add=True)  # regDate (자동 생성 시간)

    class Meta:
        db_table = 'templateCard'  # 테이블 이름 지정
        verbose_name = 'Template Card'
        verbose_name_plural = 'Template Cards'

    def __str__(self):
        return self.card_name


class GeneratedCard(models.Model):
    genNo = models.AutoField(primary_key=True)  # genNo (자동 증가)
    cardNo = models.ForeignKey(
        TemplateCard,
        on_delete=models.CASCADE,
        db_column='cardNo'  # MySQL의 cardNo와 매핑
    )
    cardName = models.CharField(max_length=20, default="None")  # category
    genImgLink = models.ImageField(null=True, upload_to="", blank=True)  # genImgLink
    text1 = models.CharField(max_length=20, default="")
    text2 = models.CharField(max_length=20, default="")
    genDate = models.DateTimeField(auto_now_add=True)  # genDate (자동 생성 시간)

    class Meta:
        db_table = 'generatedCard'  # 테이블 이름 지정
        verbose_name = 'Generated Card'
        verbose_name_plural = 'Generated Cards'

    def __str__(self):
        return f"GeneratedCard {self.gen_no}"
