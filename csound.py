# wm johnson 12022015
# tools for generating csound scores in python

class Score:
    def __init__(self, tempo=120):
	self.staves = []
	self.tempo = tempo
	self.lines = []
    
    def add_staff(self, instr, n_p):
	""" 
	adds a staff to the score

	args
	    instr: instrument number
	    n_p: number of p statements
	"""
	new_staff = Staff(instr, n_p)
	self.staves.append(new_staff)
	return new_staff

    def write_line(self, line_string):
	"""
	manually write a line to the score file, good for f tables

	args
	    line_string: string of the entire line, excluding \n
	"""
	self.lines.append([str(line_string)])
	

    def write_score_file(self, outfile_name):
	"""
	write: writes the score to a .sco file

	args
	    outfile_name: name of the outputfile including .sco	
	"""
	of = open(outfile_name, 'w')
	of.write('t 0 '+str(self.tempo)+'\n')
	for line in self.lines:
	    of.write(line+'\n')
	for staff in self.staves:
	    for event in staff.events:
		of.write('i '+str(staff.instr)+' '+str(event.start)+' '+str(event.duration)+' '+str(event.p_string)+' \n')
        of.write('e \n')
        of.close


class Staff:
    def __init__(self, instr, n_p):
	self.instr = instr
	self.events = []
	self.n_p = n_p


    def add_event(self, start, duration, list_p):
        """
        add an event to a staff

        args
	    start: start time
	    duration: length
	    list_p: list of all the p statements
        """
	if type(list_p) != list:
	    raise TypeError("p statements not a list")
	if len(list_p) != self.n_p:
	    raise ValueError("incorrect number of p-statements")
        new_event = Event(start, duration, list_p)
	self.events.append(new_event)
	return new_event


class Event:
    def __init__(self, start, duration, p_statements):
	self.start = start
	self.duration = duration
	self.p_string = self.get_string(p_statements)


    def get_string(self, ps):
        """
        returns a string with spaces of the contents of given array

        args
	    ps: array (p statements)
        """
	x = ''
	for p in ps:
	    x += str(p) + ' '
	return x

