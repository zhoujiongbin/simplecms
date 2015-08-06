#!usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from datetime import datetime

class Power(models.Model):
    level = models.IntegerField(default=0)
    text = models.CharField(max_length=20,default='超级管理员')


class User(models.Model):
    password  = models.BinaryField()
    account = models.CharField(max_length=20,unique=True)
    email = models.EmailField()
    power = models.ForeignKey(Power,default=1)
    joined_time = models.DateTimeField(default=datetime.now)
    last_login = models.TimeField(null=True)
