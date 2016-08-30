# _*_ coding: utf-8 _*_
import sys
"""리스트를 출력하는 모듈"""
def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    """이 함수는 the_list라는 인자를 가지고 있으며 파이썬 리스트를 받습니다.
    리스트, 하위리스트를 출력합니다 재귀를 이용해서 중첩되는 하위 리스트 까지
    출력할수 있습니다."""
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent == True:
                for tab_num in range(level):
                    print >> fh, '\t'#print('\t'),    #python2.7 / python3 print('\t', end='', file=fh)
            print >> fh, each_item #print(each_item)    #python3 print(each_item, file=fh)
