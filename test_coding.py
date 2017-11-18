# -*- coding: utf-8 -*-
import sys

if sys.version_info.major == 2:  # python2: 两种字符串类型为 str 和 unicode
								 # str --(decode)--> unicode --(encode)--> str

	s = '你好'  # 第一行声明意味着 s 被编码成 utf-8 编码, 
				# 即 s = '\xe4\xbd\xa0\xe5\xa5\xbd'. 
				# 没有声明则采用默认编码 gbk (可通过 sys.setdefaultencoding 来设置)
				# 注意: 如果是自带 ide 可能默认编码为 utf-8

	# if s == b'你好' and s == '\xe4\xbd\xa0\xe5\xa5\xbd' and s == b'\xe4\xbd\xa0\xe5\xa5\xbd': 
	if s == '\xe4\xbd\xa0\xe5\xa5\xbd' and s == b'\xe4\xbd\xa0\xe5\xa5\xbd':
		print("@python2: s = '你好', s == b'你好' == <b or not>'你好的utf-8编码' is True".decode('utf8').encode('gbk'))  
		# 检验: '你好' == b'你好' => True

	print(s)  # 即 print('\xe4\xbd\xa0\xe5\xa5\xbd') 
			  # 又因为 print 默认的 gbk 解码的(可通过 sys.setdefaultencoding 来设置), 
			  # 所以相当于 print(s.decode('gbk')) 即 print('浣犲ソ') 
			  # 如果是 s = u'你好' 则 print 知道是 utf-8 编码, 则按 utf-8 解码并正确打印 你好

	# ss = s.encode('gbk')  # 报错: 
					   # s 已经被编码, 应该先解码
					   # (且只有知道字符编码才能正确解码), 
					   # 后重新编码(成其他编码)

	ss = s.decode('utf8').encode('gbk')  # 正确: 
									     # 由第一行声明我们知道 s 被编码成 utf-8 编码, 
									     # 因此以 utf-8 解码后, 才能重新编码成 gbk

	print(ss)  # print 默认采用 gbk 解码, 而 ss 此时已经是 gbk 编码, 故显示正确为 你好

# 运行结果:
# 浣犲ソ
# 你好

if sys.version_info.major == 3: # python3: 两种字符串类型为 str 和 byte
								# unicode 字符串的类型也为 str, 即 type(u'你好') == 'str' is True
								# str --(encode)--> byte --(decode)--> str

	s = '你好'  # python3 中 str 类型相当于 python2 中 unicode 类型(即已经解码成 unicode 编码), 
				# 因此 s = '你好' 即 s = u'你好' (如果第一行声明为 utf-8 编码, 否则按默认编码方式)

	if s == u'你好' and s != '\xe4\xbd\xa0\xe5\xa5\xbd' and s != u'\xe4\xbd\xa0\xe5\xa5\xbd': 
		print("@python3: s = '你好', s == u'你好' != <u or not>'你好的utf-8编码' is True")  
		# 检验: '你好' == u'你好' => True

	print(s)  # python3 中 print 不解码, 来什么打印什么, 
			  # 所以这里就是 print('你好') 或 print(u'你好')

	ss = s.encode('gbk')  # 正确 ss 被编码成 byte 
						  # 即 ss = b'\xc4\xe3\xba\xc3'

	# ss = s.decode('utf8').encode('gbk')  # 报错: python3: str --(encode)--> byte --(decode)--> str 

	print(ss)  # python3 中 print 不解码, 来什么打印什么, 
			   # 所以这里就是 print(b'\xc4\xe3\xba\xc3') 打印出来就是 b'\xc4\xe3\xba\xc3'

# 运行结果:
# 你好
# b'\xc4\xe3\xba\xc3'