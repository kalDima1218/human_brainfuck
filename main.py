def get_function_definition_name(in_program, start_of_name):
	r = l = start_of_name
	while in_program[r] != '{':
		r+=1
	r-=1
	return l, r

def get_function_definition_code(in_program, start_of_code):
	r = l = start_of_code
	while in_program[r] != '}':
		r+=1
	r-=1
	return l, r

def get_function_usage_name(in_program, start_of_name):
	r = l = start_of_name
	while in_program[r] != '!':
		r+=1
	r-=1
	return l, r

def translate(in_program):
	out_program = ""
	functions = {}
	i = 0
	while i < len(in_program):
		if in_program[i] == '?':
			l, r = get_function_definition_name(in_program, i+1)
			name = in_program[l:r+1]
			l, r = get_function_definition_code(in_program, r+2)
			code = in_program[l:r+1]
			functions[name] = code
			i = r+1
		elif in_program[i] == '!':
			l, r = get_function_usage_name(in_program, i+1)
			name = in_program[l:r+1]
			out_program+=functions[name]
			i = r+1
		else:
			out_program+=in_program[i]
		i+=1
	return out_program


in_program = "?move{[->+<]}!move!"
print(translate(in_program))