from django import template
from ..models import BRNC, UNIST

register = template.Library()


@register.simple_tag
def sort_data(data):
    data_list = []
    system_list = BRNC.objects.values_list('system', flat=True).distinct()
    nation_list = BRNC.objects.values_list('nation', flat=True).distinct()
    for system in system_list:
        object_list = data.filter(system=system)
        choices = {k:v for k,v in BRNC.SYSTEM_CHOICES}
        s = choices.get(system)
        for nation in nation_list:
            objects = object_list.filter(nation=nation)
            dic = {'system': s, 'nation': nation, 'objects': objects}
            data_list.append(dic)
    return data_list
"""
@register.simple_tag
def unist_table(data):
    data_list = []
    develop_list = ['개념화', '부지조사/선정', '기준 설계/인허가 신청', '건설', '운영', '폐쇄']
    eval_list = [('Safety Context',''), ('안전전략',''), ('평가 베이시스',('부지 특성', '처분장 설계','안전성 평가 방법론')), ('안전성 평가',('운영 중 안정성 평가', '폐쇄 후 안전성 평가')), ('관리 시스템/이해관계자 및 규제기관 참여',''), ('증거들의 종합',''), ('불확실성 관리',''), ('한계점, 통제 및 조건','')]
    for eval in eval_list:
        row_data = []
        if eval[1] != '' and len(eval[1]) == 3:
            object_list = data.filter(evaluation=eval[0], evaluation1=eval[1][0], evaluation2=eval[1][1], evaluation3=eval[1][2])
        elif eval[1] != '' and len(eval[1]) == 2:
            object_list = data.filter(evaluation=eval[0], evaluation1=eval[1][0], evaluation2=eval[1][1])
        else:
            object_list = data.filter(evaluation=eval[0])
        for develop in develop_list:
            epg_objects = object_list.filter(epg__isnull=False).filter(develop=develop)
            objects = object_list.filter(epg__isnull=True).filter(develop=develop)
            obj = [epg_objects, objects]
            row_data.append(obj)
        data_list.append(row_data)
    return data_list
"""