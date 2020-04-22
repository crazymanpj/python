from zhihu import Question

url = "https://www.zhihu.com/question/40783253"
question = Question(url)
print question
answers = question.get_all_answers()
print answers
# ��ȡ������ı���
title = question.get_title()
print title
# ��ȡ���������ϸ����
detail = question.get_detail()
print detail
# ��ȡ�ش����
answers_num = question.get_answers_num()
print answers_num
# ��ȡ��ע�����������
followers_num = question.get_followers_num()
print followers_num
# ��ȡ��������������
topics = question.get_topics()
for topic in topics:
    print topic
# ��ȡ�����ⱻ�������
visit_times = question.get_visit_times()
print visit_times
# ��ȡ������һ�Ļش�
top_answer = question.get_top_answer()
print top_answer
# ��ȡ����ǰʮ��ʮ���ش�
top_answers = question.get_top_i_answers(10)
print top_answers
# ��ȡ���лش�
answers = question.get_all_answers()
i=0

print title  # �������ʵ�����ж����ã�
print detail
# �����
# ����������ڡ���ʵ���Զ�п᣿�����ţ���ʵ�����ж�п᣿
# ������       ���쿴�ˡ���ʵ�����ж�пᡰ���о���̫�ã�������
# ����������������Ӧ��ϣ���ܹ����к�һ�¡������Ǹ�������������
# ������ɡ��ȲҴ�ᡰһ������Ҳ����������ɡ��������»ᡰ������
# �ǡ�ɹ�Ҹ������������Դ�Ҵӡ���ʵ��ʵ�ʡ��ĽǶȳ����������Լ���
# ���ù��£��ô�ҿ����������ů���ܸ��ӱ�֤�ؿ������磬�Ǵ�
# ��ͱ��⹲ͬ�ġ���Ը���ɡ�
print answers_num  # �����2441
print followers_num  # �����26910
for topic in topics:
    print topic,  # �������п��� ��ʵ ��� ���˾���
print visit_times  # ���: �����⵱ǰ������Ĵ���
print top_answer
# �����<zhihu.Answer instance at 0x7f8b6582d0e0>
# Answer�����
print top_answers
# �����<generator object get_top_i_answers at 0x7fed676eb320>
# ����ǰʮ��Answer��������
print answers
# �����<generator object get_all_answer at 0x7f8b66ba30a0>
# ��������Answer��������
for answer in answers:
    answer.to_txt()
    answer.to_md()