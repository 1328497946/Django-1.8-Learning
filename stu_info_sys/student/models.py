from django.db import models

class DEPARTMENT(models.Model):
    ID = models.CharField(max_length=20, verbose_name="学院编号", primary_key=True)
    NAME_DEP = models.CharField(max_length=50, verbose_name="全称")


    class Meta:
        db_table = "DEPARTMENT"
        verbose_name = "院系"
        verbose_name_plural = "院系信息表"


    def __str__(self):
        return self.NAME_DEP


class CLASS(models.Model):
    ID = models.CharField(max_length=20, verbose_name="班级编号", primary_key=True)
    NAME_CLA = models.CharField(max_length=50, verbose_name="全称", null=True)


    class Meta:
        db_table = "CLASS"
        verbose_name = "班级"
        verbose_name_plural = "班级信息表"

    
    def __str__(self):
        if self.NAME_CLA:
            return self.NAME_CLA
        else:
            return "尚未分配班级"


class STUDENT(models.Model):
    sex_choice = (('男', '男'), ('女', '女'))
    STUDENTID = models.CharField(max_length=20, verbose_name="学号", primary_key=True)
    NAME_STU = models.CharField(max_length=10, verbose_name="姓名")
    SEX = models.CharField(max_length=1, choices=sex_choice, verbose_name="性别")
    NAME_CLA = models.ForeignKey(CLASS, verbose_name="班级", on_delete=models.CASCADE, null=True)
    NAME_DEP = models.ForeignKey(DEPARTMENT, verbose_name="院系", on_delete=models.CASCADE)
    BIRTHDAY = models.DateField(verbose_name="生日")
    NATIVE_PLACE = models.CharField(max_length=50, verbose_name="籍贯")
    PASSWORD = models.CharField(max_length=20, verbose_name="密码", default='123456')


    class Meta:
        verbose_name = "学生"
        db_table = "STUDENT"
        verbose_name_plural = "学生个人信息表"


    def __str__(self):
        return self.NAME_STU


class CHANGE_CODE(models.Model):
    CODE = models.IntegerField(verbose_name="代码", primary_key=True)
    DESCRIPTION = models.CharField(max_length=10, verbose_name="描述")


    class Meta:
        db_table = "CHANGE_CODE"
        verbose_name = "学籍变动"
        verbose_name_plural = "学籍变动代码表"


    def __str__(self):
        return self.DESCRIPTION


class REWARD_LEVELS(models.Model):
    LEVELS = models.IntegerField(verbose_name="级别", primary_key=True)
    DESCRIPTION = models.CharField(max_length=10, verbose_name="描述")


    class Meta:
        db_table = "REWARD_LEVELS"
        verbose_name = "奖励级别"
        verbose_name_plural = "奖励级别表"


    def __str__(self):
        return self.DESCRIPTION


class PUNISH_LEVELS(models.Model):
    LEVELS = models.IntegerField(verbose_name="级别")
    DESCRIPTION = models.CharField(max_length=10, verbose_name="描述")


    class Meta:
        db_table = "PUNISH_LEVELS"
        verbose_name = "处罚级别"
        verbose_name_plural = "处罚级别代码表"


    def __str__(self):
        return self.DESCRIPTION


class CHANGE(models.Model):
    ID = models.CharField(max_length=20, verbose_name="记录号", primary_key=True)
    STUDENTID = models.ForeignKey(STUDENT, verbose_name="学号", on_delete=models.CASCADE)
    CODE  = models.ForeignKey(CHANGE_CODE, verbose_name="变更代码", on_delete=models.CASCADE)
    DESCRIPTION = models.TextField(verbose_name="描述")


    class Meta:
        db_table = "CHANGE"
        verbose_name = "学籍变更"
        verbose_name_plural = "学籍变更记录"


    def __str__(self):
        return self.DESCRIPTION

    
class REWARD(models.Model):
    ID = models.CharField(max_length=20, verbose_name="记录号", primary_key=True)
    STUDENTID = models.ForeignKey(STUDENT, verbose_name="学号", on_delete=models.CASCADE)
    LEVELS = models.ForeignKey(REWARD_LEVELS, verbose_name="级别代码", on_delete=models.CASCADE)
    REC_TIME = models.DateField(verbose_name="记录时间")
    DESCRIPTION = models.TextField(verbose_name="描述")

    
    class Meta:
        db_table = "REWARD"
        verbose_name = "奖励记录"
        verbose_name_plural = "奖励记录"


    def __str__(self):
        return self.DESCRIPTION


class PUNISH(models.Model):
    enable_choice = ((True, '是'), (False, '否'))
    ID = models.CharField(max_length=20, verbose_name="记录号", primary_key=True)
    STUDENTID = models.ForeignKey(STUDENT, verbose_name="学号", on_delete=models.CASCADE)
    LEVELS = models.ForeignKey(PUNISH_LEVELS, verbose_name="级别代码", on_delete=models.CASCADE)
    ENABLE = models.BooleanField(choices=enable_choice, verbose_name="是否生效")
    REC_TIME = models.DateField(verbose_name="记录时间")
    DESCRIPTION = models.TextField(verbose_name="描述")


    class Meta:
        db_table = "PUNISH"
        verbose_name = "处罚记录"
        verbose_name_plural = "处罚记录"


    def __str__(self):
        return self.DESCRIPTION
# Create your models here.
