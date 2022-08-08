# PyDP v1.00 (http://github.com/dongyx/PyDP)
#
# Copyright 2014 Yuxuan Dong (http://www.dyx.name)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

'''
Automatically transform recursive functions to dynamic programming.

Decorate the recursive function you want to speed up with '@dp' decorator.
Visit http://github.com/dongyx/PyDP for more information.
'''

def __in_mem(mem,argv):
	if len(argv)==1:
		return argv[0] in mem
	else:
		if argv[0] in mem:
			return __in_mem(mem[argv[0]],argv[1:])
		else:
			return False

def __get_mem(mem,argv):
	if len(argv)==1:
		return mem[argv[0]]
	else:
		return __get_mem(mem[argv[0]],argv[1:])

def __set_mem(mem,argv,value):
	if len(argv)==1:
		mem[argv[0]]=value
	else:
		if argv[0] not in mem:
			mem[argv[0]]={}
		__set_mem(mem[argv[0]],argv[1:],value)

	return value

def dp(transfer):
	'''
	Decorate the recursive function you want to speed up.
	'''
	mem={}

	def wrapper(*argv):
		if __in_mem(mem,argv):
			return __get_mem(mem,argv)
		else:
			return __set_mem(mem,argv,transfer(*argv))
	
	return wrapper
