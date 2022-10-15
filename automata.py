test = ['P', 'u', 'h', 't', 'i', 'c']

automata ={
    
    'Final': 'Q14',
    
    'delta': {
        ('Q0', 'P'):'Q1',
        ('Q1', 'u'):'Q2',
        ('Q2', 'b'):'Q3',
        ('Q2', 't'):'Q2',
        ('Q2', 'h'):'Q2',
        ('Q3', 'l'):'Q4',
        ('Q4', 'i'):'Q5',
        ('Q5', 'c'):'Q6',
        
        
    },

    'estate' :[
        'Q0', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6'
    ],

    'lenguage': [
        'A', 'B', 'C', 'P', 'u', 'b', 'l', 'i', 'c', 't', 'h'
    ]

}



#print(delta.get(('Q0', 'P')))
def validation(a,b):
    try:
       assert(a in automata['estate'])
       assert(b in automata['lenguage'])
       return automata['delta'][a,b]
    except:
        return False
    

def final(a):
    if a == automata['Final']:
        return True
    else:
        return False

#print(validation(d, 'B'))

#print(automata['estate'][0])
#print(test[0])
i = 'Q0'
a = 'P'

#print(validation(automata['estate'][0], test[0]))
#print(validation(i, a))

for index, item in zip(automata['estate'], test):
    print(index, item)
    print(validation(index, item))
    print(final(validation(index, item)))

