import re

def grade(input):
	n = 0
	cnt = 0
	cat_list = []
	flag = False
	grade_list = [[], []]
	point = []
	for line in input.splitlines(True) :
		pattern = re.compile(r'^\s+(.+)\s\t(\d)\s\t\d*\s*\t([^\s]+)\s\t\d{4}\s\t[^\s]+\s?[\r\n]?$')
		grade = pattern.sub(r'\3', line)
		if (grade == '不'):
			continue 
		name = pattern.sub(r'\1', line)
		num = pattern.sub(r'\2', line)
		if '\n' in name :
			new = re.sub(r'^\s{9}(.*)\r\n$', r'\1', name)
			if (name != new) :
				grade_list[0].append(new)
			if (flag) :
				grade_list[1].append(point)
				point = []
				n += 1
				flag = False
				cnt = 0
		else:
			point.append([name, num])
			cnt += 1
			flag = True
	grade_list[1].append(point)
	# print(grade_list)

	cat_list = [["主題A",  "主題B", "主題C-基礎科目", "主題C-講義科目", "主題C-実践科目", "大学入門ゼミ", "情報リテラシー", "学問基礎科目(文系）", "学問基礎科目(理系）", "健康・スポーツ実技", "高度教養教育科目・広範教養教育科目", "初修外国語", "既修外国語", "倫理（必修）", "コミュニケーション能力（必修）", "コミュニケーション能力（選択）", "デザイン思考能力（必修）", "デザイン思考能力（選択）", "リスクマネジメント能力（必修）", "リスクマネジメント能力（選択）", "数理的基礎能力（必修）", "数理的基礎能力（選択）", "多角的思考能力（選択）", "コース専門科目：必修科目", "コース専門科目：選択科目", "卒業研究・卒業制作", "自由科目", "教職科目"], []]
	for cat in cat_list[0] :
		if cat in grade_list[0] :
			cat_list[1].append(grade_list[1][grade_list[0].index(cat)])
		else:
			cat_list[1].append([])
	# print(cat_list)

	fact_cat_list = [[["主題A", 1], ["主題B", 4], ["主題C-基礎科目", 1], ["主題C-講義科目", 2], ["主題C-実践科目", 2], ["大学入門ゼミ", 2], ["情報リテラシー", 2], ["学問基礎科目(文系）", 4], ["学問基礎科目(理系）", 4], ["健康・スポーツ実技", 2], ["高度教養教育科目・広範教養教育科目", 4], ["初修外国語", 4], ["既修外国語", 6], ["倫理", 1], ["コミュニケーション能力", 4], ["デザイン思考能力", 4], ["リスクマネジメント能力", 3], ["数理的基礎能力", 6], ["多角的思考能力", 2], ["コース専門科目", 58], ["卒業研究・卒業制作", 8], ["自由科目", 6], ["教職科目", 0]], []]
	for lcat in fact_cat_list[0] :
		cat = lcat[0]
		if cat in cat_list[0] :
			fact_cat_list[1].append(cat_list[1][cat_list[0].index(cat)])
		else:
			if (cat == '倫理') :
				fact_cat_list[1].append(cat_list[1][cat_list[0].index('倫理（必修）')])
			elif (cat == 'コミュニケーション能力') :
				fact_cat_list[1].append(cat_list[1][cat_list[0].index('コミュニケーション能力（必修）')] + cat_list[1][cat_list[0].index('コミュニケーション能力（選択）')])
			elif (cat == 'デザイン思考能力') :
				fact_cat_list[1].append(cat_list[1][cat_list[0].index('デザイン思考能力（必修）')] + cat_list[1][cat_list[0].index('デザイン思考能力（選択）')])
			elif (cat == 'リスクマネジメント能力') :
				fact_cat_list[1].append(cat_list[1][cat_list[0].index('リスクマネジメント能力（必修）')] + cat_list[1][cat_list[0].index('リスクマネジメント能力（選択）')])
			elif (cat == '数理的基礎能力') :
				fact_cat_list[1].append(cat_list[1][cat_list[0].index('数理的基礎能力（必修）')] + cat_list[1][cat_list[0].index('数理的基礎能力（選択）')])
			elif (cat == '多角的思考能力') :
				fact_cat_list[1].append(cat_list[1][cat_list[0].index('多角的思考能力（選択）')])
			elif (cat == 'コース専門科目') :
				fact_cat_list[1].append(cat_list[1][cat_list[0].index('コース専門科目：必修科目')] + cat_list[1][cat_list[0].index('コース専門科目：選択科目')])
	# print(fact_cat_list)
	return fact_cat_list