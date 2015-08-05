#coding:utf-8
from django import forms

class AddCat(forms.Form):
    cat_name = forms.CharField(label=u'分类名称',error_messages={'required':u'分类名称不能为空'},)
    #cat_father = forms.IntegerField(label=u'父类',show_hidden_initial=True)


class EditCat(forms.Form):
    cat_name = forms.CharField(label=u'分类名称',error_messages={'required':u'分类名称不能为空'},)

