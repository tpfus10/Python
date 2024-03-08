#'키-값' 쌍의 값을 받는 임의 인수(**kwargs)
#매개변수 앞에 **를 써주면 됨
#인수를 전달할 때도 '키-값' 쌍의 형태로 입력해야 하며, 개수 제한이 없음
def build_profile(first, last, **user_info):
    """사용자에 대해 아는 정보를 전부 딕셔너리에 저장합니다"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile1 = build_profile('albert', 'einstein',
                             location= 'princenton',
                             field='physics',
                             sex= 'male')

print(user_profile1)